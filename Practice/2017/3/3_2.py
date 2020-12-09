file = open('input2.txt')
input_list = [int(line.strip()) for line in file]

from math import ceil
from time import sleep
def get_spiral(num,v=False):
    edge=11
    array=[[0]*edge for i in range(edge)]
    n=1
    center=edge//2
    x=center
    y=center
    inc_x=1
    inc_y=-1
    is_x=True
    l=1
    while n<=num:
        if v:
            for i in array:
                print(*map(lambda x: str(x).ljust(7),i))
            print('\n'+'-'*77)
            sleep(0.3)
            print(("\033[A"+" "*90+"     \033[A")*9,end="\r")
        level=get_level(l)-1
        l+=1
        array[y][x]=n
        temp_x=x+inc_x
        temp_y=y+inc_y
        if level==(get_level(l)-1):
            if is_x:
                if (temp_x<(center-level) or temp_x>(center+level)):
                    inc_x= -1 if inc_x==1 else 1
                    is_x=False
                    y+=inc_y
                else:
                    x+=inc_x
            else:
                if (temp_y<(center-level) or temp_y>(center+level)):
                    inc_y= -1 if inc_y==1 else 1
                    is_x=True
                    x+=inc_x
                else:
                    y+=inc_y
        else:
            inc_x=1
            x+=inc_x
            is_x=True
        n=0
        for i,j in [(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]:
            n+=array[y+i][x+j]
    return n
def get_level(num):
    i=0
    for i in range(1,ceil(num**0.5)+2,2):
        if i*i>=num:
            break
    return i//2+1
for num in input_list:
        print(num,get_spiral(num,True))
