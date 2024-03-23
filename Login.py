import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Here, you would typically check the username and password against a database or some other form of validation
    # For simplicity, I'm just checking if both fields are filled
    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter both username and password.")
    else:
        messagebox.showinfo("Success", "Login successful!")

# Create the main window
root = tk.Tk()
root.title("Login")

root.geometry("600x400")

# Create and place widgets
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(root, text="Login", command=validate_login)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
