

def isSymm(n , orig_mat , tpos):
	for i in range(n):
		row = []
		row = orig_mat[i]
		for j in range(n):
			tpos[j][i] = row[j]
	

	if orig_mat == tpos:
		return 1
	else:
		return 0

def uppTriang(n , orig_mat):
	

	flag = False
	for i in range(0,n):
		for j in range(i+1,n):
			if orig_mat[i][j] == 0:
				continue;
			else:
				flag = True
				break;
		if flag == True:
			break;

	if not flag :
		return True

def downTriag(n , orig_mat):

	flag = False
	for i in range(0,n):
		for j in range(0 , i):
			if orig_mat[i][j] == 0:
				continue;
			else:
				flag = True
				break;
		if flag == True:
			break;

	if not flag :
		return True
	

def checkDiag(n , orig_mat):
	flag = False
	for i in range(n):
		if orig_mat[i][i] !=0:
			continue;
		else:
			flag = True
			break;
	if not flag:
		return True
	else:
		return False


T= int(input())
while T!=0:
	T-=1
	orig_mat=[]
	tpos=[]
	clone = []
	n = int(input())
	for i in range(n):
		clone = []
		row = list(map(int , input().split()))
		orig_mat.append(row)
		for ele in row:
			clone.append(ele)
		tpos.append(clone) #be careful while clning if u use row to clone then  it points to same memory loc
		

	s,t,d=0,0,0

	if uppTriang(n, orig_mat) == True or downTriag(n , orig_mat) == True :
		t = 1
	else:
		t=0

	if uppTriang(n, orig_mat) == True and downTriag(n , orig_mat) == True and checkDiag(n,orig_mat):
		#means everything else is zero and also no zero on diagnal
		d=1
	else:
		d=0

	s=isSymm(n , orig_mat , tpos)
		
	print(s+2*t+4*d)