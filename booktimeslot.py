import customtkinter 
from tkinter import *
from tkinter import messagebox




# Create the main window
app = customtkinter.CTk()
app.title("Booking Interface")
app.geometry("400x500")  # Window size

app.config(bg="#257534")  # Green theme for buttons and elements

# Functionality for Yes/No Buttons
def on_yes_click():
    messagebox.showinfo("Confirmation", "You have booked the time slot!")

def on_no_click():
   messagebox.showinfo("Returning to Previous page", "Booking canceled.")

# Create the top frame (Header with Navigation)
header_frame = customtkinter.CTkFrame(app, height=60, corner_radius=0, fg_color="#7f7f7f")
header_frame.pack(fill="x")

# Navigation Buttons (Separated into two buttons)
nav_frame = customtkinter.CTkFrame(header_frame, fg_color="#7f7f7f")  # Sub-frame for navigation buttons
nav_frame.pack(side="left", padx=10, pady=10)

# Back Button
back_button = customtkinter.CTkButton(nav_frame, text="←", width=40)
back_button.pack(side="left", padx=5)

# Forward Button
forward_button = customtkinter.CTkButton(nav_frame, text="→", width=40)
forward_button.pack(side="left", padx=5)

# Date Label
date_label = customtkinter.CTkLabel(header_frame, text="14th August 2024", font=("Arial", 16, "bold"))
date_label.pack(side="left", expand=True)

# Home Button
home_button = customtkinter.CTkButton(header_frame, text="⌂", width=50)
home_button.pack(side="right", padx=10, pady=10)

# Time Slot Section
time_slot_frame = customtkinter.CTkFrame(app, height=100, fg_color="#257534")
time_slot_frame.pack(fill="x", pady=(20, 0))

time_slot_button = customtkinter.CTkButton(time_slot_frame, text="8:30 — 12:00", width=200)
time_slot_button.pack(pady=20)

# Confirmation Section
confirmation_frame = customtkinter.CTkFrame(app, height=100, fg_color="#7f7f7f")
confirmation_frame.pack(fill="x", pady=(20, 0), padx=5)

confirmation_label = customtkinter.CTkLabel(confirmation_frame, text="Are you sure you want to book this time slot?")
confirmation_label.pack(pady=(10, 5))

# Yes/No Buttons
buttons_frame = customtkinter.CTkFrame(confirmation_frame, fg_color="#7f7f7f")
buttons_frame.pack(pady=10)

yes_button = customtkinter.CTkButton(buttons_frame, text="Yes", command=on_yes_click, width=100, fg_color="#257534")
yes_button.grid(row=0, column=0, padx=10)

no_button = customtkinter.CTkButton(buttons_frame, text="No", command=on_no_click, width=100)
no_button.grid(row=0, column=1, padx=10)

# Start the main loop
app.mainloop()
