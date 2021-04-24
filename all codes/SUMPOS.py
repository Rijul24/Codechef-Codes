#Sumpos Division 3
def sum_any(a,b,c):
	'''finds if any 2 nos add to give 3rd number '''
	if a+b==c:
		print("YES")
	elif a+c==b:
		print("YES")
	elif b+c==a:
		print("YES")
	else:
		print("NO")
T=int(input()) #test cases
while T!=0:
	T-=1
	x,y,z=input().split()
	x=int(x)
	y=int(y)
	z=int(z)
	sum_any(x,y,z)
#print(sum_any.__doc__)