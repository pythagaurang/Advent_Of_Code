file = open('input3.txt','r')

from math import ceil,floor

input_list = [line.strip() for line in file]


def binary_convert(string,zero,one,upper):
    lower=0
    i=0
    while i<(len(string)-1):
        char=string[i]
        if char==zero:
            upper=floor((lower+upper)/2)
        elif char==one:
            lower=ceil((lower+upper)/2)
        i+=1
    if string[i]==zero:
        return lower
    return upper
low_seat=10000
high_seat=0
seats=[]
for string in input_list:
    row = binary_convert(string[:-3],'F','B',127)
    col = binary_convert(string[-3:],'L','R',7)
    seat = row*8 + col
    seats.append(seat)
    high_seat=max([seat,high_seat])
    low_seat=min([seat,low_seat])

counts=[0]*(high_seat-low_seat+1)
for i in seats:
    counts[i-low_seat]+=1

i=0
while counts[i]!=0:
    i+=1
print(i+low_seat)
