#max overlap
T= int(input())
while T!=0:
	T-=1
	n = int(input()) #no of classes
	m = int(input()) 
	
	j=1
	arr=[]
	while j<=n:
		x,y= input().split()
		for i in range(int(x), int(y)+1):
			arr.append(i)
		j+=1

	#saved values of l and r
	
	class_array =[]
	for i in range(1,m):
		classes  = arr.count(i)
		class_array.append(classes)


	print( max(class_array))
	
