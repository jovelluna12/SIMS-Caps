import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Inventory System")
root.geometry("700x520")

#For the Page 1 Detail
Frame_Detail=Frame(root,width=500,height=200,bg="green")
Frame_Detail.place(x=0,y=0)

def Click_List():
    print("hello")
def Click_Stack():
    print("hello")
def Click_Delivery():
    print("hello")
def Click_Employee():
    print("hello")

label=Label(Frame_Detail,text="IMAGE",width=37,height=13)
button_List=Button(Frame_Detail,text="List",padx=20,pady=10,command=Click_List())
button_Stack=Button(Frame_Detail,text="Stack",padx=20,pady=10,command=Click_Stack())
button_Delivery=Button(Frame_Detail,text="Delivery",padx=20,pady=10,command=Click_Delivery())
button_Employee=Button(Frame_Detail,text="Employeee",padx=20,pady=10,command=Click_Employee())

label.grid(row=0,column=0,rowspan=5)
button_List.grid(row=0,column=1)
button_Stack.grid(row=0,column=2,)
button_Delivery.grid(row=1,column=1,padx=10)
button_Employee.grid(row=1,column=2,padx=10)

#For the Page LIST
Frame_List=Frame(root,width=500,height=320)
Frame_List.place(x=0,y=200)

#Table
frame_Table=ttk.Treeview(Frame_List,height=15)
frame_Table['columns']=("ID","Name","Detail","Price","Stack")
frame_Table.column("#0",width=0,stretch=NO)
frame_Table.column("ID",anchor=W,width=60,minwidth=300,stretch=NO)
frame_Table.column("Name",anchor=W,width=200,minwidth=300,stretch=NO)
frame_Table.column("Detail",anchor=E,width=80,stretch=NO)
frame_Table.column("Price",anchor=CENTER,width=80,stretch=NO)
frame_Table.column("Stack",anchor=E,width=78,stretch=NO)
#Table Head
frame_Table.heading("#0")
frame_Table.heading("ID",text="ID",anchor=W)
frame_Table.heading("Name",text="Product Name",anchor=W)
frame_Table.heading("Detail",text="Detail",anchor=E)
frame_Table.heading("Price",text="Price",anchor=CENTER)
frame_Table.heading("Stack",text="Stack",anchor=E)
frame_Table.grid(row=1,column=0)


#For the Side
Frame_Side=Frame(root,width=200,height=520,bg="yellow")
Frame_Side.place(x=500,y=0)

label=Label(Frame_Side,text="IMAGE")
button_List=Button(Frame_Side,text="List",padx=20,pady=10,command=Click_List())
button_Stack=Button(Frame_Side,text="Stack",padx=20,pady=10,command=Click_Stack())
button_Delivery=Button(Frame_Side,text="Delivery",padx=20,pady=10,command=Click_Delivery())
button_Employee=Button(Frame_Side,text="Employeee",padx=20,pady=10,command=Click_Employee())

label.grid(row=0,column=0)
button_List.grid(row=1,column=0)
button_Stack.grid(row=2,column=0)
button_Delivery.grid(row=3,column=0)
button_Employee.grid(row=4,column=0)

root.mainloop()