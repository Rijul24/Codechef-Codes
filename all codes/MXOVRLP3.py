T= int(input())
while T!=0:
	T-=1
	n= int(input())
	m= int(input())
	pos = [0]*(m+2)
	i=1
	while i<=n:
		start , end = input().split()
		start = int(start)
		end = int(end)
		#add +1 and -1 to start and end+1 resp
		pos[start] += 1
		pos[end+1] += -1
		i+=1

	#now we calculate prefix sum
	i=1
	while i < len(pos):
		pos[i] += pos[i-1] 
		i+=1

	#now max of all the numbers will give us max classes required 
	print(max(pos))
