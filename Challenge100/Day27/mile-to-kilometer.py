from tkinter import *


def mile_to_km():
    miles = float(entry_1.get())
    km = round(miles * 1.609,2)
    label_4.config(text =f"{km}")

window = Tk()
window.title("Mile To Kilometer Changer")
window.minsize(width = 200,height=200)
window.config(padx=100, pady=100)

label_1 = Label(text="is equal to",font=("Arial", 12, "bold"))
label_1.grid(column=0,row=1)
label_1.config(padx=10, pady=10)

label_2 = Label(text="Km",font=("Arial", 12, "bold"))
label_2.grid(column=3,row=1)
label_2.config(padx=10, pady=10)

label_3 = Label(text="Mile",font=("Arial", 12, "bold"))
label_3.grid(column=3,row=0)
label_3.config(padx=10, pady=10)

label_4 = Label(text = "0",font=("Arial", 12, "bold"))
label_4.grid(column=2,row=1)
label_4.config(padx=10, pady=10)



button_1 = Button(text="Calculate",command=mile_to_km)
button_1.grid(column=2,row=3)


entry_1 = Entry(width = 15)
entry_1.grid(column=2,row=0)





window.mainloop()