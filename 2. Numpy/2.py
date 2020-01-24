import random
import numpy as np
a = (np.random.sample((1000,50))*100)
a = a.astype(int)
print(a)
print(a.shape)
a  = (a - a.mean()) / a.std()
print(a)
