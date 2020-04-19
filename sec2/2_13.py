import pandas as pd

col1 = pd.read_csv('col1.txt',header = None, sep = '\t')
col2 = pd.read_csv('col2.txt',header = None, sep = '\t')
concat=pd.concat([col1,col2],axis = 1)
# print(concat)
concat.to_csv("merge.txt",header = False, index = False, sep = '\t')