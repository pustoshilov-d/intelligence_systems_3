import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

data = pd.read_csv("data2.data")

print(data)

print(data.head())
print(data['veil-type'].describe())
print(data['veil-type'])

'''for i in data:
    print(i)
    print(data[i].value_counts().index)

    names = data[i].value_counts().index
    values = data[i].value_counts().values

    plt.subplot(131)
    plt.bar(names, values)
    plt.show()'''

'''data_new = data[data['type'] == 'e']
for i in data_new:
    print(i)
    print(data_new[i].value_counts().index)

    names = data_new[i].value_counts().index
    values = data_new[i].value_counts().values

    plt.subplot(131)
    plt.bar(names, values)
    plt.show()'''

'''data_new = data[data['type'] == 'p']
for i in data_new:
    print(i)
    print(data_new[i].value_counts().index)

    names = data_new[i].value_counts().index
    values = data_new[i].value_counts().values

    plt.subplot(i)
    plt.bar(names, values)
plt.show()'''


print(data.axes)

print(data[data['stalk-root'] != "?"].describe())
data_new = data[data['stalk-root'] != "?"]
print(data_new)
'''for i in data_new:
    print(i)
    print(data_new[i].value_counts().index)'''


data_new = shuffle(data_new)
print(data_new)
print(len(data_new))


data_train, data_test = np.split(data_new, [int(0.7*len(data_new))])

num_e = len(data_train[data_train['type'] == "e"])
num_p = len(data_train) - num_e



data_train_e = data_train[data_train['type'] == "e"]
data_train_p = data_train[data_train['type'] == "p"]

k = 3


for index_row, row in data_test.iterrows():

    prop_e = prop_e_s = num_e / len(data_train)
    prop_p = prop_p_s = 1 - prop_e


    for col in data_train:
        if col != "type":
            prop_e = prop_e * len(data_train_e[data_train_e[col] == row[col]]) / num_e
            prop_p = prop_p * len(data_train_p[data_train_p[col] == row[col]]) / num_p



            if len(data_train_e[data_train_e[col] == row[col]]) == 0:
                prop_e_s = prop_e_s * (len(data_train_e[data_train_e[col] == row[col]])+k) / (num_e + k*len(data_new[col].unique()))
            else:
                prop_e_s = prop_e_s * len(data_train_e[data_train_e[col] == row[col]]) / num_e

            if len(data_train_p[data_train_p[col] == row[col]]) == 0:
                prop_p_s = prop_p_s * (len(data_train_p[data_train_p[col] == row[col]])+k) / (num_p + k*len(data_new[col].unique()))
            else:
                prop_p_s = prop_p_s * len(data_train_p[data_train_p[col] == row[col]]) / num_p

    print("без смузи: ", prop_e, prop_p)
    print("c смузи: ", prop_e_s, prop_p_s)




# смузи
k = 3
