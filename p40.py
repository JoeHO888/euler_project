import time

t1=time.time()
t2=time.time()
print(t2-t1)

#i=5+5.11111 no 
#123455
#i=0
#total=0
#while True:
#  if total>10**6:
#    break
#  total+=(i+1)*9*10**i
#  i+=1

#print(i)

test=""
for i in range(1,10**5+8*10**4+5*10**3+8*100):
  test+=str(i)
print(int(test[0])*int(test[9])*int(test[99])*int(test[999])*int(test[9999])*int(test[99999])*int(test[999999]))
