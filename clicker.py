import tkinter as tk
import time

level = 1
coins = 0
max_hp = 50
current_hp = 50
auto_attack = 0
upgrade_lvl = 1
upgrade_cost = 3
damage = 1

root = tk.Tk()
root.title("Cat Wars")
root.geometry("600x800")
# root.iconbitmap(like.ico)
root.resizable(False, False)

M_Images = [tk.PhotoImage(file="1.png"), tk.PhotoImage(file="2.png"), tk.PhotoImage(file="3.png"), tk.PhotoImage(file="4.png"), tk.PhotoImage(file="5.png")]


def update():
    lvl_label.config(text=f"Lvl:{level}")
    hp_label.config(text=f"HP:{current_hp}")
    coins_label.config(text=f"Coins:{coins}")
    upgrade_button.config(text=f"Upgrade Cost: " + str(upgrade_cost), command=upgrade_click)
    current_attack_label.config(font=("Arial", 14), text=f"Current attack: {damage}", fg="red")


def death():
    global level
    global current_hp
    global coins
    global max_hp
    coins += 4 * level
    level += 1
    click_button.config(image=M_Images[level-1])
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


def autoclick():
    global auto_attack
    global auto_click_button
    if auto_attack:
        auto_attack = 0
        print("АвтоКликер Отключен")
        auto_click_button.config(text="Autoclicker off")
    else:
        auto_attack = 1
        print("АвтоКликер Включен")
        auto_click_button.config(text="Autoclicker on")

title = tk.Label(font=("Arial", 25, "bold"), text="Cat Wars", fg="orange")
title.pack()
lvl_label = tk.Label(font=("Arial", 14), text=f"Lvl {level}")
lvl_label.pack()
coins_label = tk.Label(font=("Arial", 14), text=f"Coins: {coins}", fg="gold", bg="gray")
coins_label.pack()
click_button = tk.Button(root, image=M_Images[level-1], command=click)
click_button.pack()
hp_label = tk.Label(font=("Arial", 14), text=f"HP: {current_hp}", fg="red")
hp_label.pack()
current_attack_label = tk.Label(font=("Arial", 14), text=f"Current attack: {damage}", fg="red")
current_attack_label.pack()
auto_click_button = tk.Button(root, font=("Arial", 15), text=f"Autoclicker off", command=autoclick)
auto_click_button.pack()
upgrade_button = tk.Button(font=("Arial", 15), text="Upgrade Cost: " + str(upgrade_cost), command=upgrade_click)
upgrade_button.pack()

root.mainloop()
