import tkinter as tk
import time

root = tk.Tk()
root.title("Maze")
size = 40

class Maze:
    # ==================
    # Initialise maze
    # ==================
    def __init__(self, h, w, center):

        self.height = h + 2
        self.width = w + 2
        self.center = center
        self.maze = [[None for i in range(self.width)] for j in range(self.height)]

        # Set Boundary Walls
        for i in range(0,self.height):
            self.maze[i][0] = -1
            self.maze[i][self.width-1] = -1
        for i in range(0,self.width):
            self.maze[0][i] = -1
            self.maze[self.height-1][i] = -1

        # Set Center
        self.maze[self.center[0]][self.center[1]] = 0
        self.cursor = [0,0]

        # Create Canvas
        self.canvas_width = self.width * size
        self.canvas_height = self.height * size
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    # ============
    # Set a Wall
    # =============
    def setWall(self, x, y):
        self.maze[x][y] = -1
    
    # ===============================
    # Check if current cell is a wall
    # ===============================
    def isWall(self, x, y):
        if self.maze[x][y] == -1:
            return True
        return False
    
    # ==================================
    # Check if current position is valid
    # ==================================
    def isValidIndex(self, x, y):
        if x >= 0 and y >= 0 and x < self.height and y < self.width:
            return True
        return False
    
    # ==================
    # Print the maze
    # ==================
    def displayMaze(self):
        print("Displayed")
        self.canvas.delete("all")
        currentX = self.cursor[0]
        currentY = self.cursor[1]
        for row in range(self.width):
            for col in range(self.height):
                x1 = col * size
                y1 = row * size
                x2 = x1 + size
                y2 = y1 + size
                if self.isWall(row,col):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill='black')
                elif row == currentX and col == currentY:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill='red')
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill='white')

    # =======================================
    # DFS function to reach center from start
    # =======================================
    def move(self, initX, initY):
        self.cursor = [initX, initY]
        self.displayMaze()
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

    # ================================================        
    # BFS Function to set distance values for each cell
    # ================================================
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
        root.mainloop()