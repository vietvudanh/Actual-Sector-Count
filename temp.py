import pandas as pd

DF1 = pd.DataFrame([['FLT01', 0, 00, 10, 'T01'],
                    ['FLT01', 0, 15, 25, 'T02'],
                    ['FLT02', 0, 30, 40, 'S01'],
                    ['FLT02', 0, 45, 55, 'S02'],
                    ['FLT03', 0, 60, 70, 'A01'],
                    ['FLT03', 0, 75, 85, 'A02']],
                   columns=['planename', 'emptycol','crosstime', 'noise', 'sectorname'])

DF2 = pd.DataFrame(columns=['planename', 'crosstime1', 'crosstime2', 'from', 'to'])
DF2.to_csv('result2.csv', index=False)

print(DF1, '\n')
print(DF2, '\n')
print(DF1.at[2, 'planename'], '\n')
tmp = pd.DataFrame([[DF1.at[0, 'planename'],
                    DF1.at[0, 'crosstime'],
                    DF1.at[0+1, 'crosstime'],
                    DF1.at[0, 'sectorname'],
                    DF1.at[0+1, 'sectorname']]], columns=DF2.columns)

print(tmp, '\n')

DF2 = DF2.append(tmp, ignore_index=True)
print(DF2)
# tmp.to_csv('result2.csv', index=False, mode='a', header=None)
