n,m=map(int,input().split())
b=[]
li=[]
d1={} #DICTIONARY FOR STORING INPUT WORDS
d2={} #dictionary for storing len and position of horizontal words 
d3={} #dictionary for storing len and position of vertical words 
for i in range(n):
    p=input()
    d=[]
    a=0
    l=0
    si=0
    ei=0
    for j in range(m):
        d.append(p[j])
        if (p[j]=="b" or p[j]=="r") and a==0:
            a=1 
            l+=1
            si=j
        elif (p[j]=="b" or p[j]=="r") and a==1:
            l+=1 
            ei=j 
            d2[l]=[i,si,ei]
            l=0
        elif a==1:
            l+=1
    b.append(d)
for j in range(m):
    a=0
    l=0
    si=0
    ei=0
    for i in range(n):
        if (b[i][j]=="b" or b[i][j]=="c") and a==0:
            a=1 
            l+=1
            si=i
        elif (b[i][j]=="b" or b[i][j]=="c") and a==1:
            l+=1 
            ei=i 
            d3[l]=[j,si,ei]
            l=0
        elif a==1:
            l+=1
w=int(input())
for i in range(w):
    a=input()
    li.append(a)
    d1[len(a)]=a
row=set() #set of rows filled
column=set() #set of columns filled
sad=0
for i in d1:
    if i in d2:
        r,si,ei=map(int,d2[i])
        for j in range(i):
            sub=b[r][j+si]
            if ((sub!="r" and sub!="c" and sub!="." and sub!="b") or (j+si) in column) and sub!=d1[i][j] and sub!=".":
                print("Invalid")
                sad=1 
                break
            else:
                b[r][j+si]=d1[i][j]
        row.add(r)
    elif i in d3:
        c,si,ei=map(int,d3[i])
        for j in range(i):
            sub=b[j+si][c]
            if ((sub!="r" and sub!="c" and sub!="b") or (j+si) in row) and sub!=d1[i][j] and sub!=".":
                print("Invalid")
                sad=1
                break
            else:
                b[j+si][c]=d1[i][j]
        column.add(c)
    else:
        print("Invalid")
        break
    if sad==1:
        break
p=""
if sad==0:
    a=0
    for i in range(n):
        for j in range(m):
            rope=b[i][j]
            if rope==".":
                print("Invalid")
                a=1 
                break
            else:
                p+=rope
        if a==1:
            break
        p+="\n"
    if a==0:
        print(p)