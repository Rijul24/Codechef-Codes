#this is map int
n= int(input())
strt={'street1':set()}
int_pts = {} 

while n!=0:
	n-=1
	intpt_1 , intpt_2 , strt_name , direct = list(map(str , input().split()))
	intpt_1 = int(intpt_1)
	intpt_2 = int(intpt_2)

#-----------------------------------------------------------------------------------------------
	if direct == 'E' or direct == 'W':
		

























	if strt_name not in strt.keys():
		strt[strt_name] = {min(intpt_1 , intpt_2) , max(intpt_1, intpt_2)}
	else:
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