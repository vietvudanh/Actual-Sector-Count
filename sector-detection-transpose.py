import pandas as pd

# input the sector name
# x = input('Please input the sector name: ')

# creating the Data frame for transposing
DF = pd.DataFrame(columns=['planename', 'begintime', 'leavingtime', 'from', 'to'])

# load the input file
DF_in = pd.read_csv('result-2-T01.csv', sep=',')

# create the result file with header and empty data
DF.to_csv('result_tmp.csv', index=False)

# write the result
for row in DF_in.index:
    if row % 2 == 0:
        tmp = pd.DataFrame([[DF_in.at[row, 'planename'],
                             DF_in.at[row, 'crosstime'],
                             DF_in.at[row+1, 'crosstime'],
                             DF_in.at[row, 'sectorname'],
                             DF_in.at[row+1, 'sectorname']]])
        tmp.to_csv('result_tmp.csv', index=False, mode='a', header=None)
