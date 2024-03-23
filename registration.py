import tkinter as tk
from tkinter import messagebox

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
root.title("Registration Form")




# Load image
image = tk.PhotoImage(file="Register.png")

# Create a canvas to display the image as background
canvas = tk.Canvas(root, width=500, height=250)  # Adjust width and height as needed
canvas.pack(fill="both", expand=True)

# Set the image as background
canvas.create_image(0, 0, anchor="nw", image=image)

# Add a heading
heading = tk.Label(root, text="Welcome", font=("Helvetica", 16, "bold"), bg="white")
heading.place(relx=0.5, rely=0.05, anchor="center")

# Create and place widgets
name_label = tk.Label(root, text="Name:", bg="white")
name_label.place(relx=0.1, rely=0.2)

name_entry = tk.Entry(root)
name_entry.place(relx=0.3, rely=0.2)

password_label = tk.Label(root, text="Password:", bg="white")
password_label.place(relx=0.1, rely=0.3)

password_entry = tk.Entry(root, show="*")
password_entry.place(relx=0.3, rely=0.3)

dob_label = tk.Label(root, text="Date of Birth:", bg="white")
dob_label.place(relx=0.1, rely=0.4)

dob_entry = tk.Entry(root)
dob_entry.place(relx=0.3, rely=0.4)

address_label = tk.Label(root, text="Address:", bg="white")
address_label.place(relx=0.1, rely=0.5)

address_entry = tk.Entry(root)
address_entry.place(relx=0.3, rely=0.5)

register_button = tk.Button(root, text="Register", command=register_user)
register_button.place(relx=0.37, rely=0.6)

# Start the Tkinter event loop
root.mainloop()
