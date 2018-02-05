import time

t1=time.time()
total=0
for e in range(1,1001):
  total+=int(str(e**e)[-10:])
print(total)
t2=time.time()
print(t2-t1)
