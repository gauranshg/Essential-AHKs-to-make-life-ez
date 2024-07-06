import tkinter as tk
import csv
import os
import pyperclip
from tkinter import ttk

# Function to copy text to clipboard
def on_button_click(text):
    pyperclip.copy(text)
    root.bind("<Button-1>", paste_text)

# Function to paste text from clipboard
def paste_text(event):
    root.unbind("<Button-1>")  # Unbind the event after the first click
    focused_widget = root.focus_get()
    if isinstance(focused_widget, tk.Entry) or isinstance(focused_widget, tk.Text):
        focused_widget.insert(tk.INSERT, pyperclip.paste())

# Function to create a sample CSV if it doesn't exist
def create_sample_csv(csv_file):
    sample_data = [
        ["ID", "Button Name", "Text"],
        ["1", "Greeting", "Hello"],
        ["2", "Planet", "World"],
        ["3", "Welcome Message", "Welcome"],
        ["4", "Preposition", "To"],
        ["5", "Adjective", "Dynamic"],
        ["6", "Object", "Buttons"]
    ]
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)

# Function to load buttons from CSV
def load_buttons_from_csv(csv_file):
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if there is one
        for row in reader:
            button_text = f"ID {row[0]}: {row[1]}"
            button = tk.Button(button_frame, text=button_text, command=lambda text=row[2]: on_button_click(text))
            button.pack(pady=5)

# Function to add a new button to CSV and GUI
def add_new_button():
    new_id = next_id[0]
    button_name = new_button_name_entry.get()
    new_text = new_button_text_entry.get()
    if button_name and new_text:
        with open(csv_file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([new_id, button_name, new_text])
        button_text = f"ID {new_id}: {button_name}"
        button = tk.Button(button_frame, text=button_text, command=lambda text=new_text: on_button_click(new_text))
        button.pack(pady=5)
        next_id[0] += 1
        new_button_name_entry.delete(0, tk.END)
        new_button_text_entry.delete(0, tk.END)

# Check if CSV file exists; if not, create it
csv_file_path = 'data.csv'
if not os.path.exists(csv_file_path):
    create_sample_csv(csv_file_path)

# Determine the next ID for new rows
with open(csv_file_path, newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    next_id = [max(int(row[0]) for row in reader) + 1]  # Get the max ID and increment

# Setup Tkinter Window
root = tk.Tk()
root.title("Dynamic Button Creator")

# Customizing the appearance
root.configure(bg='#f0f0f0')  # Set background color
root.geometry('400x400')  # Set initial window size

style = ttk.Style()
style.theme_use('clam')  # Use the 'clam' theme (other options: 'alt', 'default', 'classic')
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TLabel', font=('Helvetica', 14))

label = tk.Label(root, text="Press a button to copy the text, then click to paste", font=('Helvetica', 12))
label.pack(pady=20)

button_frame = tk.Frame(root, bg='#ffffff', bd=1, relief=tk.SOLID)  # White frame with border
button_frame.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

load_buttons_from_csv(csv_file_path)

new_button_name_label = tk.Label(root, text="Button Name", font=('Helvetica', 10))
new_button_name_label.pack(pady=5)
new_button_name_entry = tk.Entry(root, font=('Helvetica', 10))
new_button_name_entry.pack(pady=5)

new_button_text_label = tk.Label(root, text="Button Text", font=('Helvetica', 10))
new_button_text_label.pack(pady=5)
new_button_text_entry = tk.Entry(root, font=('Helvetica', 10))
new_button_text_entry.pack(pady=5)

add_button = tk.Button(root, text="Add New Button", command=add_new_button, font=('Helvetica', 10), bg='#4CAF50', fg='white')
add_button.pack(pady=5)

root.mainloop()
