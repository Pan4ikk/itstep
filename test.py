import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размера окна
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
FPS = 60
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Установка заголовка окна
pygame.display.set_caption('Игра на Pygame')

# Установка цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Установка параметров объекта
object_width = 50
object_height = 50
object_x = random.randint(0, WINDOW_WIDTH - object_width)
object_y = random.randint(0, WINDOW_HEIGHT - object_height)
object_speed = 5
object_direction = random.choice(['right', 'left', 'up', 'down'])

# Установка параметров игрока
player_width = 50
player_height = 50
player_x = WINDOW_WIDTH / 2
player_y = WINDOW_HEIGHT - player_height
player_speed = 10

# Установка начального счета
score = 0
if money >= 1000000:
    text_str = font.render((money // 1000000), True, (241, 221, 56))
else:
    text_str = font.render(money, True, (241, 221, 56))

# Функция для вывода счета на экран
def display_score():
    font = pygame.font.Font(None, 36)
    text = font.render('Счет: ' + str(score), True, GREEN)
    screen.blit(text, [10, 10])


# Основной цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                # Управление игроком
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= player_speed
            if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - player_width:
                player_x += player_speed
            if keys[pygame.K_UP] and player_y > 0:
                player_y -= player_speed
            if keys[pygame.K_DOWN] and player_y < WINDOW_HEIGHT - player_height:
                player_y += player_speed

    # Движение объекта
    if object_direction == 'right':
        object_x += object_speed
    elif object_direction == 'left':
        object_x -= object_speed
    elif object_direction == 'up':
        object_y -= object_speed
    elif object_direction == 'down':
        object_y += object_speed
    elif object_direction == 'upright':
        object_x += object_speed
        object_y -= object_speed
    elif object_direction == 'upleft':
        object_x -= object_speed
        object_y -= object_speed
    elif object_direction == 'downright':
        object_x += object_speed
        object_y += object_speed
    elif object_direction == 'downleft':
        object_x -= object_speed
        object_y += object_speed

    # Отрисовка объекта
    pygame.draw.rect(screen, WHITE, [object_x, object_y, object_width, object_height])

    # Отрисовка игрока
    pygame.draw.rect(screen, GREEN, [player_x, player_y, player_width, player_height])

    if (player_x + player_width > object_x and
            player_x < object_x + object_width and
            player_y + player_height > object_y and
            player_y < object_y + object_height):
        score += 1
        object_x = random.randint(0, WINDOW_WIDTH - object_width)
        object_y = random.randint(0, WINDOW_HEIGHT - object_height)
        object_direction = random.choice(['right', 'left', 'up', 'down'])

        # Отрисовка счета
    display_score()

    # Обновление экрана
    pygame.display.update()

    # Очистка экрана
    screen.fill(BLACK)

# Завершение Pygame
pygame.quit()