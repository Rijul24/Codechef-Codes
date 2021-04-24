#acm contest
T= int(input())
while T!=0:
	T-=1
	n= int(input())
	ppl=[]
	ppl = list(input())

	i,grp =0,0
	female , male =0,0

	while i<n:
		ele = ppl[i]
		if ele =='M':
			male +=1
		else:
			female+=1
		if female == male:
			grp +=1
			male,female = 0,0
		i+=1
	print(grp)