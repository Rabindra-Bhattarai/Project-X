# login.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import backend


def login():
    username = username_entry.get()
    password = password_entry.get()

    # Authenticate user
    if backend.authenticate(username, password):
        # Hide the login window
        root.withdraw()
        # Run the admin_panel.py script
        subprocess.run(["python", "admin_panel.py"])
    else:
        messagebox.showerror("Error", "Invalid username or password")

def toggle_password_visibility():
    if show_password.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

def forgot_password():
    messagebox.showinfo("Forgot Password", "Please contact support for assistance.")

def register():
    # Hide the login window
    root.withdraw()
    # Run the registration.py script
    subprocess.run(["python", "registration.py"])

# Create main window
root = tk.Tk()
root.title("Login Page")



# Set window size and position
window_width = 500
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))

# Style
style = ttk.Style()
style.theme_use("clam")

# Colors
bg_color = "#f0f0f0"
text_color = "#333333"
login_register_button_bg_color = "#ADD8E6"  # Blue color for the login and register buttons
forgot_button_bg_color = "#ADD8E6"  # Green color for the "Forgot Password" button

# Fonts
label_font = ("Times New Roman", 12)
entry_font = ("Times New Roman", 12)
button_font = ("Times New Roman", 12, "bold")

# Configure Style
style.configure("TLabel", background=bg_color, foreground=text_color, font=label_font)
style.configure("TEntry", fieldbackground=bg_color, font=entry_font)
style.configure("TButton", font=button_font)

# Username Label and Entry
username_label = ttk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
username_entry = ttk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Password Label and Entry
password_label = ttk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
password_entry = ttk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Show Password Checkbox
show_password = tk.BooleanVar()
show_password_checkbox = ttk.Checkbutton(root, text="Show Password", variable=show_password, command=toggle_password_visibility)
show_password_checkbox.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Login Button
login_button = ttk.Button(root, text="Login", command=login)
login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="we")

# Forgot Password Button
forgot_password_button = ttk.Button(root, text="Forgot Password?", command=forgot_password,)
forgot_password_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")

# Register Button
register_button = ttk.Button(root, text="Register", command=register)
register_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="we")

root.mainloop()
