import customtkinter
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

# Create the app window
app = customtkinter.CTk()
app.title("Login")
app.geometry("450x360")
app.config(bg="#257534")
           
# Fonts
font1 = ("Helvetica", 25, "bold")
font2 = ("Arial", 17, "bold")
font3 = ("Arial", 13, "bold")
font4 = ("Arial", 13, "bold")

# Connect to database via sqlite3
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Create a table in the database (if it doesn't already exist)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        password TEXT NOT NULL)
''')

# Sign up function
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

def show_main_menu():
    # Clear the current screen
    for widget in app.winfo_children():
        widget.destroy()

    # Create main menu UI components
    menu_data = {
        "Book a new job": [],  # Not needed- should take to calendar page
        "Existing Appointments": ["June 18th - 8:30-12:30", "August 12th - 12:30-5:30"],  # placeholder figures
        "Application Process": [], #<- should display the status of the application 
        "Business Overview": ["FAQS", "Mission Statement", "Company Information"],
        "Reviews": ["5* From Bert F", "3* From John P", "4* From Samba B"]
    }

    # Nested submenus options
    sub_options_data = {
        "August 12th - 12:30-5:30": ["Job price -560", "Estimated employees 4", "Vehicles 1 chipper & 1 van"],
        "June 18th - 8:30-12:30": ["Job price - £350", "Estimated employees=3", "Vehicles=1 chipper & 1 van"],
        "5* From Bert F": ["Absolutely fantastic service! The team at JPL Tree Care were professional, efficient, and friendly from start to finish"],
        "3* From John P": ["Overall, the service was good, but there were a few things that could have been improved. The team at JPL Tree care were friendly and knowledgeable, and they completed the tree removal safely. However, there were some delays in the scheduling, and the cleanup could have been a bit more thorough."],
        "4* From Samba B": ["Very happy with the service from JPL Tree Care. The team was professional, arrived on time, and efficiently removed a large tree from our property."]
    }

    # Create a frame that takes up the entire window (fullscreen effect)
    frame3 = customtkinter.CTkFrame(app,fg_color="#73B12F", bg_color="#73B12F")
    frame3.place(x=0, y=0, relwidth=1, relheight=1)  # Make the frame take up full window size
    
    #make main menu fullscreen
    app.attributes("-fullscreen", True)
    
    # Function to close the window
    def close_window():
        app.destroy()

    # Create and place the close button
    close_button = customtkinter.CTkButton(app, text="X", command=close_window, fg_color="#2F2F2F", hover_color="#880808")
    close_button.place(x=1780, y=10)
    
    # Add a top menu bar with a title
    menu_bar = customtkinter.CTkFrame(frame3, height=50, corner_radius=0, fg_color="#73B12F")
    menu_bar.pack(fill="x")

    # Create a label for the title in the top menu bar
    main_menu_label = customtkinter.CTkLabel(menu_bar, text="Main Menu", font=("Arial", 18, "bold"), text_color="white", bg_color="#2F2F2F")
    main_menu_label.pack(fill="x", padx=10, pady=10, anchor="center")

    # Create the menu buttons
    menu_buttons_frame = customtkinter.CTkFrame(frame3)
    menu_buttons_frame.pack(pady=30, padx=10, expand=True)

    # Add buttons for each menu item
    for idx, menu_name in enumerate(menu_data.keys()):
        button = customtkinter.CTkButton(
            menu_buttons_frame,
            text=menu_name,
            font=("Arial", 16),
            fg_color="#2F2F2F",
            hover_color="#464646",
            text_color="white",
            command=lambda name=menu_name: display_main_menu(name),
            
        )
        button.grid(row=0, column=idx, padx=10, pady=10, sticky="nsew")

    # Configure the menu buttons to expand in their grid cells
    menu_buttons_frame.grid_columnconfigure(0, weight=1)
    menu_buttons_frame.grid_columnconfigure(1, weight=1)
    menu_buttons_frame.grid_columnconfigure(2, weight=1)
    menu_buttons_frame.grid_columnconfigure(3, weight=1)
    menu_buttons_frame.grid_columnconfigure(4, weight=1)

    # Frame for displaying options for the selected menu
    dropdown_frame = customtkinter.CTkFrame(frame3, width=600, height=200, corner_radius=10, fg_color="#73B12F")
    dropdown_frame.pack(pady=10, padx=10)

    # Label for displaying the selected option
    selected_label = customtkinter.CTkLabel(dropdown_frame, text="Select an option from the menu above", font=("Arial", 16), text_color="black")
    selected_label.pack(pady=10)

    # Functions to handle displaying menu and submenu options (same as in your original code)
    def display_main_menu(menu_name):
        #Display options for the selected main menu.
        for widget in dropdown_frame.winfo_children():
            widget.destroy()

        options = menu_data.get(menu_name, [])
        for option in options:
            button = customtkinter.CTkButton(
                dropdown_frame,
                text=option,
                font=("Arial", 16),
                fg_color="#2F2F2F",
                hover_color="#464646",
                text_color="white",
                command=lambda opt=option: display_sub_menu(menu_name, opt)
            )
            button.pack(pady=5)

    def display_sub_menu(menu_name, option):
        #Display sub-options for the selected main menu option.
        for widget in dropdown_frame.winfo_children():
            widget.destroy()

        sub_options = sub_options_data.get(option)
        if sub_options:
            for sub_option in sub_options:
                button = customtkinter.CTkButton(
                    dropdown_frame,
                    text=sub_option,
                    font=("Arial", 16),
                    fg_color="#2F2F2F",
                    hover_color="#464646",
                    text_color="white",
                    command=lambda sub=sub_option: display_selection(menu_name, option, sub)
                )
                button.pack(pady=5)
        else:
            display_selection(menu_name, option)

    def display_selection(menu_name, option, sub_option=None):
        #Update label to show the final selection.
        for widget in dropdown_frame.winfo_children():
            widget.destroy()

        if sub_option:
            text = f"Selected: {menu_name} > {option} > {sub_option}"
        else:
            text = f"Selected: {menu_name} > {option}"

        selected_label.config(text=text)
        selected_label.pack(pady=20)

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