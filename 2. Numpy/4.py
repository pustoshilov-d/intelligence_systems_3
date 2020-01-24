import numpy as np


b= a = np.eye(3,3)
print(a)

c = np.append(a,b, axis=0)
print(c)
