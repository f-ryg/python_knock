import math

N = int(input("Write the number: "))
f_hightemp = 'hightemp.txt'

with open(f_hightemp,'r') as f:
    lines = f.readlines()

count = len(lines)
split = math.ceil(count/N)

for i,number in zip(range(0,count,split),range(split)):
    with open("split_{}_file{}.txt".format(N,number),"w") as w_file:
        for line in lines[i:i+split]:
            w_file.write(line)