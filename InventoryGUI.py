from logging import root
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tracemalloc import start

from click import option

import Employee
import Manager
from tkcalendar import DateEntry

import Product
import randomNumGen


class InvortoryGUI:

    def __init__(self):
        self.InvorVal = None
           
    def search(self):
        result = self.Entry_Search.get()

        self.window_Frame = Frame(self.window_list, width=400, height=100,highlightbackground="black", highlightthickness=3)
        self.window_Frame.grid(row=0, column=0)

        Label_Search = Label(self.window_Frame, text="Search:")
        self.Entry_Search = Entry(self.window_Frame, width=50, borderwidth=3)
        self.button_Search = Button(self.window_Frame, text="Search", padx=5, pady=0, command=self.search())

        Label_Search.grid(row=0, column=0, sticky=W)
        self.Entry_Search.grid(row=0, column=1)
        self.button_Search.grid(row=0, column=3)

        self.window_Frame2 = Frame(self.window_list, width=400, height=250, bg="blue",highlightbackground="black", highlightthickness=3)
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

        self.window_Frame3 = Frame(self.window_list, width=400, height=50, bg="blue",highlightbackground="black", highlightthickness=3)
        self.window_Frame3.grid(row=2, column=0)

        self.button_Close = Button(self.window_Frame3, text="Close", command=self.window_list.destroy)
        self.button_Close.pack()


