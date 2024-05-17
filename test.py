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
#Sign up Function
def signup():
    username = username_entry.get()
    password = password_entry.get()
    if username !="" and password !="":
        cursor.execute("SELECT username FROM users WHERE username=?",[username])
        if cursor.fetchone() is not None:
            messagebox.showerror("Error","Email already in use")
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
    frame1.destroy()
    frame2 = customtkinter.CTkFrame(app,bg_color="#73B12F",fg_color="#73B12F",width=470,height=360)
    frame2.place(x=0,y=0)

    image1=PhotoImage(file="images.png")
    image1_label=Label(frame2,image=image1,bg="#73B12F")
    image1_label.place(x=20,y=20)
    frame2.image1= image1

    login_label2= customtkinter.CTkLabel(frame2,font=font1,text="Log in",bg_color="#73B12F",text_color="#000000")
    login_label2.place(x=280,y=20)

    global username_entry2
    global password_entry2

    username_entry2=customtkinter.CTkEntry(frame2,font=font2,text_color="#000000",fg_color="#7F7F7F",border_color="#004790",border_width=3,placeholder_text="Email Address",placeholder_text_color="#000000")
    username_entry2.place(x=230,y=80)

    password_entry2=customtkinter.CTkEntry(frame2,font=font2,show="*",text_color="#000000",fg_color="#7F7F7F",border_color="#004790",border_width=3,placeholder_text="Password",placeholder_text_color="#000000")
    password_entry2.place(x=230,y=150)

    login_button2=customtkinter.CTkButton(frame2,command=login_account,font=font4,text="Log in",text_color="#000000",fg_color="#7F7F7F",hover_color="#006e44",cursor="hand2",width=40)
    login_button2.place(x=230,y=220)



#Sign up Page
frame1 = customtkinter.CTkFrame(app,fg_color="#73B12F",bg_color="#73B12F",width=470,height=360)
frame1.place(x=0,y=0)

image1=PhotoImage(file="images.png")
image1_label = Label(frame1,image=image1)
image1_label.place(x=20,y=20)

signup_label =customtkinter.CTkLabel(frame1,font=font1,text="Sign up",text_color="#000000")
signup_label.place(x=280,y=20)

username_entry = customtkinter.CTkEntry(frame1,font=font2,text_color="#000000",fg_color="#7F7F7F",border_color="#004790",border_width=3,placeholder_text="Email Address",placeholder_text_color="#000000")
username_entry.place(x=230,y=80)

password_entry = customtkinter.CTkEntry(frame1,font=font2,show="*",text_color="#000000",fg_color="#7F7F7F",border_color="#004790",border_width=3,placeholder_text="Password",placeholder_text_color="#000000")
password_entry.place(x=230,y=150)

signup_button=customtkinter.CTkButton(frame1,command=signup,font=font2,text_color="#000000",text="Sign up",fg_color="#7F7F7F",hover_color="#006e44",cursor="hand2",corner_radius=5,width=120)
signup_button.place(x=230,y=220)

login_label=customtkinter.CTkLabel(frame1,font=font3,text="Already have an account?",fg_color="#73B12F",text_color="#000000")
login_label.place(x=230,y=250)

login_button=customtkinter.CTkButton(frame1,font=font4,text="Log in",command=login,text_color="#000000",fg_color="#7F7F7F",hover_color="#006e44",cursor="hand2",width=40)
login_button.place(x=395,y=250)

win = Toplevel()
window_width = 350
window_height = 350
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
position_top = int(screen_height / 4 - window_height / 4)
position_right = int(screen_width / 2 - window_width / 2)
win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
win.title('Forgot Password')
win.configure(background='#f8f8f8')
win.resizable(0, 0)

    # ====== Email ====================
email_entry2 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
email_entry2.place(x=40, y=30, width=256, height=34)
email_entry2.config(highlightbackground="black", highlightcolor="black")
email_label2 = Label(win, text='• Email account', fg="#89898b", bg='#f8f8f8',
                         font=("yu gothic ui", 11, 'bold'))
email_label2.place(x=40, y=0)

# ====  New Password ==================
new_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
new_password_entry.place(x=40, y=110, width=256, height=34)
new_password_entry.config(highlightbackground="black", highlightcolor="black")
new_password_label = Label(win, text='• New Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
new_password_label.place(x=40, y=80)

    # ====  Confirm Password ==================
confirm_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
confirm_password_entry.place(x=40, y=190, width=256, height=34)
confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
confirm_password_label = Label(win, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                   font=("yu gothic ui", 11, 'bold'))
confirm_password_label.place(x=40, y=160)

# ======= Update password Button ============
update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#1b87d2', font=("yu gothic ui bold", 14),
                         cursor='hand2', activebackground='#1b87d2')
update_pass.place(x=40, y=240, width=256, height=50)


forgotPassword = Button(frame1, text='Forgot password', font=("yu gothic ui", 8, "bold underline"), bg='#f8f8f8',
                        borderwidth=0, activebackground='#f8f8f8', command=lambda: forgotPassword(), cursor="hand2")
forgotPassword.place(x=290, y=290)




app.mainloop()

