import pandas as pd

f = pd.read_csv('students.csv')


for i in f[f['mark']>4]['Name']:
    print(str(i).lower())