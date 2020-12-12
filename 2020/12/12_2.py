import re

file = open('input2.txt')
input_list = []
for line in file:
    input_list.append(*re.findall(r'([NEWSFLR])(\d+)',line))
cd='E'
way_distance={'N':1,'E':10}
ship_distance={'N':0,'E':0}
for d,s in input_list:
    s=int(s)
    if d in ['F']:
        for i,j in way_distance.items():
            ship_distance[i]+=s*j
    if d in 'NE':
        way_distance[d]+=s
    if d == 'S':
        way_distance['N']-=s
    if d == 'W':
        way_distance['E']-=s
    if s in [90,270]:
        n=way_distance['N']
        e=way_distance['E']
        if s==270:
            d='L' if d=='R' else 'R'
        if d == 'L':
            way_distance['E']=-n
            way_distance['N']=e
        if d == 'R':
            way_distance['E']=n
            way_distance['N']=-e
    if s==180:
        way_distance['N']=-way_distance['N']
        way_distance['E']=-way_distance['E']
print(sum([abs(ship_distance['N']),abs(ship_distance['E'])]))
