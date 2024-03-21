import tkinter as tk
import sqlite3

class AddProductWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Product")
        
        # Set initial window size
        self.root.geometry("400x300")
        
        # Add heading with background color
        self.heading_label = tk.Label(root, text="Add Product", font=("Arial", 18, "bold"), bg="lightblue", fg="blue")
        self.heading_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        # Add product details entry fields
        self.name_label = tk.Label(root, text="Product Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=5)
        
        self.price_label = tk.Label(root, text="Price:")
        self.price_label.pack(pady=5)
        self.price_entry = tk.Entry(root)
        self.price_entry.pack(pady=5)
        
        self.quantity_label = tk.Label(root, text="Quantity:")
        self.quantity_label.pack(pady=5)
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.pack(pady=5)
        
        # Add submit button
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_product)
        self.submit_button.pack(pady=10)

        # Add payment buttons
        self.esewa_button = tk.Button(root, text="Pay with Esewa", command=self.pay_with_esewa)
        self.esewa_button.pack(pady=5)

        self.khalti_button = tk.Button(root, text="Pay with Khalti", command=self.pay_with_khalti)
        self.khalti_button.pack(pady=5)
        
        # Connect to SQLite database file
        self.conn = sqlite3.connect("product_database.db")
        self.cur = self.conn.cursor()
        
        # Create product table if not exists
        self.cur.execute('''CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            price REAL NOT NULL,
                            quantity INTEGER NOT NULL
                            )''')
        self.conn.commit()

    def pay_with_esewa(self):
        # Implement Esewa payment functionality
        pass

    def pay_with_khalti(self):
        # Implement Khalti payment functionality
        pass
        
    def submit_product(self):
        # Functionality to submit the product details
        name = self.name_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())
        
        # Insert product details into the database
        self.cur.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
        self.conn.commit()
        
        # Print confirmation message
        print("Product added successfully.")
        
        # Close the window after submitting
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AddProductWindow(root)
    root.mainloop()
