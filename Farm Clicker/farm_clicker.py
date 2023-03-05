import pygame
import random
from threading import Timer

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 675
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Простой кликер")
bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen.blit(bg, (0, 0))

money = 0
house1_count = 1
house1_earnings = 1
house1_curprice = 5
house2_count = 0
house2_earnings = 0
house2_curprice = 70
house3_count = 0
house3_earnings = 0
house3_curprice = 1000
house4_count = 0
house4_earnings = 0
house4_curprice = 14000
house5_count = 0
house5_earnings = 0
house5_curprice = 200000

# параметры кнопки
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100
COINS_LABEL = ("%.0f" % money)

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
coin_bg = pygame.transform.scale(coin_bg, (500, 50))

screen.blit(farm_bg, (0, 0))
screen.blit(coin_bg, (SCREEN_WIDTH//1.6, 10))

# Создание кнопки
button_rect1 = pygame.Rect(8, 9, BUTTON_WIDTH, BUTTON_HEIGHT)
button_rect2 = pygame.Rect(8, 120, BUTTON_WIDTH, BUTTON_HEIGHT)
button_rect3 = pygame.Rect(8, 230, BUTTON_WIDTH, BUTTON_HEIGHT)
button_rect4 = pygame.Rect(8, 341, BUTTON_WIDTH, BUTTON_HEIGHT)
button_rect5 = pygame.Rect(8, 452, BUTTON_WIDTH, BUTTON_HEIGHT)
button_rect6 = pygame.Rect(300, 560, BUTTON_WIDTH, BUTTON_HEIGHT)


#Настройка окантовки
border_color = (110, 88, 22)
border_size = 2

#Настройка шрифта и текст монеток
font = pygame.font.Font("PressStart2P-Regular.ttf", 11)
coin_border = font.render(COINS_LABEL, True, (110, 88, 22))
text = font.render(COINS_LABEL, True, (241, 221, 56))

#Тени для текста
house1_label_border1 = font.render(f"Кол-во: {house1_count}", True, border_color)
house1_label_border2 = font.render(f"Сум. добыча: {house1_earnings:.1f}", True, border_color)
house1_label_border3 = font.render(f"Стоимость: {house1_curprice:.0f}", True, border_color)
house1_label_border4 = font.render(f"Кол-во: {house2_count}", True, border_color)
house1_label_border5 = font.render(f"Сум. добыча: {house2_earnings:.1f}", True, border_color)
house1_label_border6 = font.render(f"Стоимость: {house2_curprice:.0f}", True, border_color)
house1_label_border7 = font.render(f"Кол-во: {house3_count}", True, border_color)
house1_label_border8 = font.render(f"Сум. добыча: {house3_earnings:.1f}", True, border_color)
house1_label_border9 = font.render(f"Стоимость: {house3_curprice:.0f}", True, border_color)
house1_label_border10 = font.render(f"Кол-во: {house4_count}", True, border_color)
house1_label_border11 = font.render(f"Сум. добыча: {house4_earnings:.1f}", True, border_color)
house1_label_border12 = font.render(f"Стоимость: {house4_curprice:.0f}", True, border_color)
house1_label_border13 = font.render(f"Кол-во: {house5_count}", True, border_color)
house1_label_border14 = font.render(f"Сум. добыча: {house5_earnings:.1f}", True, border_color)
house1_label_border15 = font.render(f"Стоимость: {house5_curprice:.0f}", True, border_color)

#Прописываем текст к кнопкам
house1_label1 = font.render(f"Кол-во: {house1_count}", True, (241, 221, 56))
house1_label2 = font.render(f"Сум. добыча: {house1_earnings:.1f}", True, (241, 221, 56))
house1_label3 = font.render(f"Стоимость: {house1_curprice:.0f}", True, (241, 221, 56))
###################################################################################################
house2_label1 = font.render(f"Кол-во: {house2_count}", True, (241, 221, 56))
house2_label2 = font.render(f"Сум. добыча: {house2_earnings:.1f}", True, (241, 221, 56))
house2_label3 = font.render(f"Стоимость: {house2_curprice:.0f}", True, (241, 221, 56))
###################################################################################################
house3_label1 = font.render(f"Кол-во: {house3_count}", True, (241, 221, 56))
house3_label2 = font.render(f"Сум. добыча: {house3_earnings:.1f}", True, (241, 221, 56))
house3_label3 = font.render(f"Стоимость: {house3_curprice:.0f}", True, (241, 221, 56))
###################################################################################################
house4_label1 = font.render(f"Кол-во: {house4_count}", True, (241, 221, 56))
house4_label2 = font.render(f"Сум. добыча: {house4_earnings:.1f}", True, (241, 221, 56))
house4_label3 = font.render(f"Стоимость: {house4_curprice:.0f}", True, (241, 221, 56))
###################################################################################################
house5_label1 = font.render(f"Кол-во: {house5_count}", True, (241, 221, 56))
house5_label2 = font.render(f"Сум. добыча: {house5_earnings:.1f}", True, (241, 221, 56))
house5_label3 = font.render(f"Стоимость: {house5_curprice:.0f}", True, (241, 221, 56))
###################################################################################################
###################################################################################################
###################################################################################################

def update_all():
    screen.blit(image1, button_rect1)
    screen.blit(image2, button_rect2)
    screen.blit(image3, button_rect3)
    screen.blit(image4, button_rect4)
    screen.blit(image5, button_rect5)
    screen.blit(image5, button_rect6)
    screen.blit(coin_bg, (SCREEN_WIDTH // 1.6, 10))
    screen.blit(coin_image, (SCREEN_WIDTH // 1.6, 10))
    screen.blit(text, (SCREEN_WIDTH // 1.6 + 60, 26))
    screen.blit(house1_label_border1, (button_rect1.x + 129 - border_size, button_rect1.y + 14 - border_size))
    screen.blit(house1_label1, (button_rect1.x + 125, button_rect1.y + 10))
    screen.blit(house1_label_border2, (button_rect1.x + 129 - border_size, button_rect1.y + 44 - border_size))
    screen.blit(house1_label2, (button_rect1.x + 125, button_rect1.y + 40))
    screen.blit(house1_label_border3, (button_rect1.x + 129 - border_size, button_rect1.y + 74 - border_size))
    screen.blit(house1_label3, (button_rect1.x + 125, button_rect1.y + 70))
    screen.blit(house1_label_border4, (button_rect2.x + 129 - border_size, button_rect2.y + 14 - border_size))
    screen.blit(house2_label1, (button_rect2.x + 125, button_rect2.y + 10))
    screen.blit(house1_label_border5, (button_rect2.x + 129 - border_size, button_rect2.y + 44 - border_size))
    screen.blit(house2_label2, (button_rect2.x + 125, button_rect2.y + 40))
    screen.blit(house1_label_border6, (button_rect2.x + 129 - border_size, button_rect2.y + 74 - border_size))
    screen.blit(house2_label3, (button_rect2.x + 125, button_rect2.y + 70))
    screen.blit(house1_label_border7, (button_rect3.x + 129 - border_size, button_rect3.y + 14 - border_size))
    screen.blit(house3_label1, (button_rect3.x + 125, button_rect3.y + 10))
    screen.blit(house1_label_border8, (button_rect3.x + 129 - border_size, button_rect3.y + 44 - border_size))
    screen.blit(house3_label2, (button_rect3.x + 125, button_rect3.y + 40))
    screen.blit(house1_label_border9, (button_rect3.x + 129 - border_size, button_rect3.y + 74 - border_size))
    screen.blit(house3_label3, (button_rect3.x + 125, button_rect3.y + 70))
    screen.blit(house1_label_border10, (button_rect4.x + 129 - border_size, button_rect4.y + 14 - border_size))
    screen.blit(house4_label1, (button_rect4.x + 125, button_rect4.y + 10))
    screen.blit(house1_label_border11, (button_rect4.x + 129 - border_size, button_rect4.y + 44 - border_size))
    screen.blit(house4_label2, (button_rect4.x + 125, button_rect4.y + 40))
    screen.blit(house1_label_border12, (button_rect4.x + 129 - border_size, button_rect4.y + 74 - border_size))
    screen.blit(house4_label3, (button_rect4.x + 125, button_rect4.y + 70))
    screen.blit(house1_label_border13, (button_rect5.x + 129 - border_size, button_rect5.y + 14 - border_size))
    screen.blit(house5_label1, (button_rect5.x + 125, button_rect5.y + 10))
    screen.blit(house1_label_border14, (button_rect5.x + 129 - border_size, button_rect5.y + 44 - border_size))
    screen.blit(house5_label2, (button_rect5.x + 125, button_rect5.y + 40))
    screen.blit(house1_label_border15, (button_rect5.x + 129 - border_size, button_rect5.y + 74 - border_size))
    screen.blit(house5_label3, (button_rect5.x + 125, button_rect5.y + 70))

def auto_click():
    global farm_bg
    global money
    global text
    money += house1_earnings+house2_earnings+house3_earnings+house4_earnings+house5_earnings
    screen.blit(farm_bg, (0, 0))
    text = font.render(("%.0f" % money), True, (241, 221, 56))
    update_all()
    Timer(1, auto_click).start()

def click():
    global money
    money += 1

auto_click()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame .MOUSEBUTTONDOWN and event.button == 1:
            if button_rect1.collidepoint(event.pos):
                print("Кнопка 1 нажата!")
                if money >= house1_curprice:
                    money -= house1_curprice
                    house1_count += 1
                    house1_earnings += 1
                    house1_curprice *= 1.3
                    screen.blit(farm_bg, (0, 0))
                    house1_label1 = font.render(f"Кол-во: {house1_count}", True, (241, 221, 56))
                    house1_label2 = font.render(f"Сум. добыча: {house1_earnings:.1f}", True, (241, 221, 56))
                    house1_label3 = font.render(f"Стоимость: {house1_curprice:.0f}", True, (241, 221, 56))
                    house1_label_border1 = font.render(f"Кол-во: {house1_count}", True, border_color)
                    house1_label_border2 = font.render(f"Сум. добыча: {house1_earnings:.1f}", True, border_color)
                    house1_label_border3 = font.render(f"Стоимость: {house1_curprice:.0f}", True, border_color)
                    text = font.render(COINS_LABEL, True, (241, 221, 56))
                    coin_border = font.render(COINS_LABEL, True, (110, 88, 22))
                    update_all()
            elif button_rect2.collidepoint(event.pos):
                print("Кнопка 2 нажата!")
                if money >= house2_curprice:
                    money -= house2_curprice
                    house2_count += 1
                    house2_earnings += 14
                    house2_curprice *= 1.3
                    screen.blit(farm_bg, (0, 0))
                    house2_label1 = font.render(f"Кол-во: {house2_count}", True, (241, 221, 56))
                    house2_label2 = font.render(f"Сум. добыча: {house2_earnings:.1f}", True, (241, 221, 56))
                    house2_label3 = font.render(f"Стоимость: {house2_curprice:.0f}", True, (241, 221, 56))
                    house2_label_border1 = font.render(f"Кол-во: {house2_count}", True, border_color)
                    house2_label_border2 = font.render(f"Сум. добыча: {house2_earnings:.1f}", True, border_color)
                    house2_label_border3 = font.render(f"Стоимость: {house2_curprice:.0f}", True, border_color)
                    text = font.render(COINS_LABEL, True, (241, 221, 56))
                    coin_border = font.render(COINS_LABEL, True, (110, 88, 22))
                    update_all()
            elif button_rect3.collidepoint(event.pos):
                print("Кнопка 3 нажата!")
                if money >= house3_curprice:
                    money -= house3_curprice
                    house3_count += 1
                    house3_earnings += 196
                    house3_curprice *= 1.3
                    screen.blit(farm_bg, (0, 0))
                    house3_label1 = font.render(f"Кол-во: {house3_count}", True, (241, 221, 56))
                    house3_label2 = font.render(f"Сум. добыча: {house3_earnings:.1f}", True, (241, 221, 56))
                    house3_label3 = font.render(f"Стоимость: {house3_curprice:.0f}", True, (241, 221, 56))
                    house3_label_border1 = font.render(f"Кол-во: {house3_count}", True, border_color)
                    house3_label_border2 = font.render(f"Сум. добыча: {house3_earnings:.1f}", True, border_color)
                    house3_label_border3 = font.render(f"Стоимость: {house3_curprice:.0f}", True, border_color)
                    text = font.render(COINS_LABEL, True, (241, 221, 56))
                    coin_border = font.render(COINS_LABEL, True, (110, 88, 22))
                    update_all()
            elif button_rect4.collidepoint(event.pos):
                print("Кнопка 4 нажата!")
                if money >= house4_curprice:
                    money -= house4_curprice
                    house4_count += 1
                    house4_earnings += 2800
                    house4_curprice *= 1.3
                    screen.blit(farm_bg, (0, 0))
                    house4_label1 = font.render(f"Кол-во: {house4_count}", True, (241, 221, 56))
                    house4_label2 = font.render(f"Сум. добыча: {house4_earnings:.1f}", True, (241, 221, 56))
                    house4_label3 = font.render(f"Стоимость: {house4_curprice:.0f}", True, (241, 221, 56))
                    house4_label_border1 = font.render(f"Кол-во: {house4_count}", True, border_color)
                    house4_label_border2 = font.render(f"Сум. добыча: {house4_earnings:.1f}", True, border_color)
                    house4_label_border3 = font.render(f"Стоимость: {house4_curprice:.0f}", True, border_color)
                    text = font.render(COINS_LABEL, True, (241, 221, 56))
                    coin_border = font.render(COINS_LABEL, True, (110, 88, 22))
                    update_all()
            elif button_rect5.collidepoint(event.pos):
                print("Кнопка 5 нажата!")
                if money >= house5_curprice:
                    money -= house5_curprice
                    house5_count += 1
                    house5_earnings += 39200
                    house5_curprice *= 1.3
                    screen.blit(farm_bg, (0, 0))
                    house5_label1 = font.render(f"Кол-во: {house5_count}", True, (241, 221, 56))
                    house5_label2 = font.render(f"Сум. добыча: {house5_earnings:.1f}", True, (241, 221, 56))
                    house5_label3 = font.render(f"Стоимость: {house5_curprice:.0f}", True, (241, 221, 56))
                    house5_label_border1 = font.render(f"Кол-во: {house5_count}", True, border_color)
                    house5_label_border2 = font.render(f"Сум. добыча: {house5_earnings:.1f}", True, border_color)
                    house5_label_border3 = font.render(f"Стоимость: {house5_curprice:.0f}", True, border_color)
                    text = font.render(COINS_LABEL, True, (241, 221, 56))
                    coin_border = font.render(COINS_LABEL, True, (110, 88, 22))
                    update_all()
            elif button_rect6.collidepoint(event.pos):
                click()
                update_all()

    pygame.display.update()

    pygame.time.Clock().tick(FPS)

pygame.quit()
