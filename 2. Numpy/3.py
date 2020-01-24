import random
import numpy as np


a = (np.random.sample((1000,50))*100)
a = a.astype(int)
print(a)
print(a.shape)

a  = (a - a.mean()) / a.std()
print(a)

new = a.sum(axis=0)

new = np.argwhere(new>10)
print(new.reshape(-1))
print(new.size)