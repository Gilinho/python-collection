class Example():
	def __init__(self):
		self._semiprivate = "HELLO"
		self.__privateall = "WORLD"

if __name__ == "__main__":
	e = Example()
	print e._semiprivate
	try:
		print e.__privateall
	except AttributeError:
		print e.__dict__

	print e._Example__privateall