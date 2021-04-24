#this is power , add
import sys

def add(a, b):
    print('1', a, b) 
    sys.stdout.flush()
    return int(input())
# --------------------- Do not touch anything above this line ----------------------

# The return value of this function is wrong, write the correct version of this function using the add(a, b) ...
# function defined above.

# Note that this function should return (a ** b) % m, you are guaranteed that add(a, b) returns (a + b) % m


def find_hidden_numb():
	#we try to determine value of m , we use add function and pass (a,0)
	lo = 0 
	hi = 10**9

	while lo<=hi:
		mid = lo +(hi - lo)//2
		rem = add(mid , 0)
		if rem ==0:
			return mid
		if rem == mid:
			lo = mid + 1
		elif rem < mid:
			hi = mid -1
	
	return lo

def pwr(a, b):
	m = find_hidden_numb()

	return (a**b)%m


# --------------------- Do not touch anything below this line ----------------------

a, b = map(int, input().split())
ans = pwr(a, b)
print('2', ans)
