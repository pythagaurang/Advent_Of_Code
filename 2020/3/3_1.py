file = open('input2.txt')

input_list = []

for line in file:	
    input_list.append(list(line.strip()))

y_max = len(input_list)
x_max = len(input_list[0])

def count_trees(x_inc,y_inc):
    x=0
    y=0
    count=0
    while y<y_max-1:
        x=(x+x_inc)%x_max
        y+=y_inc
        if input_list[y][x]=='#':
            count+=1
    return count

print(count_trees(3,1))

