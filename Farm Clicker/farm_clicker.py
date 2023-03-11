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

money = 9999999999999
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
house4_curprice = 20000
house5_count = 0
house5_earnings = 0
house5_curprice = 500000
sword_count = 0
sword_click = 1
sword_curprice = 1000

housex1 = 1
housex2 = 1
housex3 = 1
housex4 = 1
housex5 = 1

# параметры кнопки
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100


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
text = font.render(str(money), True, (241, 221, 56))


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

upgrade2_1 = pygame.Rect(337, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
upgrade2_2 = pygame.Rect(337, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)

upgrade3_1 = pygame.Rect(337, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
upgrade3_2 = pygame.Rect(337, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)

upgrade4_1 = pygame.Rect(337, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
upgrade4_2 = pygame.Rect(337, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)

upgrade5_1 = pygame.Rect(337, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
upgrade5_2 = pygame.Rect(337, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)

WHITE = (255, 255, 255)

def update_all():
    screen.blit(image1, button_rect1)
    screen.blit(image2, button_rect2)
    screen.blit(image3, button_rect3)
    screen.blit(image4, button_rect4)
    screen.blit(image5, button_rect5)
    screen.blit(upgrade_icon, sword)
    screen.blit(image5, upgrade1_1)
    screen.blit(image1, upgrade1_2)
    screen.blit(image5, upgrade2_1)
    screen.blit(image1, upgrade2_2)
    screen.blit(image5, upgrade3_1)
    screen.blit(image1, upgrade3_2)
    screen.blit(image5, upgrade4_1)
    screen.blit(image1, upgrade4_2)
    screen.blit(image5, upgrade5_1)
    screen.blit(image1, upgrade5_2)
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
    global sword_label1, sword_label2, sword_label3, farm_bg, money, housex1, upgrade1_2, upgrade1_1, sword, sword_count, swordx, sword_label_border1, sword_label_border2, text
    global sword_label_border3, house2_count, house3_count, house3_count, house3_count, upgrade2_1, upgrade3_1, upgrade4_1, upgrade5_1, upgrade2_2, upgrade3_2, upgrade4_2, upgrade5_2
    money += house1_earnings+house2_earnings+house3_earnings+house4_earnings+house5_earnings
    screen.blit(farm_bg, (0, 0))
    text = font.render(str(money), True, (241, 221, 56))
    if money >= 1000:
        text = font.render(f"= {money/1000:.2f}K", True, (241, 221, 56))
    if money >= 1000000:
        text = font.render(f"= {money/1000000:.2f}M", True, (241, 221, 56))
    if money >= 1000000000:
        text = font.render(f"= {money/1000000000:.2f}B", True, (241, 221, 56))
    if money >= 1000000000000:
        text = font.render(f"= {money/1000000000000:.2f}T", True, (241, 221, 56))
    sword_label_border1 = font.render(f"Уровень: {sword_count}", True, border_color)
    sword_label_border2 = font.render(f"Cум. клик: {sword_click}", True, border_color)
    sword_label_border3 = font.render(f"Стоимость: {sword_curprice}", True, border_color)
    sword_label1 = font.render(f"Уровень: {sword_count}", True, (241, 221, 56))
    sword_label2 = font.render(f"Cум. клик: {sword_click}", True, (241, 221, 56))
    sword_label3 = font.render(f"Стоимость: {sword_curprice}", True, (241, 221, 56))
    if sword_click >= 1000:
        sword_label_border2 = font.render(f"Cум. клик: {sword_click/1000:.1f}K", True, border_color)
        sword_label2 = font.render(f"Cум. клик: {sword_click/1000:.1f}K", True, (241, 221, 56))
    if sword_click >= 1000000:
        sword_label_border2 = font.render(f"Cум. клик: {sword_click/1000000:.1f}M", True, border_color)
        sword_label2 = font.render(f"Cум. клик: {sword_click/1000000:.1f}M", True, (241, 221, 56))
    if sword_curprice >= 1000:
        sword_label_border3 = font.render(f"Стоимость: {sword_curprice/1000:.2f}K", True, border_color)
        sword_label3 = font.render(f"Стоимость: {sword_curprice/1000:.2f}K", True, (241, 221, 56))
    if sword_curprice >= 1000000:
        sword_label_border3 = font.render(f"Стоимость: {sword_curprice/1000000:.2f}M", True, border_color)
        sword_label3 = font.render(f"Стоимость: {sword_curprice/1000000:.2f}M", True, (241, 221, 56))
    if sword_curprice >= 1000000000:
        sword_label_border3 = font.render(f"Стоимость: {sword_curprice/1000000000:.2f}B", True, border_color)
        sword_label3 = font.render(f"Стоимость: {sword_curprice/1000000000:.2f}B", True, (241, 221, 56))
    update_all()
    if sword_count >= 8:
        sword_label_border1 = font.render(f"Уровень: Макс.", True, border_color)
        sword_label_border2 = font.render(f"Cум. клик: {sword_click/1000000000:.2f}B", True, border_color)
        sword_label_border3 = font.render(f"Стоимость: Макс.", True, border_color)
        sword_label1 = font.render(f"Уровень: Макс.", True, (241, 221, 56))
        sword_label2 = font.render(f"Cум. клик: {sword_click/1000000000:.2f}B", True, (241, 221, 56))
        sword_label3 = font.render(f"Стоимость: Макс.", True, (241, 221, 56))
    screen.blit(sword_label_border1, (sword.x - 307, sword.y + 17))
    screen.blit(sword_label1, (sword.x - 309, sword.y + 15))
    screen.blit(sword_label_border2, (sword.x - 307, sword.y + 47))
    screen.blit(sword_label2, (sword.x - 309, sword.y + 45))
    screen.blit(sword_label_border3, (sword.x - 307, sword.y + 77))
    screen.blit(sword_label3, (sword.x - 309, sword.y + 75))
    ########################
    if house1_count >= 5:
        if housex1 >= 5:
            update_all()
        else:
            upgrade1_1 = pygame.Rect(337, 11, BUTTON_WIDTH, BUTTON_HEIGHT)
    if house1_count >= 10 and housex1 == 50:
        if housex1 >= 51:
            update_all()
        else:
            upgrade1_2 = pygame.Rect(337, 11, BUTTON_WIDTH, BUTTON_HEIGHT)
    ########################
    if house2_count >= 5:
        if housex2 >= 5:
            update_all()
        else:
            upgrade2_1 = pygame.Rect(337, 120, BUTTON_WIDTH, BUTTON_HEIGHT)
    if house2_count >= 10 and housex2 == 50:
        if housex2 >= 51:
            update_all()
        else:
            upgrade2_2 = pygame.Rect(337, 120, BUTTON_WIDTH, BUTTON_HEIGHT)
    ########################
    if house3_count >= 5:
        if housex3 >= 5:
            update_all()
        else:
            upgrade3_1 = pygame.Rect(337, 230, BUTTON_WIDTH, BUTTON_HEIGHT)
    if house3_count >= 10 and housex3 == 50:
        if housex3 >= 51:
            update_all()
        else:
            upgrade3_2 = pygame.Rect(337, 230, BUTTON_WIDTH, BUTTON_HEIGHT)
    ########################
    if house4_count >= 5:
        if housex4 >= 5:
            update_all()
        else:
            upgrade4_1 = pygame.Rect(337, 341, BUTTON_WIDTH, BUTTON_HEIGHT)
    if house4_count >= 10 and housex4 == 50:
        if housex4 >= 51:
            update_all()
        else:
            upgrade4_2 = pygame.Rect(337, 341, BUTTON_WIDTH, BUTTON_HEIGHT)
    ########################
    if house5_count >= 5:
        if housex5 >= 5:
            update_all()
        else:
            upgrade5_1 = pygame.Rect(337, 450, BUTTON_WIDTH, BUTTON_HEIGHT)
    if house5_count >= 10 and housex5 == 50:
        if housex5 >= 51:
            update_all()
        else:
            upgrade5_2 = pygame.Rect(337, 450, BUTTON_WIDTH, BUTTON_HEIGHT)
    ########################
    if sword_count == 0:
        screen.blit(sword1, sword)
    elif sword_count == 1:
        screen.blit(sword1, sword)
    elif sword_count == 2:
        screen.blit(sword2, sword)
    elif sword_count == 3:
        screen.blit(sword2, sword)
    elif sword_count == 4:
        screen.blit(sword3, sword)
    elif sword_count == 5:
        screen.blit(sword3, sword)
    elif sword_count == 6:
        screen.blit(sword4, sword)
    elif sword_count >= 7:
        screen.blit(sword4, sword)
    Timer(1, auto_click).start()
    print(housex1)

def upgrade1():
    global house1_label2, house1_label_border2, house1_earnings, housex1
    if housex1 == 50:
        house1_earnings *= 10
        housex1 *= 10
    if housex1 == 1:
        house1_earnings *= 50
        housex1 *= 50
    house1_label2 = font.render(f"Сум. добыча: {house1_earnings}", True, (241, 221, 56))
    house1_label_border2 = font.render(f"Сум. добыча: {house1_earnings}", True, border_color)
    update_all()
def upgrade2():
    global house2_label2, house2_label_border2, house2_earnings, housex2
    if housex2 == 50:
        house2_earnings *= 10
        housex2 *= 10
    if housex2 == 1:
        house2_earnings *= 50
        housex2 *= 50
    house2_label2 = font.render(f"Сум. добыча: {house2_earnings}", True, (241, 221, 56))
    house2_label_border2 = font.render(f"Сум. добыча: {house2_earnings}", True, border_color)
    update_all()
def upgrade3():
    global house3_label2, house3_label_border2, house3_earnings, housex3
    if housex3 == 50:
        house3_earnings *= 10
        housex3 *= 10
    if housex3 == 1:
        house3_earnings *= 50
        housex3 *= 50
    house3_label2 = font.render(f"Сум. добыча: {house3_earnings}", True, (241, 221, 56))
    house3_label_border2 = font.render(f"Сум. добыча: {house3_earnings}", True, border_color)
    update_all()
def upgrade4():
    global house4_label2, house4_label_border2, house4_earnings, housex4
    if housex4 == 50:
        house4_earnings *= 10
        housex4 *= 10
    if housex4 == 1:
        house4_earnings *= 50
        housex4 *= 50
    house4_label2 = font.render(f"Сум. добыча: {house4_earnings}", True, (241, 221, 56))
    house4_label_border2 = font.render(f"Сум. добыча: {house4_earnings}", True, border_color)
    update_all()
def upgrade5():
    global house5_label2, house5_label_border2, house5_earnings, housex5
    if housex5 == 50:
        house5_earnings *= 10
        housex5 *= 10
    if housex5 == 1:
        house5_earnings *= 50
        housex5 *= 50
    house5_label2 = font.render(f"Сум. добыча: {house5_earnings}", True, (241, 221, 56))
    house5_label_border2 = font.render(f"Сум. добыча: {house5_earnings}", True, border_color)
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
                    screen.blit(sword_label_border1, (sword.x - 307, sword.y + 17))
                    screen.blit(sword_label1, (sword.x - 309, sword.y + 15))
                    screen.blit(sword_label_border2, (sword.x - 307, sword.y + 47))
                    screen.blit(sword_label2, (sword.x - 309, sword.y + 45))
                    screen.blit(sword_label_border3, (sword.x - 307, sword.y + 77))
                    screen.blit(sword_label3, (sword.x - 309, sword.y + 75))
                    if house1_earnings >= 1000000:
                        house1_label_border2 = font.render(f"Сум. добыча: {house1_earnings/1000000:.1f}M", True, border_color)
                        house1_label2 = font.render(f"Сум. добыча: {house1_earnings/1000000:.1f}M", True, (241, 221, 56))
                    if house1_earnings >= 1000000000:
                        house1_label_border2 = font.render(f"Сум. добыча: {house1_earnings/1000000000:.1f}B", True, border_color)
                        house1_label2 = font.render(f"Сум. добыча: {house1_earnings/1000000000:.1f}B", True, (241, 221, 56))
                    if house1_earnings >= 1000000000000:
                        house1_label_border2 = font.render(f"Сум. добыча: {house1_earnings/1000000000000:.1f}T", True, border_color)
                        house1_label2 = font.render(f"Сум. добыча: {house1_earnings/1000000000000:.1f}T", True, (241, 221, 56))
                    if house1_curprice >= 1000000:
                        house1_label_border3 = font.render(f"Стоимость: {house1_curprice/1000000:.2f}M", True, border_color)
                        house1_label3 = font.render(f"Стоимость: {house1_curprice/1000000:.2f}M", True, (241, 221, 56))
                    if house1_curprice >= 1000000000:
                        house1_label_border3 = font.render(f"Стоимость: {house1_curprice/1000000000:.2f}B", True, border_color)
                        house1_label3 = font.render(f"Стоимость: {house1_curprice/1000000000:.2f}B", True, (241, 221, 56))
                    if house1_curprice >= 1000000000000:
                        house1_label_border3 = font.render(f"Стоимость: {house1_curprice/1000000000000:.2f}T", True, border_color)
                        house1_label3 = font.render(f"Стоимость: {house1_curprice/1000000000000:.2f}T", True, (241, 221, 56))
                    text = font.render(f"= {money:.2f}", True, (241, 221, 56))
                    update_all()
            elif button_rect2.collidepoint(event.pos):
                print("Кнопка 2 нажата!")
                if money >= house2_curprice:
                    money -= house2_curprice
                    house2_count += 1
                    house2_earnings += 14 * housex2
                    house2_curprice *= 2
                    screen.blit(farm_bg, (0, 0))
                    house2_label_border1 = font.render(f"Кол-во: {house2_count}", True, border_color)
                    house2_label_border2 = font.render(f"Сум. добыча: {house2_earnings:.1f}", True, border_color)
                    house2_label_border3 = font.render(f"Стоимость: {house2_curprice:.0f}", True, border_color)
                    house2_label1 = font.render(f"Кол-во: {house2_count}", True, (241, 221, 56))
                    house2_label2 = font.render(f"Сум. добыча: {house2_earnings:.1f}", True, (241, 221, 56))
                    house2_label3 = font.render(f"Стоимость: {house2_curprice:.0f}", True, (241, 221, 56))
                    screen.blit(sword_label_border1, (sword.x - 307, sword.y + 17))
                    screen.blit(sword_label1, (sword.x - 309, sword.y + 15))
                    screen.blit(sword_label_border2, (sword.x - 307, sword.y + 47))
                    screen.blit(sword_label2, (sword.x - 309, sword.y + 45))
                    screen.blit(sword_label_border3, (sword.x - 307, sword.y + 77))
                    screen.blit(sword_label3, (sword.x - 309, sword.y + 75))
                    if house2_earnings >= 1000000:
                        house2_label_border2 = font.render(f"Сум. добыча: {house2_earnings/1000000:.1f}M", True, border_color)
                        house2_label2 = font.render(f"Сум. добыча: {house2_earnings/1000000:.1f}M", True, (241, 221, 56))
                    if house2_earnings >= 1000000000:
                        house2_label_border2 = font.render(f"Сум. добыча: {house2_earnings/1000000000:.1f}B", True, border_color)
                        house2_label2 = font.render(f"Сум. добыча: {house2_earnings/1000000000:.1f}B", True, (241, 221, 56))
                    if house2_earnings >= 1000000000000:
                        house2_label_border2 = font.render(f"Сум. добыча: {house2_earnings/1000000000000:.1f}T", True, border_color)
                        house2_label2 = font.render(f"Сум. добыча: {house2_earnings/1000000000000:.1f}T", True, (241, 221, 56))
                    if house2_curprice >= 1000000:
                        house2_label_border3 = font.render(f"Стоимость: {house2_curprice/1000000:.2f}M", True, border_color)
                        house2_label3 = font.render(f"Стоимость: {house2_curprice/1000000:.2f}M", True, (241, 221, 56))
                    if house2_curprice >= 1000000000:
                        house2_label_border3 = font.render(f"Стоимость: {house2_curprice/1000000000:.2f}B", True, border_color)
                        house2_label3 = font.render(f"Стоимость: {house2_curprice/1000000000:.2f}B", True, (241, 221, 56))
                    if house2_curprice >= 1000000000000:
                        house2_label_border3 = font.render(f"Стоимость: {house2_curprice/1000000000000:.2f}T", True, border_color)
                        house2_label3 = font.render(f"Стоимость: {house2_curprice/1000000000000:.2f}T", True, (241, 221, 56))
                    text = font.render(f"= {money:.2f}", True, (241, 221, 56))
                    update_all()
            elif button_rect3.collidepoint(event.pos):
                print("Кнопка 3 нажата!")
                if money >= house3_curprice:
                    money -= house3_curprice
                    house3_count += 1
                    house3_earnings += 196 * housex3
                    house3_curprice *= 2
                    screen.blit(farm_bg, (0, 0))
                    house3_label_border1 = font.render(f"Кол-во: {house3_count}", True, border_color)
                    house3_label_border2 = font.render(f"Сум. добыча: {house3_earnings:.1f}", True, border_color)
                    house3_label_border3 = font.render(f"Стоимость: {house3_curprice:.0f}", True, border_color)
                    house3_label1 = font.render(f"Кол-во: {house3_count}", True, (241, 221, 56))
                    house3_label2 = font.render(f"Сум. добыча: {house3_earnings:.1f}", True, (241, 221, 56))
                    house3_label3 = font.render(f"Стоимость: {house3_curprice:.0f}", True, (241, 221, 56))
                    screen.blit(sword_label_border1, (sword.x - 307, sword.y + 17))
                    screen.blit(sword_label1, (sword.x - 309, sword.y + 15))
                    screen.blit(sword_label_border2, (sword.x - 307, sword.y + 47))
                    screen.blit(sword_label2, (sword.x - 309, sword.y + 45))
                    screen.blit(sword_label_border3, (sword.x - 307, sword.y + 77))
                    screen.blit(sword_label3, (sword.x - 309, sword.y + 75))
                    if house3_earnings >= 1000000:
                        house3_label_border2 = font.render(f"Сум. добыча: {house3_earnings/1000000:.1f}M", True, border_color)
                        house3_label2 = font.render(f"Сум. добыча: {house3_earnings/1000000:.1f}M", True, (241, 221, 56))
                    if house3_earnings >= 1000000000:
                        house3_label_border2 = font.render(f"Сум. добыча: {house3_earnings/1000000000:.1f}B", True, border_color)
                        house3_label2 = font.render(f"Сум. добыча: {house3_earnings/1000000000:.1f}B", True, (241, 221, 56))
                    if house3_earnings >= 1000000000000:
                        house3_label_border2 = font.render(f"Сум. добыча: {house3_earnings/1000000000000:.1f}T", True, border_color)
                        house3_label2 = font.render(f"Сум. добыча: {house3_earnings/1000000000000:.1f}T", True, (241, 221, 56))
                    if house3_curprice >= 1000000:
                        house3_label_border3 = font.render(f"Стоимость: {house3_curprice/1000000:.2f}M", True, border_color)
                        house3_label3 = font.render(f"Стоимость: {house3_curprice/1000000:.2f}M", True, (241, 221, 56))
                    if house3_curprice >= 1000000000:
                        house3_label_border3 = font.render(f"Стоимость: {house3_curprice/1000000000:.2f}B", True, border_color)
                        house3_label3 = font.render(f"Стоимость: {house3_curprice/1000000000:.2f}B", True, (241, 221, 56))
                    if house3_curprice >= 1000000000000:
                        house3_label_border3 = font.render(f"Стоимость: {house3_curprice/1000000000000:.2f}T", True, border_color)
                        house3_label3 = font.render(f"Стоимость: {house3_curprice/1000000000000:.2f}T", True, (241, 221, 56))
                    text = font.render(f"= {money:.2f}", True, (241, 221, 56))
                    update_all()
            elif button_rect4.collidepoint(event.pos):
                print("Кнопка 4 нажата!")
                if money >= house4_curprice:
                    money -= house4_curprice
                    house4_count += 1
                    house4_earnings += 3200 * housex4
                    house4_curprice *= 2
                    screen.blit(farm_bg, (0, 0))
                    house4_label_border1 = font.render(f"Кол-во: {house4_count}", True, border_color)
                    house4_label_border2 = font.render(f"Сум. добыча: {house4_earnings}", True, border_color)
                    house4_label_border3 = font.render(f"Стоимость: {house4_curprice}", True, border_color)
                    house4_label1 = font.render(f"Кол-во: {house4_count}", True, (241, 221, 56))
                    house4_label2 = font.render(f"Сум. добыча: {house4_earnings}", True, (241, 221, 56))
                    house4_label3 = font.render(f"Стоимость: {house4_curprice}", True, (241, 221, 56))
                    screen.blit(sword_label_border1, (sword.x - 307, sword.y + 17))
                    screen.blit(sword_label1, (sword.x - 309, sword.y + 15))
                    screen.blit(sword_label_border2, (sword.x - 307, sword.y + 47))
                    screen.blit(sword_label2, (sword.x - 309, sword.y + 45))
                    screen.blit(sword_label_border3, (sword.x - 307, sword.y + 77))
                    screen.blit(sword_label3, (sword.x - 309, sword.y + 75))
                    if house4_earnings >= 1000000:
                        house4_label_border2 = font.render(f"Сум. добыча: {house4_earnings/1000000:.1f}M", True, border_color)
                        house4_label2 = font.render(f"Сум. добыча: {house4_earnings/1000000:.1f}M", True, (241, 221, 56))
                    if house4_earnings >= 1000000000:
                        house4_label_border2 = font.render(f"Сум. добыча: {house4_earnings/1000000000:.1f}B", True, border_color)
                        house4_label2 = font.render(f"Сум. добыча: {house4_earnings/1000000000:.1f}B", True, (241, 221, 56))
                    if house4_earnings >= 1000000000000:
                        house4_label_border2 = font.render(f"Сум. добыча: {house4_earnings/1000000000000:.1f}T", True, border_color)
                        house4_label2 = font.render(f"Сум. добыча: {house4_earnings/1000000000000:.1f}T", True, (241, 221, 56))
                    if house4_curprice >= 1000000:
                        house4_label_border3 = font.render(f"Стоимость: {house4_curprice/1000000:.2f}M", True, border_color)
                        house4_label3 = font.render(f"Стоимость: {house4_curprice/1000000:.2f}M", True, (241, 221, 56))
                    if house4_curprice >= 1000000000:
                        house4_label_border3 = font.render(f"Стоимость: {house4_curprice/1000000000:.2f}B", True, border_color)
                        house4_label3 = font.render(f"Стоимость: {house4_curprice/1000000000:.2f}B", True, (241, 221, 56))
                    if house4_curprice >= 1000000000000:
                        house4_label_border3 = font.render(f"Стоимость: {house4_curprice/1000000000000:.2f}T", True, border_color)
                        house4_label3 = font.render(f"Стоимость: {house4_curprice/1000000000000:.2f}T", True, (241, 221, 56))
                    text = font.render(f"= {money:.2f}", True, (241, 221, 56))
                    update_all()
            elif button_rect5.collidepoint(event.pos):
                print("Кнопка 5 нажата!")
                if money >= house5_curprice:
                    money -= house5_curprice
                    house5_count += 1
                    house5_earnings += 90000 * housex5
                    house5_curprice *= 2
                    screen.blit(farm_bg, (0, 0))
                    house5_label_border1 = font.render(f"Кол-во: {house5_count}", True, border_color)
                    house5_label_border2 = font.render(f"Сум. добыча: {house5_earnings}", True, border_color)
                    house5_label_border3 = font.render(f"Стоимость: {house5_curprice}", True, border_color)
                    house5_label1 = font.render(f"Кол-во: {house5_count}", True, (241, 221, 56))
                    house5_label2 = font.render(f"Сум. добыча: {house5_earnings}", True, (241, 221, 56))
                    house5_label3 = font.render(f"Стоимость: {house5_curprice}", True, (241, 221, 56))
                    screen.blit(sword_label_border1, (sword.x - 307, sword.y + 17))
                    screen.blit(sword_label1, (sword.x - 309, sword.y + 15))
                    screen.blit(sword_label_border2, (sword.x - 307, sword.y + 47))
                    screen.blit(sword_label2, (sword.x - 309, sword.y + 45))
                    screen.blit(sword_label_border3, (sword.x - 307, sword.y + 77))
                    screen.blit(sword_label3, (sword.x - 309, sword.y + 75))
                    if house5_earnings >= 1000000:
                        house5_label_border2 = font.render(f"Сум. добыча: {house5_earnings/1000000:.1f}M", True, border_color)
                        house5_label2 = font.render(f"Сум. добыча: {house5_earnings/1000000:.1f}M", True, (241, 221, 56))
                    if house5_earnings >= 1000000000:
                        house5_label_border2 = font.render(f"Сум. добыча: {house5_earnings/1000000000:.1f}B", True, border_color)
                        house5_label2 = font.render(f"Сум. добыча: {house5_earnings/1000000000:.1f}B", True, (241, 221, 56))
                    if house5_earnings >= 1000000000000:
                        house5_label_border2 = font.render(f"Сум. добыча: {house5_earnings/1000000000000:.1f}T", True, border_color)
                        house5_label2 = font.render(f"Сум. добыча: {house5_earnings/1000000000000:.1f}T", True, (241, 221, 56))
                    if house5_curprice >= 1000000:
                        house5_label_border3 = font.render(f"Стоимость: {house5_curprice/1000000:.2f}M", True, border_color)
                        house5_label3 = font.render(f"Стоимость: {house5_curprice/1000000:.2f}M", True, (241, 221, 56))
                    if house5_curprice >= 1000000000:
                        house5_label_border3 = font.render(f"Стоимость: {house5_curprice/1000000000:.2f}B", True, border_color)
                        house5_label3 = font.render(f"Стоимость: {house5_curprice/1000000000:.2f}B", True, (241, 221, 56))
                    if house5_curprice >= 1000000000000:
                        house5_label_border3 = font.render(f"Стоимость: {house5_curprice/1000000000000:.2f}T", True, border_color)
                        house5_label3 = font.render(f"Стоимость: {house5_curprice/1000000000000:.2f}T", True, (241, 221, 56))
                    text = font.render(f"= {money:.2f}", True, (241, 221, 56))
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
                    sword_click += 280
                    sword_count = 2
                    sword_curprice = 1000000
                elif money >= sword_curprice and sword_count == 2:
                    money -= sword_curprice
                    sword_click += 3700
                    sword_count = 3
                    sword_curprice = 10000000
                elif money >= sword_curprice and sword_count == 3:
                    money -= sword_curprice
                    sword_click += 46000
                    sword_count = 4
                    sword_curprice = 100000000
                elif money >= sword_curprice and sword_count == 4:
                    money -= sword_curprice
                    sword_click += 570000
                    sword_count = 5
                    sword_curprice = 1000000000
                elif money >= sword_curprice and sword_count == 5:
                    money -= sword_curprice
                    sword_click += 6900000
                    sword_count = 6
                    sword_curprice = 10000000000
                elif money >= sword_curprice and sword_count == 6:
                    money -= sword_curprice
                    sword_click += 77500000
                    sword_count = 7
                    sword_curprice = 100000000000
                elif money >= sword_curprice and sword_count == 7:
                    money -= sword_curprice
                    sword_click += 914570000
                    sword_count = 8
                    sword_curprice *= (999999 * 999999)
            ############################
            ### КНОПКИ ПРОКАЧКИ ФЕРМ ###
            elif upgrade1_1.collidepoint(event.pos):
                if money >= 1000 and housex1 == 1:
                    money -= 1000
                    upgrade1()
                    upgrade1_1 = pygame.Rect(8, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
            elif upgrade1_2.collidepoint(event.pos):
                if money >= 30000 and housex1 == 50:
                    money -= 30000
                    upgrade1()
                    upgrade1_2 = pygame.Rect(8, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
            #############################################################
            elif upgrade2_1.collidepoint(event.pos):
                if money >= 27000 and housex2 == 1:
                    money -= 27000
                    upgrade2()
                    upgrade2_1 = pygame.Rect(8, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
            elif upgrade2_2.collidepoint(event.pos):
                if money >= 860000 and housex2 == 50:
                    money -= 860000
                    upgrade2()
                    upgrade2_2 = pygame.Rect(8, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
            #############################################################
            elif upgrade3_1.collidepoint(event.pos):
                if money >= 384000 and housex3 == 1:
                    money -= 384000
                    upgrade3()
                    upgrade3_1 = pygame.Rect(8, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
            elif upgrade3_2.collidepoint(event.pos):
                if money >= 12288000 and housex3 == 50:
                    money -= 12288000
                    upgrade3()
                    upgrade3_2 = pygame.Rect(8, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
            #############################################################
            elif upgrade4_1.collidepoint(event.pos):
                if money >= 7680000 and housex4 == 1:
                    money -= 7680000
                    upgrade4()
                    upgrade4_1 = pygame.Rect(8, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
            elif upgrade4_2.collidepoint(event.pos):
                if money >= 245760000 and housex4 == 50:
                    money -= 245760000
                    upgrade4()
                    upgrade4_2 = pygame.Rect(8, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
            #############################################################
            elif upgrade5_1.collidepoint(event.pos):
                if money >= 200000000 and housex5 == 1:
                    money -= 200000000
                    upgrade5()
                    upgrade5_1 = pygame.Rect(8, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
            elif upgrade5_2.collidepoint(event.pos):
                if money >= 6144000000 and housex5 == 50:
                    money -= 6144000000
                    upgrade5()
                    upgrade5_2 = pygame.Rect(8, 1000, BUTTON_WIDTH, BUTTON_HEIGHT)
            #############################################################

    pygame.display.update()
    pygame.time.Clock().tick(FPS)
pygame.quit()
