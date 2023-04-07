import tkinter as tk

# Set the size of the maze
maze_size = 4

# Initialize the maze as a 2D array of walls
maze = [['#' for i in range(maze_size)] for j in range(maze_size)]

# Create the Tkinter window and canvas
root = tk.Tk()
canvas_width = maze_size * 20
canvas_height = maze_size * 20
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Draw the maze on the canvas
for row in range(maze_size):
    for col in range(maze_size):
        x1 = col * 20
        y1 = row * 20
        x2 = x1 + 20
        y2 = y1 + 20
        if maze[row][col] == '#':
            canvas.create_rectangle(x1, y1, x2, y2, fill='black')
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill='white')

# Start the Tkinter event loop
root.mainloop()