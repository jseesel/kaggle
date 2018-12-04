from pprint import pprint
from progressbar import ProgressBar

def parse_cut(cut):
    data = cut.split(' ')
    # #3 @ 5,5: 2x2
    claim = data[0].replace('#','')
    start_pt = data[2].replace(':', '').split(',')
    size = data[3].split('x')
    return claim,start_pt, size


def make_cut(square,claim):
    if square[0] == 'x':
        return ['x']
    elif square[0] > 0:
        return ['x']
    else:
        return [claim]


with open('input.txt','r') as f:
    input = f.readlines()
data = [i.strip() for i in input]

fabric = [[[0] for i in range(0,1000,1)] for j in range(0,1000,1)]
# print fabric


expected_sizes = {}
for d in data:
    claim, loc, size = parse_cut(d)
    # print loc
    # print size
    x = int(loc[0])
    y = int(loc[1])
    x_size = int(size[0])
    y_size = int(size[1])
    expected_sizes[claim] = x_size * y_size
    for i in range(x,x+x_size,1):
        for j in range(y,y+y_size,1):
            result = make_cut(fabric[i][j], claim)
            # print result
            fabric[i][j] = result
# pprint(fabric)

bar = ProgressBar
for k in bar(expected_sizes.keys()):
    good_count = 0
    for i in range(0,1000,1):
        for j in range(0,1000,1):
            if fabric[i][j][0] == k:
                good_count += 1
    if good_count == expected_sizes[k]:
        print k

