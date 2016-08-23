class BinTNode:
	def __init__(self, dat, left=None, right=None):
		self.data = dat
		self.left = left
		self.right = right

def count_BinTNodes(t):
	if t is None:
		return 0
	else:
		return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)

def sum_BinTNodes(t):
	if t is None:
		return 0
	else:
		return t.data + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)


# 宽度优先遍历二叉树
def levelorder(t, proc):
	qu = Queue()
	qu.enqueue(t)
	while not qu.is_empty():
		n = qu.dequeue()
		if n is None:
			continue
		else:
			qu.enqueue(n.left)
			qu.enqueue(n.right)
			proc(n.data)

# 非递归先根序遍历

def preorder_nonrec(t, proc):
	s = Stack()
	while t is not None or not s.is_empty():
		while t is not None:
			proc(t.data)
			s.push(t.right)
			yield t.data
			t = t.left
		t = s.pop()

