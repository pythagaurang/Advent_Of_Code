file = open('input2.txt')
input_list = []
for line in file:
    input_list.append(list(line.strip()))
from copy import deepcopy

def get_stable():
    i=0
    while i<100:
        prev=deepcopy(input_list)
        for y in range(len(input_list)):
            for x in range(len(input_list[0])):
                    if i==0:
                        if input_list[y][x]=='L':
                            input_list[y][x]="#"
                    else:
                        c=0
                        for a,b in [(1,0),(1,1),(0,1),(-1,1),(1,-1),(-1,0),(-1,-1),(0,-1)]:
                            g=a
                            h=b
                            while 0<=a+x<len(input_list[0]) and 0<=b+y<len(input_list):
                                if prev[b+y][a+x]=='#':
                                    c+=1
                                    break
                                if prev[b+y][a+x]=='L':
                                    break
                                a+=g
                                b+=h
                        if c>=5 and prev[y][x]=='#':
                            input_list[y][x]='L'
                        if not c and prev[y][x]=='L':
                            input_list[y][x]='#'
        i+=1
        if prev==input_list:
            return count_occupied(input_list)
                        


def count_occupied(seats):
    count=0
    for i in seats:
        for j in i:
            if j=="#":
                count+=1
    return count

print(get_stable())
