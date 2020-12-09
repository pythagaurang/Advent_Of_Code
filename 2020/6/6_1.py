file = open('input1.txt')
input_list = [line.strip() for line in file]+['']

questions=set()
count=0

for line in input_list:
    if line!='':
        for letter in line:
            questions.add(letter)
    else:
        count+=len(questions)
        questions=set()

print(count)
