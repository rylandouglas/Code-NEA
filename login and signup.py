import customtkinter
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title("login")
app.geometry("450x360")
app.config(bg="#257534")

font1= ("Helvetica",25,"bold")
font2= ("Arial",17,"bold")
font3= ("Arial",13,"bold")
font4= ("Arial",13,"bold")
#connect to database via sqlite3
conn =sqlite3.connect("data.db")
cursor = conn.cursor()
#create a table in database
cursor.execute('''
    Create table  if not exists users (
        username TEXT NOT NULL,
        password TEXT NOT NULL)''')
#Sign up Function
def signup():
    username = username_entry.get()
    password = password_entry.get()
    if username !="" and password !="":
        cursor.execute("SELECT username FROM users WHERE username=?",[username])
        if cursor.fetchone() is not None:
            messagebox.showerror("Error","Username already in use")
        else:
            encoded_password = password.encode("utf-8")
            hashed_password = bcrypt.hashpw(encoded_password,bcrypt.gensalt())
            #print(hashed_password)
            cursor.execute("INSERT INTO users VALUES (?,?)",[username,hashed_password])
            conn.commit()
            messagebox.showinfo("Success","Your account has been created")
    else:
        messagebox.showerror("Error","Please enter all data")
#Log in Function
def login_account():
    username = username_entry2.get()
    password = password_entry2.get()
    if username!="" and password!="":
        cursor.execute("Select password FROM users WHERE username=?",[username])
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode("utf-8"),result[0]):
                messagebox.showinfo("Success","You have logged in successfully")
            else:
                messagebox.showerror("Error","Incorrect Password")
        else:
            messagebox.showerror("Error","Incorrect Username")
    else:
        messagebox.showerror("Error","Please enter all data")

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

    global username_entry2
    global password_entry2
    #Username & Password entry text box + submit input button
    username_entry2=customtkinter.CTkEntry(frame2,font=font2,text_color="#000000",fg_color="#7F7F7F",border_color="#004790",border_width=3,placeholder_text=" Username",placeholder_text_color="#000000")
    username_entry2.place(x=230,y=80)

    password_entry2=customtkinter.CTkEntry(frame2,font=font2,show="*",text_color="#000000",fg_color="#7F7F7F",border_color="#004790",border_width=3,placeholder_text="Password",placeholder_text_color="#000000")
    password_entry2.place(x=230,y=150)

    login_button2=customtkinter.CTkButton(frame2,command=login_account,font=font4,text="Log in",text_color="#000000",fg_color="#7F7F7F",hover_color="#006e44",cursor="hand2",width=40)
    login_button2.place(x=230,y=220)

    #Show password function for login page
    def password_command2():
        if password_entry2.cget('show') == '*':
            password_entry2.configure(show='')
        else:
            password_entry2.configure(show='*')

    #Show password button creation (login screen)
    ShowButton = customtkinter.CTkButton(frame2, fg_color='#7F7F7F',font=font4, command=password_command2, text='show password',text_color="#000000",width=7)
    ShowButton.place(x=230, y=185)

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

password_entry = customtkinter.CTkEntry(frame1,font=font2,show="*",text_color="#000000",fg_color="#7F7F7F",border_color="#004790",border_width=3,placeholder_text="Password",placeholder_text_color="#000000")
password_entry.place(x=230,y=150)

signup_button=customtkinter.CTkButton(frame1,command=signup,font=font2,text_color="#000000",text="Sign up",fg_color="#7F7F7F",hover_color="#006e44",cursor="hand2",corner_radius=5,width=120)
signup_button.place(x=230,y=220)
#text label
login_label=customtkinter.CTkLabel(frame1,font=font3,text="Already have an account?",fg_color="#73B12F",text_color="#000000")
login_label.place(x=230,y=250)
#create button that will take you to login screen
login_button=customtkinter.CTkButton(frame1,font=font4,text="Log in",command=login,text_color="#000000",fg_color="#7F7F7F",hover_color="#006e44",cursor="hand2",width=40)
login_button.place(x=395,y=250)

#show password button function on signup screen
def password_command2():
    if password_entry.cget('show') == '*':
        password_entry.configure(show='')
    else:
        password_entry.configure(show='*')

#Show password button creation (signup)
ShowButton = customtkinter.CTkButton(frame1, fg_color='#7F7F7F',font=font4, command=password_command2, text='show password',text_color="#000000",width=7)
ShowButton.place(x=230, y=185)





app.mainloop()

