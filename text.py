import tkinter as tk
from datetime import date

root = tk.Tk()
root.geometry("300x200")
root.title("Date Display")
root.resizable(True, True)

lab1 = tk.Label(root, text="Hey There!", font=("Arial", 16), bg="#0800FF")

namelbl = tk.Label(root, text="Please Enter Your Name:", font=("Arial", 12))

name_entry = tk.Entry(root, font=("Arial", 12))

textbox = tk.Text(root, font=("Arial", 12), height=5, width=30)

def display():
    name = name_entry.get()
    global message
    message = "Welcome to the application.\nToday's date is:"

    greet = "Hello " + name + "!\n"

    textbox.insert(tk.END, greet)
    textbox.insert(tk.END, "\n" + message)
    textbox.insert(tk.END, "\n" + str(date.today()))

btn = tk.Button(root, text="Submit", font=("Arial", 12), bg="DarkBlue", fg ="White", command=lambda: display())

lab1.pack(pady=10)
namelbl.pack()
name_entry.pack(pady=5)
btn.pack(pady=10)
textbox.pack(pady=10)

root.mainloop()