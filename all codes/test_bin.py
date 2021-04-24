def deciTobin(n ,output):

	if n>1:
		deciTobin(n//2 , output)

	output.append(n%2)

output=[]
deciTobin(8 , output)
print(*output)

def binTodeci(n):
	i , last = 0,0
	ans=0
	while n!=0:
		last = n %10
		ans += last*pow(2,i)
		n = n//10
		i+=1

	return ans

a = binTodeci(1000)
print(a)
