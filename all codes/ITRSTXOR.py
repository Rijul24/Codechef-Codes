#this is interesting

t= int(input())


def max_xor(c,val ,k1):
	maxi = []


	for a in range(val-1 , k1-1 , -k1):
		maxi.append((a^c)*a) # a^c = b and we store a*b for all a's

	return max(maxi)






while t!=0:
	t-=1

	c= int(input())
	d=0
	while (2**d<c):
		d+=1
	val = 2**d
	#now for values 1 to val -1 we have to find potential values


	if c%2==0:
		#end bit is 0 which means we need 1,1 or 0,0 means 2 even or 2 odd
		ans1 = max_xor(c , val , 2 )
		ans2 = max_xor(c,val,1)
		print(max(ans2,ans1))


	else:
		#we need one even one odd
		ans = max_xor(c,val,2)
		print(ans)



	







