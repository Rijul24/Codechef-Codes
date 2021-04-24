T= int(input())

def allSubSeq(test , subseq):
	n = len(test)

	#all single charcters
	'''for c in test:
		subseq.append(c)'''

	for i in range(0 , n-1):
		intial = test[0:i+1]

		for j in range(i+1 , n):
			end = test[j]
			res = intial + end
			subseq.append(res)
		#check for last char
		if i==n-2:
			res = intial + test[-1]
			subseq.append(res)




	'''for i in range(n-1):
		intial = test[:i+1]
		if i==0:
			subseq.append(intial)
		for j in range(i+1 , n):
			if i==0:
				subseq.append(test[j])
			res = intial + test[j]
			subseq.append(res)

		test2 = test
		test2 = test[i+1:]
		for k1 in range(i , len(test2)-1):
			intial = test2[:k1+1]
			if k1==0:
				subseq.append(intial)
			for k2 in range(k1+1 , len(test2)):
				if k1==0:
					subseq.append(test[0:i+1] + test2[k2])
				for m in range(i+1):
					#print( intial ,' ', test2[k2])
					res = test[0:i+1] + intial + test2[k2]
					subseq.append(res)

			if k1+1 == len(test2)-1:
				for m in range(i+1):
					#print( intial ,' ', test2[k2])
					res = test[0:i+1] + intial + test2[k1+1]
					subseq.append(res)'''


def binTodeci(n):
	n=int(n)
	i , last = 0,0
	ans=0
	while n!=0:
		last = n %10
		ans += last*pow(2,i)
		n = n//10
		i+=1

	return ans

def deciTobin(n ,output):
	n=int(n)
	if n>1:
		deciTobin(n//2 , output)

	output.append(n%2)






while T!=0:
	T-=1
	orig_bin = input()
	orig_numb= binTodeci(orig_bin)
	flag = False

	if orig_bin.count('0') ==0:
		flag= True
		print('0')
	elif orig_bin.count('1')==0:
		print('1')
		flag = True

	
	if flag == False:
		
		subseq=[]
		final_subseq=[]
		final_subseq.append('0')
		final_subseq.append('1')
		#-------------------------------------------------------------------------	
		for m in range(len(orig_bin)):
			test = orig_bin[m:]
			subseq=[]
			allSubSeq(test , subseq)
			subseq = set(subseq)
			subseq = list(subseq)
			#print(subseq)
			left = orig_bin[0:m+1]
			if m!=0:	
				for l in left:
					for c in subseq:
						RES = l + c
						for idx in range(len(RES)):
							if RES[idx]!='0':
								fl =True
								break;

						if fl:
							RES = RES[idx:]
						else:
							RES = '0'

						final_subseq.append( RES )
			else:
				for c in subseq:
					final_subseq.append(c)
		
		final_subseq = set(final_subseq)
		#print(final_subseq)

		#---------------------------------------------------------------------------
		for ele in range( 3 , orig_numb):
			output=[]
			deciTobin(ele , output)
			ele_bin =''
			for c in output:
				ele_bin += str(c)
			#if ele==12:
				#print('here' , ele_bin)
			if ele_bin not in final_subseq:
				flag= True
				break;

		if flag:
			ele_bin = int(ele_bin)
			print(ele_bin)
		else:
			ele = orig_numb + 1
			output=[]
			deciTobin(ele , output)
			ele_bin =''
			for c in output:
				ele_bin += str(c)			
			ele_bin = int(ele_bin)
			print(ele_bin)
	
