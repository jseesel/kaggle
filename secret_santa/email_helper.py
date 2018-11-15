import os
import smtplib
from email import Encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase


class Email(MIMEMultipart):
    def __init__(self):
        MIMEMultipart.__init__(self)
        self['To'] = ''
        self.text = ''
        self.html = ''
        self.recipients = []
        self.attachments = []

    def __getattr__(self, name):
        return self[name]

    def subject(self, sbj):
        self.subject = sbj
        self['Subject'] = sbj

    def add_sender(self, sender):
        self.sender = sender
        self['From'] = sender

    def list_recipients(self, rec):
        try:
            self.recipients = self.recipients + rec
            self['To'] = self['To'] + ','.join(rec)
        except TypeError:
            self.recipients.append(rec)
            self['To'] = self['To'] + rec + ','

    def body(self, text):
        self.text = text

    def html_body(self, html_text):
        self.html = html_text

    def __attach_MIMEBase__(self, attachment_file):
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attachment_file, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="%s"'
                        % os.path.basename(attachment_file))
        self.attach(part)

    def add_attachments(self, attach):
        try:
            self.attachments = self.attachments + attach
            for a in attach:
                self.__attach_MIMEBase__(a)
        except TypeError:
            self.attachments.append(attach)
            self.__attach_MIMEBase__(attach)


class EmailConnection:
    def __init__(self, usr, pwd):
        self.username = usr
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(usr, pwd)

    def get_sender(self):
        return self.username

    @staticmethod
    def __attach_email_body__(email):
        body = MIMEMultipart('alternative')
        body.attach(MIMEText(email.text, 'plain'))
        body.attach(MIMEText(email.html, 'html'))
        email.attach(body)

    def send(self, email, quit=True):
        email.add_sender(self.get_sender())
        EmailConnection.__attach_email_body__(email)
        self.server.sendmail(email.sender, email.recipients, email.as_string())
        if quit:
            self.server.quit()

    def quit(self):
        self.server.quit()
