import tkinter as tk

root = tk.Tk()

class Maze:

    # Initialise maze
    def __init__(self, h, w, center):
        self.height = h
        self.width = w
        self.center = center
        self.maze = [[None for i in range(w)] for j in range(h)]
        self.maze[center[0]][center[1]] = 0
        self.cursor = [0,0]

    # Set a Wall
    def setWall(self, x, y):
        self.maze[x][y] = -1
    
    # Check if current cell is a wall
    def isWall(self, x, y):
        if self.maze[x][y] == -1:
            return True
        return False
    
    # Check if current position is valid
    def isValidIndex(self, x, y):
        if x >= 0 and y >= 0 and x < self.height and y < self.width:
            return True
        return False
    
    # Print the maze
    def displayMaze(self, currentX, currentY):
        canvas_width = self.width * 20
        canvas_height = self.height * 20
        canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
        canvas.pack()
        for row in range(self.width):
            for col in range(self.height):
                x1 = col * 20
                y1 = row * 20
                x2 = x1 + 20
                y2 = y1 + 20
                if self.isWall(row,col):
                    canvas.create_rectangle(x1, y1, x2, y2, fill='black')
                elif row == currentX and col == currentY:
                    canvas.create_rectangle(x1, y1, x2, y2, fill='red')
                else:
                    canvas.create_rectangle(x1, y1, x2, y2, fill='white')
        root.mainloop()

    # DFS function to reach center from start
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
            
    # BFS Function to set distance values for each cell
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
    

# Sample Test

newMaze = Maze(4,4,[2,1])

newMaze.setWall(1,0)
newMaze.setWall(1,1)
newMaze.setWall(1,2)
newMaze.setWall(2,0)
newMaze.setWall(3,0)
newMaze.setWall(3,1)

newMaze.start([0,0])

