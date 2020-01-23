"""
tkinter exercise
Date: 23.01.2020
"""
from tkinter import *
from tkinter import ttk


class App:
    def __init__(self, master):
        self.label = ttk.Label(master, text='My name is: ')
        self.label.grid(column=0, row=0, columnspan=2)
        ttk.Button(master, text='Fahim',command=self.button1).grid(column=0, row=1)
        ttk.Button(master, text='Kamal', command=self.button2).grid(column=1, row=1)

    def button1(self):
        self.label.config(text='My name is Fahim')

    def button2(self):
        self.label.config(text='My name is Kamal')


def main():
    root = Tk()
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
