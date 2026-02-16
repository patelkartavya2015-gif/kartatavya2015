import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("700x600")
root.config(bg="lightblue")

# Load Image
#upload = Image.open("ioo .jpg")
#upload = upload.resize((400, 400))
#image = ImageTk.PhotoImage(upload)

#label = tk.Label(root, image=image, bg="lightblue")
#label.place(x=150, y=50)

label1 = tk.Label(root, text="Enter the amount you want to convert:",
                  font=("Arial", 14), bg="lightblue")
label1.place(x=150, y=470)


# ---------- Top Window ----------
def topwin():
    top = tk.Toplevel(root)
    top.title("Denomination Calculator")
    top.geometry("1000x1000")

    tk.Label(top, text="Enter Amount:", font=("Arial", 12)).pack(pady=10)
    entry = tk.Entry(top, font=("Arial", 12))
    entry.pack(pady=10)

    # Result Entries
    results = {}

    notes = [ 60000, 10000, 9000, 8000, 7000, 6000, 2000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 20, 10, 5, 2]

    for n in notes:
        frame = tk.Frame(top)
        frame.pack(pady=2)

        tk.Label(frame, text=f"{n} :", width=8, anchor="w",
                 font=("Arial", 12)).pack(side="left")

        e = tk.Entry(frame, width=10)
        e.pack(side="left")
        results[n] = e

    # ---------- Calculation Function ----------
    def calculate():
        try:
            amount = int(entry.get())

            for n in notes:
                count = amount // n
                amount %= n

                results[n].delete(0, tk.END)
                results[n].insert(0, str(count))

        except ValueError:
            messagebox.showerror("Error", "Enter valid number")

    tk.Button(top, text="Calculate", command=calculate,
              font=("Arial", 12), bg="lightblue").pack(pady=20)


# ---------- Start Button ----------
def msg():
    MsgBox = messagebox.askquestion(
        "Denomination Calculator",
        "Do you want to convert amount?"
    )
    if MsgBox == 'yes':
        topwin()


button1 = tk.Button(root, text="Let's get started!",
                    command=msg, font=("Arial", 12), bg="lightblue")
button1.place(x=250, y=520)

root.mainloop()
