import time

t1=time.time()
result=[]
for a in range(2,101):
  for b in range(2,101):
    result.append(a**b)

print(len(set(result)))

t2=time.time()
print(t2-t1)
