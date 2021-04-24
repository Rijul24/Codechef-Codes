n = int(input())
def cal( arr):
	sum1 = 0
	n= len(arr)
	for k in range(n):
		sum1 += arr[k]*((4/5)**k)
	return sum1/5


arr=[]
arr2=[]
for i in range(n):
	x = int(input())
	arr.append(x)
	arr2.append(x)

sum1 = 0
for k in range(n):
	sum1 += arr[k]*((4/5)**k) 
s2=0

ans=[]
for k1 in range(n):
	arr2.pop(0)
	s2 = 0
	if len(arr2)!=0:
		s2 = cal(arr2)
		ans.append(s2)


s1=0
for e in ans:
	s1 += e

print(sum1/5)
print(s1/n)