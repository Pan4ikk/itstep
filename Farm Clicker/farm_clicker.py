import pygame
import random
from threading import Timer

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 675
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Супермегакрутой кликер")
bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen.blit(bg, (0, 0))
pygame.display.set_icon(pygame.image.load("icon.png"))

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
sword_count = 0
sword_click = 1
sword_curprice = 1000

housex1 = 1

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
sword1 = pygame.image.load("sword1.png")
sword2 = pygame.image.load("sword2.png")
sword3 = pygame.image.load("sword3.png")
sword4 = pygame.image.load("sword4.png")
coin_image = pygame.image.load("coin.png")
upgrade_icon = pygame.image.load("upgrade_icon.png")

image1 = pygame.transform.scale(image1, (BUTTON_WIDTH, BUTTON_HEIGHT))
image2 = pygame.transform.scale(image2, (BUTTON_WIDTH, BUTTON_HEIGHT))
image3 = pygame.transform.scale(image3, (BUTTON_WIDTH, BUTTON_HEIGHT))
image4 = pygame.transform.scale(image4, (BUTTON_WIDTH, BUTTON_HEIGHT))
image5 = pygame.transform.scale(image5, (BUTTON_WIDTH, BUTTON_HEIGHT))
sword1 = pygame.transform.scale(sword1, (BUTTON_WIDTH, BUTTON_HEIGHT))
sword2 = pygame.transform.scale(sword2, (BUTTON_WIDTH, BUTTON_HEIGHT))
sword3 = pygame.transform.scale(sword3, (BUTTON_WIDTH, BUTTON_HEIGHT))
sword4 = pygame.transform.scale(sword4, (BUTTON_WIDTH, BUTTON_HEIGHT))
upgrade_icon = pygame.transform.scale(upgrade_icon, (BUTTON_WIDTH, BUTTON_HEIGHT))

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
sword = pygame.Rect(335, 560, BUTTON_WIDTH, BUTTON_HEIGHT)

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
###################################################################################################
sword_label_border1 = font.render(f"Уровень: {sword_count}", True, border_color)
sword_label_border2 = font.render(f"Cум. клик: {sword_click}", True, border_color)
sword_label_border3 = font.render(f"Стоимость: {sword_curprice}", True, border_color)
###################################################################################################
###################################################################################################

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
sword_label1 = font.render(f"Уровень: {sword_count}", True, (241, 221, 56))
sword_label2 = font.render(f"Cум. клик: {sword_click:}", True, (241, 221, 56))
sword_label3 = font.render(f"Стоимость: {sword_curprice:}", True, (241, 221, 56))
###################################################################################################
###################################################################################################
upgrade1_1 = pygame.Rect(337, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
upgrade1_2 = pygame.Rect(337, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
def update_all():
    screen.blit(image1, button_rect1)
    screen.blit(image2, button_rect2)
    screen.blit(image3, button_rect3)
    screen.blit(image4, button_rect4)
    screen.blit(image5, button_rect5)
    screen.blit(upgrade_icon, sword)
    screen.blit(image5, upgrade1_1)
    screen.blit(image1, upgrade1_2)
    screen.blit(coin_bg, (SCREEN_WIDTH // 1.6, 10))
    screen.blit(coin_image, (SCREEN_WIDTH // 1.6, 10))
    screen.blit(text, (SCREEN_WIDTH // 1.6 + 60, 26))
    screen.blit(sword_label_border1, (sword.x - 307, sword.y + 17))
    screen.blit(sword_label1, (sword.x - 309, sword.y + 15))
    screen.blit(sword_label_border2, (sword.x - 307, sword.y + 47))
    screen.blit(sword_label2, (sword.x - 309, sword.y + 45))
    screen.blit(sword_label_border3, (sword.x - 307, sword.y + 77))
    screen.blit(sword_label3, (sword.x - 309, sword.y + 75))
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
    global sword_label1
    global sword_label2
    global sword_label3
    global farm_bg
    global money
    global text
    global housex1
    global upgrade1_2
    global upgrade1_1
    global sword
    global sword_count
    global swordx
    global sword_label_border1
    global sword_label_border2
    global sword_label_border3
    money += house1_earnings+house2_earnings+house3_earnings+house4_earnings+house5_earnings
    screen.blit(farm_bg, (0, 0))
    text = font.render(("%.0f" % money), True, (241, 221, 56))
    update_all()
    sword_label_border1 = font.render(f"Уровень: {sword_count}", True, border_color)
    sword_label_border2 = font.render(f"Cум. клик: {sword_click}", True, border_color)
    sword_label_border3 = font.render(f"Стоимость: {sword_curprice}", True, border_color)
    sword_label1 = font.render(f"Уровень: {sword_count}", True, (241, 221, 56))
    sword_label2 = font.render(f"Cум. клик: {sword_click}", True, (241, 221, 56))
    sword_label3 = font.render(f"Стоимость: {sword_curprice}", True, (241, 221, 56))
    if sword_count >= 3:
        sword_label_border1 = font.render(f"Уровень: Макс.", True, border_color)
        sword_label_border2 = font.render(f"Cум. клик: {sword_click}", True, border_color)
        sword_label_border3 = font.render(f"Стоимость: Макс.", True, border_color)
        sword_label1 = font.render(f"Уровень: Макс.", True, (241, 221, 56))
        sword_label2 = font.render(f"Cум. клик: {sword_click}", True, (241, 221, 56))
        sword_label3 = font.render(f"Стоимость: Макс.", True, (241, 221, 56))
    if house1_count >= 5:
        if housex1 >= 5:
            update_all()
        else:
            upgrade1_1 = pygame.Rect(337, 11, BUTTON_WIDTH, BUTTON_HEIGHT)
    if house1_count >= 10 and housex1 == 5:
        if housex1 >= 25:
            update_all()
        else:
            upgrade1_2 = pygame.Rect(337, 11, BUTTON_WIDTH, BUTTON_HEIGHT)
    if sword_count == 0:
        screen.blit(sword1, sword)
    elif sword_count == 1:
        screen.blit(sword2, sword)
    elif sword_count == 2:
        screen.blit(sword3, sword)
    elif sword_count >= 3:
        screen.blit(sword4, sword)
    Timer(1, auto_click).start()
    print(housex1)

def upgrade():
    global house1_label2
    global house1_label_border2
    global house1_earnings
    global housex1
    house1_earnings *= 5
    housex1 *= 5
    house1_label2 = font.render(f"Сум. добыча: {house1_earnings}", True, (241, 221, 56))
    house1_label_border2 = font.render(f"Сум. добыча: {house1_earnings}", True, border_color)
    update_all()

auto_click()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame .MOUSEBUTTONDOWN and event.button == 1:
            ##################
            ### КНОПКИ 1-5 ###
            if button_rect1.collidepoint(event.pos):
                print("Кнопка 1 нажата!")
                if money >= house1_curprice:
                    money -= house1_curprice
                    house1_count += 1
                    house1_earnings += 1 * housex1
                    house1_curprice *= 2
                    screen.blit(farm_bg, (0, 0))
                    house1_label_border1 = font.render(f"Кол-во: {house1_count}", True, border_color)
                    house1_label_border2 = font.render(f"Сум. добыча: {house1_earnings:.1f}", True, border_color)
                    house1_label_border3 = font.render(f"Стоимость: {house1_curprice:.0f}", True, border_color)
                    house1_label1 = font.render(f"Кол-во: {house1_count}", True, (241, 221, 56))
                    house1_label2 = font.render(f"Сум. добыча: {house1_earnings:.1f}", True, (241, 221, 56))
                    house1_label3 = font.render(f"Стоимость: {house1_curprice:.0f}", True, (241, 221, 56))
                    text = font.render(COINS_LABEL, True, (241, 221, 56))
                    coin_border = font.render(COINS_LABEL, True, (110, 88, 22))
                    update_all()
            elif button_rect2.collidepoint(event.pos):
                print("Кнопка 2 нажата!")
                if money >= house2_curprice:
                    money -= house2_curprice
                    house2_count += 1
                    house2_earnings += 14
                    house2_curprice *= 2
                    screen.blit(farm_bg, (0, 0))
                    house2_label_border1 = font.render(f"Кол-во: {house2_count}", True, border_color)
                    house2_label_border2 = font.render(f"Сум. добыча: {house2_earnings:.1f}", True, border_color)
                    house2_label_border3 = font.render(f"Стоимость: {house2_curprice:.0f}", True, border_color)
                    house2_label1 = font.render(f"Кол-во: {house2_count}", True, (241, 221, 56))
                    house2_label2 = font.render(f"Сум. добыча: {house2_earnings:.1f}", True, (241, 221, 56))
                    house2_label3 = font.render(f"Стоимость: {house2_curprice:.0f}", True, (241, 221, 56))
                    text = font.render(COINS_LABEL, True, (241, 221, 56))
                    coin_border = font.render(COINS_LABEL, True, (110, 88, 22))
                    update_all()
            elif button_rect3.collidepoint(event.pos):
                print("Кнопка 3 нажата!")
                if money >= house3_curprice:
                    money -= house3_curprice
                    house3_count += 1
                    house3_earnings += 196
                    house3_curprice *= 2
                    screen.blit(farm_bg, (0, 0))
                    house3_label_border1 = font.render(f"Кол-во: {house3_count}", True, border_color)
                    house3_label_border2 = font.render(f"Сум. добыча: {house3_earnings:.1f}", True, border_color)
                    house3_label_border3 = font.render(f"Стоимость: {house3_curprice:.0f}", True, border_color)
                    house3_label1 = font.render(f"Кол-во: {house3_count}", True, (241, 221, 56))
                    house3_label2 = font.render(f"Сум. добыча: {house3_earnings:.1f}", True, (241, 221, 56))
                    house3_label3 = font.render(f"Стоимость: {house3_curprice:.0f}", True, (241, 221, 56))
                    text = font.render(COINS_LABEL, True, (241, 221, 56))
                    coin_border = font.render(COINS_LABEL, True, (110, 88, 22))
                    update_all()
            elif button_rect4.collidepoint(event.pos):
                print("Кнопка 4 нажата!")
                if money >= house4_curprice:
                    money -= house4_curprice
                    house4_count += 1
                    house4_earnings += 2800
                    house4_curprice *= 2
                    screen.blit(farm_bg, (0, 0))
                    house4_label_border1 = font.render(f"Кол-во: {house4_count}", True, border_color)
                    house4_label_border2 = font.render(f"Сум. добыча: {house4_earnings:.1f}", True, border_color)
                    house4_label_border3 = font.render(f"Стоимость: {house4_curprice:.0f}", True, border_color)
                    house4_label1 = font.render(f"Кол-во: {house4_count}", True, (241, 221, 56))
                    house4_label2 = font.render(f"Сум. добыча: {house4_earnings:.1f}", True, (241, 221, 56))
                    house4_label3 = font.render(f"Стоимость: {house4_curprice:.0f}", True, (241, 221, 56))
                    text = font.render(COINS_LABEL, True, (241, 221, 56))
                    coin_border = font.render(COINS_LABEL, True, (110, 88, 22))
                    update_all()
            elif button_rect5.collidepoint(event.pos):
                print("Кнопка 5 нажата!")
                if money >= house5_curprice:
                    money -= house5_curprice
                    house5_count += 1
                    house5_earnings += 39200
                    house5_curprice *= 2
                    screen.blit(farm_bg, (0, 0))
                    house5_label_border1 = font.render(f"Кол-во: {house5_count}", True, border_color)
                    house5_label_border2 = font.render(f"Сум. добыча: {house5_earnings:.1f}", True, border_color)
                    house5_label_border3 = font.render(f"Стоимость: {house5_curprice:.0f}", True, border_color)
                    house5_label1 = font.render(f"Кол-во: {house5_count}", True, (241, 221, 56))
                    house5_label2 = font.render(f"Сум. добыча: {house5_earnings:.1f}", True, (241, 221, 56))
                    house5_label3 = font.render(f"Стоимость: {house5_curprice:.0f}", True, (241, 221, 56))
                    text = font.render(COINS_LABEL, True, (241, 221, 56))
                    coin_border = font.render(COINS_LABEL, True, (110, 88, 22))
                    update_all()
            ###################
            ### КНОПКА МЕЧА ###
            elif sword.collidepoint(event.pos):
                money += sword_click
                if money >= sword_curprice and sword_count == 0:
                    money -= sword_curprice
                    sword_click += 19
                    sword_count = 1
                    sword_curprice = 100000
                elif money >= sword_curprice and sword_count == 1:
                    money -= sword_curprice
                    sword_click += 680
                    sword_count = 2
                    sword_curprice = 10000000
                elif money >= sword_curprice and sword_count == 2:
                    money -= sword_curprice
                    sword_click += 49300
                    sword_count = 3
                    sword_curprice *= (9999 * 999)
            ############################
            ### КНОПКИ ПРОКАЧКИ ФЕРМ ###
            elif upgrade1_1.collidepoint(event.pos):
                if money >= 200 and housex1 == 1:
                    money -= 200
                    upgrade()
                    upgrade1_1 = pygame.Rect(8, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
            elif upgrade1_2.collidepoint(event.pos):
                if money >= 10000 and housex1 == 5:
                    money -= 10000
                    upgrade()
                    upgrade1_2 = pygame.Rect(8, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)

    pygame.display.update()
    pygame.time.Clock().tick(FPS)
pygame.quit()
