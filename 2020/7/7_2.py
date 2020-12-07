import re
from collections import defaultdict
file = open('input1.txt')
input_list = defaultdict( lambda : dict())
for line in file:
    line=line.split('contain')
    outbag=line[0].strip()
    if outbag[-1]=='s':
        outbag=outbag[:-1]
    inbags=line[1].split(',')
    for bag in inbags:
        bag=bag.strip()
        bag=bag.strip('.')
        bag_s=bag.split(' ')
        nu=int(bag_s[0] if bag_s[0]!='no' else 0)
        if nu!=0:
            bag=bag.replace(str(nu),'').strip()
            if bag[-1]=='s':
                bag=bag[:-1]
            input_list[outbag][bag]=nu
        else:
            input_list[outbag]=0

def get_count(bag):
    count=0
    if bag in input_list:
        cd=input_list[bag]
        if type(cd) is not int:
            for b,c in cd.items():
                count+=c+c*get_count(b)
    return count

print(get_count('shiny gold bag'))
