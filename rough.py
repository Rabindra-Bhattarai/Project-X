import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create a new table for storing user credentials
def create_table():
    conn = sqlite3.connect('user_credentials.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT NOT NULL UNIQUE, password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Function to insert new user credentials into the database
def register_user(username, password, confirm_password):
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return
    conn = sqlite3.connect('user_credentials.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Registration successful")
    register_window.destroy()
    open_login_page()

# Function to handle forgot password functionality
def forgot_password():
    messagebox.showinfo("Forgot Password", "Please contact administrator for password reset")

# Function to open the registration page
def open_registration_page():
    global register_window
    root.withdraw()
    register_window = tk.Toplevel(root)
    register_window.title("Registration Panel")
    
    # Create username label and entry in registration window
    register_username_label = tk.Label(register_window, text="Username:")
    register_username_label.grid(row=0, column=0, padx=10, pady=5)
    register_username_entry = tk.Entry(register_window)
    register_username_entry.grid(row=0, column=1, padx=10, pady=5)

    # Create password label and entry in registration window
    register_password_label = tk.Label(register_window, text="Password:")
    register_password_label.grid(row=1, column=0, padx=10, pady=5)
    register_password_entry = tk.Entry(register_window, show="*")
    register_password_entry.grid(row=1, column=1, padx=10, pady=5)

    # Create confirm password label and entry in registration window
    confirm_password_label = tk.Label(register_window, text="Confirm Password:")
    confirm_password_label.grid(row=2, column=0, padx=10, pady=5)
    confirm_password_entry = tk.Entry(register_window, show="*")
    confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)

    # Create register button in registration window
    register_button = tk.Button(register_window, text="Register", command=lambda: register_user(register_username_entry.get(), register_password_entry.get(), confirm_password_entry.get()))
    register_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Function to open the login page
def open_login_page():
    root.deiconify()

# Function to validate login credentials
def login():
    username = username_entry.get()
    password = password_entry.get()
    conn = sqlite3.connect('user_credentials.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if c.fetchone():
        messagebox.showinfo("Success", "Login successful")
    else:
        messagebox.showerror("Error", "Invalid username or password")
    conn.close()

# Create main window
root = tk.Tk()
root.title("Login Page")

# Create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Create password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Create login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Create forgot password button
forgot_password_button = tk.Button(root, text="Forgot Password", command=forgot_password)
forgot_password_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Create register button
register_button = tk.Button(root, text="Register", command=open_registration_page)
register_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Create SQLite3 database table
create_table()

# Run the main loop
root.mainloop()
