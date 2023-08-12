import tkinter as tk

def on_click(button_text):
    current = result_var.get()

    if button_text == "=":
        try:
            result = eval(current)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif button_text == "C":
        result_var.set("")
    else:
        result_var.set(current + button_text)

app = tk.Tk()
app.title("Simple Calculator")

# Create the result display
result_var = tk.StringVar()
result_var.set("")
result_label = tk.Label(app, textvariable=result_var, font=("Arial", 20), anchor="e")
result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]


row_index = 1
col_index = 0

for button_text in buttons:
    button = tk.Button(app, text=button_text, font=("Arial", 16), width=5, height=2,
                       command=lambda btn=button_text: on_click(btn))
    button.grid(row=row_index, column=col_index, padx=5, pady=5)

    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

app.mainloop()
