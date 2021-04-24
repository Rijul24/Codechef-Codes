row, col = input().split()
row = int(row)
col = int(col)
cross_word = []
a=[]

for i in range(0,row):
	s = input()
	for k in range(0,len(s)):
		a.append(s[k])
	cross_word.append(a)
	orig_cross_Wor
#we have the crossword stored





w = int(input())
cross_dict = {}

for i in range(1,w+1):
	w1= input()
	l = len(w1)
	cross_dict[l]= w1
#stored all te cross-words
flag =  True
word_idx = []
for r in range(0,row):
	for c in range(0,col):
		ele= cross_word[r][c]
		current_row = cross_word[r]
		b_count = current_row.count('b')
		r_count = current_row.count('r')
		
		if b_count >2 or r_count >2: #not possible only one horizontal word
			print("Invalid")
			flag = False
			break;
		if b_count == 0 and r_count ==0: # skip no word to fill
			continue;
		if ele == '#' or ele == '.':
			continue;
		
		if ele == 'b' or ele == 'r':
			idx = current_row.index(ele)
			word_idx.append(idx)
	
	#now the row is checked for all the things 
	#fill the word
	if len(word_idx) == 2:
		
		start = word_idx[0]
		end = word_idx[1]
		length = end-start+1
		word_to_fill = cross_dict[length]
		row_to_fill =r
		j=0
		for i in range(start , end+1):
			if cross_word[row_to_fill][i] =='b' or cross_word[row_to_fill][i] =='r' or cross_word[row_to_fill][i] =='.':
				cross_word[row_to_fill][i] == word_to_fill[j]
				j+=1
			else:
				print("Invalid")
				break; 
	elif len(word_idx)!=0 :
		#something got missed this not a valid case
		print("Invalid")
		break;

	if flag == False:
		break; #invalid caseprinted

print(cross_word)