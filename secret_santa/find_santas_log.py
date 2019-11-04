from random import shuffle
from pprint import pprint


# TODO: email everyone, no log

# input_csv = 'test_input.csv'
input_csv = 'real_input_2019.csv'
output_csv = '2019_output.csv'
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
with open(output_csv, 'w') as f:
    f.write('giver_name,giver_email,receiver_name\n')
    for i in range(0, len(people), 1):
        curr_giver = people_map[givers[i]]
        curr_receiver = people_map[receivers[i]]
        giver_email = curr_giver['email']
        giver_name = curr_giver['name']
        receiver_name = curr_receiver['name']
        f.write('{giver_email},{giver_name},{receiver_name}\n'.format(giver_email=giver_email,giver_name=giver_name,receiver_name=receiver_name))
        print "log result for {}".format(giver_email)
