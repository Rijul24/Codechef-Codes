#complex prog here we go

def numb_op(matA , matB ,row_count ,col_count,sp_row_count,sp_col_count ):
	arr1 = max(row_count.count(0) , col_count.count(0))
	arr2 = min(row_count.count(0) , col_count.count(0))
	
	for idx in range(len(arr1)):
		
		ch = arr1[idx]
		
		while ch>1:
			change_row += 1
			ch -= 2

		if ch==1:
			if sp_row_count[idx]>0:
				change_row +=1











t = int(input())

while t!=0:
	t-=1
	row , col , E = list(map(int , input().split()))
#---------------------------------------------------------
	#taking first matrix
	arr=[]
	matA=[]
	for i in range(row):
		arr = list(input())
		matA.append(arr)

	#taking second matrix
	arr=[]
	matB=[]
	for i in range(row):
		arr = list(input())
		matB.append(arr)

#-----------------------------------------------------------	
	row_count=[]
	sp_row_count=[]
	for r in range(row):
		for c in range(col):
			ele1 = matA[r][c]
			ele2 = matB[r][c]
			
			if ele1!=ele2:
				if ele2 == '?':
					matB[r][c] = 'T'
				else:
					matB[r][c] = -1
			else:
				matB[r][c] = ' '
		
		currow = matB[r]
		row_count.append(currow.count(-1))
		sp_row_count.append(currow.count('T'))
			# '-1' means to be changed
			# 'T' signifies ? pos
			# rest all are spaces
	
#------------------------------------------------------------------
	col_count =[]
	sp_col_count=[]
	for c in range(col):
		count=0
		count1=0
		for r in range(row):
			ele = matB[r][c]
			if ele == -1 :
				count += 1
			if ele== 'T':
				count1 +=1

		col_count.append(count)
		sp_col_count.append(count1)
	
#-------------------------------------------------------------------

if E=0:
	ans = numb_op(matA , matB,row_count , col_count ,sp_row_count ,sp_col_count )