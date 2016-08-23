data = [-3,-20,-2,-1,-2,-1,-6,-7,-3]

def findMaxSubarray(data):
	for l in range(len(data)):
		if data[l] > 0:
			pass
		else:
			arr = []
			print arr
	#left array
	mid = len(data)/2
	ssum = 0
	sumLeft = 0
	leftData = data[:mid]
	leftIndex = 0
	for i in range(len(leftData)-1,-1,-1):
		ssum = ssum + leftData[i]
		if ssum > sumLeft:
			sumLeft = ssum
			leftIndex = i



	#right array
	sumRight = 0
	ssum = 0
	rightData = data[mid:]
	rightIndex = 0
	for j in range(len(rightData)):
		ssum = ssum +rightData[j]
		if ssum > sumRight:
			sumRight = ssum
			rightIndex = j
		

	#cross array
	crossData = data[leftIndex:rightIndex + mid + 1]
	sumCross = 0
	ssum = 0
	crossIndex = 0
	for x in range(len(crossData)):
		ssum = ssum + crossData[x]
		if ssum > sumCross:
			sumCross = ssum
			crossIndex = x

	maxSum = max(sumRight,sumLeft,sumCross)



if __name__ == '__main__':
	findMaxSubarray(data)
