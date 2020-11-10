from tkinter import*
root=Tk()
root.title("DaniCAl 1.2 ")
root.configure(background="#515151")
#entry box
entry=Entry(root,width=50,relief="raised")
entry.grid(column=0,columnspan=4,row=0,pady=20)

# functions
def button_click(number):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))


def buttlon_c1():
    entry.delete(0,END)


def button_kam():
    firstnumber=entry.get()
    global f_num
    global math
    math= "substraction"
    f_num=int(firstnumber)
    entry.delete(0,END)


def button_equal():
    second_number=entry.get()
    entry.delete(0,END)
    if math== "addition":
        entry.insert(0,f_num + int(second_number))
    elif math== "multiplication":
        entry.insert(0, f_num * int(second_number))
    elif math== "division":
        entry.insert(0, f_num // int(second_number))
    elif math=="substraction":
        entry.insert(0, f_num - int(second_number))




def button_dabash():
    firstnumber = entry.get()
    global f_num
    global math
    math= "division"
    f_num = int(firstnumber)
    entry.delete(0, END)

def button_karat():
    firstnumber = entry.get()
    global f_num
    global math
    math="multiplication"
    f_num = int(firstnumber)
    entry.delete(0, END)

def button_ko():
    firstnumber = entry.get()
    global f_num
    global math
    math="addition"
    f_num = int(firstnumber)
    entry.delete(0, END)




#number buttons

button_1=Button(root, text="1", padx=25, pady= 15,bg="#F5F5F5",fg="black",font=("aral",16 ),relief="raised",command=lambda: button_click(1))
button_2=Button(root, text="2", padx=25, pady= 15,bg="#F5F5F5",fg="black",font=("aral",16 ),relief="raised",command=lambda: button_click(2))
button_3=Button(root, text="3", padx=25, pady= 15,bg="#F5F5F5",fg="black",font=("aral",16 ),relief="raised",command=lambda: button_click(3))
button_4=Button(root, text="4", padx=25, pady= 15,bg="#F5F5F5",fg="black",font=("aral",16 ),relief="raised",command=lambda: button_click(4))
button_5=Button(root, text="5", padx= 25, pady= 15,bg="#F5F5F5",fg="black",font=("aral",16 ),relief="raised",command=lambda: button_click(5))
button_6=Button(root, text="6", padx= 25, pady= 15,bg="#F5F5F5",fg="black",font=("aral",16 ),relief="raised",command=lambda: button_click(6))
button_7=Button(root, text="7", padx= 25, pady= 15,bg="#F5F5F5",fg="black",font=("aral",16 ),relief="raised",command=lambda: button_click(7))
button_8=Button(root, text="8", padx= 25, pady= 15,bg="#F5F5F5",fg="black",font=("aral",16 ),relief="raised",command=lambda: button_click(8))
button_9=Button(root, text="9", padx= 25, pady= 15,bg="#F5F5F5",fg="black",font=("aral",16 ),relief="raised",command=lambda: button_click(9))
button_0=Button(root, text="0", padx= 25, pady= 89,bg="#F5F5F5",fg="black",font=("aral",16 ),relief="raised",command=lambda: button_click(0))


#operator buttons

button_equal=Button(root,text="=",padx=142 , pady=15,fg="black",bg="#68838B",font=("aral",20 ),relief="raised",command= button_equal)
button_plus=Button(root,text="+",padx=27, pady=10,bg="#9AC0CD",fg="black",font=("aral",16 ),relief="raised",command= button_ko)

button_minus=Button(root,text="-",padx=27, pady=10,bg="#9AC0CD",fg="black",font=("aral",16 ),relief="raised",command= button_kam)
button_divide=Button(root,text="/",padx=27, pady=10,bg="#9AC0CD",fg="black",font=("aral",16 ),relief="raised",command=button_dabash)
button_clear=Button(root,text="Clear",padx=126, pady= 15,bg="#68838B",fg="black",font=("aral",16 ),relief="raised",command=buttlon_c1)
button_multiply=Button(root,text="*",padx=27 , pady=10,bg="#9AC0CD",fg="black",font=("aral",16 ),relief="raised",command=button_karat)

# griding

button_1.grid(row=5,column=0)
button_2.grid(row=5,column=1)
button_3.grid(row=5,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=2,column=3,rowspan=5)
button_equal.grid(row=8,column=0,columnspan=5)
button_divide.grid(row=1,column=0)
button_plus.grid(row=1,column=1)
button_minus.grid(row=1,column=2)
button_clear.grid(row=7,column=0,columnspan=5)
button_multiply.grid(row=1,column=3)




root.mainloop()