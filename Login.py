import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
import hashlib
import os
import random  # For generating OTP
from tkinter import simpledialog  # For getting OTP from user

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check credentials
def check_credentials():
    username = entry_username.get()
    password = entry_password.get()

    # Connect to the database
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # Query the database to retrieve the hashed password for the entered username
    cursor.execute("SELECT password FROM users WHERE phone_number=?", (username,))
    result = cursor.fetchone()

    if result:
        # Retrieve the hashed password from the result
        hashed_password = result[0]

        # Hash the entered password for comparison
        hashed_entered_password = hash_password(password)

        # Compare the hashed passwords
        if hashed_entered_password == hashed_password:
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            root.destroy()  # Destroy the current window
            os.system('python dashboard.py')  # Open the dashboard.py file
        else:
            messagebox.showerror("Login Failed", "Invalid phone number or password")
    else:
        messagebox.showerror("Login Failed", "Invalid phone number or password")

    # Close the database connection
    conn.close()

# Function to handle "Forgot Password" functionality
def forgot_password():
    # Create a new window for forgot password functionality
    forgot_password_window = tk.Toplevel(root)
    forgot_password_window.title("Forgot Password")
    forgot_password_window.geometry("300x200")

    # Function to generate OTP and send it to the provided phone number
    def send_otp():
        phone_number = phone_number_entry.get()

        if phone_number:
            # Check if the phone number exists in the database
            conn = sqlite3.connect("user_data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE phone_number=?", (phone_number,))
            result = cursor.fetchone()
            conn.close()

            if result:
                # Generate a random 6-digit OTP
                otp = str(random.randint(100000, 999999))

                # In a real-world scenario, you would send this OTP to the user's phone number via SMS
                # For demonstration purposes, we will simply display the OTP
                messagebox.showinfo("OTP", f"Your OTP is: {otp}")

                # Prompt the user to enter the OTP
                entered_otp = simpledialog.askstring("OTP Verification", "Enter the OTP sent to your phone number:")

                # Compare the entered OTP with the generated OTP
                if entered_otp == otp:
                    # If OTP is correct, open the change password interface
                    change_password_window = tk.Toplevel(root)
                    change_password_window.title("Change Password")
                    change_password_window.geometry("300x200")

                    # Implement the change password interface here
                    # Include entry fields for new password and confirmation, along with a button to confirm changes
                else:
                    messagebox.showerror("Error", "Invalid OTP. Please try again.")
            else:
                messagebox.showerror("Error", "Phone number not found in our records.")
        else:
            messagebox.showerror("Error", "Please enter your phone number.")

    # Create widgets for the forgot password window
    tk.Label(forgot_password_window, text="Enter your Nepali phone number:").pack()
    phone_number_entry = tk.Entry(forgot_password_window)
    phone_number_entry.pack()

    send_otp_button = tk.Button(forgot_password_window, text="Send OTP", command=send_otp)
    send_otp_button.pack()

# Function to open registration window
def open_registration():
    root.destroy()  # Destroy the current window
    os.system('python registration.py')  # Open the registration.py file

# Create the main window
root = tk.Tk()
root.title("Login")
root.geometry("500x250")

# Add a Canvas widget to hold the background image
canvas = tk.Canvas(root, width=500, height=250)
canvas.pack()

# Load the background image
background_image = tk.PhotoImage(file="lg.png")  # Make sure lg.png is in the same directory as your script

# Place the background image on the Canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Widgets directly on the Canvas
label_username = tk.Label(canvas, text="Nepali Phone Number:", bg="white")
label_username.place(relx=0.5, rely=0.3, anchor="e")

entry_username = tk.Entry(canvas)
entry_username.place(relx=0.8, rely=0.3, anchor="e")

label_password = tk.Label(canvas, text="Password:", bg="white")
label_password.place(relx=0.5, rely=0.4, anchor="e")

entry_password = tk.Entry(canvas, show="*")
entry_password.place(relx=0.8, rely=0.4, anchor="e")

button_login = tk.Button(canvas, text="Login", command=check_credentials)
button_login.place(relx=0.7, rely=0.65, anchor="e")


forgot_password_label = tk.Label(canvas, text="Forgot Password?", fg="blue", cursor="hand2")
forgot_password_label.place(relx=0.75, rely=0.75, anchor="e")
forgot_password_label.bind("<Button-1>", lambda event: forgot_password())

# Registration option
register_label = tk.Label(canvas, text="Register", fg="blue", cursor="hand2")
register_label.place(relx=0.71, rely=0.85, anchor="e")
register_label.bind("<Button-1>", lambda event: open_registration())

# Start the Tkinter event loop
root.mainloop()
