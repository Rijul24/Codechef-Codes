#linked list implementation 

class Node:
	data = -1
	next = None

	def __init__(self , ele):
		self.data = ele



#--------------------------------------------------------------------------

def insert_at_tail(head , data):
	if head == None:
		return Node(data)

	#finding the tail first
	temp = 	head
	while temp.next != None:
		temp = temp.next

	new_node = Node(data)
	temp.next = new_node

	return head 


#---------------------------------------------------------------------------

def insert_at_head(head , data):
	if head == None:
		#head = Node(data) this is wrong bce objs are passed by copy
		return Node(data)

	new_node = Node(data)
	#store the add of head
	new_node.next = head
	#update the head
	head = new_node
	return head
#-----------------------------------------------------------------------------
def length_of_LL(head):
	temp = head
	sz =0
	while temp.next != None:
		sz += 1
		temp = temp.next

	return sz

#---------------------------------------------------------------------------

def insert_at(head , data , pos=0):
	if pos==0:
		return insert_at_head(head , data)

	if pos >=length_of_LL(head):
		return insert_at_tail(head , data)



	'''if head == None:
		return Node(data)'''

	new_node = Node(data)
	temp = head

	while pos!=1:
		pos-=1
		temp = temp.next

	#we got obj at pos-1
	new_node.next = temp.next
	temp.next = new_node
	return head


#---------------------------------------------------------------------------

def print_LL(head):
	temp = head
	while temp!=None:
		print(temp.data , end=" ")
		temp= temp.next
	print()
	return

#---------------------------------------------------------------------------
def delete_at_head(head):
	if head == None:
		return None

	temp = head 
	temp = temp.next
	head.next = None
	head = temp
	return head

'''	temp = head
	head = head.next
	temp.next = None 
	return head '''

#---------------------------------------------------------------------------

def delete_at_tail(head):
	if head == None:
		return head

	temp2 = None
	temp = head
	while temp.next != None:
		temp2 = temp
		temp = temp.next

	temp2.next = None
	return head


#---------------------------------------------------------------------------

def delete_at(head , pos=0):

	if pos==0:
		return delete_at_head(head)

	if pos>= length_of_LL(head):
		return delete_at_tail(head)

	temp = head
	temp2 = head
	pos1 = pos
	while pos!=1:
		pos-=1
		temp = temp.next
	
	while pos1!=0:
		pos1 -= 1
		temp2 = temp2.next
	
	temp.next= temp2.next

	return head

'''	#alternative approach
	temp = head
	while pos !=1:
		pos-=1
		temp = temp.next

	tobedeleted = temp.next
	temp.next = temp.next.next
	tobedeleted.nest = None

	return head '''

#---------------------------------------------------------------------------
def find_mid_node(head):
	fast , slow = head , head

	while fast.next != None and fast!= None:
		fast.next.next #fast jumps two steps
		slow.next #slow jumps one

	return  slow

#---------------------------------------------------------------------------

def add_LL(head1 , head2):

	for i in range(length_of_LL(head1)):
		data = head1.data + head2.data
		head = insert_at_head(head , data)

		return head

'''
n = int(input())
head = None
while n>0:
	n-=1
	x = int(input())
	#head = insert_at_head(head , x)
	head = insert_at_tail(head , x )


head = insert_at(head , 44, 4) #pos ---> index
print_LL(head)
head = delete_at_head(head)
print_LL(head)
head = delete_at_tail(head)
print_LL(head)
delete_at(head , 3)
print_LL(head)

'''
n = int(input())
head2 = None
while n>0:
	n-=1
	x = int(input())
	#head = insert_at_head(head , x)
	head2 = insert_at_head(head2 , x )


n1 = int(input())
head1 = None
while n>0:
	n1 -=1
	x = int(input())
	#head = insert_at_head(head , x)
	head1 = insert_at_head(head1 , x )

head= add_LL(head1 , head2)

print_LL(head)