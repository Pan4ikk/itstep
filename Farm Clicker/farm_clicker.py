import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Простой кликер")
bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen.blit(bg, (0, 0))

money = 0
house1_count = 5
house1_earnings = 1
house1_curprice = 10
house2_count = 4
house2_earnings = 5
house2_curprice = 30
house3_count = 3
house3_earnings = 15
house3_curprice = 100
house4_count = 2
house4_earnings = 50
house4_curprice = 320
house5_count = 1
house5_earnings = 200
house5_curprice = 1000

# параметры кнопки
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100
COINS_LABEL = f" = {money}"

coin_bg = pygame.image.load("bg_coin.png")
farm_bg = pygame.image.load("bg_farm.png")
image1 = pygame.image.load("farm (2).png")
image2 = pygame.image.load("farm (3).png")
image3 = pygame.image.load("farm (4).png")
image4 = pygame.image.load("farm (5).png")
image5 = pygame.image.load("farm (6).png")
coin_image = pygame.image.load("coin.png")

image1 = pygame.transform.scale(image1, (BUTTON_WIDTH, BUTTON_HEIGHT))
image2 = pygame.transform.scale(image2, (BUTTON_WIDTH, BUTTON_HEIGHT))
image3 = pygame.transform.scale(image3, (BUTTON_WIDTH, BUTTON_HEIGHT))
image4 = pygame.transform.scale(image4, (BUTTON_WIDTH, BUTTON_HEIGHT))
image5 = pygame.transform.scale(image5, (BUTTON_WIDTH, BUTTON_HEIGHT))
coin_image = pygame.transform.scale(coin_image, (50, 50))
coin_bg = pygame.transform.scale(coin_bg, (300, 50))

screen.blit(farm_bg, (0, 0))
screen.blit(coin_bg, (SCREEN_WIDTH//1.2, 10))

# Создание кнопки
button_rect1 = pygame.Rect(10, 10, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image1, button_rect1)
button_rect2 = pygame.Rect(10, 120, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image2, button_rect2)
button_rect3 = pygame.Rect(10, 230, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image3, button_rect3)
button_rect4 = pygame.Rect(10, 340, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image4, button_rect4)
button_rect5 = pygame.Rect(10, 450, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image5, button_rect5)

screen.blit(coin_image, (SCREEN_WIDTH//1.2, 10))

font = pygame.font.Font("Roboto-Regular.ttf", 24)
text = font.render(COINS_LABEL, True, (255, 255, 255))
screen.blit(text, (SCREEN_WIDTH//1.2+45, 21))


house1_label = font.render(f"Кол-во: {house1_count}", True, (0, 0, 0))
screen.blit(house1_label, (button_rect1.x+122, button_rect1.y))
house1_label = font.render(f"Сум. добыча: {house1_earnings}", True, (0, 0, 0))
screen.blit(house1_label, (button_rect1.x+122, button_rect1.y+30))
house1_label = font.render(f"Стоимость: {house1_curprice}", True, (0, 0, 0))
screen.blit(house1_label, (button_rect1.x+122, button_rect1.y+60))


house2_label = font.render(f"Кол-во: {house2_count}", True, (0, 0, 0))
screen.blit(house2_label, (button_rect2.x+122, button_rect2.y))
house2_label = font.render(f"Сум. добыча: {house2_earnings}", True, (0, 0, 0))
screen.blit(house2_label, (button_rect2.x+122, button_rect2.y+30))
house2_label = font.render(f"Стоимость: {house2_curprice}", True, (0, 0, 0))
screen.blit(house2_label, (button_rect2.x+122, button_rect2.y+60))

house3_label = font.render(f"Кол-во: {house3_count}", True, (0, 0, 0))
screen.blit(house3_label, (button_rect3.x+122, button_rect3.y))
house3_label = font.render(f"Сум. добыча: {house3_earnings}", True, (0, 0, 0))
screen.blit(house3_label, (button_rect3.x+122, button_rect3.y+30))
house3_label = font.render(f"Стоимость: {house3_curprice}", True, (0, 0, 0))
screen.blit(house3_label, (button_rect3.x+122, button_rect3.y+60))

house4_label = font.render(f"Кол-во: {house4_count}", True, (0, 0, 0))
screen.blit(house4_label, (button_rect4.x+122, button_rect4.y))
house4_label = font.render(f"Сум. добыча: {house4_earnings}", True, (0, 0, 0))
screen.blit(house4_label, (button_rect4.x+122, button_rect4.y+30))
house4_label = font.render(f"Стоимость: {house4_curprice}", True, (0, 0, 0))
screen.blit(house4_label, (button_rect4.x+122, button_rect4.y+60))

house5_label = font.render(f"Кол-во: {house5_count}", True, (0, 0, 0))
screen.blit(house5_label, (button_rect5.x+122, button_rect5.y))
house5_label = font.render(f"Сум. добыча: {house5_earnings}", True, (0, 0, 0))
screen.blit(house5_label, (button_rect5.x+122, button_rect5.y+30))
house5_label = font.render(f"Стоимость: {house5_curprice}", True, (0, 0, 0))
screen.blit(house5_label, (button_rect5.x+122, button_rect5.y+60))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame .MOUSEBUTTONDOWN and event.button == 1:
            if button_rect1.collidepoint(event.pos):
                print("Кнопка 1 нажата!")
            if button_rect2.collidepoint(event.pos):
                print("Кнопка 2 нажата!")
            if button_rect3.collidepoint(event.pos):
                print("Кнопка 3 нажата!")
            if button_rect4.collidepoint(event.pos):
                print("Кнопка 4 нажата!")
            if button_rect5.collidepoint(event.pos):
                print("Кнопка 5 нажата!")


    pygame.display.update()

    pygame.time.Clock().tick(FPS)

pygame.quit()
