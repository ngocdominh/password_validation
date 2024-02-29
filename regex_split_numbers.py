import re

name = input('Enter file:')
if len(name) < 1:
    name = 'regex_sum_1966297.txt'
handle = open(name)
ln = handle.readlines()
lst = []

for line in ln:
    numb = re.findall('[0-9]+', line)
    for i in numb:
        i = int(i)
        lst.append(i)

print(sum(lst))