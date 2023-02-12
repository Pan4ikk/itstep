import tkinter as tk

level = 1
coins = 0
hp = 50

root = tk.Tk()
root.title("Cat Wars")
root.geometry("600x800")
#root.iconbitmap(like.ico)
root.resizable(False, False)

lvl_1 = tk.PhotoImage(file="1.png")
lvl_2 = tk.PhotoImage(file="1.png")
lvl_3 = tk.PhotoImage(file="1.png")
lvl_4 = tk.PhotoImage(file="1.png")
lvl_5 = tk.PhotoImage(file="1.png")

def click():
    print("hit")

title = tk.Label(font = ("Arial", 25, "bold"), text="Cat Wars", fg = "orange")
title.pack()
lvl = tk.Label(font = ("Arial", 14), text=f"Lvl {level}")
lvl.pack()
coins = tk.Label(font = ("Arial", 14), text=f"Coins: {coins}", fg="gold", bg="gray")
coins.pack()

click_button = tk.Button(root, image=lvl_1, command=click)
click_button.pack()
hp = tk.Label(font = ("Arial", 14), text=f"HP: {hp}", fg="red")
hp.pack()

root.mainloop()
