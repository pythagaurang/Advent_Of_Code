file = open('input2.txt')
input_list = []
for line in file:
    input_list.append(list(line.strip()))
from copy import deepcopy

def get_stable():
    i=0
    while True:
        prev=deepcopy(input_list)
        for y in range(len(input_list)):
            for x in range(len(input_list[0])):
                    if i==0:
                        if input_list[y][x]=='L':
                            input_list[y][x]="#"
                    else:
                        c=0
                        for (a,b) in [(1,0),(1,1),(0,1),(-1,1),(1,-1),(-1,0),(-1,-1),(0,-1)]:
                            if 0<=a+x<len(input_list[0]) and 0<=b+y<len(input_list):
                                if prev[b+y][a+x]=='#':
                                    c+=1
                        if c>=4 and input_list[y][x]=='#':
                            input_list[y][x]='L'
                        if not c and input_list[y][x]=='L':
                            input_list[y][x]='#'
        i+=1
        #for a in input_list:
        #    print(*a)
        #print()
        if count_occupied(prev)==count_occupied(input_list):
            return count_occupied(prev)
                        


def count_occupied(seats):
    count=0
    for i in seats:
        for j in i:
            if j=="#":
                count+=1
    return count

print(get_stable())
