from tkinter import*

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
    

cal = Tk()
cal.title("CALCULATOR")
operator=""
text_Input =StringVar()

txtDisplay = Entry(cal,font=('arial', 25, 'bold'), textvariable=text_Input, bd=6, fg="white", insertwidth=4, bg="black", justify='right').grid(columnspan=4)

btn7=Button(cal,padx=27, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="7", command=lambda:btnClick(7)).grid(row=1, column=0)
btn8=Button(cal,padx=27, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="8", command=lambda:btnClick(8)).grid(row=1, column=1)
btn9=Button(cal,padx=27, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="9", command=lambda:btnClick(9)).grid(row=1, column=2)
Addition=Button(cal,padx=27.4, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="+", command=lambda:btnClick("+")).grid(row=1, column=3)

#Row 2 =========================================================================================================================

btn4=Button(cal,padx=27, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="4", command=lambda:btnClick(4)).grid(row=2, column=0)
btn5=Button(cal,padx=27, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="5", command=lambda:btnClick(5)).grid(row=2, column=1)
btn6=Button(cal,padx=27, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="6", command=lambda:btnClick(6)).grid(row=2, column=2)
Subtraction=Button(cal,padx=30.5, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="-", command=lambda:btnClick("-")).grid(row=2, column=3)

#Row 3 ==========================================================================================================================

btn1=Button(cal,padx=27, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="1", command=lambda:btnClick(1)).grid(row=3, column=0)
btn2=Button(cal,padx=27, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="2", command=lambda:btnClick(2)).grid(row=3, column=1)
btn3=Button(cal,padx=27, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="3", command=lambda:btnClick(3)).grid(row=3, column=2)
Multiplication=Button(cal,padx=27.5, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="x", command=lambda:btnClick("*")).grid(row=3, column=3)

#Row 4 ===========================================================================================================================

btnClear=Button(cal,padx=27, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="c", command=btnClearDisplay).grid(row=4, column=0)
btn0=Button(cal,padx=27, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="0", command=lambda:btnClick(0)).grid(row=4, column=1)
btnEquals=Button(cal,padx=26.4, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="=", command=btnEqualsInput).grid(row=4, column=2)
Divition=Button(cal,padx=28.5, pady=10, fg="white", bg="black", font=('arial', 20, 'bold'), text="÷", command=lambda:btnClick("/")).grid(row=4, column=3)




cal.mainloop()
 
