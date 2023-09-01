from tkinter import *

root = Tk()

root.title("Basic Calculator")
root.iconbitmap("d:/Harman/wallpapers/calculator.ico")
e = Entry(root, width= 35, borderwidth= 5)
e.grid(row=0, column=0, columnspan=3)


def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number)) #current is the last number added by the user

def button_clear_fn():
    e.delete(0,END)

def button_add_fn():
    first_num = e.get()
    e.delete(0,END)
    global math
    math = "addition"
    global f_num
    f_num = int(first_num)

def button_subtract_fn():
    first_num = e.get()
    e.delete(0,END)
    global math
    math = "subtraction"
    global f_num
    f_num = int(first_num)

def button_multiply_fn():
    first_num = e.get()
    e.delete(0,END)
    global math
    math = "multiplication"
    global f_num
    f_num = int(first_num)

def button_divide_fn():
    first_num = e.get()
    e.delete(0,END)
    global math
    math = "division"
    global f_num
    f_num = int(first_num)


def button_equal_fn():
    second_num = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0, int(second_num) + f_num)
    elif math == "subtraction":
        e.insert(0, f_num - int(second_num))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_num))
    elif math == "division":
        e.insert(0, f_num / int(second_num))
    else:
        e.insert(0, "0")

#define buttons
button_1 = Button(root, text="1",padx= 40, pady=20, command= lambda : button_click(1) ) #with lambda function you are able to pass parameters in the function
button_2 = Button(root, text= "2",padx= 40, pady=20, command= lambda : button_click(2) )
button_3 = Button(root, text= "3",padx= 40, pady=20, command= lambda : button_click(3) )
button_4 = Button(root, text="4",padx= 40, pady=20, command= lambda : button_click(4) )
button_5 = Button(root, text= "5",padx= 40, pady=20, command= lambda : button_click(5) )
button_6 = Button(root, text= "6",padx= 40, pady=20, command= lambda : button_click(6) )
button_7 = Button(root, text= "7",padx= 40, pady=20, command= lambda : button_click(7) )
button_8 = Button(root, text= "8",padx= 40, pady=20, command= lambda : button_click(8) )
button_9 = Button(root, text= "9",padx= 40, pady=20, command= lambda : button_click(9) )
button_0 = Button(root, text= "0",padx= 40, pady=20, command= lambda : button_click(0) )

button_add = Button(root, text= "+",padx= 39, pady=20, command= lambda : button_add_fn() )
button_equal = Button(root, text= "=",padx= 90, pady=20,bg= "blue",fg= "white", command= lambda : button_equal_fn() )
button_clear = Button(root, text= "clear",padx= 79, pady=20, command= lambda : button_clear_fn() )

button_subtract = Button(root, text= "-",padx= 41, pady=20, command= lambda : button_subtract_fn() )
button_multiply = Button(root, text= "*",padx= 40, pady=20, command= lambda : button_multiply_fn() )
button_divide = Button(root, text= "/",padx= 40, pady=20, command= lambda : button_divide_fn() )


#place buttons on the screen

button_7.grid(row= 1,column=0)
button_8.grid(row= 1, column= 1)
button_9.grid(row= 1, column= 2)

button_4.grid(row= 2, column= 0)
button_5.grid(row= 2, column= 1)
button_6.grid(row= 2, column= 2)

button_1.grid(row= 3, column= 0)
button_2.grid(row= 3, column= 1)
button_3.grid(row= 3, column= 2)

button_0.grid(row=4, column= 0)
button_clear.grid(row=4, column= 1,columnspan=2)

button_add.grid(row=5, column= 0)
button_equal.grid(row=5, column= 1,columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()