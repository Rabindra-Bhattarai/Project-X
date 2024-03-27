import tkinter as tk
from PIL import Image, ImageTk

def display_license_info():
    # Function to display detailed license information
    pass

def search_license():
    # Function to search for specific license information
    pass

# Create main window
root = tk.Tk()
root.title("Nepal License Written Website")
root.geometry("650x400")

# Load and display background image
bg_image = Image.open("Welcome.png")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Increase font size
font_size = 14

# Add navigation options
navigation_frame = tk.Frame(root)
navigation_frame.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# Add buttons for different license categories with larger font
btn_car_license = tk.Button(navigation_frame, text="Car License", command=display_license_info, font=("Helvetica", font_size))
btn_car_license.pack(side=tk.LEFT, padx=10)
btn_bike_registration = tk.Button(navigation_frame, text="Bike Licence", command=display_license_info, font=("Helvetica", font_size))
btn_bike_registration.pack(side=tk.LEFT, padx=10)
btn_scooter_license = tk.Button(navigation_frame, text="Scooter License", command=display_license_info, font=("Helvetica", font_size))
btn_scooter_license.pack(side=tk.LEFT, padx=10)


root.mainloop()
