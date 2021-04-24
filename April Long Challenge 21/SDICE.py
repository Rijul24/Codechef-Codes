#brute force
T= int(input())
while T!=0:
	T-=1
	n = int(input())
	if n>3:
		k1=0
		k2=0
		value1 , value2 , value3 , value4 =0,0,0,0
		'''
		#---------------------------------------
		value1 = 14*(n-1) + 20
		#----------------------------------------
		k1=n//2
		k2 = n % 2
		if k2 ==0:
			#value2 = 28*(k1-1) + 40
			value2 = 26*(k1-1) + 18+18
		elif k2 ==1:
			#value2 = 28*(k1-1) +  54
			value2 = 26*(k1-1) + 18 + 33

		#-------------------------------------------
		k1 = n//3
		k2= n%3
		if k2==0:
			value3 = 37*(k1-1) + 51
		elif k2==1:
			value3 = 37*(k1-1) + 47
		elif k2==2:
			value3 = 37*(k1-1) + 78
		'''
		#--------------------------------------------
		k1 = n//4
		k2 = n % 4
		value4=0
		if k1>0:
			if k2==0:
				value4 = 44*(k1-1) + 60
			elif k2==1:
				value4 = 44*(k1-1) + 56 +20
			elif k2==2:
				value4 = 44*(k1-1) + 88
			elif k2==3:
				value4 = 44*(k1-1) + 48 + 51


		value= max(value1 , value2 , value3 , value4)

	elif n==1:
		value = 20
	elif n==3:
	       value = 51
	else:
		value = 36

	print(value)


















'''
		if n%3==0:
			k = n//3
			value = 37*(k-1) +51
		elif n%4==0:
			k= n//4
			value = 44*(k-1) + 60
		else:
			k1 = n//4
			k2 = n%4
			if k2==1:
				value = 44*(k1-1) + 56 +20
			elif k2==2:
				value = 44*(k1-1) + 52 + 40
			elif k2==3:
				value = 44*(k1-1) + 48 + 51
			else:
				print('wrong')
           '''


	