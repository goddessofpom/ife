#定义节点类
class LNode:
	def __init__(self, elem, next_=None):
		self.elem = elem
		self.next = next_


#定义链表类
class LList:
	def __init__(self):
		self._head = None

	def is_empty(self):
		return self._head is None

	def len(self):
		if self._head is None:
			return 0
		count = 0
		p = self._head
		while p.next is not None:
			p = p.next
			count = count + 1
		return count

	def prepend(self, elem):
		self._head = LNode(elem, self._head)

	def pop(self):
		if self._head is None:
			raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
    	if self._head = None:
    		self._head = elem
    		return
    	p = self._head
    	while p.next is not None:
    		p = p.next
    	p.next = LNode(elem)

    def pop_last(self):
    	if self._head is None:
    		raise LinkedListUnderflow("in pop_last")
    	p = self._head
    	if p.next is None:
    		e = p.elem
    		self._head = None
    		return e
    	while p.next.next is not None:
    		p = p.next
    	e = self._head.next
    	p.next = None
    	return e

    def insert(self, elem ,i):
    	if self.len < i:
    		return False
    	p = self._head
    	for j in range(1,i-1):
    		p = p.next
    	p.next = LNode(elem,p.next)

    def search(self, elem):
    	p = self._head
    	count = 0
    	while p.elem != elem and p.next is not None:
    		p = p.next
    		count = count + 1
    	if p.elem == elem:
    		return count
    	else:
    		return -1

    def forall(self, op):
    	p = self._head
    	while p.next is not None:
    		after_op = p.op
    		self._head = after_op
    		p = p.next 
    	p = p.op

    def compare(self, llst):
        p = self._head
        q = llst._head
        if p is None and q is None:
            return "=="

        while p.next is not None and q.next is not None:
            if p.elem < q.elem:
                return "<"
            elif p.elem > q.elem:
                return ">"
            else:
                p = p.next
                q = q.next

        if self.len == llst.len:
            return "=="
        elif: self.len < llst.len:
            return "<"
        else:
            return ">"
            



    		


