import sqlite3
from database import create_database, insert_user, get_all_users, update_user, delete_user

# Function to create the SQLite database and table
def create_database():
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       password TEXT,
                       dob TEXT,
                       address TEXT)''')
    conn.commit()
    conn.close()

# Function to insert a new user into the database
def insert_user(name, password, dob, address):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, password, dob, address) VALUES (?, ?, ?, ?)", (name, password, dob, address))
    conn.commit()
    conn.close()

# Function to retrieve all users from the database
def get_all_users():
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

# Function to update user information in the database
def update_user(user_id, name, password, dob, address):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=?, password=?, dob=?, address=? WHERE id=?", (name, password, dob, address, user_id))
    conn.commit()
    conn.close()

# Function to delete a user from the database
def delete_user(user_id):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()

# Example usage:
if __name__ == "__main__":
    # Create the database and table if they don't exist
    create_database()
    
    # Insert a new user
    insert_user("John Doe", "password123", "1990-01-01", "123 Main St")
    
    # Retrieve all users
    users = get_all_users()
    print("All users:", users)
    
    # Update user information
    update_user(1, "John Smith", "newpassword", "1990-01-01", "456 Elm St")
    
    # Retrieve all users after update
    users = get_all_users()
    print("All users after update:", users)
    
    # Delete a user
    delete_user(1)
    
    # Retrieve all users after deletion
    users = get_all_users()
    print("All users after deletion:", users)
