from pprint import pprint

input_file = 'input_star1.txt'

with open(input_file, 'r') as f:
    data = f.readlines()

frequency_count = {0: 1}
frequency = 0
no_matches = True
loop_count = 0
while no_matches and loop_count < 200:
    for d in data:
        num = int(d.replace('+', ''))
        frequency += num
        if frequency in frequency_count.keys():
            frequency_count[frequency] += 1
            if frequency_count[frequency] == 2:
                no_matches = False
                print frequency
        else:
            frequency_count[frequency] = 1

    loop_count += 1

# print frequency

# pprint(frequency_count)

for k in frequency_count.keys():
    if frequency_count[k] > 1:
        print "%d: %d" % (k, frequency_count[k])
