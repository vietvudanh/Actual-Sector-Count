import pandas as pd

# get the sector name
x = input('Please enter a sector name: ')

# import csv data
DF = pd.read_csv("input.csv", sep=',')

# get the index of the data
idx = DF[DF.sectorname.str.contains(x, na=False)].index.tolist()

pd.DataFrame(columns=DF.columns).to_csv('result-'+x+'.csv', index=False)
pd.DataFrame(columns=DF.columns).to_csv('result-2-'+x+'.csv', index=False)

print(DF.iloc[0:5])


for i in idx:
    print(DF.iloc[[i - 1, i, i + 1]])
    temp1 = DF.iloc[[max(0, i-1), i, min(DF.index[-1], i+1)]]
    temp1.to_csv('result-'+x+'.csv', index=False, header=None, mode="a")
    temp2 = DF.iloc[[i, min(DF.index[-1], i+1)]]
    temp2.to_csv('result-2-' + x + '.csv', index=False, header=None, mode="a")

