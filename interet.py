import tkinter as tk

def calculate_intrest():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    intrest = (p * r * t) / 100
    result_label.config(text=f"Intrest: {intrest:.2f}")

root = tk.Tk()
root.title("Intrest Calculator")    
root.geometry("300x200")
principal_label = tk.Label(root, text="Principal:")
principal_label.pack()
principal_entry = tk.Entry(root)
principal_entry.pack()
rate_label = tk.Label(root, text="Rate of Intrest:")
rate_label.pack()
rate_entry = tk.Entry(root)
rate_entry.pack()
time_label = tk.Label(root, text="Time (years):")
time_label.pack()
time_entry = tk.Entry(root)
time_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_intrest)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
