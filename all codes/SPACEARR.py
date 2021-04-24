#if first wins coin = 1

def printwin(n):
	if n %2 !=0:
		print("First")
	else:
		print("Second")

T= int(input())
while T!=0:
	T-=1

	l = int(input())
	arr = [int(x) for x in input().split()]

	org_arr= []
	for i in range(1 , l+1):
		org_arr.append(i)

	arr.sort() #will help reduce TC

	count = 1
	i=0
	#count odd means first turn , even means seconds turn
	while count>0:
		#same value of i should work beacuse it is sorted
		flag = False
		while i<l:
			if arr[i] < org_arr[i] :
				flag = True
				arr[i] +=1
				break;#his turn is  over
			i+=1
		if flag == False:
			#no item was found less than org arr so current player looses
			count +=1
			printwin(count)

		count +=1