import re
from collections import defaultdict
file = open('input1.txt')
input_list = defaultdict( lambda : dict())
for line in file:
    line=line.split('contain')
    outbag=re.findall(r'(.+) bag',line[0])[0]
    content=re.findall(r'(\d+) ([\w\s]+) bag',line[1])
    for x,y in content:
        input_list[outbag][y]=int(x)
def count(bag='shiny gold'):
    c=0
    in_current_bag=input_list[bag]
    for key,value in in_current_bag.items():
        c+=value+value*count(key)
    return c
print(count())
