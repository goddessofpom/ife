inf = float("inf")

class Graph:
	def __init__(self, mat, unconn=0):
		vnum = len(mat)
		for x in mat:
			if len(x) !=vnum:
				raise Exception

		self._mat = [mat[i][:] for i in range(vnum)]
		self._unconn = unconn
		self._vum = vnum

	def vertex_num(self):
		return self._vum

	def _invalid(self, v):
		return 0 > v or v >= self._vum

	def add_vertex(self):
		raise error

	def add_edge(self, vi, vj, val=1):
		if self._invalid(vi) or self._invalid(vj):
			raise Exception
		else:
			self._mat[vi][vj] = val

	def get_edge(self, vi, vj):
		if self._invalid(vi) or self._invalid(vj):
			raise Exception
		else:
			return self.mat[vi][vj]