file = open('input1.txt')
input_list = [int(line.strip()) for line in file]

from math import ceil
from time import sleep 

def get_spiral(num,v=True):
    i=0
    for i in range(1,ceil(num**0.5)+2,2):
        if i*i>=num:
            break
    level=i//2+1
    
    edge=level*2-1
    array=[[0]*edge for i in range(edge)]
    n=edge*edge
    x=edge-1
    y=edge-1
    inc_x=-1
    inc_y=-1
    is_x=True
    while n>=1:
        if v:
            for i in array:
                print(*map(lambda x: str(x).ljust(4),i))
            print('\n'+'-'*77)
            sleep(0.1)
            print(("\033[A"+" "*90+"     \033[A")*9,end="\r")
        array[y][x]=n
        n-=1
        temp_x=x+inc_x
        temp_y=y+inc_y
        if is_x:
            if (temp_x<0 or temp_x>=edge or array[y][temp_x]!=0):
                inc_x= -1 if inc_x==1 else 1
                is_x=False
                y+=inc_y
            else:
                x+=inc_x
        else:
            if (temp_y<0 or temp_y>=edge or array[temp_y][x]!=0):
                inc_y= -1 if inc_y==1 else 1
                is_x=True
                x+=inc_x
            else:
                y+=inc_y
    for i in array:
        print(*map(lambda x: str(x).ljust(7),i))
    return array
def get_distance(num):
    spiral=get_spiral(num)
    center=None
    dest=None
    for i in range(len(spiral)):
        for j in range(len(spiral)):
            if spiral[j][i]==1:
                center=(i,j)
            if spiral[j][i]==num:
                dest=(i,j)
    return abs(center[0]-dest[0])+abs(center[1]-dest[1])

for num in [100]:
        print(num,get_distance(num))
