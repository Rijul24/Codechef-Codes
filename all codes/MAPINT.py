#this is street mapping
import bisect as b
middle_row = [0]
smiddle=[0]




n= int(input())
while n!=0:
	n-=1

	intpt_1 , intpt_2 , strt_name , direct = list(map(int , input().split()))
	strt_numb = strt_name[-1]

	#we store three rows
	if direct == 'E' or direct == 'W':
		if direct=='W':
			intpt_1 , intpt_2 = intpt_2 , intpt_1 #this is equivalent to east
		


		#store in middle for sure
		idx1 = b.bisect_right(middle_row , intpt_1)
		if idx1 >= len(middle_row):
			middle_row.append(intpt_1)
			smiddle.append(strt_numb)
		else:
			middle_row[idx1] = intpt_1
			smiddle[idx1] = strt_numb
		
		idx2 = b.bisect_right(middle_row , intpt_2)
		if idx2 >= len(middle_row):
			middle_row.append(intpt_2)
			smiddle.append(strt_numb)
		else:
			middle_row[idx2] = intpt_2
			smiddle[idx2] = strt_numb
		#stored street numb and imt pt in arrays at same indexes
		