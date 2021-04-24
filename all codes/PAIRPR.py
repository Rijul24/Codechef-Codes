T= int(input())
 
def isPrime(n) :  
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True

    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True


while T!=0:
	T-=1
	n =int(input())
	
	pr = []
	flag , cout = False , False

	for i in range(2 , n+1):

		if isPrime(i) == True:
			flag = True
			pr.append(i)

			if len(pr)>1 and flag==True:
				for j in range(len(pr)-1):
					if pr[j] + i == n:
						print( pr[j] , i)
						cout = True
						break; 
					if pr[j]*2 == n:
						print( pr[j]  , pr[j] )
						print( pr[j] , i)
						cout = True
						break; 
		
		

		flag = False
		if cout == True:
			break;

	if cout == False:
		print( -1 , -1)
