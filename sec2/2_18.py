f_hightemp = 'hightemp.txt'

with open(f_hightemp,'r') as f:
    hightemp_lines = f.readlines()
    hightemp_lines.sort(key = lambda line:float(line.split('\t')[2]),reverse = True)
    #hightemp_lines.sort(key = lambda x:x[2],reverse = True) #和歌山県　かつらぎ　うまくいかない
    for line in hightemp_lines:
        print(line,end="")