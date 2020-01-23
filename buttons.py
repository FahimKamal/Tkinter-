"""
Buttons
Date: 23.01.2020
"""
from tkinter import *
from tkinter import ttk

root = Tk()

button = ttk.Button(root, text='Click me!')
button.pack()

def callback():
    """Function will be called when button is clicked"""
    print('Clicked!')


button.config(command=callback)
# Button will be click when called invoke() function
button.invoke()
# Button will be disabled
button.state(['disabled'])
# To check a button is disabled or not
print(button.instate(['disabled']))
# To set the button to enable again
button.state(['!disabled'])
# To check if the button is enabled
print(button.instate(['!disabled']))

# Set image to button
logo = PhotoImage(file='python_logo.gif')
button.logo = logo
button.config(image=logo, compound = 'left')

# Create a small version of the logo
small_logo = logo.subsample(5, 5)
button.config(image=small_logo)
root.mainloop()
