def reverse_arr(li , st, en):
	while st<en:
		temp = li[st]
		li[st] = li[en]
		li[en] = temp
		st+=1
		en-=1

def rotate(li , k ):
	n = len(li)
	k = k%n #for cases where k>n
	reverse_arr(li , 0 ,n-1)#reverse whole list
	reverse_arr(li , 0 ,k-1)#reverse forst seg
	reverse_arr(li , k , n-1) #reverse second deg
	# 1 2 3 4 5 6 7 k=3
	# 7 6 5 4 . 3 2 1
	#5 6 7 . 1 2 3 4

li = [int(x) for x in input().split()]

k= int(input())

rotate(li , k)

print(li)
