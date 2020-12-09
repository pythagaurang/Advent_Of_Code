file = open('input2.txt')
input_list = []
for line in file:
    input_list.append(line.strip().split())

acc=0
count_list=[0]*len(input_list)

i=0
while count_list[i]!=1:
    command,ins=input_list[i]
    count_list[i]+=1
    if command=='acc':
            acc+=int(ins)
    elif command=='jmp':
        i+=int(ins)
        continue
    i+=1


print(acc)

