n , k =list(map(int , input().split()))
string = input()
k = input().split()
substr=0
flag =0
for idx in range(n):
	if string[idx] in k:
		if flag==1:
			substr+=idx+1 
		else:#flag ==0
			substr+=1
			flag =1
	else:
		flag =0
print(substr)