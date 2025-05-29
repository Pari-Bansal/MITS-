import tkinter as tk
from tkinter import ttk
import string
import random

def generate_password():
    length = int(length_var.get())
    use_upper = uppercase_var.get()
    use_lower = lowercase_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()
    custom_symbols = symbol_entry_var.get()

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        if custom_symbols.strip() == "":
            password_var.set("Please enter symbols to use.")
            return
        characters += custom_symbols

    if not characters:
        password_var.set("Please select at least one option.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400") #widthXheight
root.resizable(False, False) #horizontal,vertical

# Variables
length_var = tk.IntVar(value=12)
uppercase_var = tk.BooleanVar(value=False)
lowercase_var = tk.BooleanVar(value=False)
digits_var = tk.BooleanVar(value=False)
symbols_var = tk.BooleanVar(value=False)
symbol_entry_var = tk.StringVar(value="")
password_var = tk.StringVar()

# Layout
ttk.Label(root, text="Password Generator", font=("Arial", 18)).pack(pady=10)

length_frame = ttk.Frame(root)
length_frame.pack(pady=5)
ttk.Label(length_frame, text="Length:").pack(side="left")
ttk.Spinbox(length_frame, from_=4, to=32, textvariable=length_var, width=5).pack(side="left")

options_frame = ttk.Frame(root)
options_frame.pack(pady=10)

ttk.Checkbutton(options_frame, text="Include Uppercase", variable=uppercase_var).pack(anchor="w")
ttk.Checkbutton(options_frame, text="Include Lowercase", variable=lowercase_var).pack(anchor="w")
ttk.Checkbutton(options_frame, text="Include Digits", variable=digits_var).pack(anchor="w")
ttk.Checkbutton(options_frame, text="Include Symbols", variable=symbols_var).pack(anchor="w")

symbol_entry_frame = ttk.Frame(root)
symbol_entry_frame.pack(pady=5)
ttk.Label(symbol_entry_frame, text="Enter symbols to use:").pack(anchor="w")
ttk.Entry(symbol_entry_frame, textvariable=symbol_entry_var, width=30).pack()

ttk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

ttk.Entry(root, textvariable=password_var, font=("Courier", 12), justify="center", width=30).pack(pady=5)

# Start GUI
root.mainloop()
