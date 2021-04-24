class Node:
	data = -1
	next = None

	def __init__(self , ele):
		self.data = ele


def insert_at_head(head , data):
	if head == None:
		return Node(data)

	new_node = Node(data)
	#store the add of head
	new_node.next = head
	#update the head
	head = new_node
	return head

def print_LL(head):
	temp = head
	while temp!=None:
		print(temp.data , end=" ")
		temp= temp.next
	print()
	return


def rev_LL(start , k , head , prev = None ):
       temp = k
       k1 = k
       add = []
       
       if head == start:
              
              add.append(start.next)
              temp = start
              while k>0:
                     
                     k-=1
                     temp = temp.next
                     add.append(temp.next)
              
              temp1 = start
              temp2 = start
              i=-1
              
              while k1>0:
                     k1-=1
                     temp1.next = add[i]
                     i -= 1
                     temp1 = temp2.next
       
       else:
              k = temp
              k1 = k
              add.append(prev.next)
              
              add.append(start.next)
              temp = start
              while k>0:
                     
                     k-=1
                     temp = temp.next
                     add.append(temp.next)
              
              temp1 = start.next
              temp2 = start.next
              start.next = add[-1]
              
              i=0
              
              while k1>1:
                     k1-=1
                     temp1.next = add[i]
                     i += 1
                     temp1 = temp2.next
              prev.next = add[-2]
       
              
       
       
       return head
              
              
              
              
                     
              
                     
       

n = int(input())
arr = list(map(int , input().split()))
k = int(input())
head = None
i=0
while n>0:
	n-=1
	head = insert_at_head(head , arr[i])
	i+=1
	


numb = n//k
start = head
prev = None

while numb>0:
       k2 , k3 = k , k
       numb -= 1

       head = rev_LL(start , k , head , prev)
       while k2>1:
       
              k2-=1
              start = start.next
       prev = start
       start = start.next

print_LL(head)
