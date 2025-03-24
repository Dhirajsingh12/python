import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO


def buy_now():
    messagebox.showinfo("Purchase", "Thank you for your purchase!")


root = tk.Tk()
root.title("Welcome to Bolt E-Commerce")
root.geometry("600x400")
root.configure(bg="#f5f5f5")


# Header
header = tk.Label(root, text="Bolt - The Future of Shopping", font=("Arial", 20, "bold"), bg="#4CAF50", fg="white", pady=10)
header.pack(fill="x")


# Product Frame
product_frame = tk.Frame(root, bg="white", bd=2, relief="groove", padx=10, pady=10)
product_frame.place(x=50, y=80, width=500, height=250)


# Product Name
product_name = tk.Label(product_frame, text="⚡ Bolt Smart Watch", font=("Arial", 16, "bold"), bg="white")
product_name.pack(anchor="w", pady=(0, 5))


# Product Description
product_desc = tk.Label(product_frame, text="Track your fitness, calls, and more with our all-in-one smart watch.", 
                        font=("Arial", 12), bg="yellow", wraplength=480, justify="left")
product_desc.pack(anchor="w", pady=(0, 5))


# Load Watch Image from URL or Local File
try:
    url = "https://cdn.jiostore.online/v2/jmd-asp/jdprod/wrkr/products/pictures/item/free/resize-w:450/dYZQUqOGRO-fire-boltt-call-smart-watch-image-492849708-i-1-1200wx1200h.jpeg"
    response = requests.get(url)
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
    else:
        raise Exception("Failed to load image from URL")
except Exception as e:
    print(f"Error loading image from URL: {e}")
    # Fallback to local image if URL fails
    img = Image.open("bolt_watch.jpg")  # Make sure to place the image in the same directory

# Resize Image
img = img.resize((150, 150), Image.Resampling.LANCZOS)

# Store Image Globally to Prevent Garbage Collection
product_img = ImageTk.PhotoImage(img)

# Show Image in Label
img_label = tk.Label(product_frame, image=product_img, bg="white")
img_label.pack(anchor="w", pady=(0, 10))


# Product Price
product_price = tk.Label(product_frame, text="Price: ₹2499", font=("Arial", 14, "bold"), fg="green", bg="white")
product_price.pack(anchor="w", pady=(5, 10))


# Buy Button
buy_button = tk.Button(root, text="Buy Now", font=("Arial", 14), bg="#FF5733", fg="white", command=buy_now)
buy_button.place(x=250, y=350, width=100, height=40)


root.mainloop()
