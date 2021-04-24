#this is bin search 1
import sys

def run_program(m):
    print('1 ' + str(m))
    sys.stdout.flush()
    r = int(input())
    if r == 0:
        return False
    elif r == 1:
        return True
    exit()


# ------------------- Do not touch anything above this line -------------------------------------

# complete the function below, use run_program(x) to determine if Chef's program can consume x bytes
# The result will be True if it can and False otherwise
# If you call the function run_program more than 31 times, you will get a wrong answer verdict
def find_memory_limit():
	left = 0
	right = 1e9 #10 to the power 9
	while left<=right:
		mid = left + (right - left) //2
		if run_program(mid) == True:
			#this means all mid before also satisfy
			left = mid + 1
		else:
			#this means all mid after this will be false
			right = mid -1

	return mid




    return 0

# ------------------- Do not touch anything below this line -------------------------------------
print("2 " + str(find_memory_limit()))