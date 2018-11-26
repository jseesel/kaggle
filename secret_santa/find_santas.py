from random import shuffle
from pprint import pprint
from email_helper import Email, EmailConnection


# TODO: email everyone, no log

def send_email(giver, receiver):
    giver_email = giver['email']
    giver_name = giver['name']
    receiver_name = receiver['name']
    EMAIL_PASSWORD = open('.email_pass', 'r').read()

    html_body_text = """
    Hello {giver_name}, my little king,
    <br><br>
    If you are receiving this email, it's because you signed up for secret santa in bois chat. 
    <br>Don't show this email to anyone else to keep it a secret.
    <br><br>Your chosen boi is: <b>{receiver_name}</b>
    <br><br>Actual location/timing of gift swap still TBD but probably a bois brunch or something.
    <br>
    <br>Sincerely,
    <br>Jim
    
    """.format(giver_name=giver_name,receiver_name=receiver_name)

    # now we send the actual email
    msg = Email()
    sender_email = 'do-not-reply@grubhub.com'
    msg.add_sender(sender_email)
    msg.list_recipients(giver_email)  # [array,if,multiple] else single email
    msg.html_body(html_body_text)
    msg.subject("BOIS CHAT SECRET SANTA ASSIGNMENT")  # string
    ec = EmailConnection(sender_email, EMAIL_PASSWORD)
    ec.send(msg)
    print "sent email to {}".format(giver_email)
    # print "sent email to {} for {}".format(giver_name,receiver_name)


# input_csv = 'test_input.csv'
input_csv = 'real_input.csv'
with open(input_csv, 'r') as f:
    data = f.readlines()

people = []
for d in data:
    curr_person = d.split(',')
    people.append([curr_person[0].strip(), curr_person[1].strip()])

# shuffle(people)
print people
print range(0, len(people), 1)

people_map = {}
for i in range(0, len(people), 1):
    people_map[i] = {'name': people[i][0], 'email': people[i][1]}

pprint(people_map)
givers = [i for i in range(0, len(people), 1)]
receivers = [i for i in range(0, len(people), 1)]
matches = True
while matches:
    # print "givers   : ", givers
    # print "receivers: ", receivers
    matches = False
    for i in range(0, len(people), 1):
        if givers[i] == receivers[i]:
            # print "matched at ", i
            matches = True
            break
    if matches:
        shuffle(givers)
        shuffle(receivers)

# print "final sorts"
# print "givers   : ", givers
# print "receivers: ", receivers

for i in range(0, len(people), 1):
    curr_giver = people_map[givers[i]]
    curr_receiver = people_map[receivers[i]]
    send_email(curr_giver, curr_receiver)
