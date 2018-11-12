import pandas as pd
import math as math
import matplotlib.pyplot as plt
import numpy as np

# get the sector name
name = input('Please enter a sector name: ')

# get the observation period
d = int(input('Please enter the observation period (in hour): ')) * 60
duration = d * 60

# get the duration of one time step
step = int(input('Please enter the length of one time step (in minute): '))
step_sec = step * 60

# calculate the total step
n_step = int(d / step) + 1
print('Total number of time step:', n_step)

# create the list that contains the sector count for each time step
sector_count = [0] * n_step

# import csv data
DF = pd.read_csv("input.csv", sep=',')

# get the index of the data
idx = DF[DF.sectorname.str.contains(name, na=False)].index.tolist()

# create a new data frame to store the filtered data
DF_filtered = pd.DataFrame(columns=DF.columns)

# write data to the new filtered data frame
for i in idx:
    temp1 = DF.iloc[[max(0, i - 1), i, min(DF.index[-1], i + 1)]]
    DF_filtered = DF_filtered.append(temp1, ignore_index=True)
# print(DF_filtered, '\n')

# create a new data frame to store the transposed data frame
DF_trans = pd.DataFrame(columns=['plane_name',
                                 'begin_time',
                                 'leaving_time',
                                 'previous_sector',
                                 'current_sector',
                                 'next_sector'])

# write data to the transpose data frame
for row in range(1, len(DF_filtered.index), 3):
    temp2 = pd.DataFrame([[DF_filtered.at[row, 'planename'],
                           DF_filtered.at[row, 'crosstime'],
                           DF_filtered.at[row + 1, 'crosstime'],
                           DF_filtered.at[row - 1, 'sectorname'],
                           DF_filtered.at[row, 'sectorname'],
                           DF_filtered.at[row + 1, 'sectorname']]], columns=DF_trans.columns)
    DF_trans = DF_trans.append(temp2, ignore_index=True)
# DF_trans.to_csv('transpose_data.csv', index=False)
# print(DF_trans)

# calculate sector count
for line in DF_trans.index:
    if DF_trans.at[line, 'begin_time'] > duration:
        pass
    elif DF_trans.at[line, 'begin_time'] == duration:
        sector_count[n_step - 1] = sector_count[n_step - 1] + 1
    else:
        for i in range(math.ceil(DF_trans.at[line, 'begin_time'] / step_sec),
                       min(math.floor(DF_trans.at[line, 'leaving_time'] / step_sec) + 1, n_step)):
            sector_count[i] = sector_count[i] + 1
print('Total number of time step check:', len(sector_count), '\n')
print(sector_count)

# plotting
plt.plot(sector_count)
plt.xlabel('Time')
plt.ylabel('Sector count [number of aircraft]')
plt.title('Number of aircrafts in Sector '+name)
plt.axis([0, len(sector_count), 0, max(sector_count)+1])
plt.yticks(np.arange(0, max(sector_count)+1, 1))
# additional plotting parameters
plt.grid()
# plt.xticks(np.arange(0, len(sector_count), 5))
# plt.setp(plt.gca().get_xticklabels(), rotation=45, ha="right")
plt.show()

