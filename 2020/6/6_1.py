file = open('input2.txt')
input_list = []
for line in file:
    input_list.append(line.strip())
input_list+=['']
questions=set()
count=0
for line in input_list:
    if line!='':
        for letter in line:
            print(letter)
            questions.add(letter)
            print(questions)
    else:
        count+=len(questions)
        questions=set()
print(count)
