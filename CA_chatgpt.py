import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
CELL_SIZE = 5
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
BG_COLOR = (240, 240, 240)
CELL_COLOR = (30, 30, 30)
FPS = 60

# Initialize grid
grid = np.random.choice([0, 1], size=(ROWS, COLS), p=[0.85, 0.15])

def count_neighbors(grid, x, y):
    """Count the number of alive neighbors of a cell."""
    total = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % ROWS, (y + dy) % COLS
            total += grid[nx, ny]
    return total

def update_grid(grid):
    """Apply the rules of the automaton to update the grid."""
    new_grid = grid.copy()
    for x in range(ROWS):
        for y in range(COLS):
            neighbors = count_neighbors(grid, x, y)
            if grid[x, y] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[x, y] = 0  # Cell dies
            elif grid[x, y] == 0 and neighbors == 3:
                new_grid[x, y] = 1  # Cell becomes alive
    return new_grid

def draw_grid(screen, grid):
    """Draw the grid on the screen."""
    screen.fill(BG_COLOR)
    for x in range(ROWS):
        for y in range(COLS):
            if grid[x, y] == 1:
                pygame.draw.rect(screen, CELL_COLOR, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Cellular Automaton")
    clock = pygame.time.Clock()
    running = True
    global grid
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        grid = update_grid(grid)
        draw_grid(screen, grid)
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
