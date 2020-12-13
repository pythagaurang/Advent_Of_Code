file = open('input2.txt')
input_list = []
time_stamp=int(file.readline().strip())
bus_ids = [int(busid) for busid in file.readline().strip().split(',') if busid!='x']

def get_bus(time_stamp):
    min_time=(0,10000000)
    for i in bus_ids:
        time=i-time_stamp%i
        if time<min_time[1]:
            min_time=(i,time)
    return min_time

min_time=get_bus(time_stamp)
print(min_time,min_time[0]*min_time[1])

