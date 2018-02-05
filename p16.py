import time

t1=time.time()
total=0
for e in str(2**1000):
  total+=int(e)

print(total)
t2=time.time()
print(t2-t1)
