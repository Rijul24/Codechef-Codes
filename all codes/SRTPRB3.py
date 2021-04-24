#this is sort fractions

length = int(input())
orig_arr = [int(x) for x in input().split()]
num_arr =[]
denom_arr=[]


for i in range(0,length):
	num_arr.append(orig_arr[i])
	denom_arr.append(orig_arr[i])

#we have stored num and denom in diff arrays
output=['null']*length
fract =[]
acc =[]
#first we eliminate no of infinity
for j in range(0 , len(denom_arr)):
	if denom_arr[j] == 0 and num_arr[j]>0:
		if num_arr[j] < output[length(output)-2] or output[length(output)-2] = 'null': #there will only be one infinity
			output[len(output)-2] = num_arr[j]
			output[le(output)-1] = denom_arr[j]
	if denom_arr[j] == 0 and num_arr[j]<0:
		if abs(num_arr[j]) < abs(output[0]) or output[0] = 'null' : #there will only be one negative infinity
			output[0] = num_arr[j]
			output[1] = denom_arr[j]

	if denom_arr[j] !=0:
		fr= num_arr[j] / denom_arr[j]
		
		if fr not in fract :
			fract.append(fr)
			acc.append(num_arr[j])
			acc1.append(denom_arr[j])
		else: #case of equivalence
			idx = fract.index(fr)
			n1 = acc[idx]
			d1= acc1[idx]
			if  n1 * d1 > 0 : #if pq>0 means first case
				if n1 < num_arr[j] : #this one is prefered then
					acc[idx] = n1
					acc1[idx] = d1
			if d1 > 0 and denom_arr[j] <0 :
				#r,s pref
				acc[idx] = n1
				acc1[idx] = d1
			if denom_arr[j] * d1 > 0:
				if abs(n1) < ans(num_arr[j]):
					#r,s pref
					acc[idx] = n1
					acc1[idx]  = d1

fr_sorted = fr.sorted()

#now for printing
#print any infinity
if output[0] != 'null':
	print(output[0] , output[1] , end= " ")

for f in fr_sorted():
	curr_fr_idx = fr.index(f)
	n = acc[curr_fr_idx]
	d = acc1[curr_fr_idx]
	print( n , d , end= " ")

#print any infinity
if output[-1] != 'null':
	print( output[-1] ,  output[-2] ,end=" " )
	