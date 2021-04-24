T= int(input())
while T!=0:
	T-=1
	n , egg , bars , item1 , item2 , item3 = list(map(int , input().split()))
	count1 , count2 , count3 = 0,0,0
	

	#for item3
	while egg>0 and bars>0 :
		egg-=1
		bars-=1
		count3+=1
	

	#for item 2
	while bars>0:
		bars-=3
		count2+=1

	#for item1
	while egg>0:
		egg-=2
		count1+=1

	count = count1 +count2 +count3

	if count > n :
		extra = n-count
		costs = [0,1,2]
		idxs=[0,1,2]
		cost = [item1 , item2 , item3]
		indexes = [count1 , count2 , count3]
		costs[2] , idxs[2] = max(cost) , indexes[cost.index(max(cost))] 
		costs[0] , idxs[0] = min(cost) , indexes[cost.index(min(cost))]
		cost.remove(max(cost))
		cost.remove(min(cost))
		indexes.remove(idxs[2])
		indexes.remove(idxs[0])

		costs[1] , idxs[1] = cost[0] , indexes[0]

		#now we have costs in imcreasing order
		while idxs[2]>0 and extra>0:
			idxs[2]-=1
			extra-=1

		while idxs[1]>0 and extra>0:
			idxs[1]-=1
			extra-=1

		while idxs[0]>0 and extra>0:
			idxs[0]-=1
			extra-=1

		#we have the minimal count of items there
		final_ans = costs[2] *idxs[2] + costs[1]*idxs[1] + costs[0]*idxs[0]
		print(final_ans)


	elif count ==n:
		final_ans = item1*count1 + item2 * count2 + item3*count3
		print(final_ans)
	


	else:
		print(-1)

