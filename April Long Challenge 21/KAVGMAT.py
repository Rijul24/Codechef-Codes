import sys

def get_inpt(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))

def p_str(x): sys.stdout.write(x+"\n")
def p_int(x): sys.stdout.write(str(x) + "\n")
def p_arr(arr): sys.stdout.write(" ".join(map(str, arr)) + "\n")

#worthy matrix
import bisect as bi
T= int(input())

while T!=0:
	T-=1
	row , col , K = list(map(int , input().split()))
	matrix = []
	pref_mat = []
	bin_mat = []
	new_arr=[]

	for i in range(row):
		arr = list(map(int , input().split()))
		pref_sum  =[0]*col
		pref_sum[0] = arr[0]

		for j in range(1,col):
			pref_sum[j] = pref_sum[j-1] + arr[j]

		pref_mat.append(pref_sum)
		matrix.append(arr)
		new_arr=[0]*col
		bin_mat.append(new_arr)

	#print(pref_mat)
	#pref mat is prefix of matrix
	for c in range(col):
		for r in range(row):
			if r!=0 :
				pref_mat[r][c] = pref_mat[r-1][c] + pref_mat[r][c]






	#first we check for single elements
	'''count =0
	for r in range(row):
		idx = bi.bisect_left(matrix[r] , K)
		if idx<col:
			count += (col - idx)'''

	#now we go every other matrix

	counter =0
	idx_r = row-1
	idx_c = 0

	while (idx_r<row and idx_r >=0) and (idx_c <col and idx_c>=0):
		ele = matrix[idx_r][idx_c]
		if ele >= K:
			#decrease value
			
			bin_mat[idx_r][idx_c]=1
			for c in range(idx_c , col):
				bin_mat[idx_r][c] = 1

			for r in range(idx_r , row):
				bin_mat[r][idx_c] = 1

			#decrease value
			idx_r-=1

		else:
			#increase value
			idx_c += 1


#--------------------------------------------------

	#print(bin_mat)
	res=0

	for r in range(row):
		idx = bi.bisect_left(matrix[r] , 1)
		for c in range(idx , col):
			
			if bin_mat[r][c]==1:

				end_r = r
				end_c = c

				res +=1

				start_r = r-1
				start_c = c-1

				while (start_r>=0 and start_r < row) and (start_c >=0 and start_c <col):
	

					#----------------------------------------------------------------------------------------
					avg = pref_mat[end_r][end_c]

					if (start_c-1 >=0 and start_c-1<col):
						avg = avg - pref_mat[end_r][start_c-1]
					if (start_r-1 >=0 and start_r-1<row) :
						avg = avg - pref_mat[start_r-1][end_c]

					if (start_c-1 >=0 and start_c-1<col) and(start_r-1 >=0 and start_r-1<row):
						avg = avg + pref_mat[start_r-1][start_c-1] 




					final_avg = (avg / ((end_c-start_c + 1)**2))
					if final_avg >= K:
						#print(avg , 'here1' , start_r , end_r , start_c , end_c)

						res+=1

					#------------------------------------------------------------------------------------------------------


					start_r -=1
					start_c-=1




	print(res)





'''	res = 0
	counter = 0
	for r in range(row):
		start_r = r

		for ext_counter in range(row):
			end_r = start_r + ext_counter

			for c in range(col):
				flag = True

				start_c = c
				end_c = c + ext_counter
				if end_c<col and end_r <row:

					#external checks--------------------------------
					min_ele = matrix[start_r][start_c]
					max_ele = matrix[end_r][end_c]

					if min_ele>=K :
						#print('here' , start_r , end_r ,start_c , end_c)
						res +=1
						flag = False
						continue;
					if max_ele<K:
						flag = False
						continue;

					#actually calculating avg---------------------
					if flag:
						
						avg = pref_mat[end_r][end_c]

						if (start_c-1 >=0 and start_c-1<col):
							avg = avg - pref_mat[end_r][start_c-1]
						if (start_r-1 >=0 and start_r-1<row) :
							avg = avg - pref_mat[start_r-1][end_c]

						if (start_c-1 >=0 and start_c-1<col) and(start_r-1 >=0 and start_r-1<row):
							avg = avg + pref_mat[start_r-1][start_c-1] 


					

						final_avg = (avg / ((end_c-start_c + 1)**2))
						if final_avg >= K:
							#print(avg , 'here1' , start_r , end_r , start_c , end_c)
					
							res+=1 '''




'''
	print(res)'''