file = open('input2.txt')
input_list = []
for line in file:
    input_list.append(int(line.strip()))
from itertools import combinations
def get_difference():
    adapters=[0]+sorted(input_list)
    c=[]
    for i in range(1,len(adapters)-1):
        if adapters[i+1]-adapters[i-1]<=3:
            c.append(adapters[i])
    c+=[-1]
    temp=[c[0]]
    grouped_c=[]
    multiplier=[1,2,4,7,13,24]
    for i in range(1,len(c)):
        if temp[-1]+1==c[i]:
            temp.append(c[i])
        else:
            grouped_c.append(len(temp))
            temp=[c[i]]
    from functools import reduce
    return reduce(lambda x,y: x*multiplier[y],[1]+grouped_c)


#gotta learn dp
print(get_difference())
