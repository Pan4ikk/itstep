import tkinter as tk
import time
import itertools
from itertools import repeat

level = 1
coins = 0
hp = 50
attack = 1
auto_attack = False

root = tk.Tk()
root.title("Cat Wars")
root.geometry("600x800")
#root.iconbitmap(like.ico)
root.resizable(False, False)

lvl_1 = tk.PhotoImage(file="1.png")
lvl_2 = tk.PhotoImage(file="2.png")
lvl_3 = tk.PhotoImage(file="3.png")
lvl_4 = tk.PhotoImage(file="1.png")
lvl_5 = tk.PhotoImage(file="1.png")

def update():
    lvl_label.config(text=f"Lvl:{level}")
    hp_label.config(text=f"HP:{hp}")
    coins_label.config(text=f"Coins:{coins}")

def death():
    global level
    global hp
    global coins
    coins += 3*level
    level += 1
    if level == 2:
        click_button.config(image=lvl_2)
    elif level ==3:
        click_button.config(image=lvl_3)
    hp = 50*level


def click():
    global auto_attack
    global hp
    global level
    hp -= 1
    print(hp)
    if hp<=0:
        death()
    update()

def autoclick():
    global auto_attack
    if auto_attack:
        auto_attack = False
        print("АвтоКликер Отключен")
    else:
        auto_attack = True
        print("АвтоКликер Включен")
    if auto_attack == True:
        click()
        time.sleep(1)



title = tk.Label(font = ("Arial", 25, "bold"), text="Cat Wars", fg = "orange")
title.pack()
lvl_label = tk.Label(font = ("Arial", 14), text=f"Lvl {level}")
lvl_label.pack()
coins_label = tk.Label(font = ("Arial", 14), text=f"Coins: {coins}", fg="gold", bg="gray")
coins_label.pack()
click_button = tk.Button(root, image=lvl_1, command=click)
click_button.pack()

auto_click_button = tk.Button(root, height= 5, width=10, command=autoclick)
auto_click_button.pack()
hp_label = tk.Label(font = ("Arial", 14), text=f"HP: {hp}", fg="red")
hp_label.pack()

root.mainloop()

