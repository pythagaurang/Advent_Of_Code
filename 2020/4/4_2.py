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

import re
def validate():
    count=0
    for pass_dict in input_list:
        c=0
        for i in fields:
            if i in pass_dict:
                c+=1
        if c == 7:
            c=0
            byr=int(pass_dict['byr'])
            if 1920<=byr<=2002:
                print(byr)
                c+=1
            iyr=int(pass_dict['iyr'])
            if 2010<=iyr<=2020:
                print(iyr)
                c+=1
            eyr = int(pass_dict['eyr'])
            if 2020<=eyr<=2030:
                print(eyr)
                c+=1
            hgt = pass_dict["hgt"]
            if ('cm' in hgt and 150<=int(hgt[:-2])<=193) \
            or ('in' in hgt and 59<=int(hgt[:-2])<=76):
                print(hgt)
                c+=1
            hcl = pass_dict["hcl"].lower()
            if re.match(r'#[0-9a-f]{6}',hcl):
                print(hcl)
                c+=1
            ecl = pass_dict["ecl"].lower()
            if re.match(r'(amb|blu|brn|gry|grn|hzl|oth)',ecl):
                print(ecl)
                c+=1
            pid = pass_dict["pid"]
            if len(pid)==9 and int(pid)>=1:
                print(pid)
                c+=1
            print(pass_dict)
            print(c)
            if c==7:
                count+=1
    return count

print(validate())