#Chick List and stack Start~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def Click_List1(self):
        self.Frame_List.pack_forget()
        self.Frame_stack.pack_forget()
        self.Frame_Del.pack_forget()
        self.Frame_Empl.pack_forget()
        
        self.Frame_List.pack()
        style=ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")
        self.frame_Table=ttk.Treeview(self.Frame_List,height=24)
        self.frame_Table['columns']=("ID","Name","Status","Price","Quantity")
        self.frame_Table.column("#0",width=0,stretch=NO)
        self.frame_Table.column("ID",anchor=W,width=100,stretch=NO)
        self.frame_Table.column("Name",anchor=W,width=400,stretch=NO)
        self.frame_Table.column("Status",anchor=E,width=200,stretch=NO)
        self.frame_Table.column("Price",anchor=CENTER,width=155,stretch=NO)
        self.frame_Table.column("Quantity",anchor=E,width=200,stretch=NO)
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
        self.frame_Table=ttk.Treeview(self.Frame_stack,height=24)
        self.frame_Table['columns']=("ID","Name","Detail","Price","Stack")
        self.frame_Table.column("#0",width=0,stretch=NO)
        self.frame_Table.column("ID",anchor=W,width=100,stretch=NO)
        self.frame_Table.column("Name",anchor=W,width=400,stretch=NO)
        self.frame_Table.column("Detail",anchor=E,width=200,stretch=NO)
        self.frame_Table.column("Price",anchor=CENTER,width=155,stretch=NO)
        self.frame_Table.column("Stack",anchor=E,width=200,stretch=NO)
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
        self.frame_Table=ttk.Treeview(self.Frame_Del,height=24)
        self.frame_Table['columns']=("ID","Name","Detail","Price","Stack")
        self.frame_Table.column("#0",width=0,stretch=NO)
        self.frame_Table.column("ID",anchor=W,width=100,stretch=NO)
        self.frame_Table.column("Name",anchor=W,width=400,stretch=NO)
        self.frame_Table.column("Detail",anchor=E,width=200,stretch=NO)
        self.frame_Table.column("Price",anchor=CENTER,width=155,stretch=NO)
        self.frame_Table.column("Stack",anchor=E,width=200,stretch=NO)
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
        self.frame_Table=ttk.Treeview(self.Frame_Empl,height=24)
        self.frame_Table['columns']=("ID","Name","Detail","Username")
        self.frame_Table.column("#0",width=0,stretch=NO)
        self.frame_Table.column("ID",anchor=W,width=100,stretch=NO)
        self.frame_Table.column("Name",anchor=W,width=400,stretch=NO)
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
#Chick List and stack END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Chick ADD START!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def Click_AddP(self):
        ProdName = self.Product_CODE_EN.get()

        m = Product.product()
        if isinstance(ProdName,str):
            result=m.viewName(ProdName)
        if isinstance(ProdName,int):
            result=m.viewCode(ProdName)
        count=0

        if result=="empty":

            self.Product_Price_LA = Label(self.Frame_Add, text="Price")
            self.Product_Price_EN = Entry(self.Frame_Add, width=20, borderwidth=4)
            self.Product_Price_LA.place(x=530, y=20)
            self.Product_Price_EN.place(x=530, y=40)

            self.button_Add.config(command=self.add_to_products)

            self.Label = Label(self.Frame_Add, text="Product Not Found in Database, It will be Added Upon Clicking Add Button", fg='Red')
            self.Label.place(x=100, y=150)

        else:
            for x in result:
                count += 1
                self.frame_Table.insert(parent='', index='end', iid=count, text=x, values=x)

    def add_to_products(self):
        ProdName = self.Product_CODE_EN.get()
        date = self.Product_date_EN.get_date()
        expiry_date = self.Product_EXdate_EN.get_date()
        quantity = self.Product_Stack_EN.get()
        ProductID = randomNumGen.generateProductID()
        price = float(int(self.Product_Price_EN.get()))


        var1="ProductID_list"
        var2="ProdName_list"
        var3 = "quantity_list"
        var4 = "price_list"
        var5 = "date_list"
        var6 = "expiry_date_list"
        if var1 not in globals() and var2 not in globals() and var3 not in globals() and var4 not in globals() and var5 not in globals() and var6 not in globals():
            global ProductID_list, ProdName_list, quantity_list, price_list, date_list, expiry_date_list

            ProductID_list = []
            ProdName_list = []
            quantity_list = []
            price_list = []
            date_list = []
            expiry_date_list = []

        ProductID_list.append(int(ProductID))
        ProdName_list.append(ProdName)
        quantity_list.append(int(quantity))
        price_list.append(price)
        date_list.append(date)
        expiry_date_list.append(expiry_date)

        a=Product.product()
        a.add(ProductID,ProdName,0,price)

        self.frame_Table.insert(parent='', index='end', iid=ProductID, text=(ProductID,ProdName,price,quantity,date,expiry_date), values=(ProductID,ProdName,price,quantity,date,expiry_date))

        self.Product_CODE_EN.delete(0,'end')
        self.Product_Stack_EN.delete(0, 'end')
        self.Product_EXdate_EN.delete(0, 'end')
        self.Product_Price_EN.delete(0,'end')

        self.AddDeliveries = Button(self.Frame_Add, text="Add to Delivery List", padx=20, pady=5,command=self.Add_Deliveries)
        self.AddDeliveries.place(x=500, y=150)

        self.Product_Price_LA.place_forget()
        self.Product_Price_EN.place_forget()
        self.button_Add.config(command=self.Click_AddP)


    def Add_Deliveries(self):
        batch_code = []
        code = randomNumGen.generateBatchCode()
        for i in range(len(ProductID_list)):
            batch_code.append(code)

        item_tuple = list(zip(ProductID_list,ProdName_list,batch_code,quantity_list,price_list,expiry_date_list,'Under Delivery'))

        order_date=self.Product_date_EN.get_date()
        arrival_date=self.Product_Arrive_EN.get_date()


        a=Employee.Employee()
        print(a.addManyDeliveryList(item_tuple,code,order_date,arrival_date,'Under Delivery'))

        # b=Product.product()
        # print(b.updateProductQuantity(ProductID_list,quantity_list))


    def Click_Add(self):
        self.Add_Delivery= Toplevel()
        self.Add_Delivery.title("Add Products on Delivery")
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

        self.Product_Arrive_LA = Label(self.Frame_Add, text="Arrival Date")
        self.Product_Arrive_EN = DateEntry(self.Frame_Add, selectmode='day', width=20)
        self.Product_Arrive_LA.place(x=390, y=80)
        self.Product_Arrive_EN.place(x=390, y=100)

        self.Product_Stack_LA=Label(self.Frame_Add,text="Stack")
        self.Product_Stack_EN= Entry(self.Frame_Add,width=20,borderwidth=4)
        self.Product_Stack_LA.place(x=400,y=20)
        self.Product_Stack_EN.place(x=400,y=40)

        self.button_Add=Button(self.Frame_Add,text="Add",padx=20,pady=5,command= self.Click_AddP)
        self.button_Add.place(x=700,y=150)


        self.Frame_List=Frame(self.Add_Delivery,width=800,height=320)
        self.Frame_List.place(x=0,y=200)
        #Table
        self.frame_Table=ttk.Treeview(self.Frame_List,height=15)
        self.frame_Table['columns']=("ID","Name","Price","Quantity","Order Date","Expiration Date")
        self.frame_Table.column("#0",width=0,stretch=NO)
        self.frame_Table.column("ID",anchor=W,width=100)
        self.frame_Table.column("Name",anchor=W,width=200)

        self.frame_Table.column("Price",anchor=CENTER,width=150)
        self.frame_Table.column("Quantity",anchor=W,width=149)
        self.frame_Table.column("Order Date", anchor=W, width=149)
        self.frame_Table.column("Expiration Date", anchor=W, width=149)
        #Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID",text="ID",anchor=W)
        self.frame_Table.heading("Name",text="Product Name",anchor=W)
        self.frame_Table.heading("Price",text="Price",anchor=CENTER)
        self.frame_Table.heading("Quantity",text="Quantity",anchor=W)
        self.frame_Table.heading("Order Date", text="Order Date", anchor=W)
        self.frame_Table.heading("Expiration Date", text="Expiration Date", anchor=W)

        self.frame_Table.pack(fill='both')
        self.frame_Table.grid(row=1,column=0)

    #employee
    def Click_AddS_Em(self):
        print("this")

    def Click_Add_Em(self):
        self.Add_Employee= Toplevel()
        self.Add_Employee.title("Employeee!")
        self.Add_Employee.geometry("800x500")

        self.Frame_Add_Em=Frame(self.Add_Employee,width=800,height=500,)
        self.Frame_Add_Em.place(x=0,y=0)

        Frma=Label(self.Frame_Add_Em,text="Add Employee", width=20, font=("Arial", 35),anchor=W)
        Frma.place(x=10,y=10)

        self.Employee_Username_LA=Label(self.Frame_Add_Em,text="Username:")
        self.username = StringVar()
        self.Employee_Username_EN= Entry(self.Frame_Add_Em,width=40,textvariable=self.username,borderwidth=4)
        self.Employee_Username_LA.place(x=280,y=230)
        self.Employee_Username_EN.place(x=280,y=250)

        self.Employee_Password_LA=Label(self.Frame_Add_Em,text="Password:")
        self.password = StringVar()
        self.Employee_Password_EN= Entry(self.Frame_Add_Em,width=40,textvariable=self.password,show="*",borderwidth=4)
        self.Employee_Password_LA.place(x=540,y=230)
        self.Employee_Password_EN.place(x=540,y=250)

        self.Employee_Lname_LA=Label(self.Frame_Add_Em,text="Last Name:")
        self.Employee_Lname_EN= Entry(self.Frame_Add_Em,width=40,borderwidth=4)
        self.Employee_Lname_LA.place(x=20,y=280)
        self.Employee_Lname_EN.place(x=20,y=300)

        self.Employee_Fname_LA=Label(self.Frame_Add_Em,text="First Name:")
        self.Employee_Fname_EN= Entry(self.Frame_Add_Em,width=40,borderwidth=4)
        self.Employee_Fname_LA.place(x=280,y=280)
        self.Employee_Fname_EN.place(x=280,y=300)

        self.Employee_Mname_LA=Label(self.Frame_Add_Em,text="Middle Name:")
        self.Employee_Mname_EN= Entry(self.Frame_Add_Em,width=40,borderwidth=4)
        self.Employee_Mname_LA.place(x=540,y=280)
        self.Employee_Mname_EN.place(x=540,y=300)

        self.Employee_Address_LA=Label(self.Frame_Add_Em,text="Address:")
        self.Employee_Address_EN= Entry(self.Frame_Add_Em,width=83,borderwidth=4)
        self.Employee_Address_LA.place(x=20,y=330)
        self.Employee_Address_EN.place(x=20,y=350)

        self.Employee_Bdate_LA=Label(self.Frame_Add_Em,text="Birth Date:")
        self.Employee_Bdate_EN=DateEntry(self.Frame_Add_Em,selectmode='day',width=38)
        self.Employee_Bdate_LA.place(x=540,y=330)
        self.Employee_Bdate_EN.place(x=540,y=353)


        self.button_Add=Button(self.Frame_Add_Em,text="Add",padx=20,pady=5,command=self.Click_AddS_Em)
        self.button_Add.place(x=715,y=420)

    def AddProduct(self):
        self.frame_Table.delete(*self.frame_Table.get_children())

        Prod = Product.product()
        Prod.addMany(vals)

    #stack
    def DoneAdd_Product(self):

        ProductName = self.Stack_Product_Name_EN.get()
        
        Quantity = self.Stack_Product_Size_EN.get()
        price = price_entry.get()

        id=randomNumGen.generateProductID()

        if Quantity.isdigit():
            Quantityy=int(Quantity)

        pricee=float(int(float(price)))
        global vals
        vals=(id,ProductName,pricee,Quantityy)

        global count

        id=[]
        name=[]
        quantity=[]
        price=[]
        batch_code=[]
        status=[]

        if 'count' not in globals():
            count = 0
        else:
            count += 1
        self.frame_Table.insert(parent='', index='end', iid=count, text=vals,values=(vals))
        vals=()
        batch=randomNumGen.generateBatchCode()

        for child in self.frame_Table.get_children():
            val=self.frame_Table.item(child)["values"]
            idd=randomNumGen.generateProductID()

            id.append(idd)
            batch_code.append(batch)
            name.append(val[1])
            quantity.append(val[2])
            price.append(val[3])
            status.append("Added")

            vals=list(zip(id,name,quantity,price,batch_code,status))

        self.button_Finish.config(state='normal', command=self.AddProduct)

    def setPrice(self,event):
        choice=event.widget.get()
        res=[idx for idx, x in enumerate(lst) if x[1]==choice]
        item=lst[res[0]]
        price=item[2]
        price_entry.set(price)

    def Click_Add_Product(self):
        self.Add_Stack= Toplevel()
        self.Add_Stack.title("Add Product")
        self.Add_Stack.geometry("800x527")

        self.Frame_Add_St=Frame(self.Add_Stack,width=800,height=500,)
        self.Frame_Add_St.place(x=0,y=0)

        self.Frma=Label(self.Frame_Add_St,text="Add Product", width=20, font=("Arial", 35),anchor=W)
        self.Frma.place(x=10,y=10)

        a=Product.product()

        chosen_val=tk.StringVar(self.Frame_Add_St)
        chosen_val.set("Select Product")
        
        global lst
        lst = a.returnall()
        n=1

        self.Stack_Product_Name_LA=Label(self.Frame_Add_St,text="Product Name:")
        self.Stack_Product_Name_EN= ttk.Combobox(self.Frame_Add_St,textvariable=chosen_val)
        self.Stack_Product_Name_LA.place(x=160,y=80)
        self.Stack_Product_Name_EN.place(x=160,y=100)
        self.Stack_Product_Name_EN.config(width=20)
        self.Stack_Product_Name_EN['values']=([x[n] for x in lst])

        self.Stack_Product_Name_EN.bind("<<ComboboxSelected>>",self.setPrice)

        self.Stack_Product_Price_LA=Label(self.Frame_Add_St,text="Price:")
        global price_entry
        price_entry=tk.StringVar()
        self.Stack_Product_Price_EN= Entry(self.Frame_Add_St,width=20,textvariable=price_entry,borderwidth=4,state="disabled")
        self.Stack_Product_Price_LA.place(x=480,y=80)
        self.Stack_Product_Price_EN.place(x=480,y=100)

        self.Stack_Product_Size_LA=Label(self.Frame_Add_St,text="Quantity:")
        self.Stack_Product_Size_EN= Entry(self.Frame_Add_St,width=20,borderwidth=4)
        self.Stack_Product_Size_LA.place(x=340,y=80)
        self.Stack_Product_Size_EN.place(x=340,y=100)

        self.Frame_List=Frame(self.Add_Stack,width=800,height=320)
        self.Frame_List.place(x=0,y=200)
        #Table
        self.frame_Table=ttk.Treeview(self.Frame_List,height=15)
        self.frame_Table['columns']=("ID","Name","Price","Quantity")
        self.frame_Table.column("#0",width=0,stretch=NO)
        self.frame_Table.column("ID",anchor=W,width=100)
        self.frame_Table.column("Name",anchor=W,width=200)
        # self.frame_Table.column("Detail",anchor=E,width=200)
        self.frame_Table.column("Price",anchor=CENTER,width=150)
        self.frame_Table.column("Quantity",anchor=E,width=149)
        #Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID",text="ID",anchor=W)
        self.frame_Table.heading("Name",text="Product Name",anchor=W)
        # self.frame_Table.heading("Detail",text="Detail",anchor=E)
        self.frame_Table.heading("Price",text="Price",anchor=CENTER)
        self.frame_Table.heading("Quantity",text="Quantity",anchor=E)
        self.frame_Table.pack(fill='both')
        self.frame_Table.grid(row=1,column=0)

        self.button_Add=Button(self.Frame_Add_St,text="Add",padx=20,pady=5,command=self.DoneAdd_Product)
        self.button_Add.place(x=715,y=160)

        self.button_Delete=Button(self.Frame_Add_St,text="Delete",padx=20,pady=5,command=self.Delete)
        self.button_Delete.place(x=715,y=250)

        self.button_Finish = Button(self.Frame_Add_St, text="Finish", padx=20, pady=5, state='disabled')
        self.button_Finish.place(x=715, y=200)

    def Delete(self):
        select=self.frame_Table.selection()[0]
        self.frame_Table.delete(select)

