#fresher's party
n,m = list(map(int, input().split()))
toffee = list(map(int, input().split()))

i=0
ans=[]
toffee.sort()
while i <m-n+1: 
	mini = toffee[i]
	maxi = toffee[i+n-1]
	ans.append(maxi-mini)
	i+=1
print(min(ans))
