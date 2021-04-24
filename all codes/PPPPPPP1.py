# cook your dish here
lvl , pos = list(map(int , input().split()))
import math
numb = 2**(lvl-1)

if pos>4:
       '''
       unit = round(pos/numb , 1)
       unit = int(unit*10)'''
       unit = math.ceil(pos/4)
else:
       unit = math.ceil(pos/4) 
#print(unit)
arr1=['ABBA', 'BAAB','BAAB', 'ABBA']
arr2 = ['BAAB', 'ABBA' , 'ABBA' , 'BAAB']
upos = pos%4
no_units = numb//4

which_unit = math.ceil(unit/4)
if which_unit %2==0:
       #print('here')
       idx = unit % 4
       ele = arr2[idx-1]
       ans = ele[upos-1]
else:
       idx = unit % 4
       ele = arr1[idx-1]
       #print(ele , upos)
       ans = ele[upos-1]      

                    
if ans == 'A':
       print('Apple')
else:
       print('Banana')