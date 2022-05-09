"""https://python.plainenglish.io/build-a-sorting-algorithm-visualizer-in-python-f6f4afb1c98a"""

from tkinter import *
from tkinter import ttk

from colors import *

window = Tk()
window.title("Sorting algorithms visualization")
window.maxsize(1000, 700)
window.config(bg=DARK_GRAY)

algorithm_name = StringVar()
al_list = ['Bubble Sort', 'Merge Sort', 'Bucket Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

data = []


def draw_data(data, collorArray):
    pass


def set_speed():
    pass


def generate():
    pass


def sort():
    pass


UI_frame = Frame(window, width=900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
al_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=al_list)
al_menu.grid(row=0, column=1, padx=5, pady=5, sticky=W)
al_menu.current(0)

l1 = Label(UI_frame, text="Speed: ", bg=WHITE)
l1.grid(row=1, column=0, padx=10, pady=5, sticky=W)
al_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
al_menu.grid(row=1, column=1, padx=5, pady=5, sticky=W)
al_menu.current(1)

b1 = Button(UI_frame, text='Generate', command=generate, bg=LIGHT_GRAY)
b1.grid(row=0, column=3, padx=5, pady=5)

b2 = Button(UI_frame, text='Sort', command=sort, bg=LIGHT_GRAY)
b2.grid(row=1, column=3, padx=5, pady=5)

canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()
