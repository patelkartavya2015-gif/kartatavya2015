import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")

        self.menu = {
            "Fries": 2,
            "Burger": 5,
            "Pizza": 4,
            "Coke": 1,
            "Salad": 4,
            "Pasta": 2.5,
            "Ice Cream": 3
        }

        self.exchange = 82

        self.setup_background(root)

        frame = tk.Frame(root, bg="lightblue")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(frame, text="Restaurant Order Management",
                  font=("Arial", 20)).grid(row=0, column=0, columnspan=2, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu.items(), start=1):
            label = ttk.Label(frame, text=f"{item} (${price})",
                              font=("Arial", 14))
            label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)

            self.menu_quantities[item] = quantity_entry

        self.currency_var = tk.StringVar()

        ttk.Label(frame, text="Select Currency:",
                  font=("Arial", 14)).grid(row=len(self.menu)+1, column=0,
                                           padx=10, pady=10, sticky=tk.W)

        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            values=["USD", "INR"],
            state="readonly"
        )
        currency_dropdown.grid(row=len(self.menu)+1, column=1, padx=10, pady=10)
        currency_dropdown.current(0)

        self.currency_var.trace_add("write", self.update_prices)

        order_button = ttk.Button(frame, text="Place Order",
                                  command=self.place_order)
        order_button.grid(row=len(self.menu)+2, column=0,
                          columnspan=2, pady=20)

    def setup_background(self, root):
        bg_width, bg_height = 800, 600

        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack()

        try:
            original_bg = tk.PhotoImage(file="download.jpg")
            background = original_bg.subsample(
                max(1, original_bg.width() // bg_width),
                max(1, original_bg.height() // bg_height)
            )
            canvas.create_image(0, 0, anchor=tk.NW, image=background)
            canvas.image = background
        except:
            pass  # If image not found, app still works

    def update_prices(self, *args):
        if self.currency_var.get() == "USD":
            for item, price in self.menu.items():
                self.menu_labels[item].config(text=f"{item} (${price})")
        else:
            for item, price in self.menu.items():
                converted = round(price * self.exchange, 2)
                self.menu_labels[item].config(text=f"{item} (₹{converted})")

    def place_order(self):
        totalcost = 0
        order_summary = "Order Summary:\n"

        currency = self.currency_var.get()
        symbol = "$" if currency == "USD" else "₹"
        rate = self.exchange if currency == "INR" else 1

        for item, entry in self.menu_quantities.items():
            quantity = entry.get()

            if quantity.isdigit() and int(quantity) > 0:
                qty = int(quantity)
                price = self.menu[item] * qty * rate
                totalcost += price

                order_summary += f"{item} x {qty} = {symbol}{round(price,2)}\n"

        if totalcost > 0:
            order_summary += f"\nTotal Cost: {symbol}{round(totalcost,2)}"
            messagebox.showinfo("Order Summary", order_summary)
        else:
            messagebox.showwarning("No Items",
                                   "Please enter quantity for at least one item.")


if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantManagement(root)
    root.mainloop()