class Maze:
    def __init__(self, h, w, center):
        self.height = h
        self.width = w
        self.center = center
        self.maze = [[None for i in range(w)] for j in range(h)]
        self.maze[center[0]][center[1]] = 0
        self.cursor = [0,0]

    def setWall(self, x, y):
        self.maze[x][y] = -1
    
    def isWall(self, x, y):
        if self.maze[x][y] == -1:
            return True
        return False
    
    def isValidIndex(self, x, y):
        if x >= 0 and y >= 0 and x < self.height and y < self.width:
            return True
        return False
    
    def displayMaze(self, currentX, currentY):
        for i in range(0,self.height):
            for j in range(0,self.width):
                if self.isWall(i,j):
                    print(" # ", end="")
                elif i == currentX and j == currentY:
                    print(" C ", end="")
                else:
                    print(" %s " % str(self.maze[i][j]), end="")
            print()
        print()

    def move(self, initX, initY):
        self.displayMaze(initX, initY)
        nextPositions = []
        if [initX,initY] == self.center:
            return True
        for x,y in [[initX + 1, initY], [initX - 1, initY], [initX, initY + 1], [initX, initY - 1]]:
            if self.isValidIndex(x,y) and not self.isWall(x,y) and self.maze[x][y]<9999:
               nextPositions.append([x, y, self.maze[x][y]])
        nextPositions.sort(key = lambda k:k[2])
        for set in nextPositions:
            self.maze[set[0]][set[1]] = 9999
            if (self.move(set[0], set[1])):
                return True

    def start(self, startID):
        self.cursor = startID
        num = 1
        q = [self.center]
        while q:
            temp = []
            for initX, initY in q:
                for x,y in [[initX + 1, initY], [initX - 1, initY], [initX, initY + 1], [initX, initY - 1]]:
                    if self.isValidIndex(x,y) and self.maze[x][y] == None:
                        self.maze[x][y] = num
                        temp.append([x,y])
            q = temp
            num += 1
        self.move(self.cursor[0], self.cursor[1])
    

newMaze = Maze(4,4,[2,1])

newMaze.setWall(1,0)
newMaze.setWall(1,1)
newMaze.setWall(1,2)
newMaze.setWall(2,0)
newMaze.setWall(3,0)
newMaze.setWall(3,1)

newMaze.start([0,0])

