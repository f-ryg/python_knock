f_hightemp = 'hightemp.txt'

# with open(f_hightemp,'r') as f:
#     hightemp_lines = f.readlines()
hightemp_lines = open(f_hightemp).readlines()
data = {}
for line in hightemp_lines:
    prefec = line.split("\t")[0]
    data[prefec] = data.get(prefec, 0) + 1
    sorted_data = sorted(data.items(), key = lambda x:x[1],reverse =True)
for result in sorted_data:
    print(result)
