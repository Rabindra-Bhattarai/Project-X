import tkinter as tk
from tkinter import messagebox

def check_credentials():
    username = entry_username.get()
    password = entry_password.get()

    # You can replace this with your actual authentication logic
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login")

# Create and pack widgets
label_username = tk.Label(root, text="Username:")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

button_login = tk.Button(root, text="Login", command=check_credentials)
button_login.pack()

# Run the application
root.mainloop()
