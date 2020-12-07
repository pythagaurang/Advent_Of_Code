file = open('input2.txt')
input_list = []
for line in file:
    input_list.append([*map(int,line.strip().split('\t'))])
def checksum():
    sum_=0
    for row in input_list:
        num=[n//m for n in row for m in row if not n%m if n/m!=1]
        sum_+=sum(num)
    return sum_
print(checksum())
