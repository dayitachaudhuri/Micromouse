import tkinter as tk
import API

def createMaze(): 
    newMaze = API.Maze(10,10,[6,4])
    newMaze.setWall(1,6)
    newMaze.setWall(1,7)
    newMaze.setWall(1,8)
    newMaze.setWall(1,9)
    newMaze.setWall(1,10)
    newMaze.setWall(2,1)
    newMaze.setWall(2,2)
    newMaze.setWall(2,4)
    newMaze.setWall(2,5)
    newMaze.setWall(3,1)
    newMaze.setWall(3,4)
    newMaze.setWall(3,5)
    newMaze.setWall(3,7)
    newMaze.setWall(3,8)
    newMaze.setWall(3,9)
    newMaze.setWall(5,1)
    newMaze.setWall(5,3)
    newMaze.setWall(5,5)
    newMaze.setWall(5,6)
    newMaze.setWall(5,8)
    newMaze.setWall(5,10)
    newMaze.setWall(4,1)
    newMaze.setWall(4,3)
    newMaze.setWall(4,7)
    newMaze.setWall(4,8)
    newMaze.setWall(6,3)
    newMaze.setWall(6,8)
    newMaze.setWall(7,3)
    newMaze.setWall(7,4)
    newMaze.setWall(7,5)
    newMaze.setWall(7,6)
    newMaze.setWall(7,7)
    newMaze.setWall(7,8)
    newMaze.setWall(7,9)

    newMaze.setWall(5,2)
     
    newMaze.start([1,1]) 
    
# root = tk.Tk()
# root.title("Maze")
# size = 40

# label = tk.Label(
#     text="Micromouse Game",
#     fg="black",
#     bg="white"
# )

# label.pack()

# label1 = tk.Label(root, text="Height of Maze")
# entry1 = tk.Entry()
# h = entry1.get()
# label2 = tk.Label(root, text="Width of Maze")
# entry2 = tk.Entry()
# w = entry2.get()
# label3 = tk.Label(root, text="Target Row")
# entry3 = tk.Entry()
# r = entry3.get()
# label4 = tk.Label(root, text="Target Column")
# entry4 = tk.Entry()
# c = entry4.get()
# label1.pack()
# entry1.pack()
# label2.pack()
# entry2.pack()
# label3.pack()
# entry3.pack()
# label4.pack()
# entry4.pack()

# # button = tk.Button(
# #     text="Click me!",
# #     width=25,
# #     height=5,
# #     bg="red",
# #     fg="white",
# #     command = createMaze(h,w,r,c)
# # )

createMaze()

