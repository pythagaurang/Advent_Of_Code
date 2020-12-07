input_file = open('one/input1.txt','r')
input = []
for i in input_file:
  input.append(int(i))

print(input)

from itertools import combinations

combi = combinations(input,3)

for i,j,k in combi:
  if i+j+k==2020:
    print(i*j*k)
