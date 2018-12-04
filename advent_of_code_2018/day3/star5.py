from pprint import pprint

def parse_cut(cut):
    data = cut.split(' ')
    # #3 @ 5,5: 2x2
    start_pt = data[2].replace(':', '').split(',')
    size = data[3].split('x')
    return start_pt, size


def make_cut(square):
    if square[0] == 'x':
        return ['x']
    elif square[0] > 0:
        return ['x']
    else:
        return [1]


with open('input.txt','r') as f:
    input = f.readlines()
data = [i.strip() for i in input]

fabric = [[[0] for i in range(0,1000,1)] for j in range(0,1000,1)]
# print fabric

for d in data:
    loc, size = parse_cut(d)
    print loc
    print size
    x = int(loc[0])
    y = int(loc[1])
    x_size = int(size[0])
    y_size = int(size[1])
    for i in range(x,x+x_size,1):
        for j in range(y,y+y_size,1):
            result = make_cut(fabric[i][j])
            # print result
            fabric[i][j] = result
# pprint(fabric)


x_count = 0
for i in range(0,1000,1):
    for j in range(0,1000,1):
        if fabric[i][j][0] == 'x':
            x_count += 1

print x_count