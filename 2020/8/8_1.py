file = open('input2.txt')
input_list = []
for line in file:
    input_list.append(line.strip().split())

acc=0
count_list=[0]*len(input_list)
i=0
prev=i
while count_list[i]!=1:
    command,ins=input_list[i]
    if command=='acc':
        acc+=int(ins)
        count_list[i]+=1
        prev=i
        i+=1
    if command=='jmp':
        count_list[i]+=1
        prev=i
        i+=int(ins)
    if command=='nop':
        count_list[i]+=1
        prev=i
        i+=1


print(acc)
