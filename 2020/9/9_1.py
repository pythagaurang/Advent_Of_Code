file = open('input2.txt')
input_list = []
for line in file:
    input_list.append(int(line.strip()))

from itertools import combinations
def valid(n):
    for i in range(n,len(input_list)):
        sums=[*map(sum,combinations(input_list[i-n:i],2))]
        if input_list[i] not in sums:
            return input_list[i]
print(valid(25))
