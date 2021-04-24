#this is bubble sort algo for ascending

def bubble_sort_rs(arr):

	for i in range(0, len(arr)): #i denotes number of iterations
		swapped = False
		for j in range(0, len(arr)-i-1): #j is the pointer
			if arr[j] > arr[j+1] :
				arr[j] , arr[j+1] = arr[j+1] , arr[j] #swap 
				swapped = True
		

		if swapped == False: #if after any iteration not swapped = it is sorted no need to go further
			return
	return


li = [int(x) for x in input().split()]
bubble_sort_rs(li)
print(li)