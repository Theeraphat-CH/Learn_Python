import tkinter as tk
import random

# Create a new window
window = tk.Tk()

window.title("Dice Rolling Simulator")

# Set the window size
window.geometry("300x200")

# Create a label
label = tk.Label(text="Dice Rolling Simulator")
label.pack()

#Create a function
def rolling():
    result = random.randint(1, 6)
    label_result.config(text=f"Rolling Number : {result}")
# Create a button
button = tk.Button(text="Rolling!", command=rolling)
button.pack()

label_result = tk.Label(text="Rolling Number")
label_result.pack()

# Start the main event loop
window.mainloop()
