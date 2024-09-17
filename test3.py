import customtkinter as ctk
import tkinter as tk
from tkinter import StringVar

# Initialize the main application window
app = ctk.CTk()
app.title("Login")
app.geometry("1920x1080")
app.config(bg="#257534")
app.attributes("-fullscreen", True)

# Define text fonts
font1 = ("Helvetica", 25, "bold")

# Create and place the header label
JPLTREECARElabel = ctk.CTkLabel(app, font=font1, text="JPL TREE CARE")
JPLTREECARElabel.place(x=865, y=125)

# Define items for the nested menus
items_list = [
    {"Category 1": ["Option 1.1", "Option 1.2", "Option 1.3"], "Category 2": ["Option 2.1", "Option 2.2"], "Category 3": ["Option 3.1", "Option 3.2", "Option 3.3", "Option 3.4"]},
    {"Category A": ["Option A.1", "Option A.2"], "Category B": ["Option B.1", "Option B.2", "Option B.3"]},
    {"Category X": ["Option X.1", "Option X.2", "Option X.3"], "Category Y": ["Option Y.1", "Option Y.2"], "Category Z": ["Option Z.1", "Option Z.2", "Option Z.3", "Option Z.4"]},
    {"Group 1": ["Item 1.1", "Item 1.2"], "Group 2": ["Item 2.1", "Item 2.2", "Item 2.3"], "Group 3": ["Item 3.1", "Item 3.2"]},
    {"Section 1": ["Element 1.1", "Element 1.2", "Element 1.3"], "Section 2": ["Element 2.1", "Element 2.2"], "Section 3": ["Element 3.1", "Element 3.2", "Element 3.3"]}
]

# Function to handle selection
def on_select(value, selected_value):
    selected_value.set(value)

# Create a function to generate nested dropdown menus
def create_nested_dropdown(parent, items, default_text):
    # Create a variable to store the selected value
    selected_value = tk.StringVar(value=default_text)

    # Create the top-level menu
    top_menu = tk.Menu(parent, tearoff=False)

    # Populate the menu with items
    for category, options in items.items():
        category_menu = tk.Menu(top_menu, tearoff=False)
        for option in options:
            category_menu.add_command(label=option, command=lambda opt=option: on_select(opt, selected_value))
        top_menu.add_cascade(label=category, menu=category_menu)

    # Create a button to display the menu
    menu_button = ctk.CTkButton(parent, textvariable=selected_value, 
                                command=lambda: top_menu.post(menu_button.winfo_rootx(), menu_button.winfo_rooty() + menu_button.winfo_height()))
    menu_button.pack(fill=tk.X, pady=10, side=tk.LEFT, expand=True)

# Default texts for each dropdown
default_texts = [
    "Book a new job?",
    "Existing appointments",
    "Application process",
    "FAQs",
    "Reviews"
]

# Create nested dropdown menus with different options and default texts
for items, default_text in zip(items_list, default_texts):
    create_nested_dropdown(app, items, default_text)

# Function to close the window
def close_window():
    app.destroy()

# Create and place the close button
close_button = ctk.CTkButton(app, text="X", command=close_window, fg_color="#7F7F7F", hover_color="#880808")
close_button.place(x=1780, y=0)

# Start the application
app.mainloop()
