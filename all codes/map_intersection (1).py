def no_of_intersections(maps):
	frequency={}
	frequency_street={}
	for i in range(n):
		a=maps[i][0]
		name=maps[i][2]
		street=[]
		street.append(a)
		street.append(name)
		street=tuple(street)

		if frequency.get(street)!=None:
			frequency[street]+=1
		else:
			frequency[street]=1

	for j in range(n):
		v=maps[j][1]
		name1=maps[j][2]
		street1=[]
		street1.append(v)
		street1.append(name1)
		street1=tuple(street1)
		if frequency.get(street1)!=None:
			frequency[street1]+=1

		else:
			frequency[street1]=1


	values=frequency.values()
	keys=frequency.keys()
	count=0

	for f in keys:
		#if frequency[f]<2:
		 #frequency[f]='no'

		if frequency[f]>=2:
			checking=f[0]
			checking_array=f
			for j in keys:
				if frequency[j]>=2 and j[0]==checking and j!=checking_array:
					count+=1


	#print(count//2)


	return count//2



n=int(input())
maps=[]
for i in range(n):
	tup=[]
	a,b,name,direction=input().split()
	a=int(a)
	b=int(b)
	tup.append(a)
	tup.append(b)
	tup.append(name)
	tup.append(direction)

	maps.append(tup)


print(no_of_intersections(maps))



