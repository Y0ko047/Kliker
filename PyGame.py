import sys
from operator import truediv

import pygame
from pygame.examples.go_over_there import screen

pygame.init()

# Создаем окна

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Простое окошко Pygame")

# Создаем основый цикл приложения

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Проверяем на закрытие окона
            running = False
        elif event.type == pygame.KEYDOWN: # Обработка нажатий клавиш
            running = False
            if event.key == pygame.K_ESCAPE: # Закрыть окно при нажатии Esc
                running = False


screen.fill((255,255,255))

pygame.display.update()

pygame.quit()
sys.exit()