import time

t1=time.time()

def is_prime(n):
  if n == 2 or n==3 or n==5:
    return True
  if n%6 == 1 or n%6 == 5:
    i=2
    while i**2<=n:
      if n%i==0:
        return False
      i+=1
    return True
  return False


def primegen(n):
  for i in range (2,n):
    if is_prime(i):
      yield i

prime=[e for e in primegen(10**6//21+1)]

prime_len=len(prime)
length=1
candidate=2         #7.222335577011108 997651


for i in range(prime_len-1):
  for j in range(i+length,prime_len):
    if sum(prime[i:j]) <10**6:
      if is_prime(sum(prime[i:j])):
        length=j-i
        candidate=sum(prime[i:j])
    else:
      break

print(candidate)
t2=time.time()
print(t2-t1)
