import pandas as pd
f = pd.read_csv('students2.csv')
print(f.head(3))
print(f.sort_values(['group','fio']))
print(f.axes)
print(f.groupby('group').mean()[['m1','m2','m3','m4','m5']])
print(f.loc[f['age'].max()])
'''print(f.iloc(f['age'].idxmax()))'''
