#test
def test(l1 , l2):
	l1[0] +=1

	return

l1=[]
l2=[]

n= int(input())
for i in range(n):
	x= int(input())
	l1.append(x)
	l2.append(x)

test(l1 , l2)


#l1 and l2 shouldn;t be same
print(l1)
print(l2)		
