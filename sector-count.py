import pandas as pd
import math as math

# get the time step, should be a divisor of 60
x = int(input('Please input the time step you want (in minute): '))

# second conversion
y = x*60

# get the input file
DF = pd.read_csv('result_tmp.csv', sep=',')

# calculate the total step
step = int(720/x) + 1
print(step)

# create the list that contains the sector count for each time step
sector_count = [0]*step

for row in DF.index:
    if DF.at[row, 'begintime'] > 43200:
        pass
    elif DF.at[row, 'begintime'] == 43200:
        sector_count[step] = sector_count[step] + 1
    elif DF.at[row, 'begintime'] < 43200:
        if int(DF.at[row, 'begintime']/y) == int(DF.at[row, 'leavingtime']/y):
            pass
        else:
            for i in range(math.ceil(DF.at[row, 'begintime']/y), math.floor(DF.at[row, 'leavingtime']/y)+1):
                sector_count[i] = sector_count[i] + 1
print(sector_count)
