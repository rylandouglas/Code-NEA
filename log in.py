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

conn =sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute('''
    Create table  if not exists users (
        username TEXT NOT NULL,
        password TEXT NOT NULL)''')

frame1 = customtkinter.CTkFrame(app,fg_color="#73B12F",bg_color="#73B12F",width=470,height=360)
frame1.place(x=0,y=0)

image1=PhotoImage(file="images.png")
image1_label = Label(frame1,image=image1)
image1_label.place(x=20,y=20)

signup_label =customtkinter.CTkLabel(frame1,font=font1,text="Sign up",text_color="#000000")
signup_label.place(x=280,y=20)

username_entry = customtkinter.CTkEntry(frame1,font=font2,text_color="#000000",fg_color="#7F7F7F",border_color="#004790",border_width=3,placeholder_text="Username",placeholder_text_color="#000000")
username_entry.place(x=230,y=80)

password_entry = customtkinter.CTkEntry(frame1,font=font2,show="*",text_color="#000000",fg_color="#7F7F7F",border_color="#004790",border_width=3,placeholder_text="Password",placeholder_text_color="#000000")
password_entry.place(x=230,y=150)

signup_button=customtkinter.CTkButton(frame1,font=font2,text_color="#000000",text="Sign up",fg_color="#7F7F7F",hover_color="#006e44",cursor="hand2",corner_radius=5,width=120)
signup_button.place(x=230,y=220)

login_label=customtkinter.CTkLabel(frame1,font=font3,text="Already have an account?",fg_color="#73B12F",text_color="#000000")
login_label.place(x=230,y=250)

login_button=customtkinter.CTkButton(frame1,font=font4,text="Log in",text_color="#000000",fg_color="#7F7F7F",hover_color="#006e44",cursor="hand2",width=40)
login_button.place(x=395,y=250)





app.mainloop()

