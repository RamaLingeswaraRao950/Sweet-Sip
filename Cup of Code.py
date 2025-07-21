import tkinter as tk
from tkinter import messagebox


class Chai:
    def __init__(self, size, sweetness, milk_level, owner="Guest"):
        self.size = size
        self.sweetness = sweetness
        self.milk_level = milk_level
        self.owner = owner

    def add_sugar(self, amount):
        self.sweetness += amount
        return f"➕ Added {amount} sugar. New Sweetness: {self.sweetness}/5"

    def sip(self):
        return "😋 Sipping chai... So soothing!"

    def rate_experience(self, rating):
        if 1 <= rating <= 5:
            return f"⭐ You rated this chai: {rating}/5. Thank you, {self.owner}!"
        return "❌ Rating must be between 1 and 5."


# 🫖 Price logic
price_chart = {"small": 10, "medium": 15, "large": 20}
emoji_map = {"small": "🧉", "medium": "🥤", "large": "🍵"}


def make_chai():
    try:
        size = size_var.get()
        sweetness = int(entry_sweetness.get())
        milk = int(entry_milk.get())
        name = entry_name.get() or "Guest"

        if size not in price_chart:
            messagebox.showerror("Input Error", "Please select a cup size.")
            return

        global chai
        chai = Chai(size, sweetness, milk, name)
        result_var.set(
            f"{emoji_map[size]} {size.capitalize()} Chai for {name}\nSweetness: {sweetness}/5, Milk: {milk}/5\nPrice: ₹{price_chart[size]}"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


def add_sugar():
    try:
        amount = int(entry_sugar.get())
        result_var.set(chai.add_sugar(amount))
    except:
        messagebox.showerror("Input Error", "Enter valid sugar amount.")


def sip_chai():
    if chai:
        result_var.set(chai.sip())


def rate_chai():
    try:
        rating = int(entry_rating.get())
        result_var.set(chai.rate_experience(rating))
    except:
        messagebox.showerror(
            "Input Error", "Rating must be a number from 1 to 5.")


# 🎨 GUI Layout
root = tk.Tk()
root.title("☕ Sweet Sip : Ultimate Chai Customizer")
root.geometry("400x600")
root.configure(bg="#fff8f0")

chai = None
result_var = tk.StringVar()

tk.Label(root, text="🫖 Welcome to Sweet Sip", font=(
    "Arial", 16, "bold"), fg="#8b4513", bg="#fff8f0").pack(pady=10)

# Name
tk.Label(root, text="Your Name:", bg="#fff8f0").pack()
entry_name = tk.Entry(root)
entry_name.pack()

# Cup Size
tk.Label(root, text="Choose Cup Size:", bg="#fff8f0", pady=5).pack()
size_var = tk.StringVar()
for size in ("small", "medium", "large"):
    tk.Radiobutton(root, text=f"{emoji_map[size]} {size.capitalize()}",
                   variable=size_var, value=size, bg="#fff8f0").pack(anchor="w", padx=30)

# Sweetness
tk.Label(root, text="Sweetness Level (0–5):", bg="#fff8f0").pack()
entry_sweetness = tk.Entry(root)
entry_sweetness.pack()

# Milk Level
tk.Label(root, text="Milk Level (0–5):", bg="#fff8f0").pack()
entry_milk = tk.Entry(root)
entry_milk.pack()

# Make Chai Button
tk.Button(root, text="🍵 Make Chai", command=make_chai,
          bg="#d2691e", fg="white").pack(pady=10)

# Add Sugar
tk.Label(root, text="Add Sugar (scoops):", bg="#fff8f0").pack()
entry_sugar = tk.Entry(root)
entry_sugar.pack()
tk.Button(root, text="➕ Add Sugar", command=add_sugar).pack(pady=5)

# Sip
tk.Button(root, text="😋 Sip Chai", command=sip_chai).pack(pady=5)

# Rating
tk.Label(root, text="Rate Your Chai (1–5):", bg="#fff8f0").pack()
entry_rating = tk.Entry(root)
entry_rating.pack()
tk.Button(root, text="⭐ Rate Chai", command=rate_chai).pack(pady=5)

# Output
tk.Label(root, textvariable=result_var, wraplength=350,
         fg="green", bg="#fff8f0", pady=10).pack()

root.mainloop()
