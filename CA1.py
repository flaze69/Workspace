import pygame
import random
import time

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 500

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("CA1")
clock = pygame.time.Clock()

SIZE = 20 #Cube size
CUBE_COLOR = (30, 30, 30)

for x in range(WINDOW_WIDTH//SIZE):
        for y in range(WINDOW_HEIGHT//SIZE):
            pygame.draw.rect(screen, CUBE_COLOR, (x*SIZE, y*SIZE, SIZE, SIZE))

while True:
    screen.fill((255, 255, 255))

    
            

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
    clock.tick(60)