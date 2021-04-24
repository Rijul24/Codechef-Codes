T= int(input())
while T!=0:
    T-=1
    n = int(input())
    orig_arr =  [int(x) for x in input().split()]
    temp_arr =[]
    for i in range(0,n):
        temp_arr.append(orig_arr[i])
        
    
    temp_arr.sort(reverse = True)
    
    for i in range(0,n):
      
        a= orig_arr[i]
        hr = temp_arr.index(a)
        print( hr+1 , end =" ")
        temp_arr[temp_arr.index(a)] = 0
    
    print()     
        
        



def check_rect(arr):
    n = len(arr)
    k=0
    val = 0
    for i in range(0,n):
        if arr[i]==0 and k ==0:
            continue;
        elif arr[i]!=0:
            k=1
            val = arr[i]
            for j in range(i,n):
                if arr[j]!=val and arr[j]!=0:
                    return -1
                elif arr[j] ==0:
                    for k in range(k,n):
                        if arr[k] !=0:
                            return -1
                    return 1    
            return 1
            
            
            












T= int(input())
while T!=0:
    T-=1
    r,c = input().split()
    r= int(r)
    c = int(c)
    a=[]
    arr=[]
    for i in range(0,r)
        s= input()
        s = list(s)
        for j in range(0 , len(s)):
            a.append(int(s[j]))
        arr.append(a)
    
    
    col=[]
    for i in range(0,c):
        s_col =0
        for j in range(0,r):
            s_col += arr[r][c]
        col.append(s_col)
        
    row =[]
    for i in range(0,r):
        s_row =0
        for j in range(0,c):
            s_row += arr[r][c]
        row.append(s_row)
        
    f1= check_rect(row)
    f2 = check_rect(col)
    if f1 ==1 and f2==1:
        print("YES")
    else:
        print("NO")
    
        
        

        
        
