input_file = open('input1.txt','r')
input = []
for i in input_file:
  input.append(int(i))

print(input)

from itertools import combinations

combi = combinations(input,2)

for i,j in combi:
  if i+j==2020:
    print(i*j)
