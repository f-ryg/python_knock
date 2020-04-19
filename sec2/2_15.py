N = input("Write the number of lines to display: ")
f_hightemp = 'hightemp.txt'

with open(f_hightemp,'r') as f:
    lines = list(f)
    for line in lines[-int(N):]:
        print(line, end = "")
