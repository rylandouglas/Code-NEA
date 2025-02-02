import customtkinter
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import Label
from tkinter import PhotoImage
import sqlite3
import bcrypt


# Set up the app window (start with a windowed mode)
app = customtkinter.CTk()
app.geometry("450x360")  # Initial window size for login/signup
app.config(bg="#257534")

# Fonts
font1 = ("Helvetica", 25, "bold")
font2 = ("Arial", 17, "bold")
font3 = ("Arial", 13, "bold")
font4 = ("Arial", 13, "bold")

# Connect to the database via sqlite3
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Calendar

# Function to clear the main menu screen and show the calendar (Frame4)
def show_calendar_frame():
    # Destroy previous screen elements
    for widget in app.winfo_children():
        widget.destroy()

    # Create the frame 4 and make it full screen
    frame4 = customtkinter.CTkFrame(app, fg_color="#73B12F", bg_color="#73B12F")
    frame4.place(x=0, y=0, relwidth=1, relheight=1)  # Full screen

    # Menu bar with title
    menu_bar = customtkinter.CTkFrame(frame4, height=50, corner_radius=0, fg_color="#73B12F")
    menu_bar.pack(fill="x")

    newjob_label = customtkinter.CTkLabel(menu_bar, text="Book a new job", font=("Arial", 18, "bold"), text_color="white", bg_color="#2F2F2F")
    newjob_label.pack(fill="x", padx=10, pady=10, anchor="center")

    # Create a calendar widget 
    calendar = Calendar(frame4, selectmode='day', date_pattern='yyyy-mm-dd')
    calendar.place(relx=0.5, rely=0.5, anchor="center", relheight=0.8, relwidth=0.8)  # Centre the calendar

    # Label to show the selected date
    selected_date_label = customtkinter.CTkLabel(frame4, text="Selected Date: None", font=font3, text_color="black")
    selected_date_label.place(relx=0.5, rely=0.92, anchor="center")  # Centre the selected date label

    # Function to confirm the booking
    def confirm_booking():
        selected_date = calendar.get_date()
        show_confirmation_frame(selected_date)

    # Confirm button (disabled initially)
    confirm_button = customtkinter.CTkButton(frame4, text="Confirm Booking", font=font2, command=confirm_booking, state="disabled")
    confirm_button.place(relx=0.5, rely=0.95, anchor="center")  # Centre the confirm button

    # Function to handle date selection
    def on_date_selected(event):
        selected_date = calendar.get_date()
        selected_date_label.configure(text=f"Selected Date: {selected_date}")
        confirm_button.configure(state="normal")  # Enable the confirm button only when a date is selected

    # Bind the date selection event to the on_date_selected function
    calendar.bind("<<CalendarSelected>>", on_date_selected)

    # Close button to exit the application
    close_button = customtkinter.CTkButton(frame4, text="X", font=font2, command=app.quit, fg_color="#2F2F2F", hover_color="#880808")
    close_button.place(x=1780, y=10)

# Function to show the confirmation screen (frame5)
def show_confirmation_frame(selected_date):
    # Destroy previous screen elements
    for widget in app.winfo_children():
        widget.destroy()

    # Create the confirmation frame (frame5)
    frame5 = customtkinter.CTkFrame(app, fg_color="#73B12F", bg_color="#73B12F")
    frame5.place(x=0, y=0, relwidth=1, relheight=1)  # Full screen

    # Question label asking for confirmation
    confirmation_label = customtkinter.CTkLabel(frame5, text=f"Are you sure you want to book for {selected_date}?", font=font1, text_color="white")
    confirmation_label.place(relx=0.5, rely=0.4, anchor="center")  # Center the label

    # Function to go back to the calendar screen (frame4)
    def go_back_to_calendar():
        show_calendar_frame()  # Show the calendar frame again

    # Function to go to frame6 (success screen)
    def go_to_success_screen():
        show_success_screen()  # Show the success screen

    # Create "Yes" button
    yes_button = customtkinter.CTkButton(frame5, text="Yes", font=font2, command=go_to_success_screen, fg_color="#006e44", hover_color="#004d33")
    yes_button.place(relx=0.4, rely=0.6, anchor="center")  # Position it slightly to the left

    # Create "No" button (to go back to calendar)
    no_button = customtkinter.CTkButton(frame5, text="No", font=font2, command=go_back_to_calendar, fg_color="#880808", hover_color="#660000")
    no_button.place(relx=0.6, rely=0.6, anchor="center")  # Position it slightly to the right

