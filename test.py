import random

def generate_maze(rows, cols):
    # create a grid with all walls
    maze = [['#' for j in range(cols)] for i in range(rows)]

    # choose a random starting point
    current_row = random.randint(0, rows - 1)
    current_col = random.randint(0, cols - 1)

    # mark starting point as open
    maze[current_row][current_col] = ' '

    # create a list of directions to move in
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # iterate until all cells are visited
    while any('#' in row for row in maze):
        # shuffle the directions list
        random.shuffle(directions)

        # check each direction in random order
        for dx, dy in directions:
            next_row = current_row + dy
            next_col = current_col + dx

            # check if next cell is out of bounds
            if (next_row < 0 or next_row >= rows or
                next_col < 0 or next_col >= cols):
                continue

            # check if next cell is already open
            if maze[next_row][next_col] == ' ':
                continue

            # carve a path and mark cell as open
            if dx == 1:
                maze[current_row][current_col+1] = ' '
            elif dx == -1:
                maze[current_row][current_col-1] = ' '
            elif dy == 1:
                maze[current_row+1][current_col] = ' '
            else:
                maze[current_row-1][current_col] = ' '

            maze[next_row][next_col] = ' '

            # move to the next cell
            current_row, current_col = next_row, next_col

    return maze

def print_maze(maze):
    for row in maze:
        print(' '.join(row))

# example usage
maze = generate_maze(10, 10)
print_maze(maze)