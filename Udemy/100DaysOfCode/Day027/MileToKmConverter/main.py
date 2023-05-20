from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def mile_to_km_converter():
    miles = int(miles_field.get())
    print(miles)
    km = miles * 1.6
    print(km)
    km_value_label.config(text=str(km))


miles_field = Entry()
miles_field.insert(0, '0')
miles_field.grid(row=0, column=1)

is_equal_to_label = Label(text='is_equal_to')
is_equal_to_label.grid(row=1, column=0)
is_equal_to_label.config(padx=10, pady=10)

miles_label = Label(text='Miles')
miles_label.grid(row=0, column=2)
miles_label.config(padx=10, pady=10)

km_value_label = Label(text='0')
km_value_label.grid(row=1, column=1)

km_label = Label(text='Km')
km_label.grid(row=1, column=2)

calculate_button = Button(text='Calculate', command=mile_to_km_converter)
calculate_button.grid(row=2, column=1)

window.mainloop()
