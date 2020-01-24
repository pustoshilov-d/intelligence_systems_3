import numpy as np

a = np.arange(24).reshape(4,6)
for i in range(len(a)):
    if i % 2 == 1:
        print(a[i,][::-1])
    else:
        print(a[i,])