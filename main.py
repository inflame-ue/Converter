# TODO: Python converter program with tkinter:
from tkinter import *

# Constants:
FONT = ("Comic Sans", 10)


# TODO: 2. Create a logic of the program(convert given miles to kilometrs with formula)
def convert():
    user_input = entry.get()
    result = int(user_input) * 1.60934
    label_three.config(text=str(result))


# TODO: 1. Create a window and setup the design with all widgets:
window = Tk()
window.minsize(width=300, height=130)
window.title("Converter")
window.config(padx=20, pady=20)
window.columnconfigure(index=0, weight=1)
window.columnconfigure(index=1, weight=1)
window.columnconfigure(index=2, weight=1)


# 1. Entry widget:
entry = Entry()
entry.config(width=10)
entry.grid(column=1, row=0)


# 2. First label widget:
label_one = Label(text="Miles", font=FONT)
label_one.config(padx=10, pady=10)
label_one.grid(column=2, row=0)

# 3. Second label:
label_two = Label(text="is equal to", font=FONT)
label_two.config(padx=10, pady=10)
label_two.grid(column=0, row=1)

# 4. Third label:
label_three = Label(text="0", font=FONT)
label_three.config(padx=10, pady=10)
label_three.grid(column=1, row=1)

# 5. Forth label:
label_four = Label(text="Km", font=FONT)
label_four.config(padx=10, pady=10)
label_four.grid(column=2, row=1)

# 6. Button:
button = Button(text="Calculate", font=FONT, command=convert)
button.grid(column=1, row=2)

# The end:
window.mainloop()