from tkinter import *
from tkinter import ttk

# Starting position of the GUI
root = Tk()
# Create the label object
label = ttk.Label(root,text='Hello world')
# put it on the screen
label.pack()
# Changes the text of the lebel
label.config(text='Howdy, Tkinter!')
label.config(text='Hello Tkinter it\'s been a while e last met. Great to see you again!')
# Changes the text length
label.config(wraplength=150)
# Justification of the text: LEFT, RIGHT, CENTER
label.config(justify=CENTER)
# Set the color of the label
label.config(foreground='blue', background='yellow' )
# Set font of the text in the label font(name, size, [bold, italic, etc])
label.config(font=('Courier', 18, 'bold'))
label.config(text='Hello world')
# Create image object
logo = PhotoImage(file = 'python_logo.gif')
# set the image to label
label.config(image=logo)
# set to show only text
label.config(compound='text')
# set to show image and text in the center
label.config(compound='center')
# set to show image on the left and text on the right
label.config(compound='left')
# set to show image on the right and text on the left
label.config(compound='right')

label.img = logo
label.config(image=label.img)
root.mainloop()