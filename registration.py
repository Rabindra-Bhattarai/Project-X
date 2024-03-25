import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
import os

def create_database():
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")  # Drop the existing table if it exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       email TEXT UNIQUE,
                       password TEXT,
                       dob TEXT,
                       address TEXT)''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def insert_user(email, password, dob, address):
    try:
        conn = sqlite3.connect("user_data.db")
        cursor = conn.cursor()
        hashed_password = hash_password(password)
        cursor.execute("INSERT INTO users (email, password, dob, address) VALUES (?, ?, ?, ?)",
                       (email, hashed_password, dob, address))
        conn.commit()
        conn.close()
        messagebox.showinfo("Registration Successful", "User registered successfully!")
        root.destroy()
        os.system('python Login.py')
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def register_user():
    email = email_entry.get()

    if not email.endswith('@gmail.com'):
        messagebox.showerror("Error", "Please enter a valid Gmail address.")
        return

    password = password_entry.get()
    dob = dob_entry.get()
    address = address_entry.get()
    insert_user(email, password, dob, address)

root = tk.Tk()
root.title("Registration Form")

create_database()

image = tk.PhotoImage(file="Register.png")

canvas = tk.Canvas(root, width=500, height=250)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=image)

heading = tk.Label(root, text="Welcome", font=("Helvetica", 16, "bold"), bg="white")
heading.place(relx=0.5, rely=0.05, anchor="center")

email_label = tk.Label(root, text="Gmail Address:", bg="white")
email_label.place(relx=0.1, rely=0.2)

email_entry = tk.Entry(root)
email_entry.place(relx=0.3, rely=0.2)

password_label = tk.Label(root, text="Password:", bg="white")
password_label.place(relx=0.1, rely=0.3)

password_entry = tk.Entry(root, show="*")
password_entry.place(relx=0.3, rely=0.3)

dob_label = tk.Label(root, text="Date of Birth (DD/MM/YYYY):", bg="white")
dob_label.place(relx=0.1, rely=0.4)

dob_entry = tk.Entry(root)
dob_entry.place(relx=0.3, rely=0.4)

address_label = tk.Label(root, text="Address:", bg="white")
address_label.place(relx=0.1, rely=0.5)

address_entry = tk.Entry(root)
address_entry.place(relx=0.3, rely=0.5)

register_button = tk.Button(root, text="Register", command=register_user)
register_button.place(relx=0.37, rely=0.6)

root.mainloop()
