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

def forgot_password():
    # Implement the logic for password recovery here
    # For simplicity, just display a message box
    messagebox.showinfo("Forgot Password", "Please contact support to reset your password.")

def open_registration():
    # Destroy the current window
    root.destroy()
    
    # Open the registration window
    import registration

def toggle_password_visibility():
    if password_visible.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

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
label_username = tk.Label(canvas, text="Username:", bg="white")
label_username.place(relx=0.5, rely=0.3, anchor="e")

entry_username = tk.Entry(canvas)
entry_username.place(relx=0.8, rely=0.3, anchor="e")

label_password = tk.Label(canvas, text="Password:", bg="white")
label_password.place(relx=0.5, rely=0.4, anchor="e")

entry_password = tk.Entry(canvas, show="*")
entry_password.place(relx=0.8, rely=0.4, anchor="e")

password_visible = tk.BooleanVar()
show_password_checkbutton = tk.Checkbutton(canvas, text="Show Password", variable=password_visible, command=toggle_password_visibility)
show_password_checkbutton.place(relx=0.8, rely=0.5, anchor="e")

button_login = tk.Button(canvas, text="Login", command=check_credentials)
button_login.place(relx=0.7, rely=0.65, anchor="e")

forgot_password_label = tk.Label(canvas, text="Forgot Password?", fg="blue", cursor="hand2")
forgot_password_label.place(relx=0.75, rely=0.75, anchor="e")
forgot_password_label.bind("<Button-1>", lambda event: forgot_password())

register_label = tk.Label(canvas, text="Register", fg="blue", cursor="hand2")
register_label.place(relx=0.71, rely=0.85, anchor="e")
register_label.bind("<Button-1>", lambda event: open_registration())

# Run the application
root.mainloop()
