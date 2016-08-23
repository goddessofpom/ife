class MazeWalker():
	def __init__(self, pos):
		self._pos = pos
		dirs = [(0,1),(0,-1),(1,0),(-1,0)]

	def mark(maze, pos):
		maze[pos[0]][pos[1]] = 2

	def passable(maze, pos):
		return maze[pos[0]][pos[1]] == 0

	def find_path(maze, pos, end):
		self.mark(maze,pos)
		if pos == end:
			return True
		for i in range(4):
			nextstep = pos[0] + dirs[i](0), pos[1] + dirs[i](1)
			if passable(maze, nextstep):
				self.find_path(maze,nextstep , end)
				return True
		return False
