import math
T= int(input())
while T!=0:
	T-=1
	k1 , k2 , k3 , v = list(map(float , input().split()))
	v_final = k3 * v * k1 * k2
	if v_final!=0:

		t = 100.00/v_final
	else:
		t=-1.00

	t = round(t , 2)

	if t<9.58 and t>0:
		print("yes")
	else:
		print('no')