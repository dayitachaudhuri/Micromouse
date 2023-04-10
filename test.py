import pygame
import time
from maze_gen import *

# Define the maze matrix

# Initialize Pygame
pygame.init()

# Set the screen size and title
screen_size = (500, 500)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Maze Animation")
fps = 60 

# Define the colors
background_color = (255, 255, 255)
wall_color = (0, 0, 0)
path_color = (255, 0, 0)
button_color = (0, 128, 0)
button_text_color = (255, 255, 255)

# Set the size of the maze cells and the margin
cell_size = 20
margin = 1

# Define the button properties
button_width = 120
button_height = 50
button_x = (screen_size[0] - button_width) // 2
button_y = screen_size[1] - 80

# Define a function to draw the maze
def draw_maze(maze, render_flag=True):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col]:
                pygame.draw.rect(screen, wall_color, [(margin+cell_size)*col+margin, (margin+cell_size)*row+margin, cell_size, cell_size])
            else:
                pygame.draw.rect(screen, path_color, [(margin+cell_size)*col+margin, (margin+cell_size)*row+margin, cell_size, cell_size])
            
            if render_flag:
                time.sleep(0.001)
                pygame.display.update()
    render_flag = False

    return render_flag

# Define a function to draw the button
def draw_button():
    pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
    font = pygame.font.Font(None, 36)
    text = font.render("Generate", True, button_text_color)
    text_rect = text.get_rect(center=(button_x + button_width / 2, button_y + button_height / 2))
    screen.blit(text, text_rect)

def main(maze):
    # Main game loop
    running = True
    render_flag = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(background_color)
        render_flag = draw_maze(maze, render_flag)
        # Draw the maze


        # Update the display
        pygame.display.update()
        clock.tick(fps)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    maze = make_binary_maze(10,10)
    main(maze)


