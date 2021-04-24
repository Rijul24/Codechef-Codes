#this is merge sort algo 

def merge(array1 , array2): 
	
	#merges two sorted arrays

	l1 = len(array1)
	l2 = len(array2)

	output = [0]*(l1 + l2)
	i,j,k=0,0,0

	while ( i <l1 and j<l2): #till one of the array is exhausted loop goe on

		if array1[i] <= array2[j] : # equal to to make it stable
			#conbtender to be in final list is array1
			output[k] = array1[i]
			i+=1
			k+=1

		else:

			output[k] = array2[j]
			j+=1
			k+=1

	#now append the rest of the remaining elemnts

	while j<l2:
		output[k] = array2[j]
		j+=1
		k+=1
	
	while i<l1:
		output[k] = array1[i]
		i+=1
		k+=1

	#output array is ready 
	return output



def merge_sort_rs(arr , left , right):

	if left == right: #base case only one elemnt is sorted
		return [arr[left]] 

	mid = ( left + right) //2 

	left_array = merge_sort_rs(arr , left , mid)
	right_array = merge_sort_rs(arr, mid+1 , right)

	output = merge(left_array , right_array)

	return output


li = [int(x) for x in input().split()]
li = merge_sort_rs(li , 0 , len(li)-1)
print(li)
























