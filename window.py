from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Connect Four")

player1 = StringVar()
player1.set("")

player2 = StringVar()
player2.set("")

player1_color = StringVar()
player1_color.set("")


def start():
    if player1.get() == player2.get() == "Computer":
        messagebox.showerror("Connect Four", "Computer vs Computer is not Possible!")
    elif not all([player1.get(), player2.get(), player1_color.get()]):
        messagebox.showerror("Connect Four", "All fields are mandatory!")
    else:
        root.destroy()


def can_start():
    if player1.get() == player2.get() == "Computer":
        return False
    elif not all([player1.get(), player2.get(), player1_color.get()]):
        return False
    else:
        return True


def new_window():
    global root, player1, player2, player1_color
    try:
        l = Label(root)
    except:
        root = Tk()
        root.title("Connect Four")

        player1 = StringVar()
        player1.set("")

        player2 = StringVar()
        player2.set("")

        player1_color = StringVar()
        player1_color.set("")

    colors = [
        "Red",
        "Yellow"
    ]
    players = [
        "Human",
        "Computer"
    ]

    label1 = Label(root, text="New Game")
    label1.grid(row=1, column=2)

    drop1 = OptionMenu(root, player1, *players)
    drop1.grid(row=2, column=1)

    label2 = Label(root, text="vs")
    label2.grid(row=2, column=2)

    drop2 = OptionMenu(root, player2, *players)
    drop2.grid(row=2, column=3)

    label3 = Label(root, text="Player1 Color : ")
    label3.grid(row=3, column=1)

    drop3 = OptionMenu(root, player1_color, *colors)
    drop3.grid(row=3, column=2)

    start_button = Button(root, text="Start", command=start)
    start_button.grid(row=4, column=2)

    root.mainloop()
