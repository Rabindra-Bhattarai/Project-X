import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
import hashlib
import os
import random

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_credentials(entry_password):  # Pass entry_password as an argument
    email = entry_email.get()

    # Check if the email is a valid Gmail address
    if not email.endswith('@gmail.com'):
        messagebox.showerror("Login Failed", "Please enter a valid Gmail address.")
        return

    password = entry_password.get()  # Use the entry_password passed as an argument

    conn = sqlite3.connect("ravi.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE email=?", (email,))
    result = cursor.fetchone()

    if result:
        hashed_password = result[0]

        hashed_entered_password = hash_password(password)

        if hashed_entered_password == hashed_password:
            messagebox.showinfo("Login Successful", "Welcome, " + email + "!")
            root.destroy()
            os.system('python dashboard.py')
        else:
            messagebox.showerror("Login Failed", "Invalid email or password")
    else:
        messagebox.showerror("Login Failed", "Invalid email or password")

    conn.close()

def forgot_password():
    forgot_password_window = tk.Toplevel(root)
    forgot_password_window.title("Forgot Password")
    forgot_password_window.geometry("300x200")

    def send_otp():
        email = email_entry.get()

        if not email.endswith('@gmail.com'):
            messagebox.showerror("Error", "Please enter a valid Gmail address.")
            return

        conn = sqlite3.connect("ravi.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        result = cursor.fetchone()
        conn.close()

        if result:
            otp = str(random.randint(100000, 999999))
            messagebox.showinfo("OTP", f"Your OTP is: {otp}")
            entered_otp = simpledialog.askstring("OTP Verification", "Enter the OTP sent to your email:")
            if entered_otp == otp:
                change_password_window = tk.Toplevel(root)
                change_password_window.title("Change Password")
                change_password_window.geometry("300x200")
                # Implement the change password interface here
            else:
                messagebox.showerror("Error", "Invalid OTP. Please try again.")
        else:
            messagebox.showerror("Error", "Email not found in our records.")

    tk.Label(forgot_password_window, text="Enter your Gmail address:").pack()
    email_entry = tk.Entry(forgot_password_window)
    email_entry.pack()

    send_otp_button = tk.Button(forgot_password_window, text="Send OTP", command=send_otp)
    send_otp_button.pack()

def toggle_password_visibility(entry):
    if entry.cget("show") == "":
        entry.config(show="*")
        show_hide_button.config(text="Show")
    else:
        entry.config(show="")
        show_hide_button.config(text="Hide")

def open_registration():
    root.destroy()
    os.system('python registration.py')

# Create a main window for the application
root = tk.Tk()
root.title("Login")
root.geometry("500x250")

canvas = tk.Canvas(root, width=500, height=250)
canvas.pack()

background_image = tk.PhotoImage(file="lg.png")
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

label_email = tk.Label(canvas, text="Gmail Address:", bg="white")
label_email.place(relx=0.5, rely=0.3, anchor="e")

entry_email = tk.Entry(canvas)
entry_email.place(relx=0.8, rely=0.3, anchor="e")

label_password = tk.Label(canvas, text="Password:", bg="white")
label_password.place(relx=0.5, rely=0.4, anchor="e")

# Create the entry widget for password input and assign it the name entry_password
entry_password = tk.Entry(canvas, show="*")
entry_password.place(relx=0.8, rely=0.4, anchor="e")

show_hide_button = tk.Button(canvas, text="Hide", command=lambda: toggle_password_visibility(entry_password))
show_hide_button.place(relx=0.85, rely=0.4, anchor="w")

button_login = tk.Button(canvas, text="Login", command=lambda: check_credentials(entry_password))
button_login.place(relx=0.7, rely=0.65, anchor="e")

forgot_password_label = tk.Label(canvas, text="Forgot Password?", fg="blue", cursor="hand2")
forgot_password_label.place(relx=0.75, rely=0.75, anchor="e")
forgot_password_label.bind("<Button-1>", lambda event: forgot_password())

register_label = tk.Label(canvas, text="Register", fg="blue", cursor="hand2")
register_label.place(relx=0.71, rely=0.85, anchor="e")
register_label.bind("<Button-1>", lambda event: open_registration())

root.mainloop()
