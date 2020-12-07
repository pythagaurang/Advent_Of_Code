import re

file = open('input2.txt')

input_list = []

for line in file:
    line=line.split(" ")
    least_most = line[0].split("-")
    least = int(least_most[0])
    most = int(least_most[1])
    char = line[1][0]
    password = line[2].strip()
    line = (least,most,char,password)
    input_list.append(line)

count=0
for least,most,char,password in input_list:
    if (password[least-1]==char or password[most-1]==char) and password[least-1]!=password[most-1]:
        count+=1

print(count)
