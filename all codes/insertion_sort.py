#this is insertion sort algo ascending order

def insertion_sort_rs(arr):

	for i in range(1, len(arr)): #starts from 2nd elemnt
		ele = arr[i]
		j = i-1 #compaison on the left side

		while j>=0 and arr[j] > ele :
			arr[j+1] = arr[j] #alterntive for swapping
			j-=1

		arr[j+1] = ele #part of swapping

	return



li = [int(x) for x in input().split()]

insertion_sort_rs(li)
print(li)