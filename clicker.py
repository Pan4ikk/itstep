import tkinter as tk
import time

level = 1
coins = 0
max_hp = 50
current_hp = 50
attack = 1
auto_attack = 0
upgrade_lvl = 1
upgrade_cost = 3
damage = 1

root = tk.Tk()
root.title("Cat Wars")
root.geometry("600x800")
# root.iconbitmap(like.ico)
root.resizable(False, False)

lvl_1 = tk.PhotoImage(file="1.png")
lvl_2 = tk.PhotoImage(file="2.png")
lvl_3 = tk.PhotoImage(file="3.png")
lvl_4 = tk.PhotoImage(file="1.png")
lvl_5 = tk.PhotoImage(file="1.png")


def update():
    lvl_label.config(text=f"Lvl:{level}")
    hp_label.config(text=f"HP:{current_hp}")
    coins_label.config(text=f"Coins:{coins}")
    upgrade_button.config(text=f"Upgrade Cost: " + str(upgrade_cost), command=upgrade_click)


def death():
    global level
    global current_hp
    global coins
    global max_hp
    coins += 4 * level
    level += 1
    if level == 2:
        click_button.config(image=lvl_2)
    elif level == 3:
        click_button.config(image=lvl_3)
    max_hp *= 2
    current_hp = max_hp * level


def click():
    global current_hp
    global level
    global damage
    current_hp -= damage
    print(current_hp)
    if current_hp <= 0:
        death()
    update()


def autoclick():
    global auto_attack
    if auto_attack:
        auto_attack = 0
        print("АвтоКликер Отключен")
    else:
        auto_attack = 1
        print("АвтоКликер Включен")


def upgrade_click():
    global coins
    global upgrade_lvl
    global upgrade_cost
    global damage
    if coins >= upgrade_cost:
        coins -= upgrade_cost
        upgrade_lvl += 1
        upgrade_cost += 3 * upgrade_lvl
        damage *= upgrade_lvl
    print("Damage: " + str(damage))
    update()


title = tk.Label(font=("Arial", 25, "bold"), text="Cat Wars", fg="orange")
title.pack()
lvl_label = tk.Label(font=("Arial", 14), text=f"Lvl {level}")
lvl_label.pack()
coins_label = tk.Label(font=("Arial", 14), text=f"Coins: {coins}", fg="gold", bg="gray")
coins_label.pack()
click_button = tk.Button(root, image=lvl_1, command=click)
click_button.pack()
auto_click_button = tk.Button(text="Autoclicker", command=autoclick)
auto_click_button.pack()
upgrade_button = tk.Button(text="Upgrade Cost: " + str(upgrade_cost), command=upgrade_click)
upgrade_button.pack()
hp_label = tk.Label(font=("Arial", 14), text=f"HP: {current_hp}", fg="red")
hp_label.pack()

root.mainloop()
