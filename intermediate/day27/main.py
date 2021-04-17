from tkinter import ttk, Tk

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Components
# Label
my_label = ttk.Label(text="I Am a Label", font=("Arial", 24))
my_label.pack()


# Buttons
def button_clicked(): my_label.config(text=entry.get())


button = ttk.Button(text="Click me", command=button_clicked)
button.pack()

# Entry
entry = ttk.Entry(width=10)
entry.pack()

window.mainloop()
