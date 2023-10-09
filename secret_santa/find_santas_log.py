from random import shuffle
from pprint import pprint
from datetime import datetime

# this job takes an input of .secret santa signups and randomly assigns them to each other
# example data: Timestamp,Who are you?,What's your email?,Street Address,City,State,Zip code,Any gift suggestions?


# input_csv = 'test_data.tsv'
output_csv = 'test_output.tsv'

input_csv = 'real_input_{}.tsv'.format(datetime.now().year)
# output_csv = '{}_boismas_output.tsv'.format(datetime.now().year)
with open(input_csv, 'r') as f:
    data = f.readlines()

people = []
for d in data[1:]:
    curr_person = d.split('\t')
    people.append(curr_person)
    # people.append([curr_person[0].strip(), curr_person[1].strip()])

last_year_csv = '{}_boismas_output.tsv'.format(datetime.now().year - 1)
with open(last_year_csv, 'r') as f:
    prior_output = f.readlines()

last_year = []
for p in prior_output[1:]:
    curr_row = p.split('\t')
    last_year.append(curr_row)

# shuffle(people)
# pprint(people)
# print(range(0, len(people), 1))

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

last_year_map = {}
for i in range(0, len(last_year), 1):
    giver = last_year[i][1]
    taker = last_year[i][2]
    last_year_map[giver] = taker
    

pprint(people_map)
givers = [i for i in range(0, len(people), 1)]
receivers = [i for i in range(0, len(people), 1)]
matches = True
while matches:
    # print("givers   : ", givers)
    # print("receivers: ", receivers)
    matches = False
    for i in range(0, len(people), 1):
        if givers[i] == receivers[i]:
            # print("matched at ", i)
            matches = True
            break
        giver_name = people_map[givers[i]]['name']
        receiver_name = people_map[receivers[i]]['name']
        # print("{}: this year {} | last year {}".format(giver_name, receiver_name, last_year_map[giver_name]))
        if receiver_name == last_year_map[giver_name]:
            # print("matched last year for ", givers[i])
            matches = True
            break
    if matches:
        shuffle(givers)
        shuffle(receivers)

# print("final sorts")
# for i in range(0, len(givers), 1):
#     print("{} gives to {}".format(givers[i], receivers[i]))

with open(output_csv, 'w') as f:
    f.write('giver_email\tgiver_name\treceiver_name\treceiver_address\tsuggestions\n')
    for i in range(0, len(people), 1):
        curr_giver = people_map[givers[i]]
        curr_receiver = people_map[receivers[i]]
        f.write('{giver_email}\t{giver_name}\t{receiver_name}\t{address}\t{suggestions}\n'.format(
            giver_email=curr_giver['email'], giver_name=curr_giver['name'], receiver_name=curr_receiver['name'],
            address=curr_receiver['address'],suggestions=curr_receiver['suggestions'] ))
        print("log result for {}".format(curr_giver['name']))
