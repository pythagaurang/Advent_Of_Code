file = open('input2.txt')
input_list = []
for line in file:
    input_list.append(int(line.strip()))

def get_difference():
    diff=[0]*100
    adapters=sorted(input_list)
    diff[adapters[0]-0]+=1
    diff[3]+=1
    for i in range(len(adapters)-1):
        diff[adapters[i+1]-adapters[i]]+=1
    print(diff)
    print(adapters)
    return diff[1]*diff[3]
print(get_difference())
