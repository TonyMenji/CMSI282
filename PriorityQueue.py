class PriorityQueue:
	
	def __init__(self):
		self.items = []
	
	def add(self, item):
		self.items.append(item)
		self.sift_up(len(self) - 1)
	
	def peek(self):
		if (len(self) == 0):
			raise ValueError, "There are no items in the Queue"
	
		else:
			return self.items[0]
	
	def remove(self):
		if (len(self) == 0):
			raise ValueError, "There are no items in the Queue"
	
		elif (len(self) == 1):
			self.items.pop(0)
	
		else:
			self.items[0] = self.items.pop(len(self) - 1)
			self.sift_down(0)
	
	def __len__(self):
		return len(self.items)
	
	def __str__(self):
		return str(self.items)
	
	def sift_up(self, index):
		parent = (index - 1) / 2
		if (parent >= 0 and self.items[parent] > self.items[index]):
			self.items[index], self.items[parent] = self.items[parent], self.items[index]
			self.sift_up(parent)
	
	def sift_down(self, index):
		child = (index * 2) + 1
		if (child >= len(self) - 1):
			return self.items
	
		if (child + 1 < len(self) - 1 and self.items[child] > self.items[child + 1]):
				child += 1
	
		if (self.items[index] > self.items[child]):
			self.items[child], self.items[index] = self.items[index], self.items[child + 1]
			self.sift_down(child)