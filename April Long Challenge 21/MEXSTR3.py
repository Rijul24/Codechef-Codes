
def binaryToDecimal(x): # inp -> Bstring; out -> int
    x = list(x); sum = 0
    for i in range(len(x) - 1, -1, -1):
        sum += int(x[i])*pow(2, len(x)-i-1)
    return sum

def decimalToBinary(n): # inp -> int; out -> string
    return "{0:b}".format(int(n))


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
	
	
def isSubsequence(a, target): # is target subseq of a
    i = 0; j =0
    while i < len(target) and j < len(a):
        if a[j] == target[i]:
            i += 1
        j += 1
    return i == len(target)
    
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




	orig_num = binaryToDecimal(orig_str)



	for i in range( 0 ,orig_num+2):
		ele_bin= decimalToBinary(i)

	
		#print(ele_bin , orig_str)
		if isSubsequence(orig_str , ele_bin)== False:
			break;
			
	print(ele_bin)