import tkinter as tk

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except Exception as e:
        equation.set(" error ")
        expression = ""

# Function to clear the entry
def clear():
    global expression
    expression = ""
    equation.set("")

# GUI Window setup
window = tk.Tk()
window.configure(background="light gray")
window.title("Simple Calculator")
window.geometry("300x400")

expression = ""
equation = tk.StringVar()

# Input field
input_field = tk.Entry(window, textvariable=equation, font=('Arial', 18), justify='right')
input_field.grid(columnspan=4, ipadx=8, ipady=25)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    action = lambda x=text: press(x) if x != "=" else equalpress()
    tk.Button(window, text=text, fg="black", bg="white",
              font=('Arial', 18), command=action, height=2, width=6).grid(row=row, column=col)

# Clear button
tk.Button(window, text='Clear', fg='white', bg='red',
          font=('Arial', 18), command=clear, height=2, width=26).grid(row=5, column=0, columnspan=4)

window.mainloop()
