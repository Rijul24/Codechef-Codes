def find_missing(arr):
	n = len(arr)
	lo = 0
	hi = n-1
	for i in range(max(arr)):
		flag = False
		while lo<=hi:
			mid=( lo + hi ) //2
			if arr[mid] == i:
				flag = True
				break;
			elif arr[mid]>i:
				hi = mid-1
			else:
				lo = mid+1

		if flag == False:
			print(i)
			break;
		