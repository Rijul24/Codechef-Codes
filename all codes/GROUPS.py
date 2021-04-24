T= int(input())


while T!=0:
	T-=1
	string = input()
	idx =0
	grp =0
	while idx < len(string):

		seat = string[idx]

		if seat == '0' : 
			idx +=1
			continue;
		else: #seat is 1
			grp += 1
			i = idx +1
			while string[i] != '0':
				i+=1
			#after this loop index of i gives position of 1
			idx = i
	print(grp)
