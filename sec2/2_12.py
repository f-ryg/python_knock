import pandas as pd

data = pd.read_csv('hightemp.txt',header = None, sep = '\t')
# print(data)
col1 = data[[0]]
col2 = data[[1]]
col1.to_csv("col1.txt",header = False, index = False)
col2.to_csv("col2.txt",header = False, index = False)
