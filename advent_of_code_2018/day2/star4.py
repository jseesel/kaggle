from pprint import pprint

def check_match(word1,word2):
    diff_count = 0
    diff_loc = -1
    for i in range(0,len(word1),1):
        if word1[i] != word2[i]:
            diff_count += 1
            diff_loc = i

    return diff_count, diff_loc

with open('input.txt', 'r') as f:
    data = f.readlines()

for d in data:
    for e in data:
        diff_count, diff_loc = check_match(d.strip(), e.strip())
        if diff_count == 1:
            print d.strip()
            print e.strip()
            print diff_loc
            print d[:diff_loc] + d[diff_loc:]



