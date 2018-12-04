

input_file = 'input_star1.txt'

with open(input_file,'r') as f:
    data = f.readlines()

frequency = 0
for d in data:
    num = int(d.replace('+',''))
    frequency += num

print frequency