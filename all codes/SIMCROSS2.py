row, col = input().split()
row = int(row)
col = int(col)
cross_word = []
orig_cross_word = []


for i in range(0,row):
    a=[]
    s = input()
    for k in range(0,len(s)):
    	a.append(s[k])
    cross_word.append(a)
    orig_cross_word.append(a)
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
	word_idx=[]
	for c in range(0,col):
		ele= cross_word[r][c]
		current_row = cross_word[r]
	
		b_count = current_row.count('b')
		r_count = current_row.count('r')
	
		
		if b_count >2 or r_count >2: #not possible only one horizontal word
			print("Invalid1")
			flag = False
			break;
		if b_count == 0 and r_count ==0: # skip no word to fill
			continue;
		if ele == '#' or ele == '.':
			continue;
		
		if ele == 'b' or ele == 'r':
			word_idx.append(c)

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
			if cross_word[row_to_fill][i] !='#' :
				cross_word[row_to_fill][i] = word_to_fill[j]
				j+=1
			else:
				print("Invalid2")
				break; 


	if flag == False:
		break; #invalid caseprinted

#now all the rows are filled time for columns
#we will check for b and c in orig array and fill in cross word array

for c in range(0,col):
	word_idx=[]
	for r in range(0,row):
		ele= orig_cross_word[r][c]
		if ele == '#' or ele == '.':
			continue;
		
		if ele == 'b' or ele == 'c':
			word_idx.append(r)

	#now the column is checked for all the things 
	#fill the word

	if len(word_idx) == 2:
		start = word_idx[0]
		end = word_idx[1]
		length = end-start+1
		word_to_fill = cross_dict[length]
		column_to_fill =c
		j=0
	    
		for i in range(start , end+1):
			letter_to_fill = word_to_fill[j]
			ele_at_pos = cross_word[i][column_to_fill]
			if ele_at_pos != '#':
				if ele_at_pos == letter_to_fill or ele_at_pos == 'b' or ele_at_pos == 'c' or ele_at_pos == '.':
					cross_word[i][column_to_fill] = letter_to_fill  
					j+=1
				else:
					print("Invalid")
					break;
			else:
				print("Invalid2")
				break; 

print(cross_word)