def no_of_ways(n, current_pos ,  output,o,x):
    if len(output)-1>x or current_pos ==0:
        o.append(len(output))
        print(output)
        return
    if current_pos<0:
        return 

    no_of_ways(0 , current_pos-3 , "3"+output,o,x)
    no_of_ways(0 , current_pos-2 ,"2"+output,o,x)
    no_of_ways(0 , current_pos-1, "1"+output,o,x) #if we go from current_pos-1 to 0 we append 1 everytime
    no_of_ways(0 , 0 , "0"+output , o,x)
    if current_pos<=n-3:

        no_of_ways(0 , current_pos+1 ,"a"+output,o,x)
        no_of_ways(0 , current_pos+2 ,"b"+output,o,x)
        no_of_ways(0 , current_pos+3 ,"c"+output,o,x)
    
    
    
T= int(input())
while T!=0:
    T-=1
    n , x = input().split()
    n = int(n)
    x = int(x)
    o=[]
    if n!=0:
        no_of_ways(0 , n, "",o,x)
    count=0
    
    
    print(len(o))