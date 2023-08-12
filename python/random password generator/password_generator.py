import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    length = int(password_length.get())

    if length < 8:
        messagebox.showwarning("Invalid Length", "Password length should be at least 8 characters.")
        return

    characters = ""
    if include_uppercase.get():
        characters += string.ascii_uppercase
    if include_lowercase.get():
        characters += string.ascii_lowercase
    if include_digits.get():
        characters += string.digits
    if include_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("No Characters Selected", "Please select at least one character type.")
        return

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    password_result.set(generated_password)

# Create the main application window
app = tk.Tk()
app.title("Random Password Generator")

# Create the widgets
password_length_label = tk.Label(app, text="Password Length:")
password_length_label.grid(row=0, column=0, padx=10, pady=5)

password_length = tk.Entry(app)
password_length.grid(row=0, column=1, padx=10, pady=5)

include_uppercase = tk.BooleanVar()
include_uppercase.set(True)
uppercase_checkbutton = tk.Checkbutton(app, text="Include Uppercase Letters", variable=include_uppercase)
uppercase_checkbutton.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

include_lowercase = tk.BooleanVar()
include_lowercase.set(True)
lowercase_checkbutton = tk.Checkbutton(app, text="Include Lowercase Letters", variable=include_lowercase)
lowercase_checkbutton.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

include_digits = tk.BooleanVar()
include_digits.set(True)
digits_checkbutton = tk.Checkbutton(app, text="Include Digits", variable=include_digits)
digits_checkbutton.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

include_symbols = tk.BooleanVar()
include_symbols.set(True)
symbols_checkbutton = tk.Checkbutton(app, text="Include Symbols", variable=include_symbols)
symbols_checkbutton.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

password_result = tk.StringVar()
password_result_label = tk.Label(app, textvariable=password_result, font=("Courier", 12))
password_result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Start the main event loop
app.mainloop()