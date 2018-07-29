# reference : https://www.youtube.com/watch?v=ieW0ccjpNyc

from tkinter import *
from tkinter import messagebox
main = Tk()

main.title("Replace Stuff 1.0")
main.geometry("400x400")

def copy():
    temp = inputBox.get()
    output.insert(END, temp)
    inputBox.delete(0,END)

inputBox = Entry(main, width=20, bg="light grey")
inputBox.grid(row=0, column=0, sticky=W)

# we need to define the grid for input,output, button etc. Below, row=1 because 0 is taken by inputbox
Button(main, width=10, text="Copiar", command = copy).grid(row=1, column=0, sticky =W)

output = Text(main, width=20, height=5, background="light grey")
output.grid(row=3, column=0, sticky=W)

main.mainloop()