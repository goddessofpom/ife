class SStack():
	def __init__(self):
		self._elems = []

	def is_empty(self):
		return self.elems == []

	def top(self):                 #访问栈顶
		if self._elems == []:
			raise Exception()
		return self._elems[-1]

	def push(self, elem):
		self._elems.append(elem)

	def pop(self):
		if self._elems == []:
			raise Exception()
		return self._elems.pop()