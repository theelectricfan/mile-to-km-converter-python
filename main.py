import tkinter

window = tkinter.Tk()
window.title("Miles to km converter")
window.config(padx=20, pady=20)

input_miles = tkinter.Entry(width=10, justify="center")
input_miles.grid(column=0, row=0, ipadx=5, ipady=5, padx=5, pady=5)

label_miles = tkinter.Label(text="miles")
label_miles.grid(column=1, row=0, ipadx=5, ipady=5, padx=5, pady=5)

label_equal = tkinter.Label(text="is equal to")
label_equal.grid(column=0, row=1, columnspan=2, ipadx=5, ipady=5, padx=5, pady=5)

label_km_number = tkinter.Label(text="__________")
label_km_number.grid(column=0, row=2, ipadx=5, ipady=5, padx=5, pady=5)

label_km = tkinter.Label(text="km")
label_km.grid(column=1, row=2, ipadx=5, ipady=5, padx=5, pady=5)

def calculate():
    miles = float(input_miles.get())
    km = miles * 1.609
    label_km_number.config(text=km)

calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(column=0, row=3, columnspan=2, ipadx=5, ipady=5, padx=5, pady=5)


window.mainloop()
