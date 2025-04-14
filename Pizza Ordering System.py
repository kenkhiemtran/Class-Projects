#PROJECT 3

from tkinter import *
from tkinter import messagebox, ttk

window = Tk()
window.geometry("500x600")
window.title("Pizza Order Form")

pizzariaImage = PhotoImage (file='Pizzaria2.png')
imgLabel = Label ( window, image = pizzariaImage )
imgLabel.grid( row=0, column=0, columnspan=3)

nameLabel = Label(window,
                  text='Customer Name:',
                  font=('Arial', 15))
nameLabel.grid(row=1, column=0, sticky=E, pady=(20,20))
userName = Entry(window)
userName.grid(row=1, column=1, columnspan = 2, sticky=W)


size = StringVar() # Used by Radio buttons 


smallRadio =      Radiobutton(window,
                           text="Small",
                           variable=size,
                           value="Small",
                           font=('Arial', 15))


mediumRadio =       Radiobutton(window,
                          text="Medium",
                          variable=size,
                          value="Medium",
                          font=('Arial', 15))


largeRadio =    Radiobutton(window,
                         text="Large",
                         variable=size,
                         value="Large",
                         font=('Arial', 15))

smallRadio.select()#SETS DEFAULT
smallRadio.grid(row=2, column=0, sticky=W)
mediumRadio.grid(row=2, column=1, sticky=W)
largeRadio.grid(row=2, column=2, sticky=W)


toppingsLabel = Label(window, text ="TOPPINGS", font=('Arial', 15))
toppingsLabel.grid(row=4, column=0, columnspan = 2, sticky=W,pady=10)

pp = IntVar()
ol = IntVar()
pin = IntVar()
ss = IntVar()
on = IntVar()
bp = IntVar()

pepperoni = Checkbutton(window,
                         text="Pepperoni",
                         variable=pp,
                         onvalue =1,
                         offvalue=0,
                         padx=30,
                         font=('Arial', 14))


olives = Checkbutton(window,
                         text="Olives",
                         variable=ol,
                         onvalue =1,
                         offvalue=0,
                         padx=30,
                        font=('Arial', 14))



pineapple = Checkbutton(window,
                         text="Pineapple ",
                         variable=pin,
                         onvalue =1,
                         offvalue=0,
                         padx=30,
                      font=('Arial', 14))


sausage = Checkbutton(window,
                         text="Sausage",
                         variable=ss,
                         onvalue =1,
                         offvalue=0,
                         padx=30,
                      font=('Arial', 14))

onions = Checkbutton(window,
                         text="Onions",
                         variable=on,
                         onvalue =1,
                         offvalue=0,
                         padx=30,
                      font=('Arial', 14))


bellpepper = Checkbutton(window,
                         text="Bell Pepper",
                         variable=bp,
                         onvalue =1,
                         offvalue=0,
                         padx=30,
                      font=('Arial', 14))

pepperoni.grid(row=5, column=0, sticky=W)
olives.grid(row=6, column=0, sticky=W)
pineapple.grid(row=7, column=0, sticky=W)
sausage.grid(row=5, column=1, sticky=W)
onions.grid(row=6, column=1, sticky=W)
bellpepper.grid(row=7, column=1, sticky=W)

paymentLabel = Label(window, text ="PAYMENT", font=('Arial', 15))
paymentLabel.grid(row=9, column=0,sticky=E,pady=20)

def selection_changed(event):
    selection = payment.get()   # gets the selected item from combo 

payment = ttk.Combobox( values=["Visa", "Cash", "Venmo", "Zelle"]   )   # Declare a Combobox
payment.bind("<<ComboboxSelected>>",  selection_changed)

payment.grid(row=9, column=1,sticky=W,padx=20)  # Position the Combobox in the Window

  






def resetFields():
    userName.delete(0,END)
    pepperoni.deselect()
    olives.deselect()
    pineapple.deselect()
    sausage.deselect()
    onions.deselect()
    bellpepper.deselect()
    largeRadio.select() #SETS DEFAULT Radiobutton
    payment.set("Visa")

def writeToFile():
    if not userName.get().strip():
        messagebox.showerror("Error", "Customer name cannot be empty.")
        return
    log = open("order.txt", 'a')
    log.write('Name: %s\n' % userName.get())
    log.write(f'Size: {size.get()}\n')

    if pp.get(): log.write("      Pepperoni\n")
    if ol.get(): log.write("      Olives\n")
    if pin.get():log.write("      Pineapple\n")
    if ss.get(): log.write("      Sausage\n")
    if on.get(): log.write("      Onions\n")
    if bp.get(): log.write("      Bell Pepper\n")
    
    log.write(f'Card: {payment.get()}\n')
    from datetime import datetime
    timestamp = datetime.now().strftime('%m/%d/%Y %I:%M %p')
    log.write(f'Time: {timestamp}\n')
    log.write("===================================================\n")
    log.close()

    messagebox.showinfo( title="Order Summary",   
                         message=f"Order Has Been Processed" )
    resetFields()

clear  = Button(window,
               text='Clear',
               command=resetFields,
               font=('Arial', 16))
resetFields()
submit = Button(window,
               text='Submit',
               command=writeToFile,
               font=('Arial', 16))

clear.grid(row=10, column=0, sticky=E)
submit.grid(row=10, column=2, sticky=W)


window.mainloop()
