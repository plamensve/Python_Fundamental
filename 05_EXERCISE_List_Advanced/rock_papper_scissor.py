import random
from tkinter import *

iface = Tk()
iface.geometry("500x200")
iface.resizable(False, False)
iface.title("Rock Paper Scissors")


def button_press(x):
    global expression
    global win
    global draw
    global lose

    player_choice = "You choose: " + x

    computer_random_number = random.randint(1, 3)

    if computer_random_number == 1:
        computer_move = "rock"
    elif computer_random_number == 3:
        computer_move = "scissors"
    else:
        computer_move = "paper"
    comp_choice = "Computer choose: " + computer_move

    if x == computer_move:
        result = "Draw!"
        draw += 1
        result_draw.set("Draw: " + str(draw))
    elif (x == "rock" and computer_move == "scissors") or (x == "paper" and computer_move == "rock"):
        result = "You win!"
        win += 1
        result_win.set("Win: " + str(win))
    else:
        result = "You lose!"
        lose += 1
        result_lose.set("Lose: " + str(lose))

    expression = str(player_choice + ", " + comp_choice + " Result: " + result)
    input_text.set(expression)

    return result


expression = ""
input_text = StringVar()
result_win = StringVar()
result_draw = StringVar()
result_lose = StringVar()

win = 0
draw = 0
lose = 0

result_lose.set("Lose: " + str(lose))
result_win.set("Win: " + str(win))
result_draw.set("Draw: " + str(draw))

input_frame = Frame(iface, width=500, height=50, bd=0, highlightbackground="grey", highlightcolor="grey",
                    highlightthickness=2)

input_frame.pack(side=TOP)

input_field = Entry(input_frame, state="readonly", font=('arial', 8, 'bold'), textvariable=input_text, width=80,
                    fg="black", readonlybackground="#fff", bd=0, justify=CENTER)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)

btns_frame = Frame(iface, width=500, height=150, bg="white")

btns_frame.pack()

Button(btns_frame, text="Rock", fg="black", width=21, height=4, bd=0, bg="#ccc", cursor="hand2",
       command=lambda: button_press("rock")).grid(row=0, column=0, padx=5, pady=5)

Button(btns_frame, text="Paper", fg="black", width=21, height=4, bd=0, bg="#ccc", cursor="hand2",
       command=lambda: button_press("paper")).grid(row=0, column=1, padx=5, pady=5)

Button(btns_frame, text="Scissors", fg="black", width=21, height=4, bd=0, bg="#ccc", cursor="hand2",
       command=lambda: button_press("scissors")).grid(row=0, column=2, padx=5, pady=5)
Label(btns_frame, textvariable=result_win, fg="white", bg="green", width=15, height=2, bd=0,
      justify=CENTER, font=('arial', 12, 'bold')).grid(row=1, column=0, padx=5, pady=5)
Label(btns_frame, textvariable=result_draw, fg="black", bg="yellow", width=15, height=2, bd=0,
      justify=CENTER, font=('arial', 12, 'bold')).grid(row=1, column=1, padx=5, pady=5)
Label(btns_frame, textvariable=result_lose, fg="white", bg="red", width=15, height=2, bd=0,
      justify=CENTER, font=('arial', 12, 'bold')).grid(row=1, column=2, padx=5, pady=5)

iface.mainloop()