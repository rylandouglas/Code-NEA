import customtkinter 
from tkinter import *
from tkinter import messagebox

# Initialize the customtkinter environment
customtkinter.set_appearance_mode("light")  # Light mode (you can switch to "dark")
customtkinter.set_default_color_theme("#257534")  # Green theme for buttons and elements

# Create the main application window
app = customtkinter.CTk()
app.title("Booking Form")
app.geometry("600x600")  # Adjusted window size for more content

# Functionality for Submit Button
def on_submit_click():
    # Collect data from form fields
    street_name = street_name_entry.get()
    city = city_entry.get()
    postcode = postcode_entry.get()
    forename = forename_entry.get()
    surname = surname_entry.get()
    phone_number = phone_number_entry.get()
    
    # Here you would normally save the data to a database or a file
    print(f"Street: {street_name}, City: {city}, Postcode: {postcode}")
    print(f"Forename: {forename}, Surname: {surname}, Phone: {phone_number}")

    # Simple feedback
    messagebox.showinfo("Data Submitted", "Your information has been saved.")

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

# Username Label
username_label = customtkinter.CTkLabel(header_frame, text="(Username)", font=("Arial", 14, "bold"))
username_label.pack(side="left", padx=20)

# Date and Time Label
datetime_label = customtkinter.CTkLabel(header_frame, text="14th August 2024\n8:30 — 12", font=("Arial", 16, "bold"))
datetime_label.pack(side="left", expand=True)

# Home Button
home_button = customtkinter.CTkButton(header_frame, text="⌂", width=50)
home_button.pack(side="right", padx=10, pady=10)

# Form Section
form_frame = customtkinter.CTkFrame(app, fg_color="#a8d58b", corner_radius=10)
form_frame.pack(pady=20, padx=10, fill="both", expand=True)

# Street Name Entry
street_name_label = customtkinter.CTkLabel(form_frame, text="Street name")
street_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
street_name_entry = customtkinter.CTkEntry(form_frame, width=200)
street_name_entry.grid(row=0, column=1, padx=10, pady=5)

# Forename Entry
forename_label = customtkinter.CTkLabel(form_frame, text="Forename")
forename_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")
forename_entry = customtkinter.CTkEntry(form_frame, width=200)
forename_entry.grid(row=0, column=3, padx=10, pady=5)

# City Entry
city_label = customtkinter.CTkLabel(form_frame, text="City")
city_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
city_entry = customtkinter.CTkEntry(form_frame, width=200)
city_entry.grid(row=1, column=1, padx=10, pady=5)

# Surname Entry
surname_label = customtkinter.CTkLabel(form_frame, text="Surname")
surname_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")
surname_entry = customtkinter.CTkEntry(form_frame, width=200)
surname_entry.grid(row=1, column=3, padx=10, pady=5)

# Postcode Entry
postcode_label = customtkinter.CTkLabel(form_frame, text="Postcode")
postcode_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
postcode_entry = customtkinter.CTkEntry(form_frame, width=200)
postcode_entry.grid(row=2, column=1, padx=10, pady=5)

# Phone Number Entry
phone_number_label = customtkinter.CTkLabel(form_frame, text="Phone number")
phone_number_label.grid(row=2, column=2, padx=10, pady=5, sticky="w")
phone_number_entry = customtkinter.CTkEntry(form_frame, width=200)
phone_number_entry.grid(row=2, column=3, padx=10, pady=5)

# Submit Button
submit_button = customtkinter.CTkButton(app, text="Submit", command=on_submit_click)
submit_button.pack(pady=10)

# Start the main loop
app.mainloop()
