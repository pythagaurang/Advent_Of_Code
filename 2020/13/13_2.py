file = open('input2.txt')
input_list = []
file.readline()
for line in file:
    bus_ids = [int(busid) if busid!='x' else 1 for busid in line.strip().split(',')]
    input_list.append(bus_ids)

def get_lcm(remainders):
    m,r=remainders[0]
    for i in remainders[1:]:
        if i[0]!=1:
            r,m=multiply(i[0],i[1],m,r)
    return r
def multiply(a,ar,b,br):
    m=br
    while m%a!=ar:
        m+=b
    return m,a*b
for bus_ids in input_list:
    remainders=[*map(lambda x: (x,(x-bus_ids.index(x))%x),bus_ids)]
    print(get_lcm(remainders))

