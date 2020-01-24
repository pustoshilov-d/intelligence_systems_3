c = [i*3 for i in "okey google"]
print(c)
c.clear()
for i in range(1,10):
    c.extend((i,i,i))
print(c)