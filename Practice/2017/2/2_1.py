file = open('input2.txt')
input_list = []
for line in file:
    input_list.append([*map(int,line.strip().split('\t'))])
def checksum():
    sum=0
    for row in input_list:
        diff=max(row)-min(row)
        sum+=diff
    return sum
print(checksum())
