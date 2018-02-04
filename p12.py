import time

t1=time.time()
def number_of_divisor(n,end,start=1, total=0):
  for j in range(start,end,1+n%2):
    if n%j ==0:
      return number_of_divisor(n,n//j,j+1+n%2,total+2)
  return total


threshold=500
i=0
while True:
  target=int(i*(i+1)/2)
  if number_of_divisor(target,target)>=threshold:
    print (target)
    break
  i+=1

t2=time.time()
print(t2-t1)
