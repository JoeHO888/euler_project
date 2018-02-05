import time
import math
t1=time.time()


def is_prime(n):
  if n==2 or n==3:
    return True
  if n%6==1 or n%6==5:
    i=2
    while i**2 <= n:
      if n%i ==0:
        return False
      i+=1
    return True
  return False


def prime_generator(n):
  for i in range(3,n,2):
    if is_prime(i):
      yield i
first=[2]+[e for e in prime_generator(math.ceil(math.sqrt(50*10**6+1)) )]
second=[2]+[e for e in prime_generator(math.ceil((50*10**6+1)**(1.0/3)))]
last=[2]+[e for e in prime_generator(math.ceil((50*10**6+1)**(1.0/4)))]

count=[]
for i in range(len(first)):
  for j in range(len(second)):
    if first[i]**2+second[j]**3>=50*10**6:
      break
    for k in range(len(last)):
      if first[i]**2+second[j]**3+last[k]**4<50*10**6:
        count.append(first[i]**2+second[j]**3+last[k]**4)
      else:
        break

#print(len(count))
print(len(set(count)))
t2=time.time()

print(t2-t1)



















  
  
