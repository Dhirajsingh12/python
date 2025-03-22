import tkinter as tk
from tkinter import messagebox

def buy_now():
    messagebox.showinfo("Purchase", "Thank you for your purchase!")


root = tk.Tk()
root.title("Welcome to Bolt E-Commerce")
root.geometry("600x400")
root.configure(bg="#f5f5f5")


header = tk.Label(root, text="Bolt - The Future of Shopping", font=("Arial", 20, "bold"), bg="#4CAF50", fg="white", pady=10)
header.pack(fill="x")


product_frame = tk.Frame(root, bg="white", bd=2, relief="groove", padx=10, pady=10)
product_frame.place(x=50, y=80, width=500, height=200)


product_name = tk.Label(product_frame, text="⚡ Bolt Smart Watch", font=("Arial", 16, "bold"), bg="white")
product_name.pack(anchor="w", pady=(0, 5))

product_desc = tk.Label(product_frame, text="Track your fitness, calls, and more with our all-in-one smart watch.", font=("Arial", 12), bg="white", wraplength=480, justify="left")
product_desc.pack(anchor="w")


product_price = tk.Label(product_frame, text="Price: ₹2499", font=("Arial", 14, "bold"), fg="green", bg="white")
product_price.pack(anchor="w", pady=(5, 10))

buy_button = tk.Button(root, text="Buy Now", font=("Arial", 14), bg="#FF5733", fg="white", command=buy_now)
buy_button.place(x=250, y=300, width=100, height=40)


root.mainloop()
