class Fastsort():
	def __init__(self,slist=[]):
		self.slist = slist
		self.fastsort()

	def fastsort(self):
		slist = self.slist
		r = slist[-1]
		i,j = 0,0
		if i == 0:
			slist[i] = slist[0]
			i = i + 1
			j = j + 1
		if slist[j] > r:
			j = j + 1
		elif j < len(slist):
			slist[i] = slist[j]
			i = i + 1
			j = j + 1
		else:
			s = slist[i]
			slist[i] = r
			slist[-1] = s

		return slist


if __name__ == '__main__':
	data = Fastsort([2,5,4,7,3])
	print data.fastsort()


