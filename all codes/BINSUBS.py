#binary subsequence div 3
#case missing where already nondecreasing string is there

def str_bin(s):
	''' function checks if every element is 0 or 1 and counts them '''
	i,z,o=0,0,0
	while i<len(s):
		if s[i]=="0":
			z+=1
		elif s[i]=="1":
			o+=1
		else:
			return False
		i+=1
	a=[o,z]	
	return a	
#test case starts here		
T=int(input())
sum=0
while T!=0:
	if sum<10*6:
		N=int(input())
		s=input()
		if str_bin(s):
			a=str_bin(s)
			#no of zeroes are more or one's
			if a[1]<a[0]:
				if s[0]=="0":
					print(a[1]-1)
				else:
					print(a[1])
			else:
				print(a[0])
		else:
			break;
		sum+=N
		T-=1
	else:
		break;