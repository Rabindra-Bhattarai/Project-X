# Importing necessary modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import backend
from tkcalendar import Calendar



# Define cal globally
cal = None

# Function to generate username and password
def generate_username_password():
    global username_entry, password_entry, address_entry, dob_entry, gender_combobox
    
    username = username_entry.get()
    password = password_entry.get()
    address = address_entry.get()
    dob = dob_entry.get()
    gender = gender_combobox.get()

    if username == "" or password == "" or address == "" or dob == "" or gender == "":
        messagebox.showerror("Error", "Please fill in all fields.")
    else:
        # Generate a random number and append it to the username
        random_number = random.randint(100, 999)
        new_username = username + str(random_number)
        
        # Insert the user into the database
        backend.insert_user(new_username, password)
        
        # Show the generated username and password
        messagebox.showinfo("Generated Credentials", f"Username: {new_username}\nPassword: {password}")

# Function to go back to the login panel
def go_back_to_login():
    global root
    # Close the registration panel and open the login panel
    root.destroy()
    import login  # Import and run the login script

# Function to open the calendar dialog
def open_calendar(event):
    global cal
    cal = Calendar(root, selectmode="day", year=2000, month=1, day=1, width=200, height=200)
    cal.grid(row=4, column=1, padx=10, pady=10, columnspan=2)
    cal.bind("<<CalendarSelected>>", lambda event: set_selected_date(cal.selection_get()))  # Bind double-click event to date selection

# Function to set the selected date in the dob_entry field
def set_selected_date(selected_date):
    global cal
    if selected_date:
        dob_entry.delete(0, tk.END)  # Clear existing entry
        dob_entry.insert(0, selected_date.strftime('%Y-%m-%d'))  # Set selected date
        cal.destroy()  # Destroy the calendar after selecting the date



# Create main window
root = tk.Tk()
root.title("Registration Panel")
root.geometry("600x450")



# Style
style = ttk.Style()
style.theme_use("clam")

# Colors
bg_color = "#f0f0f0"
text_color = "#333333"
button_bg_color = "#2196f3"  # Blue color for buttons

# Fonts
label_font = ("Times New Roman", 12)
entry_font = ("Times New Roman", 12)
button_font = ("Times New Roman", 12, "bold")

# Configure Style
style.configure("TLabel", background=bg_color, foreground=text_color, font=label_font)
style.configure("TEntry", fieldbackground=bg_color, font=entry_font)
style.configure("TButton", background=button_bg_color, foreground="white", font=button_font)

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

# Address Label and Entry
address_label = ttk.Label(root, text="Address:")
address_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
address_entry = ttk.Entry(root)
address_entry.grid(row=2, column=1, padx=10, pady=10)

# Date of Birth Label and Entry
dob_label = ttk.Label(root, text="Date of Birth:")
dob_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

dob_entry = ttk.Entry(root)
dob_entry.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

# Bind click event to open calendar
dob_entry.bind("<Button-1>", open_calendar)

# Gender Label and Combobox
gender_label = ttk.Label(root, text="Gender:")
gender_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
gender_combobox = ttk.Combobox(root, values=["Male", "Female", "Other"])
gender_combobox.grid(row=4, column=1, padx=10, pady=10)

# Register Button
register_button = ttk.Button(root, text="Register", command=generate_username_password)
register_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="we")

# Go back to Login Button
login_button = ttk.Button(root, text="Back to Login", command=go_back_to_login)
login_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="we")

root.mainloop()
