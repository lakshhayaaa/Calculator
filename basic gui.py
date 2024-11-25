import tkinter as tk

window=tk.Tk()
window.title("Calculator App")
window.geometry("1000x700")

expression=""

display=tk.StringVar()
display.set("")  

def click(thing):
    global expression
    expression+=str(thing)  
    display.set(expression)  

def error():
    error_message.pack(pady=10)
    window.after(1500, lambda: error_message.pack_forget())
    clear()

def backspace():
    global expression
    expression=expression[0:len(expression)-1:]
    display.set(expression)

def clear():
    global expression
    expression=""
    display.set(expression)

def evaluate():
    global expression
    try:
        if expression[-1].isnumeric():
            expression=eval(expression)
            display.set(expression)
        else:
            error()
    except:
        error()
        clear()

error_message = tk.Label(window, text="Syntax error", font=("Times New Roman", 16))

title=tk.Label(window, text="Calculator", font=("Times New Roman", 20))
title.pack(pady=10)

trig=tk.Label(window, text="Trigonometric and inverse trigonometric:", font=("Times New Roman", 20))
trig.place(x=600,y=150)

logexp=tk.Label(window, text="Logarithmic and exponential functions:", font=("Times New Roman", 20))
logexp.place(x=100,y=450)

bitwise=tk.Label(window, text="Bitwise functions:", font=("Times New Roman", 20))
bitwise.place(x=100,y=350)

label=tk.Label(window, textvariable=display, font=("Times New Roman", 16), fg="blue", bg="white", width=30)
label.pack(pady=10)

#the buttons:
button_0=tk.Button(window, text="0", command=lambda: click(0), width=3)
button_0.place(x=200,y=300)

button_1=tk.Button(window, text="1", command=lambda: click(1), width=3)
button_1.place(x=100,y=250)

button_2=tk.Button(window, text="2", command=lambda: click(2), width=3)
button_2.place(x=200,y=250)

button_3=tk.Button(window, text="3", command=lambda: click(3), width=3)
button_3.place(x=300,y=250)

button_4=tk.Button(window, text="4", command=lambda: click(4), width=3)
button_4.place(x=100,y=200)

button_5=tk.Button(window, text="5", command=lambda: click(5), width=3)
button_5.place(x=200,y=200)

button_6=tk.Button(window, text="6", command=lambda: click(6), width=3)
button_6.place(x=300,y=200)

button_7=tk.Button(window, text="7", command=lambda: click(7), width=3)
button_7.place(x=100,y=150)

button_8=tk.Button(window, text="8", command=lambda: click(8), width=3)
button_8.place(x=200,y=150)

button_9=tk.Button(window, text="9", command=lambda: click(9), width=3)
button_9.place(x=300,y=150)

button_add=tk.Button(window, text="+", command=lambda: click("+"), width=3)
button_add.place(x=400,y=300)

button_subtract=tk.Button(window, text="-", command=lambda: click("-"), width=3)
button_subtract.place(x=400,y=250)

button_multiply=tk.Button(window, text="*", command=lambda: click("*"), width=3)
button_multiply.place(x=400,y=200)

button_divide=tk.Button(window, text="/", command=lambda: click("/"), width=3)
button_divide.place(x=400,y=150)

button_backspace=tk.Button(window, text="del", command=backspace, width=3)
button_backspace.place(x=300,y=300)

button_clear=tk.Button(window, text="AC", command=clear, width=3)
button_clear.place(x=100,y=300)

button_eval=tk.Button(window, text="=", command=evaluate, width=3, bg="blue")
button_eval.place(x=100,y=100)

button_leftbrack=tk.Button(window, text="(", command=lambda: click("("), width=1)
button_leftbrack.place(x=490,y=150)

button_rightbrack=tk.Button(window, text=")", command=lambda: click(")"), width=1)
button_rightbrack.place(x=530,y=150)

button_expo=tk.Button(window, text="power", command=lambda: click("**"), width=3)
button_expo.place(x=500,y=200)

button_modulo=tk.Button(window, text="modulo", command=lambda: click("%"), width=3)
button_modulo.place(x=500,y=250)

button_floor=tk.Button(window, text="floor", command=lambda: click("//"), width=3)
button_floor.place(x=500,y=300)

button_bitwiseAND=tk.Button(window, text="AND &", command=lambda: click("&"), width=3)
button_bitwiseAND.place(x=100,y=400)

button_bitwiseOR=tk.Button(window, text="OR |", command=lambda: click("|"), width=3)
button_bitwiseOR.place(x=200,y=400)

button_bitwiseXOR=tk.Button(window, text="XOR ^", command=lambda: click("^"), width=3)
button_bitwiseXOR.place(x=300,y=400)

button_bitwiseNOT=tk.Button(window, text="NOT ~", command=lambda: click("~"), width=3)
button_bitwiseNOT.place(x=400,y=400)

button_bitwiseLSHIFT=tk.Button(window, text="<<", command=lambda: click("<<"), width=1)
button_bitwiseLSHIFT.place(x=490,y=400)

button_bitwiseRSHIFT=tk.Button(window, text=">>", command=lambda: click(">>"), width=1)
button_bitwiseRSHIFT.place(x=530,y=400)

window.mainloop()
