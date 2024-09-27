import pygame
import sys
from pygame.color import THECOLORS

pygame.init()
# Дополнительное занятие, работа с фигурами
screen = pygame.display.set_mode((800, 600))
screen.fill(THECOLORS['orange'])
r = pygame.Rect(300, 400, 200, 200)
pygame.draw.rect(screen, (255, 0, 0), r, 0)

t = pygame.Rect(50, 50, 100, 100)
pygame.draw.rect(screen, (100, 0, 0), t, 0)

pygame.draw.circle(screen, (50, 0, 0), (700, 100), 40, 1)

triangle_points = [(400, 250), (350, 400), (450, 400)]  # Координаты вершин треугольника
pygame.draw.polygon(screen, (0, 255, 0), triangle_points)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()

