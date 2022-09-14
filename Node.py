class Node:

	
	def __init__(self,Value):
		self.Value = Value
		self.Next = None
		self.Previous = None
	
	def setValue(self,Value):
		self.Value = Value
	
	def setNext(self,Next):
		self.Next = Next
	
	def setPrev(self,Previous):
		self.Previous = Previous
	
	def getValue(self):
		return self.Value
	
	def getNext(self):
		return self.Next
	
	def getPrev(self):
		return self.Previous 
	
	def __str__(self):
		value = "[" + self.Value + "]"
		return value

