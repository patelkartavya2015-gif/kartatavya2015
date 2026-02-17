import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x300")
root.title("Password checker")

label1 = tk.Label(root, text="Enter your password here")
label1.grid(column=0, row=1)

paas = tk.Entry(root, show="*")
paas.grid(column=0, row=4)

result_btn = tk.Button(root, text="", relief="groove", width=20)
result_btn.grid(column=0, row=6)

def check():
    password = paas.get()
    length = len(password)

    if length < 5:
        result_btn.config(bg="#FF0000", text="Very Weak")
        messagebox.showwarning("Alert", "Password is too weak!")

    elif 5 <= length < 8:
        result_btn.config(bg="#ED6363", text="Weak")
        messagebox.showwarning("Warning", "Try not to use this password")

    elif 8 <= length < 12:
        result_btn.config(bg="#FFD700", text="Medium")
        messagebox.showinfo("Info", "Decent password")

    else:
        result_btn.config(bg="#11FF00", text="Strong")
        messagebox.showinfo("Success", "Amazing password!")

button2 = tk.Button(root, text="Check", command=check)
button2.grid(column=0, row=9)

root.mainloop()
