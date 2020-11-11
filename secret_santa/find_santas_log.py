from random import shuffle
from pprint import pprint
from datetime import datetime

# TODO: email everyone, no log

# example data: Timestamp,Who are you?,What's your email?,Street Address,City,State,Zip code,Any gift suggestions?


input_csv = 'test_data.tsv'
# input_csv = 'real_input_2020.tsv'
output_csv = '{}_output.tsv'.format(datetime.now().year)
with open(input_csv, 'r') as f:
    data = f.readlines()

people = []
for d in data[1:]:
    curr_person = d.split('\t')
    people.append(curr_person)
    # people.append([curr_person[0].strip(), curr_person[1].strip()])

# shuffle(people)
pprint(people)
print(range(0, len(people), 1))

people_map = {}
for i in range(0, len(people), 1):
    try:
        suggestion = people[i][7]
    except IndexError:
        suggestion = ''
    people_map[i] = {
        'name': people[i][1].strip(),
        'email': people[i][2].strip(),
        'address': people[i][3] + ' ' + people[i][4] + ', ' + people[i][5] + ' ' + people[i][6].strip(),
        'suggestions': suggestion.strip()
    }

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
with open(output_csv, 'w') as f:
    f.write('giver_email\tgiver_name\treceiver_name\treceiver_address\tsuggestions\n')
    for i in range(0, len(people), 1):
        curr_giver = people_map[givers[i]]
        curr_receiver = people_map[receivers[i]]
        f.write('{giver_email}\t{giver_name}\t{receiver_name}\t{address}\t{suggestions}\n'.format(
            giver_email=curr_giver['email'], giver_name=curr_giver['name'], receiver_name=curr_receiver['name'],
            address=curr_receiver['address'],suggestions=curr_receiver['suggestions'] ))
        print "log result for {}".format(curr_giver['name'])
