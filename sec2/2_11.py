with open('hightemp.txt','r') as f:
    count = 0
    for line in f:
        line.replace("\t",",")
        print(line,end="")