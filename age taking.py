import tkinter as tk
from tkinter import RAISED, GROOVE
from datetime import date
import calendar
from tkinter import messagebox

root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x400")
root.config(bg="#000000")

frame1 = tk.Frame(master=root, bg="#000000", relief=RAISED, borderwidth=5)
frame1.pack(pady=20)

# ----------- LABELS ----------- #
tk.Label(frame1, text="Name:", bg="#000000", fg="white", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
tk.Label(frame1, text="Date:", bg="#000000", fg="white", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
tk.Label(frame1, text="Month:", bg="#000000", fg="white", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
tk.Label(frame1, text="Year:", bg="#000000", fg="white", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10)

# ----------- ENTRIES ----------- #
name_entry = tk.Entry(frame1, font=("Arial", 14), relief=GROOVE, borderwidth=8)
day_entry = tk.Entry(frame1, font=("Arial", 14), relief=GROOVE, borderwidth=8)
month_entry = tk.Entry(frame1, font=("Arial", 14), relief=GROOVE, borderwidth=8)
year_entry = tk.Entry(frame1, font=("Arial", 14), relief=GROOVE, borderwidth=8)

name_entry.grid(row=0, column=1, padx=10, pady=10)
day_entry.grid(row=1, column=1, padx=10, pady=10)
month_entry.grid(row=2, column=1, padx=10, pady=10)
year_entry.grid(row=3, column=1, padx=10, pady=10)

def calculate_age():
    try:
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        birth_date = date(year, month, day)
        today = date.today()
        age_years = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age_years -= 1
        tk.Label(frame1, text=f"Age of {name}: {age_years} years", bg="#000000", fg="white", font=("Arial", 12)).grid(row=4, column=0, columnspan=2, pady=10)
    except (ValueError, SyntaxError, calendar.IllegalMonthError):
        messagebox.showerror("Error", "Please enter valid date values or our system is not working properly.")
calculate_button = tk.Button(frame1, text="Calculate Age", command=calculate_age, font=("Arial", 12), relief=RAISED, borderwidth=5)
calculate_button.grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()
