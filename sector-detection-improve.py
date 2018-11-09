import pandas as pd

# get the sector name
x = input('Please enter a sector name: ')

# import csv data
DF = pd.read_csv("input.csv", sep=',')

# get the index of the data
idx = DF[DF.sectorname.str.contains(x, na=False)].index.tolist()

# pd.DataFrame(columns=DF.columns).to_csv('result-'+x+'.csv', index=False)
# pd.DataFrame(columns=DF.columns).to_csv('result-2-'+x+'.csv', index=False)

# create a new data frame to store the filtered data

DF_filtered = pd.DataFrame(columns=DF.columns)


for i in idx:
    # print(DF.iloc[[i - 1, i, i + 1]])
    temp1 = DF.iloc[[max(0, i-1), i, min(DF.index[-1], i+1)]]
    DF_filtered = DF_filtered.append(temp1, ignore_index=True)
    # temp1.to_csv('result-'+x+'.csv', index=False, header=None, mode="a")
    # temp2 = DF.iloc[[i, min(DF.index[-1], i+1)]]
    # temp2.to_csv('result-2-' + x + '.csv', index=False, header=None, mode="a")

# create a new data frame to store the transposed data
DF_trans = pd.DataFrame(columns=['plane_name',
                                 'begin_time',
                                 'leaving_time',
                                 'previous_sector',
                                 'current_sector',
                                 'next_sector'])
for row in range(1, len(DF_filtered.index), 3):
    # if row % 2 == 1:
        temp2 = pd.DataFrame([[DF_filtered.at[row, 'planename'],
                             DF_filtered.at[row, 'crosstime'],
                             DF_filtered.at[row+1, 'crosstime'],
                             DF_filtered.at[row-1, 'sectorname'],
                             DF_filtered.at[row, 'sectorname'],
                             DF_filtered.at[row+1, 'sectorname']]], columns=DF_trans.columns)
        DF_trans = DF_trans.append(temp2, ignore_index=True)

# print(DF_filtered, '\n')

print(DF_trans)
