import tkinter as tk

window = tk.Tk()
window.title("Calculator App")
window.geometry("800x600")

expression = ""

display=tk.StringVar()
display.set("")  

def click(thing):
    global expression
    expression+=str(thing)  
    display.set(expression)  
    
title = tk.Label(window, text="Calculator", font=("Times New Roman", 20))
title.pack(pady=20)

label = tk.Label(window, textvariable=display, font=("Times New Roman", 16), fg="blue", bg="white", width=30)
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

window.mainloop()
