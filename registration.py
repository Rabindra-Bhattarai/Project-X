import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage, Label, Entry, Button

def register_user():
    name = name_entry.get()
    password = password_entry.get()
    dob = dob_entry.get()
    address = address_entry.get()
    
    # Here, you would typically save the registration information to a database
    # For simplicity, I'm just displaying the information in a message box
    messagebox.showinfo("Registration Successful", f"Name: {name}\nPassword: {password}\nDOB: {dob}\nAddress: {address}")

# Create the main window
root = tk.Tk()

root.title("Registration")

# Load image and keep a reference
image = PhotoImage(file="apple.png")
label = Label(root, image=image)
label.pack()


# Calculate center coordinates
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 500  # Adjust as needed
window_height = 250  # Adjust as needed
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set window size and position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create and place widgets

name_label = tk.Label(root, text="Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

dob_label = tk.Label(root, text="Date of Birth:")
dob_label.pack()

dob_entry = tk.Entry(root)
dob_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()

address_entry = tk.Entry(root)
address_entry.pack()

register_button = tk.Button(root, text="Register", command=register_user)
register_button.pack()
