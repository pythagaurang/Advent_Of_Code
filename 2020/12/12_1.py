import re

file = open('input2.txt')
input_list = []
for line in file:
    input_list.append(*re.findall(r'([NEWSFLR])(\d+)',line))
print(input_list)
cd='E'
distance={'W':0,'N':0,'S':0,'E':0}
for d,s in input_list:
    s=int(s)
    if d in ['F']:
        distance[cd]+=s
    if d in ['N','S','E','W']:
        distance[d]+=s
    directions=['N','E','S','W']
    if d in ['L','R']:
        i=directions.index(cd)
        if d=='L':
            cd=directions[i-s//90]
        if d=='R':
            cd=directions[(i+s//90)%4]

print(sum([abs(distance['N']-distance['S']),abs(distance['E']-distance['W'])]))
