import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Length")

label1 = tk.Label(root, text="This converts a length in to another for mat of length")

# example:      meter | down aroow
#                   down aroow
#                centimeter | down arow
#         label = root.Label("ans is ____m/km/hm/dam/m/dm/cm/mm")
Lengths = ["meter", "kilometer", "hectometer", "decameter", "decimeter", "centimeter", "millimeter"]
var1 = tk.StringVar(root)
var1.set(Lengths[0])
option1 = tk.OptionMenu(root, var1, *Lengths)
var2 = tk.StringVar(root)
var2.set(Lengths[0])
option2 = tk.OptionMenu(root, var2, *Lengths)
entry = tk.Entry(root)
button = tk.Button(root, text="Convert")
label1.pack()
option1.pack()
option2.pack()
entry.pack()
button.pack()
root.mainloop()
