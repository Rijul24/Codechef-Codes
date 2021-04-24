#this quick sort algo
from random import randrange
def partition(arr , left , right):
	m = left # boundary variable
	pivot_index = randrange(left , right)
	pivot = arr[pivot_index] #stroing sp that it cant change

	arr[right], arr[pivot_index ] = arr[pivot_index] , arr[right] #swap with last elemnt necessary

	for i in range(left , right):
		if arr[i]<=pivot: #equal to is important
			arr[i], arr[m] = arr[m], arr[i]
			m += 1

	arr[m] , arr[right] = arr[right] , arr[m]#swap again back with last element

	return m  #return pivot index final


def quick_sort_rs(arr,left , right):

	if left >= right:
		return

	pivot_index = partition(arr ,left , right)
	quick_sort_rs(arr, left , pivot_index-1)
	quick_sort_rs(arr , pivot_index+1 , right)

	return #this is in place so dont need to return


li = [ int(x) for x in input().split()]
quick_sort_rs(li,0 , len(li)-1)
print(li)
