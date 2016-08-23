class LStack():
	def __init__(self):
		self._top = None

	def is_empty(self):
		return self._top is None

	def top(self):
		if self._top is None:
			raise Exception()
		return self._top.elem

	def push(self, elem):
		self._top = LNode(elem, self._top)

	def pop(self):
		if self._top is None:
			raise Exception()
		p = self._top
		self._top = p.next
		return p.elem 