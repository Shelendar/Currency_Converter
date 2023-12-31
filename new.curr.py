from forex_python.converter import CurrencyRates 
from tkinter import *                                                         
import tkinter.messagebox                                                     


root=Tk()                                                                     

root.title("CURRENCY CONVERTER")
root.geometry("500x500") 

a1= StringVar(root)
a2=StringVar(root)

a1.set("select")
a2.set("select")

def RealTimeCurrencyConversion():
    c=CurrencyRates()

    from_currency=a1.get()
    to_currency=a2.get()

    if (value.get()==""):
        tkinter.messagebox.showerror("Error", "Amount not entered .\n please enter a valid number")

    elif (from_currency=="select" or to_currency=="select"):
        tkinter.messagebox.showerror("Error","Currency not selected.\n please select currency")

    else:
        new_amt= c.convert(from_currency,to_currency,float(value.get()))
        new_amount=float("{:4f}".format(new_amt))
        output.insert(0,str(new_amount))

def clear():
    value.delete(0,END)
    output.delete(0,END)
    a1.set("select")
    a2.set("select")


CurrencyCode_list = ["INR","USD","KWD","BHD","OMR","KYD","EUR","CHF","JOD","GBP","BSD"]

                                                                                           
label1=Label(root,font=('helvertica',15, 'bold'), text="Amount:", fg='black')                   
label1.place(x=20, y=30)                                                                        

label2=Label(root, font=('helvertica', 15,'bold'), text="From :", fg='black')
label2.place(x=20, y=120)

label3=Label(root,font=('helvertica', 15, 'bold'), text="To :", fg='black')
label3.place(x=20,y=160)

label4=Label(root, font=('helvertica', 15, 'bold'), text="ConvertedAmount:", fg="black")
label4.place(x=20, y=280)


FromCurrency_option = OptionMenu(root, a1 , *CurrencyCode_list)
ToCurrency_option = OptionMenu(root, a2, *CurrencyCode_list)

FromCurrency_option.place(x=100, y=120)
ToCurrency_option.place(x=100, y=160)

value=Entry(root)
value.place(x=150, y=35) 

output=Entry(root)
output.place(x=200,y=300)

convert =Button(root, font=('Arial',15, 'bold'), text="Convert", padx=2, command =RealTimeCurrencyConversion, fg='blue')
convert.place(x=200, y=220)

reset=Button(root, font=("Arial",15, "bold"), text="Reset", padx=2, command= clear, fg='blue')
reset.place(x=200,y=400)

root.mainloop()





