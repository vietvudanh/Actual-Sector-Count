import pandas as pd
import math as math
import matplotlib.pyplot as plt
import numpy as np

'''
This part is to get all the needed input:
- name (in CAPITAL letter): the name of the sector we need to investigate;
- duration (in hour): period of time we need to investigate;
- step(in minute): duration of one time step;
- DF: the DataFrame that contain the input csv file;
'''

# get the sector name
name = input('Please enter a sector name: ')

# get the observation period
duration = int(input('Please enter the observation period (in hour): ')) * 3600

# get the duration of one time step
step = int(input('Please enter the length of one time step (in minute): ')) * 60

# import csv data
DF = pd.read_csv("input.csv", sep=',')

'''
This part defines all needed functions for the program
parameters in the function, need to be synchronized:
- d: duration of observed period
- st: duration of one time step
- nst: total time step
- df: DataFrame name
- sn: sector name
- idx: list containing index
- count: list that contains sector count for each time step
'''

# calculate the number of time steps
'''
def no_of_step(d, st):
    t_step = int(d / st) + 1
    return t_step
'''


# filtered data and write it to a new DataFrame
def fil_df(df, sn):
    idx = df[df.sectorname.str.contains(sn, na=False)].index.tolist()
    filtered_df = pd.DataFrame(columns=df.columns)
    for i in idx:
        temp1 = df.iloc[[max(0, i - 1), i, min(df.index[-1], i + 1)]]
        filtered_df = filtered_df.append(temp1, ignore_index=True)
    return filtered_df


# convert data
def transpose_df(df):
    tdf = pd.DataFrame(columns=['plane_name',
                                'begin_time',
                                'leaving_time',
                                'previous_sector',
                                'current_sector',
                                'next_sector'])

    for row in range(1, len(df.index), 3):
        temp = pd.DataFrame([[df.at[row, 'planename'],
                              df.at[row, 'crosstime'],
                              df.at[min(row + 1, len(df.index) - 1), 'crosstime'],
                              df.at[row - 1, 'sectorname'],
                              df.at[row, 'sectorname'],
                              df.at[min(row + 1, len(df.index) - 1), 'sectorname']]], columns=tdf.columns)
        tdf = tdf.append(temp, ignore_index=True)
    return tdf


# function to calculate sector count
def sector_count(df, d, st):
    nst = int(d / st) + 1
    count = [0] * nst
    for line in df.index:
        if df.at[line, 'begin_time'] > d:
            pass
        elif df.at[line, 'begin_time'] == d:
            count[nst - 1] = count[nst - 1] + 1
        elif df.at[line, 'begin_time'] < d:
            if int(df.at[line, 'begin_time'] / st) == int(df.at[line, 'leaving_time'] / st):
                pass
            else:
                for i in range(math.ceil(df.at[line, 'begin_time'] / st),
                               min(nst, math.floor(df.at[line, 'leaving_time'] / st) + 1)):
                    count[i] = count[i] + 1
    return count


# output to csv file
def output_csv_no_index(df, sn):
    df.to_csv('result/result-' + sn + '.csv', index=False)


# plotting function
def plotting(count, sn):
    plt.plot(count)
    plt.xlabel('Time')
    plt.ylabel('Sector count [number of airplanes]')
    plt.title('Number of airplanes in Sector ' + sn)
    plt.axis([0, len(z), 0, max(z) + 1])
    plt.yticks(np.arange(0, max(z) + 1, 1))
    # additional plotting parameters
    plt.grid()
    # plt.xticks(np.arange(0, len(sector_count), 5))
    # plt.setp(plt.gca().get_xticklabels(), rotation=45, ha="right")
    plt.show()


# write data to the new DataFrame
x = fil_df(DF, name)
# print(x)

# convert data
y = transpose_df(x)

# sector count
z = sector_count(y, duration, step)

# output result
# output_csv_no_index(y, name)

# plotting
plotting(z, name)

