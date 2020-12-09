file = open('input2.txt')
input_list = []
for line in file:
    input_list.append(line.strip().split())

count=0
for passphrase in input_list:
    count+=len(passphrase)==len(set(passphrase))
print(count)
