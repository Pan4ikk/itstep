import pygame
import random
from threading import Timer

# Инициализация Pygame
pygame.init()

# Установка размера окна
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
FPS = 60
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)

WHITE = (255, 255, 255)

money = 10
house1_count = 1
house1_earnings = 1
house1_curprice = 5

# параметры кнопки
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100
COINS_LABEL = ("%.0f" % money)


font = pygame.font.Font("PressStart2P-Regular.ttf", 11)
text = font.render(COINS_LABEL, True, (241, 221, 56))

button_rect1 = pygame.Rect(8, 9, BUTTON_WIDTH, BUTTON_HEIGHT)

pygame.draw.rect(screen, WHITE, button_rect1)

# Установка заголовка окна
pygame.display.set_caption('Игра на Pygame')

# Установка цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

def click():
    global money
    money += 1
    text = font.render('Счет: ' + str(money), True, WHITE)
    screen.blit(text, [10, 10])

# Основной цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect1.collidepoint(event.pos):
                print("Кнопка нажата!")
                print(money)
                click()

    screen.blit(text, (WINDOW_WIDTH // 1.6 + 60, 26))

    # Обновление экрана
    pygame.display.update()

    # Очистка экрана
    screen.fill(BLACK)
# Завершение Pygame
pygame.quit()