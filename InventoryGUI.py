from logging import root
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tracemalloc import start

import Employee
import Manager
from tkcalendar import DateEntry

class InvortoryGUI:

    def __init__(self):
        self.InvorVal = None
           
    def search(self):
        result = self.Entry_Search.get()

        self.window_Frame = Frame(self.window_list, width=400, height=100)
        self.window_Frame.grid(row=0, column=0)

        Label_Search = Label(self.window_Frame, text="Search:")
        self.Entry_Search = Entry(self.window_Frame, width=50, borderwidth=3)
        self.button_Search = Button(self.window_Frame, text="Search", padx=5, pady=0, command=self.search())

        Label_Search.grid(row=0, column=0, sticky=W)
        self.Entry_Search.grid(row=0, column=1)
        self.button_Search.grid(row=0, column=3)

        self.window_Frame2 = Frame(self.window_list, width=400, height=250, bg="blue")
        self.window_Frame2.grid(row=1, column=0)

        self.Search_Table = ttk.Treeview(self.window_Frame2, height=12)
        self.Search_Table['column'] = ("ID", "Name", "Price", "Stack")
        self.Search_Table.column("#0", width=0, stretch=NO, anchor=W)
        self.Search_Table.column("ID", width=50, stretch=NO, anchor=W)
        self.Search_Table.column("Name", width=148, stretch=NO, anchor=W)
        self.Search_Table.column("Price", width=100, stretch=NO, anchor=E)
        self.Search_Table.column("Stack", width=80, stretch=NO, anchor=E)

        self.Search_Table.heading("#0")
        self.Search_Table.heading("ID", text="ID", anchor=W)
        self.Search_Table.heading("Name", text="Name", anchor=W)
        self.Search_Table.heading("Price", text="Price", anchor=W)
        self.Search_Table.heading("Stack", text="Stack", anchor=W)
        self.Search_Table.grid(row=0, column=0)

        self.window_Frame3 = Frame(self.window_list, width=400, height=50, bg="blue")
        self.window_Frame3.grid(row=2, column=0)

        self.button_Close = Button(self.window_Frame3, text="Close", command=self.window_list.destroy)
        self.button_Close.pack()

    def Click_List1(self):
        self.Frame_List.pack_forget()
        self.Frame_stack.pack_forget()
        self.Frame_Del.pack_forget()
        self.Frame_Empl.pack_forget()
        
        self.Frame_List.pack()
        style=ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")
        self.frame_Table=ttk.Treeview(self.Frame_List,height=25)
        self.frame_Table['columns']=("ID","Name","Status","Price","Quantity")
        self.frame_Table.column("#0",width=0,stretch=NO)
        self.frame_Table.column("ID",anchor=W,width=100,stretch=NO)
        self.frame_Table.column("Name",anchor=W,width=200,stretch=NO)
        self.frame_Table.column("Status",anchor=E,width=200,stretch=NO)
        self.frame_Table.column("Price",anchor=CENTER,width=200,stretch=NO)
        self.frame_Table.column("Quantity",anchor=E,width=198,stretch=NO)
        #Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID",text="ID",anchor=W)
        self.frame_Table.heading("Name",text="Product Name",anchor=W)
        self.frame_Table.heading("Status",text="Status",anchor=E)
        self.frame_Table.heading("Price",text="Price",anchor=CENTER)
        self.frame_Table.heading("Quantity",text="Quantity",anchor=E)
        self.frame_Table.pack()
        m1=Manager.Manager()
        result=m1.inventoryList()
        count=0
        for x in result:
            count+=1
            self.frame_Table.insert(parent='',index='end',iid=count,text=x,values=x)   

    def Click_Stack(self):
        #Table
        self.Frame_List.pack_forget()
        self.Frame_stack.pack_forget()
        self.Frame_Del.pack_forget()
        self.Frame_Empl.pack_forget()
        self.Frame_stack.pack(fill='both')
        style=ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")
        self.frame_Table=ttk.Treeview(self.Frame_stack,height=25)
        self.frame_Table['columns']=("ID","Name","Detail","Price","Stack")
        self.frame_Table.column("#0",width=0,stretch=NO)
        self.frame_Table.column("ID",anchor=W,width=100,stretch=NO)
        self.frame_Table.column("Name",anchor=W,width=200,stretch=NO)
        self.frame_Table.column("Detail",anchor=E,width=200,stretch=NO)
        self.frame_Table.column("Price",anchor=CENTER,width=200,stretch=NO)
        self.frame_Table.column("Stack",anchor=E,width=198,stretch=NO)
        #Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID",text="Stack-ID",anchor=W)
        self.frame_Table.heading("Name",text="Product Name",anchor=W)
        self.frame_Table.heading("Detail",text="Detail",anchor=E)
        self.frame_Table.heading("Price",text="Price",anchor=CENTER)
        self.frame_Table.heading("Stack",text="Stack",anchor=E)
        self.frame_Table.pack(fill='both')
        m1=Manager.Manager()
        result=m1.inventoryList()
        count=0
        for x in result:
            count+=1
            self.frame_Table.insert(parent='',index='end',iid=count,text=x,values=x)
        
    def Click_Delivery(self):
        #Table\
        self.Frame_List.pack_forget()
        self.Frame_stack.pack_forget()
        self.Frame_Del.pack_forget()
        self.Frame_Empl.pack_forget()
        
        self.Frame_Del.pack()
        style=ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")
        self.frame_Table=ttk.Treeview(self.Frame_Del,height=25)
        self.frame_Table['columns']=("ID","Name","Detail","Price","Stack")
        self.frame_Table.column("#0",width=0,stretch=NO)
        self.frame_Table.column("ID",anchor=W,width=100,stretch=NO)
        self.frame_Table.column("Name",anchor=W,width=200,stretch=NO)
        self.frame_Table.column("Detail",anchor=E,width=200,stretch=NO)
        self.frame_Table.column("Price",anchor=CENTER,width=200,stretch=NO)
        self.frame_Table.column("Stack",anchor=E,width=198,stretch=NO)
        #Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID",text="Delivery-ID",anchor=W)
        self.frame_Table.heading("Name",text="Product Name",anchor=W)
        self.frame_Table.heading("Detail",text="Detail",anchor=E)
        self.frame_Table.heading("Price",text="Price",anchor=CENTER)
        self.frame_Table.heading("Stack",text="Stack",anchor=E)
        self.frame_Table.pack()
        m1=Employee.Employee()
        result=m1.viewDeliveryList()
        count=0
        for x in result:
            count+=1
            self.frame_Table.insert(parent='',index='end',iid=count,text=x,values=x)
            
    def Click_Employee(self):
        self.Frame_List.pack_forget()
        self.Frame_stack.pack_forget()
        self.Frame_Del.pack_forget()
        self.Frame_Empl.pack_forget()
        self.Frame_Empl.pack()
        style=ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")
        self.frame_Table=ttk.Treeview(self.Frame_Empl,height=25)
        self.frame_Table['columns']=("ID","Name","Detail","Username")
        self.frame_Table.column("#0",width=0,stretch=NO)
        self.frame_Table.column("ID",anchor=W,width=100,stretch=NO)
        self.frame_Table.column("Name",anchor=W,width=200,stretch=NO)
        self.frame_Table.column("Detail",anchor=E,width=200,stretch=NO)
        self.frame_Table.column("Username",anchor=CENTER,width=200,stretch=NO)

        #Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID",text="Employee ID",anchor=W)
        self.frame_Table.heading("Name",text="Name",anchor=W)
        self.frame_Table.heading("Detail",text="Role",anchor=E)
        self.frame_Table.heading("Username",text="Username",anchor=CENTER)

        self.frame_Table.pack()
        m1=Manager.Manager()
        result=m1.viewEMPList()
        count=0
        for x in result:
            count+=1
            self.frame_Table.insert(parent='',index='end',iid=count,text=x,values=x)

    
    def Click_AddP(self):
        print("this")

    def Click_Add(self):
        self.Add_Delivery= Toplevel()
        self.Add_Delivery.title("Quantity!")
        self.Add_Delivery.geometry("800x550")

        self.Frame_Add=Frame(self.Add_Delivery,width=800,height=200)
        self.Frame_Add.place(x=0,y=0)
        self.Product_CODE_LA=Label(self.Frame_Add,text="Enter Product Name/Code:")
        self.Product_CODE_EN= Entry(self.Frame_Add,width=60,borderwidth=4)
        self.Product_CODE_LA.place(x=20,y=20)
        self.Product_CODE_EN.place(x=20,y=40)

        self.Product_date_LA=Label(self.Frame_Add,text="Date")
        self.Product_date_EN=DateEntry(self.Frame_Add,selectmode='day',width=20)
        self.Product_date_LA.place(x=20,y=80)
        self.Product_date_EN.place(x=20,y=100)

        self.Product_Exdate_LA=Label(self.Frame_Add,text="Expiration Date")
        self.Product_EXdate_EN=DateEntry(self.Frame_Add,selectmode='day',width=20)
        self.Product_Exdate_LA.place(x=200,y=80)
        self.Product_EXdate_EN.place(x=200,y=100)
        
        self.Product_Stack_LA=Label(self.Frame_Add,text="Stack")
        self.Product_Stack_EN= Entry(self.Frame_Add,width=20,borderwidth=4)
        self.Product_Stack_LA.place(x=400,y=20)
        self.Product_Stack_EN.place(x=400,y=40)

        self.button_Add=Button(self.Frame_Add,text="Add",padx=20,pady=5,command=self.Click_AddP)
        self.button_Add.place(x=700,y=150)


        self.Frame_List=Frame(self.Add_Delivery,width=800,height=320)
        self.Frame_List.place(x=0,y=200)
        #Table
        self.frame_Table=ttk.Treeview(self.Frame_List,height=15)
        self.frame_Table['columns']=("ID","Name","Detail","Price","Stack")
        self.frame_Table.column("#0",width=0,stretch=NO)
        self.frame_Table.column("ID",anchor=W,width=100)
        self.frame_Table.column("Name",anchor=W,width=200)
        self.frame_Table.column("Detail",anchor=E,width=200)
        self.frame_Table.column("Price",anchor=CENTER,width=150)
        self.frame_Table.column("Stack",anchor=E,width=149)
        #Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID",text="ID",anchor=W)
        self.frame_Table.heading("Name",text="Product Name",anchor=W)
        self.frame_Table.heading("Detail",text="Detail",anchor=E)
        self.frame_Table.heading("Price",text="Price",anchor=CENTER)
        self.frame_Table.heading("Stack",text="Stack",anchor=E)
        self.frame_Table.pack(fill='both')
        self.frame_Table.grid(row=1,column=0)


    def InvorGUI(self):
        self.InvorVal = Tk()
        self.InvorVal.title("Inventory System")
        width= self.InvorVal.winfo_screenwidth()
        height=self.InvorVal.winfo_screenheight()
        self.InvorVal.geometry("%dx%d"%(width,height))
        
        #For the Page 1 Detail
        self.Frame_Detail=Frame(self.InvorVal,width=900,height=200,)
        self.Frame_Detail.place(x=0,y=0)
        label=Label(self.Frame_Detail,text="IMAGE",width=37,height=13).place(x=0,y=0)
        self.button_List=Button(self.Frame_Detail,text="List",padx=10,pady=10,width=10,height=1,bg='#54FA9B',command=self.Click_List1).place(x=480,y=40)
        self.button_Stack=Button(self.Frame_Detail,text="Stack",padx=10,pady=10,width=10,height=1,bg='#54FA9B',command=self.Click_Stack).place(x=690,y=40)
        self.button_Delivery=Button(self.Frame_Detail,text="Delivery",padx=10,pady=10,width=10,height=1,bg='#54FA9B',command=self.Click_Delivery).place(x=480,y=120)
        self.button_Employee=Button(self.Frame_Detail,text="Employeee",padx=10,pady=10,width=10,height=1,bg='#54FA9B',command=self.Click_Employee).place(x=690,y=120)
        
        #For the Page LIST
        self.Frame_main=Frame(self.InvorVal,width=900,height=520)
        self.Frame_main.place(x=2,y=210)
        self.Frame_List=Frame(self.Frame_main,width=900,height=520)
        self.Frame_stack=Frame(self.Frame_main,width=900,height=520)
        self.Frame_Empl=Frame(self.Frame_main,width=900,height=520)
        self.Frame_Del=Frame(self.Frame_main,width=900,height=520)
        
        #For the Side
        self.Frame_Side=Frame(self.InvorVal,width=300,height=740)
        self.Frame_Side.place(x=910,y=0)
        label=Label(self.Frame_Side,text="IMAGE").place(x=100,y=10)

        self.Add_Del=Button(self.Frame_Side,text="Delivery",padx=10,pady=10,width=10,height=1,bg='#54FA9B',command=self.Click_Add).place(x=100,y=100)
        #button_List=Button(Frame_Side,text="List",padx=20,pady=10,width=10,height=1,command=self.Click_List()).place(x=40,y=50)
        
        self.InvorVal.mainloop()
    
    def start(self,id):
        self.InvorGUI()
