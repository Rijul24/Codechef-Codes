n , v = list(map(float , input().split()))
arr = list(map(float , input().split()))
n = int(n)

arr.sort(reverse = True)



def coins(arr , v , k1 , res):
       
       ans =0.00
       orig_v = k1
       for ele in arr:
              flag = True
              i = 1.00
              while flag == True:
                     if v>= i*ele:
                            #print(round(i*ele ,  , v)
                            orig_v = round(v,2)
                            #print(orig_v , i*ele)
                            orig_v = orig_v - round(i*ele ,2)
                            i += 1.00 
                     else:
                            break;
              ans += (i-1)
              #print(ans)
              v = round(orig_v , 2)
       
       #print('here' ,ans , v)
              
       if v==0:
              res.append(ans)
              
       
       if len(arr) !=0:
              
              arr.pop(0)
              #print(arr , k1)
              coins(arr , k1 , k1 , res)
              
       return res



res = []
ans = coins(arr , v , v , res)
if len(res)  ==0:
       pr = 0
else:
       pr = min(res)
print(int(pr))