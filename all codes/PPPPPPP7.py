x = int(input())
i= 0
while 2**i <=x:
       
       i+=1
       
       
i=i-1

left = x - (2**i)

if x==1:
       print('1')
else:
       
       print(left + 1)
