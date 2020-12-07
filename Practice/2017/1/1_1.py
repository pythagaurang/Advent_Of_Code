import re

file = open('input2.txt')
input_list = []

for line in file:
    input_list.append(line.strip())

def get_sum(num):
    l=len(num)
    return sum(int(num[i]) for i in range(len(num)) if num[i]==num[(i+1)%l])
for num in input_list:
    print(get_sum(num))