# Function to show success screen (frame6)
def show_success_screen():
    # Destroy previous screen elements
    for widget in app.winfo_children():
        widget.destroy()

    # Create frame6 (Success screen)
    frame6 = customtkinter.CTkFrame(app, fg_color="#73B12F", bg_color="#73B12F")
    frame6.place(x=0, y=0, relwidth=1, relheight=1)  # Full screen

    # Success message
    success_label = customtkinter.CTkLabel(frame6, text="Booking Confirmed!", font=font1, text_color="white")
    success_label.place(relx=0.5, rely=0.4, anchor="center")  # Center the label

    # Optionally, add more content here, like a message or button to go back to the main menu.
    go_to_menu_button = customtkinter.CTkButton(frame6, text="Back to Main Menu", font=font2, command=show_main_menu, fg_color="#006e44", hover_color="#004d33")
    go_to_menu_button.place(relx=0.5, rely=0.6, anchor="center")

# Call this function when the user selects "Book a new job" in the main menu
def book_new_job():
    show_calendar_frame()

# Main Menu Screen (frame3)
def show_main_menu():
    # Switch to fullscreen mode after successful login
    app.attributes('-fullscreen', True)  # Switch to fullscreen

    # Clear the current screen
    for widget in app.winfo_children():
        widget.destroy()

    # Create main menu UI components
    menu_data = {
        "Book a new job": book_new_job,  # This will open the calendar screen
        "Existing Appointments": ["June 18th - 8:30-12:30", "August 12th - 12:30-5:30"],  # placeholder figures
        "Application Process": [],  # Show application status
        "Business Overview": ["FAQS", "Mission Statement", "Company Information"],
        "Reviews": ["5* From Bert F", "3* From John P", "4* From Samba B"]
    }

    # Create frame for the main menu
    frame3 = customtkinter.CTkFrame(app, fg_color="#73B12F", bg_color="#73B12F")
    frame3.place(x=0, y=0, relwidth=1, relheight=1)

    # Menu bar with title
    menu_bar = customtkinter.CTkFrame(frame3, height=50, corner_radius=0, fg_color="#73B12F")
    menu_bar.pack(fill="x")

    main_menu_label = customtkinter.CTkLabel(menu_bar, text="Main Menu", font=("Arial", 18, "bold"), text_color="white", bg_color="#2F2F2F")
    main_menu_label.pack(fill="x", padx=10, pady=10, anchor="center")

    # Add buttons for each menu item
    menu_buttons_frame = customtkinter.CTkFrame(frame3)
    menu_buttons_frame.pack(pady=30, padx=10, expand=True)

    for idx, menu_name in enumerate(menu_data.keys()):
        button = customtkinter.CTkButton(
            menu_buttons_frame,
            text=menu_name,
            font=("Arial", 16),
            fg_color="#2F2F2F",
            hover_color="#464646",
            text_color="white",
            command=menu_data[menu_name],
        )
        button.grid(row=0, column=idx, padx=10, pady=10, sticky="nsew")

    menu_buttons_frame.grid_columnconfigure(0, weight=1)
    menu_buttons_frame.grid_columnconfigure(1, weight=1)
    menu_buttons_frame.grid_columnconfigure(2, weight=1)
    menu_buttons_frame.grid_columnconfigure(3, weight=1)
    menu_buttons_frame.grid_columnconfigure(4, weight=1)

    # Function to close the window
    def close_window():
        app.destroy()

    # Create and place the close button (main menu)
    close_button = customtkinter.CTkButton(app, text="X", command=close_window, fg_color="#2F2F2F", hover_color="#880808")
    close_button.place(x=1780, y=10)

# Start the app
app.mainloop()
