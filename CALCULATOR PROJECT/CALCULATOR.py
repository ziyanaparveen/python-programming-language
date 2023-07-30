from tkinter import *


def btnClick(number):
    global val
    val = val + str(number)
    data.set(val)


def btnClear():
    global val
    val = ""
    data.set("")


def btnEquals():
    try:
        global val
        result = str(eval(val))
        data.set(result)
        val = result

    except SyntaxError:
        data.set("syntax error")
        val = ""

    except ZeroDivisionError:
        data.set("arthmatic error")
        val = ""


window = Tk()
window.title("calculator")
window.geometry("361x381+500+200")
val = ""
data = StringVar()

display = Entry(window, textvariable=data, justify="right", bd=29, bg="powder blue", font=("ariel", 20))
display.grid(row=0, columnspan=4)

btn7 = Button(window, text="7", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(7))
btn7.grid(row=1, column=0)
btn8 = Button(window, text="8", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(8))
btn8.grid(row=1, column=1)
btn9 = Button(window, text="9", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(9))
btn9.grid(row=1, column=2)
btn_add = Button(window, text="+", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick('+'))
btn_add.grid(row=1, column=3)

btn4 = Button(window, text="4", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(4))
btn4.grid(row=2, column=0)
btn5 = Button(window, text="5", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(5))
btn5.grid(row=2, column=1)
btn6 = Button(window, text="6", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(6))
btn6.grid(row=2, column=2)
btn_sub = Button(window, text="-", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick('-'))
btn_sub.grid(row=2, column=3)

btn1 = Button(window, text="1", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(1))
btn1.grid(row=3, column=0)
btn2 = Button(window, text="2", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(2))
btn2.grid(row=3, column=1)
btn3 = Button(window, text="3", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(3))
btn3.grid(row=3, column=2)
btn_mul = Button(window, text="*", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick('*'))
btn_mul.grid(row=3, column=3)

btnC = Button(window, text="C", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=btnClear)
btnC.grid(row=4, column=0)
btn0 = Button(window, text="0", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(0))
btn0.grid(row=4, column=1)
btn_equal = Button(window, text="=", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=btnEquals)
btn_equal.grid(row=4, column=2)
btn_div = Button(window, text="/", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick('/'))
btn_div.grid(row=4, column=3)

window.mainloop()
