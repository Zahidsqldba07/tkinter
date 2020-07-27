# from tkinter import *
import tkinter as tk

# The frame of the application is a the root widget
# Called root because tkinter follows file system format

# Widgets always have two steps:
# 1. Create the widget
# 2. Display the widget

root = tk.Tk()

# label = tk.Label(root, text='Hello, World!')
# label2 = tk.Label(root, text='Hello, Universe')

# label.grid(row=3, column=5)
# label2.grid(row=0, column=0)

entry = tk.Entry(master=root)
entry.grid(row=0, column=0)

def on_call():
    print(entry.get())

button = tk.Button(master=root, text='Submit', command=on_call)
button.grid(row=0,column=1)

# button = tk.Button(master=root, text='Click me!', padx=50, pady=10, command=on_call, fg="blue")
# button.grid(row=0, column=0)

root.mainloop()
