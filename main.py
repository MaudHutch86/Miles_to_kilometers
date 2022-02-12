from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)


def conversion():
    new_text = float(input.get())
    km = new_text * 1.609
    result_label.config(text=f"{km}")


input = Entry(width=7)
input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=conversion)
button.grid(column=1, row=2)

window.mainloop()
