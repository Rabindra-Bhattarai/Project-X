import tkinter as tk
import os

class BrandRawAdminHub:
    def __init__(self, root):
        self.root = root
        self.root.title("BrandRaw Admin Hub")
        
        # Set initial window size
        self.root.geometry("800x600")
        
        # Add heading with background color
        self.heading_label = tk.Label(root, text="Welcome to BrandRaw Admin Hub", font=("Arial", 18, "bold"), bg="lightblue", fg="blue")
        self.heading_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        # Create user details frame
        self.user_frame = tk.Frame(root, width=200, height=100)
        self.user_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        # Load and display user picture
        self.user_image = tk.PhotoImage(file="c.png")
        self.canvas = tk.Canvas(self.user_frame, width=80, height=80, bg="white", bd=0, highlightthickness=0)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.user_image)
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Add user name label
        self.user_name_label = tk.Label(self.user_frame, text="Rabindra Bhattarai", font=("Arial", 12), cursor="hand2")
        self.user_name_label.pack(side=tk.LEFT, padx=10, pady=5)
        self.user_name_label.bind("<Button-1>", self.open_profile)  # Bind click event
        
        # Create a frame for buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        # Add buttons
        self.add_product_button = tk.Button(self.button_frame, text="Add Product", command=self.add_product)
        self.add_product_button.pack(pady=10, padx=20, fill=tk.X)
        
        
        self.manage_orders_button = tk.Button(self.button_frame, text="Manage Orders", command=self.manage_orders)
        self.manage_orders_button.pack(pady=10, padx=20, fill=tk.X)
        
        self.view_sales_button = tk.Button(self.button_frame, text="View Sales", command=self.view_sales)
        self.view_sales_button.pack(pady=10, padx=20, fill=tk.X)
        
        # Add logout button
        self.logout_button = tk.Button(self.button_frame, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10, padx=20, fill=tk.X)
        
        # Add dark mode and light mode button
        self.mode_button = tk.Button(self.button_frame, text="Dark Mode", command=self.toggle_mode)
        self.mode_button.pack(pady=10, padx=20, fill=tk.X)
        self.dark_mode = False
        
    def add_product(self):
        # Functionality to add a product
        self.root.destroy()  # Close the current window
        os.system("python add_product.py")  # Open the add_product.py file
    
    def manage_orders(self):
        # Functionality to manage orders
        pass
    
    def view_sales(self):
        # Functionality to view sales statistics
        pass
    
    def logout(self):
        # Destroy the window when logout button is clicked
        self.root.destroy()
        
    def open_profile(self, event):
        # Functionality to open user profile
        # You can open another frame or window here
        pass
    
    def toggle_mode(self):
        # Toggle between dark mode and light mode
        if self.dark_mode:
            self.root.config(bg="white")
            self.heading_label.config(bg="lightblue", fg="blue")
            self.user_frame.config(bg="white")
            self.button_frame.config(bg="white")
            self.mode_button.config(text="Dark Mode")
            self.dark_mode = False
        else:
            self.root.config(bg="black")
            self.heading_label.config(bg="darkblue", fg="white")
            self.user_frame.config(bg="black")
            self.button_frame.config(bg="black")
            self.mode_button.config(text="Light Mode")
            self.dark_mode = True

if __name__ == "__main__":
    root = tk.Tk()
    app = BrandRawAdminHub(root)
    root.mainloop()
