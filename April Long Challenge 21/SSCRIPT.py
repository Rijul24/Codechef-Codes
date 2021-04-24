T = int(input())

while T!=0:
	T-=1
	n , k_orig = list(map(int , input().split()))
	orig_str = input()
	
	if orig_str[0] =='*':
		k=1
		count=1
	else:
		k=0
		count =0

	i=1
	flag = False
	while i<n:
		char = orig_str[i]
		if count>=k_orig:
			#print( i , 'here')
			flag = True
			break;
		
		#print(char)
		if char == "*":
			k=1
			count += 1
			i+=1
			'''if k==1:				
				count+=1
				k=1
				i+=1
			else:
				k=1
				i+=1'''
		else:
			count =0
			k=0
			i+=1
	if i>=n:
		if count>=k_orig:
			flag = True


	if flag:
		print('yes')
	else:
		print('no')