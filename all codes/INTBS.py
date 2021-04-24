def find_ones(arr):
	n = len(arr)
	lo = 0 
	hi = n-1
	mid = 0
	while lo<=hi:
		mid = (lo + hi )//2
		if arr[mid] ==1:
			return mid
		else:
			lo = mid+1
	return lo


li = list(map(int , input().split()))
c = find_ones(li)
print( len(li) - c)

