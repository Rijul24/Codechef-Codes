#stable selection sort algo for ascending order

def find_min_idx(arr , start):
	min_idx = start

	start +=1
	while start < len(arr):
		if arr[start] <= arr[min_idx]: #applying equal to makes it stable
			min_idx = start
		start+=1

	return min_idx


def selection_sort_rs(arr):

	j=0
	while j < len(arr):
		min_idx = find_min_idx(arr,j)

		#now we need to swap if mi inddx not equal to j
		if min_idx !=j:
			arr[j] , arr[min_idx] = arr[min_idx] , arr[j]

		j+=1

	return #dont need to return anything as list is passed by refernce

li = [int(x) for x in input().split()]
a= selection_sort_rs(li)
print("sorted" , li)
