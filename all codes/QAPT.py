# cook your dish here
T = int(input())
while T!=0:
    T-=1
    n = int(input())
    k=0
    while n!=1:
        if k==0:
            #alice
            i=0
            while 2**i<=n:
               i+=1
            
            if 2**(i-1)==n:
                n = n//2
            else:
                n = n - 2**(i-1)
            k=1
        else:
                        #alice
            i=0
            while 2**i<=n:
               i+=1
            
            if 2**(i-1)==n:
                n = n//2
            else:
                n = n - 2**(i-1)
            k=0
            
    if k==1:
        print('Alice')
    else:
        print('Bob')
            
            