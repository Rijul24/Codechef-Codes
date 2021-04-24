a= [[1,2,3],[4,5,6]]
def test(a):
	a[0][0] = 5
	return a

b = test(a)
print(b)