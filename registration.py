import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
import os
import re

# Function to create the SQLite database and table
def create_database():
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       email TEXT UNIQUE,
                       password TEXT,
                       dob TEXT,
                       address TEXT)''')
    conn.commit()
    conn.close()

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to validate and format date of birth (DOB)
def validate_dob(dob):
    # Regular expression pattern for DD/MM/YYYY format
    pattern = r'\b(0?[1-9]|[12]\d|3[01])/(0?[1-9]|1[0-2])/\d{4}\b'
    if re.match(pattern, dob):
        return True
    else:
        return False

# Function to validate and format address
def validate_address(address):
  
    if address.isalpha():
        return True
    else:
        return False

# Function to validate password requirements
def validate_password(password):
    # Password must be at least 8 characters long and include at least one number, one letter, and one special character
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[a-zA-Z]', password):
        return False
    if not re.search(r'[!@#$%^&*()-_+=]', password):
        return False
    return True

# Function to insert a new user into the database
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
        root.destroy()  # Destroy the registration window
        os.system('python Login.py')  # Open the Login.py file
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to handle user registration
def register_user():
    email = email_entry.get()
    password = password_entry.get()
    dob = dob_entry.get()
    address = address_entry.get()

    # Validate and format DOB
    if not validate_dob(dob):
        messagebox.showerror("Error", "Invalid Date of Birth format. Please use DD/MM/YYYY.")
        return

    # Validate address
    if not validate_address(address):
        messagebox.showerror("Error", "Please enter a valid address.")
        return

    # Validate password
    if not validate_password(password):
        messagebox.showerror("Error", "Password must be at least 8 characters long and include at least one number, one letter, and one special character.")
        return

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

password_entry = tk.Entry(root)  # Password entry without hiding
password_entry.place(relx=0.3, rely=0.3)

dob_label = tk.Label(root, text="DOB (D/M/Y):", bg="white")
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
