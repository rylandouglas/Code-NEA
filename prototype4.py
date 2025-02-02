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

#Calendar

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
    calendar.place(relx=0.5, rely=0.5, anchor="center",relheight=0.8,relwidth=0.8)  # Centre the calendar

    # Label to show the selected date
    selected_date_label = customtkinter.CTkLabel(frame4, text="Selected Date: None", font=font3, text_color="black")
    selected_date_label.place(relx=0.5, rely=0.92, anchor="center")  # Centre the selected date label

    # Function to confirm the booking
    def confirm_booking():
        selected_date = calendar.get_date()
        messagebox.showinfo("Booking Confirmed", f"Your job has been booked for {selected_date}")

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





# Call this function when the user selects "Book a new job" in the main menu
def book_new_job():
    show_calendar_frame()


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
    
    # Function to close the window2
    def close_window():
        app.destroy()
    
    # Create and place the close button (main menu)
    close_button = customtkinter.CTkButton(app, text="X", command=close_window, fg_color="#2F2F2F", hover_color="#880808")
    close_button.place(x=1780, y=10)

# Clear current screen and show login or sign-up screen
def clear_screen():
    for widget in app.winfo_children():
        widget.destroy()

# Sign-up function
def signup():
    username = username_entry.get()
    password = password_entry.get()
    if username != "" and password != "":
        cursor.execute("SELECT username FROM users WHERE username=?", [username])
        if cursor.fetchone() is not None:
            messagebox.showerror("Error", "Username already in use")
        else:
            encoded_password = password.encode("utf-8")
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            cursor.execute("INSERT INTO users VALUES (?, ?)", [username, hashed_password])
            conn.commit()
            messagebox.showinfo("Success", "Your account has been created")
    else:
        messagebox.showerror("Error", "Please enter all data")

# Log in function
def login_account():
    username = username_entry2.get()
    password = password_entry2.get()
    if username != "" and password != "":
        cursor.execute("SELECT password FROM users WHERE username=?", [username])
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode("utf-8"), result[0]):
                messagebox.showinfo("Success", "You have logged in successfully")
                show_main_menu()  # Show main menu after successful login
            else:
                messagebox.showerror("Error", "Incorrect Password")
        else:
            messagebox.showerror("Error", "Incorrect Username")
    else:
        messagebox.showerror("Error", "Please enter all data")

# Login Page
def login():
    # Remove sign up screen and create log in screen
    frame1.destroy()
    frame2 = customtkinter.CTkFrame(app, bg_color="#73B12F", fg_color="#73B12F", width=470, height=360)
    frame2.place(x=0, y=0)
    
    #background image
    image1=PhotoImage(file="placeholder.png")
    image1_label=Label(frame2,image=image1,bg="#73B12F")
    image1_label.place(x=20,y=20)
    frame2.image1= image1
    # Text label
    login_label2 = customtkinter.CTkLabel(frame2, font=font1, text="Log in", bg_color="#73B12F", text_color="#000000")
    login_label2.place(x=280, y=20)

    global username_entry2
    global password_entry2

    # Username & Password entry text box + submit input button
    username_entry2 = customtkinter.CTkEntry(frame2, font=font2, text_color="#000000", fg_color="#7F7F7F", border_color="#004790", border_width=3, placeholder_text="Username", placeholder_text_color="#000000")
    username_entry2.place(x=230, y=80)

    password_entry2 = customtkinter.CTkEntry(frame2, font=font2, show="*", text_color="#000000", fg_color="#7F7F7F", border_color="#004790", border_width=3, placeholder_text="Password", placeholder_text_color="#000000")
    password_entry2.place(x=230, y=150)

    login_button2 = customtkinter.CTkButton(frame2, command=login_account, font=font4, text="Log in", text_color="#000000", fg_color="#7F7F7F", hover_color="#006e44", cursor="hand2", width=40)
    login_button2.place(x=230, y=220)

    # Show password function for login page
    def password_command2():
        if password_entry2.cget('show') == '*':
            password_entry2.configure(show='')
        else:
            password_entry2.configure(show='*')

    # Show password button creation (login screen)
    ShowButton = customtkinter.CTkButton(frame2, fg_color='#7F7F7F', font=font4, command=password_command2, text='show password', text_color="#000000", width=7)
    ShowButton.place(x=230, y=185)

# Sign up Page

frame1 = customtkinter.CTkFrame(app, fg_color="#73B12F", bg_color="#73B12F", width=470, height=360)
frame1.place(x=0, y=0)

# Text label
signup_label = customtkinter.CTkLabel(frame1, font=font1, text="Sign up", text_color="#000000")
signup_label.place(x=280, y=20)
#background image
image1=PhotoImage(file="placeholder.png")
image1_label=Label(frame1,image=image1,bg="#73B12F")
image1_label.place(x=20,y=20)
frame1.image1= image1
# Username & Password entry text box + submit input button
username_entry = customtkinter.CTkEntry(frame1, font=font2, text_color="#000000", fg_color="#7F7F7F", border_color="#004790", border_width=3, placeholder_text="Username", placeholder_text_color="#000000")
username_entry.place(x=230, y=80)

password_entry = customtkinter.CTkEntry(frame1, font=font2, show="*", text_color="#000000", fg_color="#7F7F7F", border_color="#004790", border_width=3, placeholder_text="Password", placeholder_text_color="#000000")
password_entry.place(x=230, y=150)

signup_button = customtkinter.CTkButton(frame1, command=signup, font=font2, text_color="#000000", text="Sign up", fg_color="#7F7F7F", hover_color="#006e44", cursor="hand2", corner_radius=5, width=120)
signup_button.place(x=230, y=220)

# Text label
login_label = customtkinter.CTkLabel(frame1, font=font3, text="Already have an account?", fg_color="#73B12F", text_color="#000000")
login_label.place(x=230, y=250)

# Create button that will take you to login screen
login_button = customtkinter.CTkButton(frame1, font=font4, text="Log in", command=login, text_color="#000000", fg_color="#7F7F7F", hover_color="#006e44", cursor="hand2", width=40)
login_button.place(x=395, y=250)

# Show password button function on signup screen
def password_command():
    if password_entry.cget('show') == '*':
        password_entry.configure(show='')
    else:
        password_entry.configure(show='*')

# Show password button creation (signup)
ShowButton = customtkinter.CTkButton(frame1, fg_color='#7F7F7F', font=font4, command=password_command, text='show password', text_color="#000000", width=7)
ShowButton.place(x=230, y=185)




# Start the app
app.mainloop()
