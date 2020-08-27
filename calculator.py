import tkinter
from tkinter import *
from tkinter import messagebox


root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)                 # this is boolean value means we can't resize window
root.title("Calculator")


val = ""
Z=0
operator=""


def btn1_is_clicked():
    global val
    val=val+ "1"
    data.set(val)


def btn2_is_clicked():
    global val
    val=val+ "2"
    data.set(val)


def btn3_is_clicked():
    global val
    val=val+ "3"
    data.set(val)


def btn4_is_clicked():
    global val
    val=val+ "4"
    data.set(val)


def btn5_is_clicked():
    global val
    val=val+ "5"
    data.set(val)  



def btn6_is_clicked():
    global val
    val=val+ "6"
    data.set(val)



def btn7_is_clicked():
    global val
    val=val+ "7"
    data.set(val)



def btn8_is_clicked():
    global val
    val=val+ "8"
    data.set(val)



def btn9_is_clicked():
    global val
    val=val+ "9"
    data.set(val)



def btn0_is_clicked():
    global val
    val=val+ "0"
    data.set(val)   



def btn_plus_clicked():
    global Z
    global operator
    global val
    Z= int(val)
    operator="+"
    val=val+ "+"
    data.set(val)



def btn_minus_clicked():
    global Z
    global operator
    global val
    Z= int(val)
    operator="-"
    val=val+"-"
    data.set(val)


def btn_mul_clicked():
    global Z
    global operator
    global val
    Z= int(val)
    operator="*"
    val=val+"*"
    data.set(val)


def btn_div_clicked():
    global Z
    global operator
    global val
    Z= int(val)
    operator="/"
    val=val+"/"
    data.set(val)       



def c_is_pressed():
    global Z
    global operator
    global val
    val=""
    z=0
    operator=""
    data.set(val)        


def result():
    global Z
    global operator
    global val
    val2=val
    if operator=="+":
        x= int((val2.split("+")[1]))
        C= Z+x
        data.set(C)
        val=str(C)

    elif operator=="-":
        x= int((val2.split("-")[1]))
        C= Z-x
        data.set(C)
        val=str(C) 


    elif operator=="*":
        x= int((val2.split("*")[1]))
        C= Z*x
        data.set(C)
        val=str(C)   


    elif operator=="/":
        x= int((val2.split("/")[1]))
        if x==0:
            messagebox.showerror("Error","Cant't divisible by 0")
            Z=""
            val=""
            data.set(val)
        else:
            C=int(Z/x)
            data.set(C)
            val=str(C)    


data= StringVar()
lbl= Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana",20),
    textvariable = data,
    background ="#fff",
    fg="#000"
)
lbl.pack(expand = True, fill = "both")

btnrow1= Frame(root,bg="#000")
btnrow1.pack(expand = True , fill = "both")                      #here we use pack to place label above frame for symmetry

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")



btn7 = Button(
    btnrow1,
    text = "7",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = btn7_is_clicked,
)
btn7.pack(side = LEFT , expand = True, fill = "both")

btn8 = Button(
    btnrow1,
    text = "8",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = btn8_is_clicked,
)
btn8.pack(side = LEFT , expand = True, fill = "both")

btn9 = Button(
    btnrow1,
    text = "9",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = btn9_is_clicked,
)
btn9.pack(side = LEFT , expand = True, fill = "both")

btnMul = Button(
    btnrow1,
    text = "*",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = btn_mul_clicked,
)
btnMul.pack(side = LEFT , expand = True, fill = "both")


btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = btn4_is_clicked,
)
btn4.pack(side = LEFT , expand = True, fill = "both")

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = btn5_is_clicked,
)
btn5.pack(side = LEFT , expand = True, fill = "both")

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = btn6_is_clicked,
)
btn6.pack(side = LEFT , expand = True, fill = "both")

btnMinus = Button(
    btnrow2,
    text = "-",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = btn_minus_clicked,
)
btnMinus.pack(side = LEFT , expand = True, fill = "both")



btn1 = Button(
    btnrow3,
    text = "1",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = btn1_is_clicked
)
btn1.pack(side = LEFT , expand = True, fill = "both")

btn2 = Button(
    btnrow3,
    text = "2",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = btn2_is_clicked,
)
btn2.pack(side = LEFT , expand = True, fill = "both")

btn3 = Button(
    btnrow3,
    text = "3",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = btn3_is_clicked,
)
btn3.pack(side = LEFT , expand = True, fill = "both")

btnplus = Button(
    btnrow3,
    text = "+",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = btn_plus_clicked,

)
btnplus.pack(side = LEFT , expand = True, fill = "both")



btnc = Button(
    btnrow4,
    text = "C",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = c_is_pressed,
)
btnc.pack(side = LEFT , expand = True, fill = "both")

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = btn0_is_clicked,
)
btn0.pack(side = LEFT , expand = True, fill = "both")

btndiv = Button(
    btnrow4,
    text = "/",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = btn_div_clicked,
)
btndiv.pack(side = LEFT , expand = True, fill = "both")

btnres = Button(
    btnrow4,
    text = "=",
    font = ("Verdana",22),
    relief = GROOVE,
    border =0,
    command = result,
)
btnres.pack(side = LEFT , expand = True, fill = "both")

root.mainloop()