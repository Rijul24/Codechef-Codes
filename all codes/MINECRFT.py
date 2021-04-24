#this is minecraft 
T= int(input())
import bisect
while T!=0:
	T-=1
	stacks =[]
	max_row=[]
	row , col , q = list(map(int , input().split()))
	for i in range(row):
		a=list(map(int , input().split()))
		max_row.append(max(a)) #stores max heoght of row
		stacks.append(a)

	poss_heights=[]
	for j in range(q):
		poss_heights.append(int(input()))

	#for every height we have to print the coordinate
	for h in poss_heights:
		idx = bisect.bisect_left(max_row , h)
		ans_row = idx
		for j in range(col):
			if stacks[ans_row][j] == h:
				print(ans_row , j )
				break;

