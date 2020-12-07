file = open('input2.txt','r')

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
high_seat=0
for string in input_list:
    row = binary_convert(string[:-3],'F','B',127)
    col = binary_convert(string[-3:],'L','R',7)
    seat = row*8 + col
    high_seat=max([seat,high_seat])
print(high_seat)
