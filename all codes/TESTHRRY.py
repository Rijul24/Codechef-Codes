n = int(input())
arr = list(map(int , input().split()))
k = int(input())
start = 0
end = k-1
rev = []
while end < n:
	for i in range(end , start-1 , -1):
		print(arr[i])
		rev.append(arr[i])

	start = end + 1
	end = start+k -1

while start <n:
	rev.append(arr[start])
	start+=1

for ele in rev:
	print(ele , end = " ")