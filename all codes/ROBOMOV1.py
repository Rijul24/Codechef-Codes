T= int(input())

while T!=0:
	T-=1
	x_orig , y_orig , x_fin , y_fin = list(map(int , input().split()))

	h_steps , v_steps = abs(x_fin - x_orig) , abs(y_fin - y_orig) #along side rectangle of these endpoints
	#assuming we move along sides

	steps = h_steps + v_steps
	print(steps)
	if x_fin < x_orig:
		#go left or west
		for i in range(h_steps):
			print("W" , end= "")
	else:
		#go right or east
		for i in range(h_steps):
			print("E" , end = "")

	if y_fin > y_orig:
		#go up
		for i in range(v_steps):
			print("N" , end= "")
	else:
		#go down
		for i in range(v_steps):
			print("S" , end = "")
	


	print()