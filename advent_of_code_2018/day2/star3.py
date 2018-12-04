from pprint import pprint

def letter_check(word):
    double_letter = False
    triple_letter = False
    letter_counts = {}
    for l in word:
        try:
            letter_counts[l] += 1
        except:
            letter_counts[l] = 1

    for k in letter_counts.keys():
        if letter_counts[k] == 2:
            double_letter = True
        if letter_counts[k] == 3:
            triple_letter = True

    # pprint(letter_counts)

    return double_letter, triple_letter


with open('input.txt', 'r') as f:
    data = f.readlines()


double_count = 0
triple_count = 0
for d in data:
    # print d
    double, triple = letter_check(d.strip())
    # print "%s %s\n" % (double, triple)
    if double:
        double_count += 1
    if triple:
        triple_count += 1

print double_count
print triple_count
print double_count * triple_count