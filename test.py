import customtkinter
from tkinter import *
from tkinter import messagebox
import bcrypt
import sqlite3


app = customtkinter.CTk()
app.title("login")
app.geometry("450x360")
app.config(bg="#257534")

font1= ("Helvetica",25,"bold")
font2= ("Arial",17,"bold")
font3= ("Arial",13,"bold")
font4= ("Arial",15,"bold")

#connect to database via sqlite3
conn =sqlite3.connect("data.db")
cursor = conn.cursor()

#create a table in database
cursor.execute('''
    Create table  if not exists users (
        username TEXT NOT NULL,
        password TEXT NOT NULL)''')

def login_account():
    # Get the username and password from the user input fields
    username = username_entry2.get()
    password = password_entry2.get()

    # Check if both username and password are provided
    if username != "" and password != "":
        
        # Validate if username and password are not longer than 20 characters
        if len(username) > 20 or len(password) > 20:
            messagebox.showerror("Error", "Username and password must be less than 20 characters.")
        else:
            # Check if the username exists in the database
            cursor.execute("SELECT password FROM users WHERE username=?", [username])
            result = cursor.fetchone()
            
            if result:
                # Check if the provided password matches the hashed password in the database
                if bcrypt.checkpw(password.encode("utf-8"), result[0]):
                    messagebox.showinfo("Success", "You have logged in successfully")
                else:
                    messagebox.showerror("Error", "Incorrect Password")
            else:
                messagebox.showerror("Error", "Incorrect Username")
    else:
        # Show an error if either the username or password is missing
        messagebox.showerror("Error", "Please enter all data")
   

#Log in Page
def login():
    #remove sign up screen and create log in screen
    frame1.destroy()
    frame2 = customtkinter.CTkFrame(app,bg_color="#73B12F",fg_color="#73B12F",width=470,height=360)
    frame2.place(x=0,y=0)
    #background image
    image1=PhotoImage(file="placeholder.png")
    image1_label=Label(frame2,image=image1,bg="#73B12F")
    image1_label.place(x=20,y=20)
    frame2.image1= image1
    #Text label
    login_label2= customtkinter.CTkLabel(frame2,font=font1,text="Log in",bg_color="#73B12F",text_color="#000000")
    login_label2.place(x=280,y=20)
    #global variables
    global username_entry2
    global password_entry2
    #Username & Password entry text box + submit input button
    username_entry2=customtkinter.CTkEntry(frame2,font=font2,text_color="#000000",fg_color="#7F7F7F",border_color="#004790",border_width=3,placeholder_text=" Username",placeholder_text_color="#000000")
    username_entry2.place(x=230,y=80)

    password_entry2=customtkinter.CTkEntry(frame2,font=font2,text_color="#000000",fg_color="#7F7F7F",border_color="#004790",border_width=3,placeholder_text="Password",placeholder_text_color="#000000")
    password_entry2.place(x=230,y=150)

    login_button2=customtkinter.CTkButton(frame2,command=login_account,font=font4,text="Log in",text_color="#000000",fg_color="#7F7F7F",hover_color="#006e44",cursor="hand2",width=40)
    login_button2.place(x=230,y=220)

#signup function
def signup():
    # Get the username and password entered by the user
    username = username_entry.get()
    password = password_entry.get()

    # Check if both username and password are provided
    if username != "" and password != "":
        
        # Check if the username or password exceed 20 characters
        if len(username) > 20 or len(password) > 20:
            messagebox.showerror("Error", "Username and password must be less than 20 characters.")
        
        else:
            # Check if the username already exists in the database
            cursor.execute("SELECT username FROM users WHERE username=?", [username])
            if cursor.fetchone() is not None:
                messagebox.showerror("Error", "Username already in use")
            else:
                # Encode and hash the password with bcrypt
                encoded_password = password.encode("utf-8")
                hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
                
                # Insert the new user into the database
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", [username, hashed_password])
                conn.commit()  # Commit the changes to the database
                
                # Show success message
                messagebox.showinfo("Success", "Your account has been created")
    else:
        # Show error if username or password is empty
        messagebox.showerror("Error", "Please enter all data")

     


#Sign up Page
#create sign up
frame1 = customtkinter.CTkFrame(app,fg_color="#73B12F",bg_color="#73B12F",width=470,height=360)
frame1.place(x=0,y=0)
#insert background image
image1=PhotoImage(file="placeholder.png")
image1_label = Label(frame1,image=image1)
image1_label.place(x=20,y=20)
#text label
signup_label =customtkinter.CTkLabel(frame1,font=font1,text="Sign up",text_color="#000000")
signup_label.place(x=280,y=20)
#Username & Password entry text box + submit input button
username_entry = customtkinter.CTkEntry(frame1,font=font2,text_color="#000000",fg_color="#7F7F7F",border_color="#004790",border_width=3,placeholder_text="Username",placeholder_text_color="#000000")
username_entry.place(x=230,y=80)

password_entry = customtkinter.CTkEntry(frame1,font=font2,text_color="#000000",fg_color="#7F7F7F",border_color="#004790",border_width=3,placeholder_text="Password",placeholder_text_color="#000000")
password_entry.place(x=230,y=150)

signup_button=customtkinter.CTkButton(frame1,command=signup,font=font2,text_color="#000000",text="Sign up",fg_color="#7F7F7F",hover_color="#006e44",cursor="hand2",corner_radius=5,width=120)
signup_button.place(x=230,y=220)

#text label
login_label=customtkinter.CTkLabel(frame1,font=font3,text="Already have an account?",fg_color="#73B12F",text_color="#000000")
login_label.place(x=230,y=250)
#create button that will take you to login screen
login_button=customtkinter.CTkButton(frame1,font=font4,text="Log in",command=login,text_color="#000000",fg_color="#7F7F7F",hover_color="#006e44",cursor="hand2",width=40)
login_button.place(x=395,y=250)




app.mainloop()

