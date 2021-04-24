#this is DECREC


def permut(skip):
	ref_list = ['a','b','c','d','e','f','g','h']
	map_list= ['a','b','c','d','e','f','g','h']
	skip_orig = skip
	i=0
	solution_dict = {}
	while i < 8:
		skip = skip_orig
		ref_ele = ref_list[i]
		j=0
		solution_dict = maptodict(j , solution_dict, ref_ele , map_list , skip)
		i+=1
	return solution_dict


def maptodict(start , dic, eletomap, maplist , skip):

	temp =0
	while start<len(maplist):
		print( start , "here" , eletomap , maplist[start] , skip)
		while skip >0: #skip iterations for different values
			skip-=1
			start+=1
			continue;

		if maplist[start] != eletomap and maplist[start]!=0:
			temp = start
			dic[eletomap] = maplist[start]
			break;
		start+=1
	
	maplist[temp] =0 #remov the mapped element
	return dic


s=0
while s<8 :
	d= permut(s)
	print(d)
	s+=1