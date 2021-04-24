def merge(left,right):
    i=0
    j=0
    x=[]
    while i<len(left) and j<len(right):
        pq,rs=left[i][0]/left[i][1],right[j][0]/right[j][1]
        if pq<rs:
            x.append(left[i])
            i+=1
        else:
            x.append(right[j])
            j+=1
    while i<len(left):
        x.append(left[i])
        i+=1 
    while j<len(right):
        x.append(right[j])
        j+=1 
    return x
# Correct this function so that the correct output is given
def mergesort(x):
    if len(x)==1:
        return x
    mid=len(x)//2
    left=mergesort(x[:mid])
    right=mergesort(x[mid:])
    arr=merge(left,right)
    return arr
def get_distinct_fractions(x):
    d={}
    c=[]
    for i in range(len(x)):
        p,q=x[i][0],x[i][1]
        if q==0:
            if p>0:
                if 9223372036854775807 in d:
                    if p<d[9223372036854775807][0]:
                        d[9223372036854775807]=x[i]
                else:
                    d[9223372036854775807]=x[i]
            else:
                if -9223372036854775807 in d:
                    if p>d[-9223372036854775807][0]:
                        d[-9223372036854775807]=x[i]
                else:
                    d[-9223372036854775807]=x[i]
        else:
            f=p/q
            if f in d:
                r,s=d[f][0],d[f][1]
                if f>0:
                    if p<r:
                        d[f]=x[i]
                else:
                    if q>0 and s<0:
                        d[f]=x[i]
                    elif q*s>0 and abs(p)<abs(r):
                        d[f]=x[i]
            else:
                d[f]=x[i]
    #print(d)
    for i in d:
        if i!=-9223372036854775807 and i!=9223372036854775807:
            c.append(d[i])
    op=mergesort(c)
    if -9223372036854775807 in d:
        op=[d[-9223372036854775807]]+op
    if 9223372036854775807 in d:
        op+=[d[9223372036854775807]]
    #print(c)
    return op
    

 
# ----------------------Do not change anything below this line --------------------------
 
n = int(input())
arr_strip = list(map(int, input().split()))
arr = []
for i in range(0, 2*n, 2):
    arr.append((arr_strip[i], arr_strip[i+1]))
 
result = get_distinct_fractions(arr)
print(len(result))
for x in result:
    print(x[0], x[1], end = ' ')