def no_of_ways(n, current_pos ,  output,o):
    if current_pos>n:
        return 
    if current_pos==n:
        o.append(len(output))
        print(output)
        return 
    no_of_ways(n , current_pos , "0"+output ,o)
    no_of_ways(n , current_pos+1, "1"+output,o)
    no_of_ways(n , current_pos+2 ,"2"+output,o)
    no_of_ways(n , current_pos+3 , "3"+output,o)
    
    
    
T= int(input())
while T!=0:
    T-=1
    n , x = input().split()
    n = int(n)
    x = int(x)
    o=[]
    if n!=0:
        no_of_ways(n , 0 , "",o)
    count=0
    
    for ele in o:
        if o ==x:
            count+=1
    
    print(count)