import pandas as pd
f= pd.read_csv('books.csv')
print('Books are loaded\n')
while True:
    print('Press\n 1 to show all books\n 2 to search\n 3 to delete book\n 4 to insert')
    bt = input()
    if bt == '1': print(f)
    elif bt == '2':
        print('Что?')
        bt2 = input().split(',')
        print(bt2)
        print(f[f[bt2[0]] == bt2[1]])
    elif bt == '3':
        print('Write index')
        bt2 = input()
        f[f['index'] == int(bt2)] = None
    elif bt == '4':
        print('Write all axes')
        bt2 = input().split(',')
        print(bt2)
        print(type(bt2))

        bt2 = pd.Series(bt2, index = ['index','author','title','year'])
        f = f.append(bt2, ignore_index=True)
        print(f)



        ##5,Jaja,Kinky,2022


        