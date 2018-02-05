import time

t1=time.time()
def factorial(n):
  result=1
  for i in range(2,n+1):
    result*=i
  return result
  
total=0
for e in str(factorial(100)):
  total+=int(e)
print(total)
t2=time.time()
print(t2-t1)
