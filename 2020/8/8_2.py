file = open('input2.txt')
input_list = []
for line in file:
    input_list.append(line.strip().split())

j=0
og_list=[i for i in input_list]
while j<len(input_list):
    input_list=[i for i in og_list]
    acc=0
    count_list=[0]*len(input_list)
    i=0
    if input_list[j][0] in ['jmp','nop']:
        input_list[j]=['nop' if input_list[j][0]=='jmp' else 'jmp',input_list[j][1]]
        while i<len(count_list) and count_list[i]!=1:
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
    if i==len(count_list):
        print(acc,i)
    j+=1
