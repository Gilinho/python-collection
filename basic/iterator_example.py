class ReverseIterator:
	"""Create iterator to looping over a sequence"""
	def __init__(self, data):
		self.data = data
		self.index = len(data)

	def __iter__(self):
		# We must create __iter__ method to make this class iterable
		return self

	def next(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index-1
		return self.data[self.index]

if __name__ == "__main__":
	data = ("Hello", "World", "Blah")
	value = ReverseIterator(data)
	for char in value:
		print char