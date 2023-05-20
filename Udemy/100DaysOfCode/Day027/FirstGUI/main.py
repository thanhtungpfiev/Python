import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
label.grid(row=0, column=0)
label.config(padx=20, pady=20)


def button_clicked():
    label.config(text=entry.get())


button1 = tkinter.Button(text='Button', command=button_clicked)
button1.grid(row=1, column=1)

entry = tkinter.Entry()
entry.grid(row=2, column=3)

button2 = tkinter.Button(text='New Button', command=button_clicked)
button2.grid(row=0, column=2)

window.mainloop()
