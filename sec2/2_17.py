f_hightemp = 'hightemp.txt'

with open(f_hightemp,'r') as f:
    set_list = set()
    for line in f:
        col = line.split('\t')
        set_list.add(col[0])
        # print(col[0])
print(set_list)