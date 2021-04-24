#this is map int
n= int(input())
strt={'test':set()}
int_pts = {} 

while n!=0:
	n-=1
	intpt_1 , intpt_2 , strt_name , direct = list(map(str , input().split()))
	intpt_1 = int(intpt_1)
	intpt_2 = int(intpt_2)

#-----------------------------------------------------------------------------------------------
	if direct == 'E' or direct == 'W':
		

		if strt_name not in strt.keys():
			if direct == 'E':
				strt[strt_name] = {intpt_1 , intpt_2}
			else:
				strt[strt_name] = {intpt_2 , intpt_1}
		else:

			if intpt_1 in strt[strt_name] or intpt_2 in strt[strt_name]:
				if (intpt_1 in strt[strt_name] and direct =='W') or (intpt_2 in strt[strt_name] and direct == 'E'):
					# 4 , 1 , E   or 1,4,W 
					temp = list(strt[strt_name])
					if intpt_1 in strt[strt_name]:
						#add input 2 before input 1
						idx = temp.index(intpt_1)
						temp.insert(idx , intpt_2)
					if intpt_2 in strt[strt_name]:
						#add input 1 before input 2
						idx = temp.index(intpt_2)
						temp.inser6(idx , intpt_1)
					strt[strt_name] = set(temp)

				else:
					#1,4,E or 4,1, W
					#directy add
					strt[strt_name].add(intpt_1)
					strt[strt_name].add(intpt_2)


	if direct == 'N' or direct == 'S':
	

		if strt_name not in strt.keys():
			if direct == 'S':
				strt[strt_name] = {intpt_1 , intpt_2}
			else:
				strt[strt_name] = {intpt_2 , intpt_1}
		else:

			if intpt_1 in strt[strt_name] or intpt_2 in strt[strt_name]:
				if (intpt_1 in strt[strt_name] and direct =='N') or (intpt_2 in strt[strt_name] and direct == 'S'):
					# 4 , 1 , E   or 1,4,W 
					temp = list(strt[strt_name])
					if intpt_1 in strt[strt_name]:
						#add input 2 before input 1
						idx = temp.index(intpt_1)
						temp.insert(idx , intpt_2)
					if intpt_2 in strt[strt_name]:
						#add input 1 before input 2
						idx = temp.index(intpt_2)
						temp.inser6(idx , intpt_1)
					strt[strt_name] = set(temp)

				else:
					#1,4,E or 4,1, W
					#directy add
					strt[strt_name].add(intpt_1)
					strt[strt_name].add(intpt_2)


	if intpt_1 not in int_pts.keys():
		int_pts[intpt_1]= {strt_name}
	else:
		int_pts[intpt_1].add(strt_name)

	if intpt_2 not in int_pts.keys():
		int_pts[intpt_2] = {strt_name}
	else:
		int_pts[intpt_2].add(strt_name)

print(strt)
print()
print(int_pts)


#now we see how many good intersections
count =0
for intersection in int_pts.keys():
	str_passing = int_pts[intersection]
	if len(str_passing) == 1 or len(str_passing) >=3:
		continue;
	else:
		#number of streets passign are two
		#now check it should pass THROUGH
		str_passing = list(str_passing)
		s1 = str_passing[0]
		s2 = str_passing[1]
		
		int_for_street1 = list(strt[s1])
		int_for_street2 = list(strt[s2])


		if int_for_street1[0] != intersection and int_for_street1[-1] != intersection and int_for_street2[0] != intersection and int_for_street2[-1] != intersection:
			count +=1


print(count)	