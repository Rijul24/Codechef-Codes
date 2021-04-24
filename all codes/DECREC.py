#decrpyt code here
def mapping(chef_words, enc_word,map_arr ):

	imp_words = []
	ref_list = ['a', 'b', 'c','d','e','f','g','h'] #for keeping track of indexes in 2d array

	for i in chef_words: #all words with same length are stored in a new array
		if len(enc_word) == len(i):
			imp_words.append(i)
	
	for imp_w in imp_words:
		j=0
		while j< len(enc_word):
			orig_letter= enc_word[j]
			imp_letter = imp_w[j]
			if orig_letter in ref_list and imp_letter in ref_list:
				orig_idx = ref_list.index(orig_letter)
				imp_idx = ref_list.index(imp_letter)
			else: #anythinbg other than those 8 alphabets
				j+=1
				continue;
			map_arr[imp_idx][orig_idx] = 1 # ARR[ROW][COL]
			j+=1
	#it maps the all possible encryption-decryption ways where row= encrpyted ; col = decrpyted
	for i in range(0,8):
		map_arr[i][i] = 0 #no same values! = unique mapping
	
	return map_arr
	


def map_finder(maparr , n , skip_iteration ):
	#maparr = for which we have to find ways , n= from which column we have to start
	k=0
	if n>7:   #base case
		k=-1

	col=n
	if k==0:
		for i in range(0,8) :
			if maparr[i][col]==1:
				if skip_iteration >0:
					skip_iteration -=1
					continue;
				row = i
				column = col
				for j in range(0,8): #puts every other element in row to zero
					if column !=j:
						maparr[row][j]=0
				for k in range(0,8): #puts every other element in column to zero
					if  row !=k:
						maparr[k][column]=0
	else:
		return maparr
	#now we have sol array with one step fixed in pathway 
	map_finder(maparr, n+1)
	return maparr
	#this goes to different columns and fixes a path and in the end returns the sol array


def decrpyt_string(dec_list, final_arr, chef_dict ):
	
	ref_list = ['a', 'b', 'c','d','e','f','g','h'] #for keeping track of indexes in 2d array
	flag = True
	decrpyt_word=" "
	print("here")
	for word1 in dec_list:
		#bringing encrypted word

		for char in word1:
			print(char)
			#going letter by letter
			count = False

			if char in ref_list:
				column = ref_list.index(char)
				for r in range(0,8):
					if final_arr[r][column] == 1:
						count= True
						row =r
						decrpt_letter = ref_list[row]
						print("hereeeeeeeeee")
						decrpyt_word += decrpt_letter
				if count == False: #if all zeroes in a column
					flag= False
					break;
			else:
				decrpt_letter = char #if any other alphabet add as it is
				decrpyt_word = decrypt_word + decrpt_letter

		if flag == False:
			return '-1'
		print(decrpyt_word)
		

	return decrypt_word





words = [] #stores chef's dictionary
n= int(input())

for i in range(0,n):
	words.append(input())

ref_list = ['a', 'b', 'c','d','e','f','g','h'] #for keeping track of indexes in 2d array
map_arr_original= [[0,0,0,0,0,0,0,0], #big brain concept 0 = no , 1= yes
[0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0] ] #made an empty mapping 2d array

map_arr_ways = map_arr_original
encrpyted_word = input().split() #stores whole encrypted string in list



for i in range(0, len(encrpyted_word)): #does all the mapping

	map_arr_ways = mapping(words, encrpyted_word[i] , map_arr_ways)

a= [[0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0], 
[1,0,0,0,0,0,1,0], 
[0,1,0,0,0,0,0,0], 
[0,0,0,0,0,1,0,0], 
[1,0,0,0,0,0,0,1], 
[0,1,0,0,0,0,1,0], 
[0,0,0,1,0,0,0,1] ]

c,r=0,0
counter = True
flag = True
count_of_ones = 0
k= 'error'
while c<8 and flag == True:
	count_of_ones = 0
	while r<8 and counter== True :
		counter = True
		if map_arr_ways[r][c]==1:
			
			solution_arr= map_finder(map_arr_ways, c , count_of_ones)
			count_of_ones +=1
			print(solution_arr , " ", count_of_ones)
			k= decrpyt_string(encrpyted_word, solution_arr,words)
			if k == '-1': #find another solution
				r+=1
				continue; 
			else:
				flag = False
				counter = False
		r+=1

	c+=1	

print (k)
	
















