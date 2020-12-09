file = open('input2.txt')
input_list = []
for line in file:
    input_list.append(int(line.strip()))

from itertools import combinations
def valid(n):
    sums=[]
    i=0
    l=2
    while n not in sums and l<len(input_list):
        sums=[]
        i=0
        while i+l<len(input_list):
            cw=input_list[i:i+l]
            if sum(cw)==n:
                print(min(cw)+max(cw))
            i+=1
        l+=1
print(valid(1124361034))
