import sys

def get_inpt(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))

T= int(input())

while T!=0:
    T-=1
    n = int(input())
    coins = get_array() #for fast io inbuilt function
    prefix=[0]*n
    prefix[0] = coins[0]
    for i in range(1,n):
        prefix[i] =prefix[i-1] + coins[i]
    
    
    q = int(input())
    for i in range(q):
        start , end = list(map(int , input().split()))

        #sum = coins[end-1] - coins[start-1] + coins[start-1] -coins
        sum = prefix[end-1] - prefix[start-1] + coins[start-1]
        print(sum)