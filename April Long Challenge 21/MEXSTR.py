def binTodeci(n):
	i , last = 0,0
	ans=0
	while n!=0:
		last = n %10
		ans += last*pow(2,i)
		n = n//10
		i+=1

	return ans

def deciTobin(n ,output):

	if n>1:
		deciTobin(n//2 , output)

	output.append(n%2)

def isSubseq(test , orig):
	test = list(test)
	n = len(test)
	orig = list(orig)

	i=1
	flag = False
	if test[0] in orig:

		idx = orig.index(test[0])
		flag = True

	while i<n:
		ele = test[i]
		if ele in orig:
			try:

				idx = orig.index(ele , idx+1)
			except:
				return False
		i+=1
	return True


T = int(input())

while T!=0:
	T-=1
	orig_str  = input()




	orig_num = binTodeci(int(orig_str))

	flag = False
	if orig_str.count('0') ==0:
		flag= True
		print('0')
	elif orig_str.count('1')==0:
		print('1')
		flag = True


	if flag == False:

		for i in range( 3 ,orig_num+2):
			output=[]
			ele_bin=''
			deciTobin(i,output)
			for c in output:
				ele_bin += str(c)

			ele_bin = str(ele_bin)
			#print(ele_bin , orig_str)
			if isSubseq(ele_bin , orig_str)== False:
				break;
				
		print(ele_bin)