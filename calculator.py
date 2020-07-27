import tkinter as tk

root = tk.Tk()
root.title("Calculator")

input_field = tk.Entry(master=root, width=35, borderwidth=5)
input_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

buttons = []
counter = 0
chain = []

def button_command(number):
    input_field.insert(tk.END, number)

def button_clear():
    input_field.delete(0, tk.END)
    global chain
    chain = []

def button_add():
    global chain
    chain.append(int(input_field.get()) if len(input_field.get()) > 0 else 0)
    input_field.delete(0, tk.END)
    print('Total:', chain)

def button_equals():
    global chain
    chain.append(int(input_field.get()) if len(input_field.get()) > 0 else 0)
    total = 0
    for value in chain:
        total += value
    input_field.delete(0, tk.END)
    input_field.insert(0, total)
    print('Total:', chain)

for row in range(1, 5):
    for col in range(3):
        counter += 1
        digit = (4 - row) * 3 - (2 - col) if counter != 10 else 0
        button = tk.Button(master=root, text=digit, padx=42, pady=20, command=lambda digit=digit:button_command(digit))
        buttons.append(button)
        buttons[-1].grid(row=row, column=col)

        if counter == 10:
            break

add = tk.Button(master=root, text='+', padx=41, pady=20, command=button_add)
clear = tk.Button(master=root, text='Clear', padx=80, pady=20, command=button_clear)
equals = tk.Button(master=root, text='=', padx=91, pady=20, command=button_equals)

clear.grid(row=4, column=1, columnspan=2)
add.grid(row=5, column=0)
equals.grid(row=5, column=1, columnspan=2)

root.resizable(False, False)
root.mainloop()