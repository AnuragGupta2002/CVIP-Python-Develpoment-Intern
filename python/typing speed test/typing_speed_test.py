import tkinter as tk
import random
import time

def generate_random_text():
    # List of words for typing test
    word_list = [
        "python", "typing", "speed", "test", "accuracy", "practice",
        "programming", "language", "development", "challenge",
        "opportunity", "learning", "knowledge", "keyboard", "skill",
        "improvement", "fun", "exercise", "code", "algorithm","quick","brown","fox",
        "jumps","over","a","lazy",'dog'
    ]
    return " ".join(random.choices(word_list, k=25))

def start_typing_test():
    global start_time
    global current_text

    current_text = generate_random_text()
    text_to_type.config(state=tk.NORMAL)
    text_to_type.delete(1.0, tk.END)
    text_to_type.insert(tk.END, current_text)
    text_to_type.config(state=tk.DISABLED)
    input_text.config(state=tk.NORMAL)
    input_text.delete(0, tk.END)
    input_text.focus_set()

    start_time = time.time()

def end_typing_test():
    input_text.config(state=tk.DISABLED)
    elapsed_time = time.time() - start_time
    typed_text = input_text.get()
    word_count = len(current_text.split())
    typed_word_count = len(typed_text.split())
    accuracy = calculate_accuracy(current_text, typed_text)

    if word_count > 0 and typed_word_count > 0:
        wpm = int(typed_word_count / (elapsed_time / 60))
    else:
        wpm = 0

    result_label.config(text=f"Your Typing Speed: {wpm} WPM\nAccuracy: {accuracy:.2f}%")

def calculate_accuracy(actual_text, typed_text):
    actual_words = actual_text.split()
    typed_words = typed_text.split()
    correct_word_count = sum(1 for actual, typed in zip(actual_words, typed_words) if actual == typed)
    return (correct_word_count / len(actual_words)) * 100

# Create the main application window
app = tk.Tk()
app.title("Typing Speed Test")

current_text = ""
start_time = 0

# Create and place the widgets
text_to_type = tk.Text(app, wrap=tk.WORD, width=60, height=5, font=("Arial", 14), state=tk.DISABLED)
text_to_type.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

input_text = tk.Entry(app, width=60, font=("Arial", 14), state=tk.DISABLED)
input_text.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

start_button = tk.Button(app, text="Start Typing Test", font=("Arial", 14), command=start_typing_test)
start_button.grid(row=2, column=0, padx=10, pady=5, sticky="e")

end_button = tk.Button(app, text="End Typing Test", font=("Arial", 14), command=end_typing_test)
end_button.grid(row=2, column=1, padx=10, pady=5, sticky="w")

result_label = tk.Label(app, text="", font=("Arial", 16))
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
app.mainloop()
