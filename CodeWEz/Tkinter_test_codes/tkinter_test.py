import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Modern Tkinter App")
root.geometry("400x300")

# Configure styles
style = ttk.Style()
style.theme_use('clam')  # Use the 'clam' theme (other options: 'alt', 'default', 'classic')
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TLabel', font=('Helvetica', 14))

# Create a frame for layout
frame = ttk.Frame(root, padding=20)
frame.pack(fill='both', expand=True)

# Add widgets with styles
label = ttk.Label(frame, text="Welcome to the Modern Tkinter App")
label.pack(pady=10)

button1 = ttk.Button(frame, text="Button 1")
button1.pack(pady=5)

button2 = ttk.Button(frame, text="Button 2")
button2.pack(pady=5)

# Run the application
root.mainloop()
