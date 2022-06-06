class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head =  Node()

	def append(self, data):
		new_node = Node(data)
		cur_node = self.head
		while cur_node.next != None:
			cur_node = cur_node.next
		cur_node = new_node

	def display(self):
		cur_node = self.head
		while cur_node.next != None:
			cur_node = cur_node.next
			arr.append(cur_node.data)
		print(arr)
		return arr

	def length(self):
		cur_node = self.head
		c = 0
		while cur_node.next != None:
			cur_node = cur_node.next
			c += 1
		print(c)
		return c 

	def search(self, key):
		cur_node = self.head
		while cur_node.next != None:
			cur_node = cur_node.next
			if cur_node.data == key:
				print(True)
				return True
		print(False)
		return False

	def erase(self, index):
		cur_node = self.head
		
		c = 0
		while cur_node.next != None:
			prior_node = cur_node
			cur_node = cur_node.next
			if c == index:
				prior_node.next = cur_node.next
				return
			c += 1

	def insertAt(self, index, data):
		cur_node = self.head
		new_node = Node(data)
		c = 0
		while cur_node.next != None:
			prior_node = cur_node
			cur_node = cur_node.next
			if c == index:
				prior_node = new_node
				new_node.next = cur_node
				return
			c += 1

	def get(self, index):
		cur_node = self.head
		c = 0
		while cur_node.next != None:
			cur_node = cur_node.next
			if c == index:
				return cur_node.data
			c += 1

	def set(self, index):
		cur_node = self.head
		c = 0
		while cur_node.next != None:
			cur_node = cur_node.next
			if c == index:
				cur_node.data = data
				return
			c += 1

	def __get__(self, index):
		print(self.get(index))
		return self.get(index)






