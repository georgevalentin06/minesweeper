import random
import tkinter as tk


# TK Window setup
window = tk.Tk()
window.title("Minesweeper")
window.maxsize(380, 460)
window.minsize(380, 460)
title = tk.Label(text="The game has started! Good luck!", font=('normal', 15))
title.grid(row=0, columnspan=10, pady=14)


# Get 10 random bombs
def get_bombs(number_of_bombs):
    bombs = []

    for x in range(number_of_bombs):
        bombs.append(tuple(random.randint(0, 9) for _ in range(2)))

    return bombs

# Get the field
def start_game(bombs, rows, columns):
    field = [[0 for i in range(columns)] for j in range(rows)]

    for bomb in bombs:
        field[bomb[0]][bomb[1]] = "X"

        row_range = range(bomb[0] - 1, bomb[0] + 2)
        columns_range = range(bomb[1] - 1, bomb[1] + 2)

        for i in row_range:
            for j in columns_range:
                if (0 <= i < rows and 0 <= j < columns and field[i][j] != "X"):
                    field[i][j] += 1

    return field

# Create the buttons
dict = {}
bombs = get_bombs(10)
field = start_game(bombs, 10, 10)

for row in range(10):
    for column in range(10):
        square_symbol = field[row][column]
        btn = tk.Button(width=4, height=2 ,text='')
        btn.grid(row=row+1, column=column)
        dict[row, column] = btn
        btn.config(command=lambda btn=dict[row, column], square_symbol=square_symbol, title=title, btn_location=(row, column): [btn.config(text=square_symbol, state='disabled'),
            (title.config(text="The game has ended! You pressed on a bomb!", font=('normal', 12)), disable_btn()) if (square_symbol=='X') else None, dict.pop(btn_location),
            (title.config(text='The game has ended! You won!!!'), disable_btn()) if check_for_win() else None])

# check for win/loss
def check_for_win(dict=dict):
    if len(dict) == 10:
        return True

def disable_btn(dict=dict):
    for key, value in dict.items():
        value.config(state='disabled')

window.mainloop()





