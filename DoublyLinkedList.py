from Node import Node

class DoublyLinkedList(Node):

	def __init__(self):
			self.Head = None
			self.Tail = None
	def __str__(self):
		while self.getNext != 
	
	def last(self):
		return self.Tail
	
	def append(self, Value):
		if self.Head == None:
			self.Head = Node(Value)
			self.Tail = self.Head
		else:	
			Tail.next = Node(Value)
			self.Tail = Tail.next
	def prepend(self, Value):
		if self.Head == None:
			self.Head = Node(Value)
			self.Tail = self.Head
		else:	
			newNode = Node(Value)
			newNode.Next = self.Head
			self.Head = newNode
	
	def find(self,Value):
		current = self.Head
		while current != None:
			if current.Value == Value:
				return current
				break
			current = current.Next
		return None
	
	def delete(self,Value):
		
		current = find(Value)
		if current == self.Head:
			self.Head = current.Next
		elif current == self.Tail:
			self.Tail = current.Previous
		else:	
			current.Previous.Next = current.Next
			current.Next.Previous = current.Previous
		
	
	def insertAfter(self,x,y):
		
		if find(x) == self.Tail:
			append(y)
		else:	
			newNode = Node(y)
			newNode.Next = find(x).Next
			find(x).Next = newNode
			newNode.Previous = find(x)
			newNode.Next.Previous = newNode
		