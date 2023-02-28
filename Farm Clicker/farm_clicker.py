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
button_rect1 = pygame.Rect(8, 9, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image1, button_rect1)
button_rect2 = pygame.Rect(8, 120, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image2, button_rect2)
button_rect3 = pygame.Rect(8, 230, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image3, button_rect3)
button_rect4 = pygame.Rect(8, 341, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image4, button_rect4)
button_rect5 = pygame.Rect(8, 452, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image5, button_rect5)

screen.blit(coin_image, (SCREEN_WIDTH//1.2, 10))

#Настройка окантовки
border_color = (110, 88, 22)
border_size = 2

#Настройка шрифта и текст монеток
font = pygame.font.Font("PressStart2P-Regular.ttf", 11)
coin_border = font.render(COINS_LABEL, True, (110, 88, 22))
text = font.render(COINS_LABEL, True, (241, 221, 56))
screen.blit(coin_border, (SCREEN_WIDTH//1.2+47, 23))
screen.blit(text, (SCREEN_WIDTH//1.2+45, 21))

#Тени для текста
house1_label_border1 = font.render(f"Кол-во: {house1_count}", True, border_color)
house1_label_border2 = font.render(f"Сум. добыча: {house1_earnings}", True, border_color)
house1_label_border3 = font.render(f"Стоимость: {house1_curprice}", True, border_color)
house1_label_border4 = font.render(f"Кол-во: {house2_count}", True, border_color)
house1_label_border5 = font.render(f"Сум. добыча: {house2_earnings}", True, border_color)
house1_label_border6 = font.render(f"Стоимость: {house2_curprice}", True, border_color)
house1_label_border7 = font.render(f"Кол-во: {house3_count}", True, border_color)
house1_label_border8 = font.render(f"Сум. добыча: {house3_earnings}", True, border_color)
house1_label_border9 = font.render(f"Стоимость: {house3_curprice}", True, border_color)
house1_label_border10 = font.render(f"Кол-во: {house4_count}", True, border_color)
house1_label_border11 = font.render(f"Сум. добыча: {house4_earnings}", True, border_color)
house1_label_border12 = font.render(f"Стоимость: {house4_curprice}", True, border_color)
house1_label_border13 = font.render(f"Кол-во: {house5_count}", True, border_color)
house1_label_border14 = font.render(f"Сум. добыча: {house5_earnings}", True, border_color)
house1_label_border15 = font.render(f"Стоимость: {house5_curprice}", True, border_color)

#Прописываем текст к кнопкам
house1_label = font.render(f"Кол-во: {house1_count}", True, (241, 221, 56))
screen.blit(house1_label_border1, (button_rect1.x+129-border_size, button_rect1.y+14-border_size))
screen.blit(house1_label, (button_rect1.x+125, button_rect1.y+10))
house1_label = font.render(f"Сум. добыча: {house1_earnings}", True, (241, 221, 56))
screen.blit(house1_label_border2, (button_rect1.x+129-border_size, button_rect1.y+44-border_size))
screen.blit(house1_label, (button_rect1.x+125, button_rect1.y+40))
house1_label = font.render(f"Стоимость: {house1_curprice}", True, (241, 221, 56))
screen.blit(house1_label_border3, (button_rect1.x+129-border_size, button_rect1.y+74-border_size))
screen.blit(house1_label, (button_rect1.x+125, button_rect1.y+70))
###################################################################################################
house2_label = font.render(f"Кол-во: {house2_count}", True, (241, 221, 56))
screen.blit(house1_label_border4, (button_rect2.x+129-border_size, button_rect2.y+14-border_size))
screen.blit(house2_label, (button_rect2.x+125, button_rect2.y+10))
house2_label = font.render(f"Сум. добыча: {house2_earnings}", True, (241, 221, 56))
screen.blit(house1_label_border5, (button_rect2.x+129-border_size, button_rect2.y+44-border_size))
screen.blit(house2_label, (button_rect2.x+125, button_rect2.y+40))
house2_label = font.render(f"Стоимость: {house2_curprice}", True, (241, 221, 56))
screen.blit(house1_label_border6, (button_rect2.x+129-border_size, button_rect2.y+74-border_size))
screen.blit(house2_label, (button_rect2.x+125, button_rect2.y+70))
###################################################################################################
house3_label = font.render(f"Кол-во: {house3_count}", True, (241, 221, 56))
screen.blit(house1_label_border7, (button_rect3.x+129-border_size, button_rect3.y+14-border_size))
screen.blit(house3_label, (button_rect3.x+125, button_rect3.y+10))
house3_label = font.render(f"Сум. добыча: {house3_earnings}", True, (241, 221, 56))
screen.blit(house1_label_border8, (button_rect3.x+129-border_size, button_rect3.y+44-border_size))
screen.blit(house3_label, (button_rect3.x+125, button_rect3.y+40))
house3_label = font.render(f"Стоимость: {house3_curprice}", True, (241, 221, 56))
screen.blit(house1_label_border9, (button_rect3.x+129-border_size, button_rect3.y+74-border_size))
screen.blit(house3_label, (button_rect3.x+125, button_rect3.y+70))
###################################################################################################
house4_label = font.render(f"Кол-во: {house4_count}", True, (241, 221, 56))
screen.blit(house1_label_border10, (button_rect4.x+129-border_size, button_rect4.y+14.5-border_size))
screen.blit(house4_label, (button_rect4.x+125, button_rect4.y+10))
house4_label = font.render(f"Сум. добыча: {house4_earnings}", True, (241, 221, 56))
screen.blit(house1_label_border11, (button_rect4.x+129-border_size, button_rect4.y+44.5-border_size))
screen.blit(house4_label, (button_rect4.x+125, button_rect4.y+40))
house4_label = font.render(f"Стоимость: {house4_curprice}", True, (241, 221, 56))
screen.blit(house1_label_border12, (button_rect4.x+129-border_size, button_rect4.y+74.5-border_size))
screen.blit(house4_label, (button_rect4.x+125, button_rect4.y+70))
###################################################################################################
house5_label = font.render(f"Кол-во: {house5_count}", True, (241, 221, 56))
screen.blit(house1_label_border13, (button_rect5.x+129-border_size, button_rect5.y+11.5-border_size))
screen.blit(house5_label, (button_rect5.x+125, button_rect5.y+7))
house5_label = font.render(f"Сум. добыча: {house5_earnings}", True, (241, 221, 56))
screen.blit(house1_label_border14, (button_rect5.x+129-border_size, button_rect5.y+41.5-border_size))
screen.blit(house5_label, (button_rect5.x+125, button_rect5.y+37))
house5_label = font.render(f"Стоимость: {house5_curprice}", True, (241, 221, 56))
screen.blit(house1_label_border15, (button_rect5.x+129-border_size, button_rect5.y+71.5-border_size))
screen.blit(house5_label, (button_rect5.x+125, button_rect5.y+67))
###################################################################################################
###################################################################################################
###################################################################################################

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
