from tkinter import *

window = Tk()
window.title("Kilometres to Miles")
# window.minsize(width=100, height=100)
window.config(padx=20,pady=20)


is_eq_label = Label(text="is equal to")
is_eq_label.grid(column=0, row=1)

km_distance = Entry(width=20)
km_distance.grid(column=1, row=0)

mile_distance_label = Label(text="0")
mile_distance_label.grid(column=1, row=1)

def calculate():
    kms = km_distance.get()
    miles = float(kms) / 1.609
    mile_distance_label.config(text = str(miles))

calculate_btn = Button(text="Calculate",command=calculate)
calculate_btn.grid(column=1,row=2)

km = Label(text="Km")
km.grid(column=2, row=0)

miles = Label(text = "Miles")
miles.grid(column=2, row=1)

window.mainloop()