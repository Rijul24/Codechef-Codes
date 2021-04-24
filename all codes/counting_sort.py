# this is counting sort

def counting_sort_rs(arr):

	#making freq array
	freq = [0]*(max(arr)+1)

	#filling freq array
	for i in range(0, len(arr)):
		freq[arr[i]] += 1

	#preparing prefix sum array 

	for i in range(1,len(freq)):
		freq[i] += freq[i-1]

	#now we have prefix sum and need to create sorted array

	sorted_Arr = [0]*(len(arr))

	for i in range(len(arr)-1 , -1 , -1): #starts from last goes till 0th element
		sorted_Arr[freq[arr[i]]-1] = arr[i] #at freq we have the position so -1 to obtain idx
		freq[arr[i]] -=1 #reducing filled freq


	return sorted_Arr


li = [int(x) for x in input().split()]
li = counting_sort_rs(li)
print(li)

