#this is interesting

t= int(input())


def max_xor(c,val):
	maxi = [0]


	for a in range(val-1 , 0 , -1):
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


	ans = max_xor(c,val)
	print(ans)



	







