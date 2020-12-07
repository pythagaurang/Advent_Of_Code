file = open('input2.txt')

fields=[
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        ]

input_list=[]
input_dict={}
for line in file:
    line = line.strip()
    if line != "":
        line = line.split(" ")
        for block in line:
            key_value=block.strip().split(":")
            input_dict[key_value[0]]=key_value[1]
    else:
        input_list.append(input_dict)
        input_dict={}

def validate():
    count=0
    for pass_dict in input_list:
        c=0
        for i in fields:
            if i in pass_dict:
                c+=1
        if c == 7:
            count+=1
    return count

print(validate())

