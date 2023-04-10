
from random import shuffle, randrange
import numpy as np
import matplotlib.pyplot as plt


def print_colored_maze(maze):
    for i in range(maze.shape[0]):
        row = ""
        for j in range(maze.shape[1]):
            if maze[i][j] == 1:
                row += "\033[40m  \033[0m"  # black background for wall
            else:
                row += "\033[47m  \033[0m"  # white background for path
        print(row)


def make_binary_maze(w=16, h=8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["10"] * w + ['1'] for _ in range(h)] + [[]]
    hor = [["11"] * w + ['1'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                hor[max(y, yy)][x] = "10"
            if yy == y:
                ver[y][max(x, xx)] = "00"
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = []
    for (a, b) in zip(hor, ver):
        temp = []
        for i in a:
            temp.extend((i))
        s.append(list(map(int,temp)))
        temp = []
        for i in b:
            temp.extend(i)
        s.append(list(map(int,temp)))
    s.pop(-1)

    return np.array(s)


def make_maze(w=16, h=8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                hor[max(y, yy)][x] = "+  "
            if yy == y:
                ver[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])

    return s

def bfs(maze):
    n, m = len(maze), len(maze[0])
    queue = [(1, 1)]
    height = [[0] * m for _ in range(n)]
    height[1][1] = 1
    
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        x, y = queue.pop(0)
        
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maze[nx][ny] == 1 or height[nx][ny] != 0:
                continue
            height[nx][ny] = height[x][y] + 1
            queue.append((nx, ny))
            
    return np.array(height)


if __name__ == '__main__':
    maze = make_maze(5, 5)
    print(maze)
    bin_maze = make_binary_maze(15,15)
    print_colored_maze(bin_maze)
    heights = bfs(bin_maze)
    heights[heights < 1] = 255
    plt.imshow(heights)
    plt.show()