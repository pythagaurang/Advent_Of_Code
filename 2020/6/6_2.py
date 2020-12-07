file = open('input2.txt')
input_list = []
for line in file:
    input_list.append(line.strip())
input_list+=['']
count=0
from collections import defaultdict
l=0
questions=defaultdict(lambda : 0)
for line in input_list:
    if line!='':
        l+=1
        for letter in line:
            questions[letter]+=1
    else:
        c=0
        for x,y in questions.items():
            if y==l:
                c+=1
        count+=c
        l=0
        questions=defaultdict(lambda : 0)

print(count)
