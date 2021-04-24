import math
def fn(m , b ,c):
	quad = float(m**2 + b*m + c)
	denom = math.sin(m)
	if denom!=0:
		val = quad/ denom
	else:
		return False
	
	return val



T = int(input())
while T!=0:
	T-=1

	b , c = list(map(int , input().split()))

	lo , hi = 0.0 , math.pi/2

	for i in range(200):

		m1 = lo + (hi - lo)/3
		m2 = hi - (hi - lo)/3

		d1=fn(m1,b,c)
		d2=fn(m2,b,c)
		if d1 !=False and d2!= False:

			if  d1 > d2 :
				lo = m1
			else:
				hi = m2
		else:
			lo+=0.0000001
			hi -= 0.0000001

	print("{:0.6f}".format(fn(lo , b ,c),6))