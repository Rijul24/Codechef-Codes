#max overlap
T= int(input())
while T!=0:
	T-=1
	n = int(input()) #no of classes
	m = int(input()) 
	start_time=[]
	end_time=[]
	i=1
	while i<=n:
		x,y= input().split()
		start_time.append(int(x))
		end_time.append(int(y))
		i+=1
	#saved values of l and r
	i=1
	class_array =[]
	while i<=m:
		classes=0
		for j in range(0,len(start_time)):
			if start_time[j] == i :
				classes +=1
			if  start_time[j]< i  and end_time[j]<=i :
				classes +=1  
				
		class_array.append(classes)
		i+=1
	print( max(class_array))
	
