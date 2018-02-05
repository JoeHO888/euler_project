
import time

t1=time.time()
def examine(n,table,length=1):
  if n in table.keys():
    return table[n]+length
  else:
    if n%2==0:
      return examine(n//2, table,length+1)
    return examine(3*n+1, table,length+1)

longest=1
target=1
whole={1:0}
for i in range(1,10**6):
  whole[i]=examine(i,whole)
t2=time.time()

max_values = max(whole.values())
for e in whole:
  if whole[e] == max_values:
    print(e)

print(t2-t1)









  
