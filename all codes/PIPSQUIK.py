T= int(input())

while T!=0:
	T-=1
	barrier , height , duck , jump , life = list(map(int , input().split()))
	count=0
	for i in range(barrier):
		t , h_barr = list(map(int , input().split()))
		
		if t==1 and life!=0:
			#needs to duck
			if height-duck<= h_barr:
				count+=1
			else:
				life-=1
				if life ==0:
					continue;
				else:
					count+=1

		if t==2 and life != 0:
			#need to jump

			if jump >= h_barr:
				count+=1
			else:
				life-=1
				if life ==0:
					continue;
				else:
					count+=1

	print(count)