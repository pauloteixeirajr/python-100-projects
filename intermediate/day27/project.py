from tkinter import ttk, Tk

FONT = ("Arial", 18)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=15, pady=15, background="#ececec")

entry = ttk.Entry(width=10)
entry.grid(row=0, column=1)

miles_lbl = ttk.Label(text="Miles", font=FONT)
miles_lbl.grid(row=0, column=2)

is_equal_lbl = ttk.Label(text="is equal to", font=FONT)
is_equal_lbl.grid(row=1, column=0)

km_val_lbl = ttk.Label(text="0", font=FONT)
km_val_lbl.grid(row=1, column=1)

km_lbl = ttk.Label(text="Km", font=FONT)
km_lbl.grid(row=1, column=2)


def calculate_km():
    miles = float(entry.get())
    km = round(miles * 1.609, 2)
    km_val_lbl.config(text=km)


button = ttk.Button(text="Calculate", command=calculate_km)
button.grid(row=2, column=1)

window.mainloop()
