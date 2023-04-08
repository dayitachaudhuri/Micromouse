import tkinter as tk
import API

def createMaze(h,w,r,c): 
    newMaze = API.Maze(h,w,[r,c])
    newMaze.setWall(2,1)
    newMaze.setWall(2,2)
    newMaze.setWall(2,3)
    newMaze.setWall(3,1)
    newMaze.setWall(4,0)
    newMaze.setWall(3,2)  
    newMaze.start([1,2]) 

createMaze(5, 5, 3, 3)

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

# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="red",
#     fg="white",
#     command = createMaze(h,w,r,c)
# )