#Chick ADD END!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def InvorGUI(self):
        self.InvorVal = Tk()
        self.InvorVal.title("Cresdel Pharmacy!!")
        width= self.InvorVal.winfo_screenwidth()
        height=self.InvorVal.winfo_screenheight()
        self.InvorVal.geometry("%dx%d"%(width,height))
        
        #For the Page 1 Detail
        self.Frame_Detail=Frame(self.InvorVal,width=1063,height=200,highlightbackground="black", highlightthickness=3)
        self.Frame_Detail.place(x=0,y=0)
        label=Label(self.Frame_Detail,text="IMAGE",width=37,height=10).place(x=0,y=0)
        
        #For the Page LIST
        self.Frame_main=Frame(self.InvorVal,width=1063,height=498,highlightbackground="black", highlightthickness=3)
        self.Frame_main.place(x=0,y=199)
        self.Frame_List=Frame(self.Frame_main,width=1063,height=498)
        self.Frame_stack=Frame(self.Frame_main,width=1063,height=498)
        self.Frame_Empl=Frame(self.Frame_main,width=1063,height=498)
        self.Frame_Del=Frame(self.Frame_main,width=1063,height=498)
        
        #For the Side
        self.Frame_Side=Frame(self.InvorVal,width=300,height=697,highlightbackground="black", highlightthickness=3)
        self.Frame_Side.place(x=1060,y=0)

        Detail=Label(self.Frame_Side,text="Detail Button",width=37,anchor=W).place(x=40,y=270)
        self.button_List=Button(self.Frame_Side,text="List",padx=10,pady=10,width=10,height=1,bg='#54FA9B',command=self.Click_List1).place(x=40,y=300)
        self.button_Stack=Button(self.Frame_Side,text="Stack",padx=10,pady=10,width=10,height=1,bg='#54FA9B',command=self.Click_Stack).place(x=160,y=300)
        self.button_Delivery=Button(self.Frame_Side,text="Delivery",padx=10,pady=10,width=10,height=1,bg='#54FA9B',command=self.Click_Delivery).place(x=40,y=350)
        self.button_Employee=Button(self.Frame_Side,text="Employeee",padx=10,pady=10,width=10,height=1,bg='#54FA9B',command=self.Click_Employee).place(x=160,y=350)

        label=Label(self.Frame_Side,text="IMAGE").place(x=100,y=10)
        Add=Label(self.Frame_Side,text="ADD Button",width=37,anchor=W).place(x=40,y=420)
        self.Add_Del=Button(self.Frame_Side,text="ADD Delivery",padx=10,pady=10,width=10,height=1,bg='#54FA9B',command=self.Click_Add).place(x=40,y=450)
        self.button_Add_Em=Button(self.Frame_Side,text="ADD Employee",padx=10,pady=10,width=10,height=1,bg='#54FA9B',command=self.Click_Add_Em).place(x=160,y=450)
        self.button_Add_Pm=Button(self.Frame_Side,text="ADD Product",padx=10,pady=10,width=10,height=1,bg='#54FA9B',command=self.Click_Add_Product).place(x=40,y=500)
        self.button_Add_prodref=Button(self.Frame_Side,text="Reference",padx=10,pady=10,width=10,height=1,bg='#54FA9B',command=self.ProdRef).place(x=160,y=500)

        self.InvorVal.mainloop()

    def ProdRef(self):
        self.Add_Stack= Toplevel()
        self.Add_Stack.title("Product Reference")
        

        self.Frame_Add_St=Frame(self.Add_Stack)
        self.Frame_Add_St.pack()

        self.Frma=Label(self.Frame_Add_St,text="Product Reference Menu", width=20, font=("Arial", 35),anchor=W)
        self.Frma.pack()

        self.add=Button(self.Frame_Add_St, text="Add Reference", padx=20, pady=5, command=self.Click_Add_Ref).pack()
        self.edit=Button(self.Frame_Add_St, text="Edit Reference", padx=20, pady=5, command=self.Click_Edit_Ref).pack()


    def Click_Edit_Ref(self):
        self.Add_Stack= Toplevel()
        self.Add_Stack.title("Edit Product Reference")
        # self.Add_Stack.geometry("800x527")

        self.Frame_Add_St=Frame(self.Add_Stack,width=800,height=500,)
        self.Frame_Add_St.pack()

        self.Frma=Label(self.Frame_Add_St,text="Edit Product Reference", width=20, font=("Arial", 35),anchor=W)
        self.Frma.pack()

        a=Product.product()

        chosen_val=tk.StringVar(self.Frame_Add_St)
        chosen_val.set("Select Product")
        
        global lst
        lst = a.returnall()
        n=1

        
        self.Stack_Product_Name_LA=Label(self.Frame_Add_St,text="Product Reference Name:")
        self.Stack_Product_Name_EN= ttk.Combobox(self.Frame_Add_St,textvariable=chosen_val)
        self.Stack_Product_Name_LA.pack()
        self.Stack_Product_Name_EN.pack()
        self.Stack_Product_Name_EN.config(width=20)
        self.Stack_Product_Name_EN['values']=([x[n] for x in lst])

        global ref_id_entry
        ref_id_entry=StringVar()
        self.Stack_Product_ID_Label=Label(self.Frame_Add_St,text="Reference ID:").pack()
        self.Stack_Product_ID_EN=Entry(self.Frame_Add_St,textvariable=ref_id_entry,state="disabled").pack()

        global ref_name_entry
        ref_name_entry=StringVar()
        self.Stack_Product_Name_Label=Label(self.Frame_Add_St,text="New Product Reference Name:").pack()
        self.Stack_Product_Name_ENN=Entry(self.Frame_Add_St,textvariable=ref_name_entry).pack()

        global ref_price_entry
        ref_price_entry=StringVar()
        self.Stack_Product_Name_Label=Label(self.Frame_Add_St,text="New Product Reference Price:").pack()
        self.Stack_Product_Price_EN=Entry(self.Frame_Add_St,textvariable=ref_price_entry).pack()

        self.submit=Button(self.Frame_Add_St, text="Submit Changes", padx=20, pady=5, command=self.Click_ref_submit).pack()

        self.Stack_Product_Name_EN.bind("<<ComboboxSelected>>",self.setRefVals)

    def Click_ref_submit(self):
        id=ref_id_entry.get()
        name=ref_name_entry.get()
        price=ref_price_entry.get()

        idd=int(id)
        
        pricee=int(price)
        priceee=float(pricee)

        Prod=Product.product()
        Prod.editReference(idd,name,priceee)

    def setRefVals(self,event):
        global choice
        choice=event.widget.get()
        res=[idx for idx, x in enumerate(lst) if x[1]==choice]
        item=lst[res[0]]
        price=item[2]
        name=item[1]
        id=item[0]

        ref_price_entry.set(price)
        ref_name_entry.set(name)
        ref_id_entry.set(id)


    def Click_Add_Ref(self):
        
        self.Add_Stack= Toplevel()
        self.Add_Stack.title("Add Product Reference")
        self.Add_Stack.geometry("800x527")

        self.Frame_Add_St=Frame(self.Add_Stack,width=800,height=500,)
        self.Frame_Add_St.place(x=0,y=0)

        self.Frma=Label(self.Frame_Add_St,text="Add Product Reference", width=20, font=("Arial", 35),anchor=W)
        self.Frma.place(x=10,y=10)

        self.Stack_Product_Name_LA=Label(self.Frame_Add_St,text="Product Name:")
        self.Stack_Product_Name_EN=Entry(self.Frame_Add_St,width=20,borderwidth=4)
        self.Stack_Product_Name_LA.place(x=160,y=80)
        self.Stack_Product_Name_EN.place(x=160,y=100)

        self.Stack_Product_Price_LA=Label(self.Frame_Add_St,text="Price:")
        global price_entry
        price_entry=tk.StringVar()
        self.Stack_Product_Price_EN= Entry(self.Frame_Add_St,width=20,textvariable=price_entry,borderwidth=4)
        self.Stack_Product_Price_LA.place(x=480,y=80)
        self.Stack_Product_Price_EN.place(x=480,y=100)

        self.Frame_List=Frame(self.Add_Stack,width=800,height=320)
        self.Frame_List.place(x=0,y=200)
        #Table
        self.frame_Table=ttk.Treeview(self.Frame_List,height=15)
        self.frame_Table['columns']=("ID","Name","Price")
        self.frame_Table.column("#0",width=0,stretch=NO)
        self.frame_Table.column("ID",anchor=W,width=100)
        self.frame_Table.column("Name",anchor=W,width=200)
        self.frame_Table.column("Price",anchor=CENTER,width=150)
        
        #Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID",text="ID",anchor=W)
        self.frame_Table.heading("Name",text="Product Name",anchor=W)
        self.frame_Table.heading("Price",text="Price",anchor=CENTER)
       
        self.frame_Table.pack(fill='both')
        self.frame_Table.grid(row=1,column=0)

        self.button_Add=Button(self.Frame_Add_St,text="Add",padx=20,pady=5,command=self.reference_Done)
        self.button_Add.place(x=715,y=160)

        self.button_Finish = Button(self.Frame_Add_St, text="Finish", padx=20, pady=5, state='disabled')
        self.button_Finish.place(x=715, y=200)

    def reference_Done(self):
        ProductName = self.Stack_Product_Name_EN.get()
        price = price_entry.get()
        id=randomNumGen.generateProductID()
        
        pricee=int(price)
        priceee=float(pricee)
        
        global vals
        vals=(id,ProductName,priceee)

        global count

        id=[]
        name=[]
        price=[]

        if 'count' not in globals():
            count = 0
        else:
            count += 1
        self.frame_Table.insert(parent='', index='end', iid=count, text=vals,values=(vals))
        vals=()

        for child in self.frame_Table.get_children():

            val=self.frame_Table.item(child)["values"]
            idd=randomNumGen.generateProductID()

            id.append(idd)
            name.append(val[1])         
            price.append(val[2])
          

            vals=list(zip(id,name,price))

        self.button_Finish.config(state='normal', command=self.AddReference)

    def AddReference(self):
        self.frame_Table.delete(*self.frame_Table.get_children())
        Prod=Product.product()
        Prod.addReference(vals)

    def Click_List(self):
        global Entry_Search
        global Search_Table
        window_list = Toplevel()
        window_list.title("Delivery Batch")
        window_list.geometry("500x430")

        window_Frame = Frame(window_list, width=400, height=100)
        window_Frame.grid(row=0, column=0)

        window_Frame2 = Frame(window_list, width=400, height=250, bg="blue")
        window_Frame2.grid(row=1, column=0)

        Search_Table = ttk.Treeview(window_Frame2, height=12)
        Search_Table['column'] = ("Batch Code", "Order Date", "Arrival Date")
        Search_Table.column("#0", width=0, stretch=NO, anchor=W)
        Search_Table.column("Batch Code", width=100, stretch=NO, anchor=W)
        Search_Table.column("Order Date", width=148, stretch=NO, anchor=W)
        Search_Table.column("Arrival Date", width=100, stretch=NO, anchor=E)


        Search_Table.heading("#0")
        Search_Table.heading("Batch Code", text="Batch Code", anchor=W)
        Search_Table.heading("Order Date", text="Order Date", anchor=W)
        Search_Table.heading("Arrival Date", text="Arrival Date", anchor=W)

        Search_Table.grid(row=0, column=0)

        Label_Search = Label(window_Frame, text="Search Batch:")
        Entry_Search = Entry(window_Frame, width=50, borderwidth=3)
        button_Search = Button(window_Frame, text="Mark Arrived", padx=5, pady=0, command=self.search)

        Label_Search.grid(row=0, column=0, sticky=W)
        Entry_Search.grid(row=0, column=1)
        button_Search.grid(row=0, column=3)

        m = Employee.Employee()
        m1 = m.ListAllBatches()
        count = 0

        for x in m1:
            count += 1
            Search_Table.insert(parent='', index='end', iid=count, text=x, values=x)



    def search(self):
        search_field = Entry_Search.get()

        e=Employee.Employee()
        e.MarkBatchArrived(search_field)

    def start(self,id):
        self.InvorGUI()
