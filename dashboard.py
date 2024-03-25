import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
from tkinter import ttk

def refresh_data():
    # Clear the treeview
    for row in treeview.get_children():
        treeview.delete(row)
    
    # Connect to the database
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # Retrieve all data from the users table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Insert data into the treeview
    for row in rows:
        treeview.insert('', 'end', values=row)

    # Close the database connection
    conn.close()

def delete_data():
    # Get the selected item from the treeview
    selected_item = treeview.selection()

    if not selected_item:
        messagebox.showerror("Error", "Please select a record to delete.")
        return

    # Retrieve the ID of the selected item
    item_id = treeview.item(selected_item)['values'][0]

    # Connect to the database
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # Delete the record with the corresponding ID
    cursor.execute("DELETE FROM users WHERE id=?", (item_id,))
    conn.commit()

    # Update IDs in the database to maintain continuity
    cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=SEQ-1 WHERE NAME='users' AND SEQ>?", (item_id,))
    conn.commit()

    # Close the database connection
    conn.close()

    # Refresh the data in the treeview
    refresh_data()

def search_data():
    # Get the search query from the entry widget
    query = search_entry.get()

    # Connect to the database
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # Execute a SQL query to search for the data
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + query + '%',))
    rows = cursor.fetchall()

    # Clear the treeview
    refresh_data()

    # Insert the search results into the treeview
    for row in rows:
        treeview.insert('', 'end', values=row)

    # Close the database connection
    conn.close()

def open_update_or_add_frame(is_update=True):
    # Get the selected item from the treeview if updating
    if is_update:
        selected_item = treeview.selection()

        if not selected_item:
            messagebox.showerror("Error", "Please select a record to update.")
            return

        # Retrieve the ID of the selected item
        item_id = treeview.item(selected_item)['values'][0]

    # Create a new window for updating or adding data
    update_window = tk.Toplevel(root)
    if is_update:
        update_window.title("Update Data")
    else:
        update_window.title("Add Data")

    # Create labels and entry fields for each data field
    tk.Label(update_window, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(update_window)
    name_entry.grid(row=0, column=1)

    tk.Label(update_window, text="Password:").grid(row=1, column=0)
    password_entry = tk.Entry(update_window)
    password_entry.grid(row=1, column=1)

    tk.Label(update_window, text="Date of Birth (DD/MM/YYYY):").grid(row=2, column=0)
    dob_entry = tk.Entry(update_window)
    dob_entry.grid(row=2, column=1)

    tk.Label(update_window, text="Address:").grid(row=3, column=0)
    address_entry = tk.Entry(update_window)
    address_entry.grid(row=3, column=1)

    # Function to update or add the data to the database
    def update_or_add_data():
        name = name_entry.get()
        password = password_entry.get()
        dob = dob_entry.get()
        address = address_entry.get()

        # Connect to the database
        conn = sqlite3.connect("user_data.db")
        cursor = conn.cursor()

        if is_update:
            # Update the record with the new data
            cursor.execute("UPDATE users SET name=?, password=?, dob=?, address=? WHERE id=?",
                           (name, password, dob, address, item_id))
        else:
            # Insert the new record into the database
            cursor.execute("INSERT INTO users (name, password, dob, address) VALUES (?, ?, ?, ?)",
                           (name, password, dob, address))

        conn.commit()
        conn.close()

        # Close the window after updating or adding data
        update_window.destroy()

        # Refresh the data in the treeview
        refresh_data()

    # Button to update or add the data
    if is_update:
        button_text = "Update Data"
    else:
        button_text = "Add Data"
    update_button = tk.Button(update_window, text=button_text, command=update_or_add_data)
    update_button.grid(row=4, columnspan=2, pady=10)

# Create the main window
root = tk.Tk()
root.title("Dashboard")
root.geometry("800x400")

# Create a frame for the treeview
frame_treeview = tk.Frame(root)
frame_treeview.pack(pady=20)


# Create a treeview widget
treeview = ttk.Treeview(frame_treeview, columns=('ID', 'Name', 'Password', 'Date of Birth', 'Address'), show='headings')
treeview.heading('ID', text='ID')
treeview.heading('Name', text='Name')
treeview.heading('Password', text='Password')
treeview.heading('Date of Birth', text='Date of Birth')
treeview.heading('Address', text='Address')
treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar for the treeview
scrollbar = tk.Scrollbar(frame_treeview, orient=tk.VERTICAL, command=treeview.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
treeview.configure(yscrollcommand=scrollbar.set)

# Retrieve and display data initially
refresh_data()

# Create buttons for actions
frame_buttons = tk.Frame(root)
frame_buttons.pack()

btn_delete = tk.Button(frame_buttons, text="Delete Data", command=delete_data)
btn_delete.grid(row=0, column=0, padx=10)

btn_update = tk.Button(frame_buttons, text="Update Data", command=lambda: open_update_or_add_frame(True))
btn_update.grid(row=0, column=1, padx=10)

btn_add = tk.Button(frame_buttons, text="Add Data", command=lambda: open_update_or_add_frame(False))
btn_add.grid(row=0, column=2, padx=10)

# Start the Tkinter event loop
root.mainloop()