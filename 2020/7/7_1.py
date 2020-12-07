import re
from collections import defaultdict
file = open('input2.txt')
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

def get_count(bag,input_dict,it=[0]):
    count=0
    for b,n in input_dict.items():
        isin=False
        for b1,n1 in n.items():
            if bag==b1:
                isin=True
            else:
                if b1 in input_list:
                    isin=bool(get_count(bag,{b1:input_list[b1]}))
            if isin: break
        count+=isin
    return count

print(get_count('shiny gold bag',input_list))
