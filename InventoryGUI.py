from logging import root
import datetime
from datetime import datetime

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tracemalloc import start
import Employee
import Manager
from tkcalendar import DateEntry
from PIL import Image, ImageTk

import Product
import randomNumGen

import pandas as pd
from openpyxl.workbook import Workbook
import os


class InvortoryGUI:

    def __init__(self):
        self.InvorVal = None

    def search(self):
        result = self.Entry_Search.get()

    # Chick List and stack Start~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def Click_List1(self):
        self.button_List.config(state="disabled")
        self.button_Stack.config(state="normal")
        self.button_Delivery.config(state="normal")
        self.button_Employee.config(state="normal")

        self.Frame_stack.pack_forget()
        self.Frame_Del.pack_forget()
        self.Frame_Empl.pack_forget()

        self.Frame_List.pack()
        self.Label_title = Label(self.Frame_List, text="List Page", font=("Arial", 15)).place(x=0, y=0)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")
        self.frame_Table = ttk.Treeview(self.Frame_List, height=21)
        self.frame_Table['columns'] = ("ID", "Name", "Status", "Price", "Quantity")
        self.frame_Table.column("#0", width=0, stretch=NO)
        self.frame_Table.column("ID", anchor=W, width=100, stretch=NO)
        self.frame_Table.column("Name", anchor=W, width=400, stretch=NO)
        self.frame_Table.column("Status", anchor=E, width=200, stretch=NO)
        self.frame_Table.column("Price", anchor=CENTER, width=131, stretch=NO)
        self.frame_Table.column("Quantity", anchor=E, width=200, stretch=NO)
        # Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID", text="ID", anchor=W)
        self.frame_Table.heading("Name", text="Product Name", anchor=W)
        self.frame_Table.heading("Status", text="Status", anchor=W)
        self.frame_Table.heading("Price", text="Price", anchor=CENTER)
        self.frame_Table.heading("Quantity", text="Quantity", anchor=W)
        self.frame_Table.place(x=0, y=30)
        m1 = Manager.Manager()
        result = m1.inventoryList()
        count = 0
        for x in result:
            count += 1
            self.frame_Table.insert(parent='', index='end', iid=count, text=x, values=x)

    def Click_Stack(self):
        self.button_List.config(state="normal")
        self.button_Stack.config(state="disabled")
        self.button_Delivery.config(state="normal")
        self.button_Employee.config(state="normal")

        self.Frame_List.pack_forget()
        self.Frame_Del.pack_forget()
        self.Frame_Empl.pack_forget()

        self.Frame_stack.pack(fill='both')
        self.Label_title = Label(self.Frame_stack, text="Stack Page", font=("Arial", 15)).place(x=0, y=0)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")
        self.frame_Table = ttk.Treeview(self.Frame_stack, height=21)
        self.frame_Table['columns'] = ("ID", "Name", "Items Sold", "Price", "Sales", "Date Purchased")
        self.frame_Table.column("#0", width=0, stretch=NO)
        self.frame_Table.column("ID", anchor=W, width=100, stretch=NO)
        self.frame_Table.column("Name", anchor=W, width=400, stretch=NO)
        self.frame_Table.column("Items Sold", anchor=W, width=100, stretch=NO)
        self.frame_Table.column("Price", anchor=CENTER, width=131, stretch=NO)
        self.frame_Table.column("Sales", anchor=E, width=100, stretch=NO)
        self.frame_Table.column("Date Purchased", anchor=E, width=200, stretch=NO)
        # Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID", text="Purchase ID", anchor=W)
        self.frame_Table.heading("Name", text="Product Name", anchor=W)
        self.frame_Table.heading("Items Sold", text="Items Sold", anchor=W)
        self.frame_Table.heading("Price", text="Price", anchor=CENTER)
        self.frame_Table.heading("Sales", text="Sales", anchor=W)
        self.frame_Table.heading("Date Purchased", text="Date Purchased", anchor=W)
        self.frame_Table.place(x=0, y=30)
        m1 = Manager.Manager()
        result = m1.productSales()
        count = 0
        for x in result:
            count += 1
            self.frame_Table.insert(parent='', index='end', iid=count, text=x, values=x)

    def Click_Delivery_onDouble_Click(self, event):
        item = self.frame_Table.selection()[0]
        batch = self.frame_Table.item(item)['values'][0]
        prod = Product.product()

        batch = (batch,)
        result = prod.retrieveBatch(batch)

        self.Add_Delivery = Toplevel()
        self.Add_Delivery.title("Confirm Delivery")
        self.Add_Delivery.geometry("800x550")
        self.Add_Delivery.resizable(False, False)

        self.Frame_Add = Frame(self.Add_Delivery, width=800, height=200)
        self.Frame_Add.place(x=0, y=0)

        self.Frame_ListD = Frame(self.Add_Delivery, width=800, height=320, highlightbackground="black",
                                 highlightthickness=1, padx=10, pady=10)
        self.Frame_ListD.place(x=0, y=200)

        global idd, namee, qty, price
        idd = StringVar()
        namee = StringVar()
        qty = StringVar()
        price = StringVar()

        self.Product_ID_LA = Label(self.Frame_Add, text="Product ID")
        self.Product_ID_EN = Entry(self.Frame_Add, width=20, textvariable=idd, borderwidth=4, state='disabled')
        self.Product_ID_LA.place(x=200, y=70)
        self.Product_ID_EN.place(x=200, y=90)

        self.Product_Price_LA = Label(self.Frame_Add, text="Product Name")
        self.Product_Price_EN = Entry(self.Frame_Add, width=20, textvariable=namee, borderwidth=4, state='disabled')
        self.Product_Price_LA.place(x=380, y=70)
        self.Product_Price_EN.place(x=380, y=90)

        self.Product_Stack_LA = Label(self.Frame_Add, text="Price")
        self.Product_price_EN = Entry(self.Frame_Add, width=20, textvariable=price, borderwidth=4, state='disabled')
        self.Product_Stack_LA.place(x=650, y=150)
        self.Product_price_EN.place(x=650, y=170)

        self.Product_date_LA = Label(self.Frame_Add, text="Expiry Date")
        self.Product_date_EN = DateEntry(self.Frame_Add, selectmode='day', width=20, state='disabled')
        self.Product_date_LA.place(x=450, y=120)
        self.Product_date_EN.place(x=450, y=140)

        self.Product_Stack_LA = Label(self.Frame_Add, text="Quantity")
        self.Product_Stack_EN = Entry(self.Frame_Add, width=20, textvariable=qty, borderwidth=4, state='disabled')
        self.Product_Stack_LA.place(x=520, y=70)
        self.Product_Stack_EN.place(x=520, y=90)

        Label(self.Frame_Add, text="Confirming Delivery will Mark it as Received and Sellable").place(x=100, y=130)

        self.frame_Table = ttk.Treeview(self.Frame_ListD, height=15)
        self.frame_Table['columns'] = ("ID", "Name", "Price", "Quantity", "Order Date", "Expiration Date")
        self.frame_Table.column("#0", width=0, stretch=NO)
        self.frame_Table.column("ID", anchor=W, width=50)
        self.frame_Table.column("Name", anchor=W, width=246)
        self.frame_Table.column("Price", anchor=CENTER, width=100)
        self.frame_Table.column("Quantity", anchor=E, width=80)
        self.frame_Table.column("Order Date", anchor=E, width=150)
        self.frame_Table.column("Expiration Date", anchor=E, width=150)

        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID", text="ID", anchor=W)
        self.frame_Table.heading("Name", text="Product Name", anchor=W)
        self.frame_Table.heading("Price", text="Price", anchor=CENTER)
        self.frame_Table.heading("Quantity", text="Quantity", anchor=W)
        self.frame_Table.heading("Order Date", text="Order Date", anchor=W)
        self.frame_Table.heading("Expiration Date", text="Expiration Date", anchor=W)

        self.frame_Table.pack(fill='both')
        self.frame_Table.grid(row=1, column=0)

        def confirm_delivery():
            prod = Product.product()
            id = idd.get()
            name = namee.get()
            qtyy = qty.get()

            for item in self.frame_Table.get_children():
                id = self.frame_Table.item(item)['values'][0]
                name = self.frame_Table.item(item)['values'][1]
                priceeee = self.frame_Table.item(item)['values'][2]
                qtyyy = self.frame_Table.item(item)['values'][3]
                datee = self.frame_Table.item(item)['values'][5]
                prod.editDelivery(id, name, priceeee, qtyyy, datee)

            self.frame_Table.delete(*self.frame_Table.get_children())

        self.button = Button(self.Frame_Add, text="Confirm Delivery", command=confirm_delivery)
        self.button.place(x=100, y=90)

        def saveChanges():
            selectedItem = self.frame_Table.selection()[0]
            x = self.frame_Table.item(item)['values'][4]
            self.frame_Table.item(selectedItem, values=(
            idd.get(), namee.get(), price.get(), qty.get(), x, self.frame_Table.item(item)['values'][5]))

        self.button = Button(self.Frame_Add, text="Save", command=saveChanges)
        self.button.place(x=700, y=90)

        def selectItem(event):
            selected_item = self.frame_Table.selection()[0]
            id = self.frame_Table.item(selected_item)['values'][0]
            name = self.frame_Table.item(selected_item)['values'][1]
            pricee = self.frame_Table.item(selected_item)['values'][2]
            quantity = self.frame_Table.item(selected_item)['values'][3]
            expire = self.frame_Table.item(selected_item)['values'][5]

            self.Product_Price_EN.config(state='normal')
            self.Product_Stack_EN.config(state='normal')
            self.Product_date_EN.config(state='normal')
            self.Product_price_EN.config(state='normal')

            date = datetime.strptime(expire, '%Y-%m-%d')

            self.Product_date_EN.set_date(date)
            idd.set(id)
            namee.set(name)
            qty.set(quantity)
            price.set(pricee)

        count = 0
        for i in result:
            self.frame_Table.insert(parent='', index='end', iid=count, text=i, values=i)
            count += 1

        self.frame_Table.bind("<Double-1>", selectItem)

    def Click_Delivery(self):
        self.button_List.config(state="normal")
        self.button_Stack.config(state="normal")
        self.button_Delivery.config(state="disabled")
        self.button_Employee.config(state="normal")

        self.Frame_List.pack_forget()
        self.Frame_stack.pack_forget()
        self.Frame_Empl.pack_forget()

        self.Frame_Del.pack()
        self.Label_title = Label(self.Frame_Del, text="Delivery Page", font=("Arial", 15)).place(x=0, y=0)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")
        self.frame_Table = ttk.Treeview(self.Frame_Del, height=21)
        self.frame_Table['columns'] = ("ID", "Name", "Detail", "Price", "Quantity", "Arrival")
        self.frame_Table.column("#0", width=0, stretch=NO)
        self.frame_Table.column("ID", anchor=W, width=100, stretch=NO)
        self.frame_Table.column("Name", anchor=W, width=400, stretch=NO)
        self.frame_Table.column("Detail", anchor=W, width=200, stretch=NO)
        self.frame_Table.column("Price", anchor=CENTER, width=91, stretch=NO)
        self.frame_Table.column("Quantity", anchor=E, width=100, stretch=OFF)
        self.frame_Table.column("Arrival", anchor=E, width=140, stretch=OFF)
        # Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID", text="Batch Code", anchor=W)
        self.frame_Table.heading("Name", text="Product Name", anchor=W)
        self.frame_Table.heading("Detail", text="Detail", anchor=W)
        self.frame_Table.heading("Price", text="Price", anchor=CENTER)
        self.frame_Table.heading("Quantity", text="Quantity", anchor=W)
        self.frame_Table.heading("Arrival", text="Arrival Day", anchor=W)
        self.frame_Table.place(x=0, y=30)
        self.frame_Table.bind("<Double-1>", self.Click_Delivery_onDouble_Click)

        m1 = Employee.Employee()
        result = m1.viewDeliveryList()
        count = 0
        for x in result:
            count += 1
            self.frame_Table.insert(parent='', index='end', iid=count, text=x, values=x)

    def Click_Employee(self):
        self.button_List.config(state="normal")
        self.button_Stack.config(state="normal")
        self.button_Delivery.config(state="normal")
        self.button_Employee.config(state="disabled")

        self.Frame_List.pack_forget()
        self.Frame_stack.pack_forget()
        self.Frame_Del.pack_forget()

        self.Frame_Empl.pack()
        self.Label_title = Label(self.Frame_Empl, text="Employee Page", font=("Arial", 15)).place(x=0, y=0)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")

        self.frame_Table = ttk.Treeview(self.Frame_Empl, height=21)
        self.frame_Table['columns'] = ("ID", "Name", "Username", "Detail")
        self.frame_Table.column("#0", width=0, stretch=NO)
        self.frame_Table.column("ID", anchor=W, width=98, stretch=NO)
        self.frame_Table.column("Name", anchor=W, width=420, stretch=NO)
        self.frame_Table.column("Username", anchor=W, width=280, stretch=NO)
        self.frame_Table.column("Detail", anchor=CENTER, width=230, stretch=NO)

        # Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID", text="Employee ID", anchor=W)
        self.frame_Table.heading("Name", text="Name", anchor=W)
        self.frame_Table.heading("Username", text="Username", anchor=W)
        self.frame_Table.heading("Detail", text="Role", anchor=CENTER)
        self.frame_Table.place(x=0, y=30)

        m1 = Manager.Manager()
        result = m1.viewEMPList()
        count = 0
        for x in result:
            count += 1
            self.frame_Table.insert(parent='', index='end', iid=count, text=x, values=x)

    # Chick List and stack END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Chick ADD START!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def Click_AddP(self):
        self.add_to_products

    def add_to_products(self):
        global order_date, arrival_date
        ProdName = self.Product_CODE_EN.get()
        date = self.Product_date_EN.get_date()
        expiry_date = self.Product_EXdate_EN.get_date()
        quantity = self.Product_Stack_EN.get()
        ProductIDD = randomNumGen.generateProductID()
        price = float(int(self.Product_Price_EN.get()))
        order_date = self.Product_date_EN.get_date()
        arrival_date = self.Product_Arrive_EN.get_date()

        var1 = "ProductID_list"
        var2 = "ProdName_list"
        var3 = "quantity_list"
        var4 = "price_list"
        var5 = "date_list"
        var6 = "expiry_date_list"
        var7 = "ref_id_list"

        if var1 not in globals() and var2 not in globals() and var3 not in globals() and var4 not in globals() and var5 not in globals() and var6 not in globals() and var7 not in globals():
            global ProductID_list, ProdName_list, ref_id_list, quantity_list, price_list, date_list, expiry_date_list, status_list, arrival_date_list, order_date_list

            ProductID_list = []
            ProdName_list = []
            quantity_list = []
            price_list = []
            date_list = []
            expiry_date_list = []
            order_date_list = []
            status_list = []
            ref_id_list = []

        prod = Product.product()
        ref_id = prod.get_ref_id(ProdName)

        ProductID_list.append(int(ProductIDD))
        ProdName_list.append(ProdName)
        quantity_list.append(int(quantity))
        price_list.append(price)
        date_list.append(date)
        expiry_date_list.append(expiry_date)
        order_date_list.append(order_date)
        status_list.append("Under Delivery")
        ref_id_list.append(ref_id[0][0])

        self.frame_Table.insert(parent='', index='end', iid=ProductIDD,
                                text=(ProductIDD, ProdName, price, quantity, date, expiry_date),
                                values=(ProductIDD, ProdName, price, quantity, date, expiry_date))

        self.Product_CODE_EN.delete(0, 'end')
        self.Product_Stack_EN.delete(0, 'end')
        self.Product_EXdate_EN.delete(0, 'end')
        self.Product_Price_EN.delete(0, 'end')

        self.AddDeliveries = Button(self.Frame_Add, text="Add to Delivery List", padx=15, pady=5,
                                    command=self.Add_Deliveries)
        self.AddDeliveries.place(x=544, y=150)

        self.button_Add.config(command=self.add_to_products)

    def Add_Deliveries(self):
        if 'batch_code' not in locals():
            batch_code = randomNumGen.generateBatchCode()
        if 'batch_code_list' not in locals():
            batch_code_list = []
        for i in ProductID_list:
            batch_code_list.append(batch_code)

        item_tuple = list(
            zip(ProductID_list, ref_id_list, ProdName_list, quantity_list, price_list, status_list, batch_code_list,
                expiry_date_list))

        values = (batch_code, order_date, arrival_date, 'Under Delivery')

        b = Product.product()
        b.add_deliveryBatch(values)

        b.addMany_Del(item_tuple)

        self.frame_Table.delete(*self.frame_Table.get_children())

        ProductID_list.clear()
        batch_code_list.clear()
        ProdName_list.clear()
        quantity_list.clear()
        price_list.clear()
        date_list.clear()
        expiry_date_list.clear()
        arrival_date_list.clear()
        order_date_list.clear()
        status_list.clear()


    def Click_Add(self):
        self.Add_Del.config(state='disabled')
        self.button_Add_Em.config(state='disabled')
        self.button_Add_Pm.config(state='disabled')
        self.btn_Notification.config(state='disabled')

        self.Add_Delivery = Toplevel()
        self.Add_Delivery.title("Add Products on Delivery")
        self.Add_Delivery.geometry("800x550")
        self.Add_Delivery.resizable(False, False)

        global btn, frame
        btn = self.Add_Del
        frame = self.Add_Delivery

        self.Add_Delivery.protocol("WM_DELETE_WINDOW", self.close_window)

        global lst
        a = Product.product()
        lst = a.returnall()
        n = 1

        self.Frame_Add = Frame(self.Add_Delivery, width=800, height=200)
        self.Frame_Add.place(x=0, y=0)

        self.chosen_val = tk.StringVar(self.Frame_Add)
        self.chosen_val.set("Select Product")
        global price_entry
        price_entry = tk.StringVar()

        self.APD = Label(self.Frame_Add, text="Add Products on Delivery", font=("Arial", 40)).place(x=10, y=5)
        self.Product_CODE_LA = Label(self.Frame_Add, text="Select Product Name")
        self.Product_CODE_EN = ttk.Combobox(self.Frame_Add, textvariable=self.chosen_val, state='readonly', width=50)
        self.Product_CODE_LA.place(x=20, y=70)
        self.Product_CODE_EN.place(x=20, y=90)

        if lst != "empty":
            self.Product_CODE_EN['values'] = ([x[n] for x in lst])

        self.Product_CODE_EN.bind("<<ComboboxSelected>>", self.setPrice)

        self.Product_date_LA = Label(self.Frame_Add, text="Date")
        self.Product_date_EN = DateEntry(self.Frame_Add, selectmode='day', width=20)
        self.Product_date_LA.place(x=20, y=120)
        self.Product_date_EN.place(x=20, y=140)

        self.Product_Exdate_LA = Label(self.Frame_Add, text="Expiration Date")
        self.Product_EXdate_EN = DateEntry(self.Frame_Add, selectmode='day', width=20)
        self.Product_Exdate_LA.place(x=200, y=120)
        self.Product_EXdate_EN.place(x=200, y=140)

        self.Product_Arrive_LA = Label(self.Frame_Add, text="Arrival Date")
        self.Product_Arrive_EN = DateEntry(self.Frame_Add, selectmode='day', width=20)
        self.Product_Arrive_LA.place(x=380, y=120)
        self.Product_Arrive_EN.place(x=380, y=140)

        self.Product_Price_LA = Label(self.Frame_Add, text="Price")
        self.Product_Price_EN = Entry(self.Frame_Add, width=20, borderwidth=4, textvariable=price_entry,
                                      state='disabled')
        self.Product_Price_LA.place(x=380, y=70)
        self.Product_Price_EN.place(x=380, y=90)

        self.Product_Stack_LA = Label(self.Frame_Add, text="Quantity")
        self.Product_Stack_EN = Entry(self.Frame_Add, width=20, borderwidth=4)
        self.Product_Stack_LA.place(x=520, y=70)
        self.Product_Stack_EN.place(x=520, y=90)

        self.button_Add = Button(self.Frame_Add, text="Add", padx=20, pady=5, command=self.add_to_products)
        self.button_Add.place(x=700, y=150)

        self.button_Delete = Button(self.Frame_Add, text="Delete", padx=20, pady=5, command=self.Delete)
        self.button_Delete.place(x=700, y=110)

        self.Frame_List1 = Frame(self.Add_Delivery, width=800, height=320, highlightbackground="black",
                                 highlightthickness=1, padx=10, pady=10)
        self.Frame_List1.place(x=0, y=200)
        # Table
        self.frame_Table = ttk.Treeview(self.Frame_List1, height=15)
        self.frame_Table['columns'] = ("ID", "Name", "Price", "Quantity", "Order Date", "Expiration Date")
        self.frame_Table.column("#0", width=0, stretch=NO)
        self.frame_Table.column("ID", anchor=W, width=50)
        self.frame_Table.column("Name", anchor=W, width=246)
        self.frame_Table.column("Price", anchor=CENTER, width=100)
        self.frame_Table.column("Quantity", anchor=E, width=80)
        self.frame_Table.column("Order Date", anchor=E, width=150)
        self.frame_Table.column("Expiration Date", anchor=E, width=150)
        # Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID", text="ID", anchor=W)
        self.frame_Table.heading("Name", text="Product Name", anchor=W)
        self.frame_Table.heading("Price", text="Price", anchor=CENTER)
        self.frame_Table.heading("Quantity", text="Quantity", anchor=W)
        self.frame_Table.heading("Order Date", text="Order Date", anchor=W)
        self.frame_Table.heading("Expiration Date", text="Expiration Date", anchor=W)

        self.frame_Table.pack(fill='both')
        self.frame_Table.grid(row=1, column=0)
        self.Add_Delivery.mainloop()

    # employee
    def Click_AddS_Em(self):
        username = self.username.get()
        password = self.password.get()
        Fname = self.Fname.get()
        role = self.chosen_val.get()

        print(username, password, Fname, role)
        man = Manager.Manager()
        id = randomNumGen.generateEmpID()
        man.AddEmp(id, Fname, username, password, role)

    def Click_Add_Em(self):
        self.Add_Del.config(state='disabled')
        self.button_Add_Em.config(state='disabled')
        self.button_Add_Pm.config(state='disabled')
        self.btn_Notification.config(state='disabled')

        self.Add_Employee = Toplevel()
        self.Add_Employee.title("Employeee!")
        self.Add_Employee.geometry("500x400")
        self.Add_Employee.resizable(False, False)

        global btn, frame
        btn = self.button_Add_Em
        frame = self.Add_Employee

        self.Add_Employee.protocol("WM_DELETE_WINDOW", self.close_window)

        self.Frame_Add_Em = Frame(self.Add_Employee, width=800, height=500, )
        self.Frame_Add_Em.place(x=0, y=0)

        Frma = Label(self.Frame_Add_Em, text="Add Employee", width=20, font=("Arial", 35), anchor=W)
        Frma.place(x=20, y=20)

        self.Fname = StringVar()
        self.Employee_Lname_LA = Label(self.Frame_Add_Em, text="Full Name:")
        self.Employee_Lname_EN = Entry(self.Frame_Add_Em, width=60, borderwidth=4, textvariable=self.Fname)
        self.Employee_Lname_LA.place(x=60, y=110)
        self.Employee_Lname_EN.place(x=60, y=130)

        self.Employee_Username_LA = Label(self.Frame_Add_Em, text="Username:")
        self.username = StringVar()
        self.Employee_Username_EN = Entry(self.Frame_Add_Em, width=60, textvariable=self.username, borderwidth=4)
        self.Employee_Username_LA.place(x=60, y=160)
        self.Employee_Username_EN.place(x=60, y=180)

        self.Employee_Password_LA = Label(self.Frame_Add_Em, text="Password:")
        self.password = StringVar()
        self.Employee_Password_EN = Entry(self.Frame_Add_Em, width=60, textvariable=self.password, show="*",
                                          borderwidth=4)
        self.Employee_Password_LA.place(x=60, y=210)
        self.Employee_Password_EN.place(x=60, y=230)

        self.Employee_Role_LA = Label(self.Frame_Add_Em, text="Role:")
        self.chosen_val = tk.StringVar(self.Frame_Add_Em)
        self.chosen_val.set("Select Role")
        self.Role = ttk.Combobox(self.Frame_Add_Em, textvariable=self.chosen_val, state='readonly')
        self.Role['values'] = ('Cashier', 'Manager')
        self.Role.place(x=60, y=280)
        self.Employee_Role_LA.place(x=60, y=260)

        self.button_Add = Button(self.Frame_Add_Em, text="Add", padx=20, pady=5, command=self.Click_AddS_Em)
        self.button_Add.place(x=360, y=330)
        self.Add_Employee.mainloop()

    def AddProduct(self):
        self.frame_Table.delete(*self.frame_Table.get_children())

        Prod = Product.product()
        Prod.addMany(vals)

    # stack
    def DoneAdd_Product(self):

        ProductName = self.Stack_Product_Name_EN.get()

        Quantity = self.Stack_Product_Size_EN.get()
        price = price_entry.get()

        id = randomNumGen.generateProductID()

        if Quantity.isdigit():
            Quantityy = int(Quantity)

        pricee = float(int(float(price)))
        global vals
        vals = (id, ProductName, pricee, Quantityy)

        global count

        id = []
        name = []
        quantity = []
        price = []
        batch_code = []
        status = []

        if 'count' not in globals():
            count = 0
        else:
            count += 1
        self.frame_Table.insert(parent='', index='end', iid=count, text=vals, values=(vals))
        vals = ()
        batch = randomNumGen.generateBatchCode()

        for child in self.frame_Table.get_children():
            val = self.frame_Table.item(child)["values"]
            idd = randomNumGen.generateProductID()

            id.append(idd)
            batch_code.append(batch)
            name.append(val[1])
            quantity.append(val[2])
            price.append(val[3])
            status.append("Added")

            vals = list(zip(id, name, quantity, price, batch_code, status))

        self.button_Finish.config(state='normal', command=self.AddProduct)

    def setPrice(self, event):
        choice = event.widget.get()
        res = [idx for idx, x in enumerate(lst) if x[1] == choice]
        item = lst[res[0]]
        price = item[2]
        price_entry.set(price)

    def Click_Add_Product(self):
        self.Add_Del.config(state='disabled')
        self.button_Add_Em.config(state='disabled')
        self.button_Add_Pm.config(state='disabled')
        self.btn_Notification.config(state='disabled')

        self.Add_Stack = Toplevel()
        self.Add_Stack.title("Add Product")
        self.Add_Stack.geometry("800x540")
        self.Add_Stack.resizable(False, False)

        global btn, frame
        btn = self.button_Add_Pm
        frame = self.Add_Stack

        self.Add_Stack.protocol("WM_DELETE_WINDOW", self.close_window)

        self.Frame_Add_St = Frame(self.Add_Stack, width=800, height=505, )
        self.Frame_Add_St.place(x=0, y=0)

        self.Frma = Label(self.Frame_Add_St, text="Add Product", width=20, font=("Arial", 35), anchor=W)
        self.Frma.place(x=10, y=10)

        a = Product.product()

        self.chosen_val = tk.StringVar(self.Frame_Add_St)
        self.chosen_val.set("Select Product")

        global lst
        lst = a.returnall()
        n = 1

        self.Stack_Product_Name_LA = Label(self.Frame_Add_St, text="Product Name:")
        self.Stack_Product_Name_EN = ttk.Combobox(self.Frame_Add_St, textvariable=self.chosen_val)
        self.Stack_Product_Name_LA.place(x=20, y=80)
        self.Stack_Product_Name_EN.place(x=20, y=100)
        self.Stack_Product_Name_EN.config(width=50)

        if lst != 'empty':
            self.Stack_Product_Name_EN['values'] = ([x[n] for x in lst])

        self.Frame_ListAP = Frame(self.Add_Stack, width=800, height=320, padx=10, pady=10, highlightbackground="black",
                                  highlightthickness=1)
        self.Frame_ListAP.place(x=0, y=150)
        # Table
        self.frame_Table = ttk.Treeview(self.Frame_ListAP, height=17)
        self.frame_Table['columns'] = ("ID", "Name", "Price")
        self.frame_Table.column("#0", width=0, stretch=NO)
        self.frame_Table.column("ID", anchor=W, width=90)
        self.frame_Table.column("Name", anchor=W, width=555)
        self.frame_Table.column("Price", anchor=CENTER, width=130)
        # Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID", text="ID", anchor=W)
        self.frame_Table.heading("Name", text="Product Name", anchor=W)
        self.frame_Table.heading("Price", text="Price", anchor=W)
        self.frame_Table.pack(fill='both')
        self.frame_Table.grid(row=1, column=0)

        a = Product.product()
        res = a.returnall()

        for i in res:
            self.frame_Table.insert(parent='', index='end', iid=i[0], text=i, values=i)

        def AddProduct_ChangeName(event):
            global val
            val = self.chosen_val.get()
            val = (val)

        def search():
            a = Product.product()
            res = a.return_one(val)

            self.frame_Table.delete(*self.frame_Table.get_children())
            for i in res:
                self.frame_Table.insert(parent='', index='end', iid=i[0], text=i, values=i)

        def edit():

            var = self.chosen_val.get()

            self.Click_Edit_Ref(var)

        self.Stack_Product_Name_EN.bind("<<ComboboxSelected>>", AddProduct_ChangeName)

        self.button_Find = Button(self.Frame_Add_St, text="Search", padx=20, pady=5, command=search)
        self.button_Find.place(x=350, y=90)

        self.button_Add = Button(self.Frame_Add_St, text="Add Product", padx=20, pady=5, command=self.Click_Add_Ref)
        self.button_Add.place(x=500, y=90)

        self.button_Edit = Button(self.Frame_Add_St, text="Edit", padx=20, pady=5, command=edit)
        self.button_Edit.place(x=623, y=90)

        self.button_Delete = Button(self.Frame_Add_St, text="Delete", padx=20, pady=5, command=self.Delete)
        self.button_Delete.place(x=700, y=90)

        self.Add_Stack.update()

        self.Add_Stack.mainloop()

    def Delete(self):
        select = self.frame_Table.selection()[0]
        self.frame_Table.delete(select)

    # start UI for Notification ---------------
    def notify_UI(self):
        self.Add_Del.config(state='disabled')
        self.button_Add_Em.config(state='disabled')
        self.button_Add_Pm.config(state='disabled')
        self.btn_Notification.config(state='disabled')

        self.Add_Notify = Toplevel()

        global btn, frame
        btn = self.btn_Notification
        frame = self.Add_Notify

        self.Add_Notify.protocol("WM_DELETE_WINDOW", self.close_window)
        self.Add_Notify.title("Export to Spreadsheet")
        self.Add_Notify.geometry("800x583")
        self.Add_Notify.resizable(False, False)

        self.Frame_Add_nofi = Frame(self.Add_Notify, width=800, height=200)
        self.Frame_Add_nofi.place(x=0, y=0)

        self.Frma = Label(self.Frame_Add_nofi, text="Export to Spreadsheet", width=20, font=("Arial", 35), anchor=W)
        self.Frma.place(x=10, y=10)

        Label(self.Add_Notify, text="Select What to Export").place(x=20, y=70)
        reports = ttk.Combobox(self.Add_Notify, width=20)
        reports.place(x=20, y=90)
        reports['values'] = ("Sales", "Inventory", "Delivery")

        Label(self.Add_Notify, text="Select Date Scope").place(x=250, y=70)
        scope = DateEntry(self.Add_Notify, selectmode='day', width=20)
        scope.place(x=250, y=90)

        Label(self.Add_Notify, text="Click this Button to Start Exporting").place(x=450, y=70)
        export = Button(self.Add_Notify, text="Export", state='disabled')
        export.place(x=500, y=90)

        # Table for Exports ; this dont filter out with the data to be exported =========================

        self.export_Table = ttk.Treeview(self.Add_Notify, height=15)
        self.export_Table['columns'] = (
        "Invoice Number", "Item", "Quantity", "Total Price", "Discount", "Date Purchased")
        self.export_Table.column("#0", width=0, stretch=NO)
        self.export_Table.column("Invoice Number", anchor=W, width=100)
        self.export_Table.column("Item", anchor=W, width=250)
        self.export_Table.column("Quantity", anchor=E, width=100)
        self.export_Table.column("Total Price", anchor=E, width=100)
        self.export_Table.column("Discount", anchor=E, width=100)
        self.export_Table.column("Date Purchased", anchor=E, width=100)

        self.export_Table.heading("#0")
        self.export_Table.heading("Invoice Number", text="Invoice Number", anchor=W)
        self.export_Table.heading("Item", text="Item", anchor=W)
        self.export_Table.heading("Quantity", text="Quantity", anchor=W)
        self.export_Table.heading("Total Price", text="Total Price", anchor=W)
        self.export_Table.heading("Discount", text="Discount", anchor=W)
        self.export_Table.heading("Date Purchased", text="Date Purchased", anchor=W)

        self.export_Table.place(x=0, y=250)

        # ==========================================================================================

        def export_report():
            report_type = reports.get()
            date = scope.get_date()
            man = Manager.Manager()
            result = man.get_export_data(report_type, date)
            if report_type == 'Sales':
                df = pd.DataFrame(result, columns=['Invoice Number', 'Purchase ID', 'Item', 'Quantity', 'Total Price',
                                                   'Discount', 'Date Purchased'])
            if report_type == 'Inventory':
                df = pd.DataFrame(result, columns=['Reference ID', "Item", "Price", "Remaining Quantity"])
            if report_type == "Delivery":
                df = pd.DataFrame(result, columns=['Batch Code', 'Item', 'Quantity', 'Price', 'Status'])
            title = str.lower(report_type) + str(date) + '.xlsx'
            df.to_excel(title, "Sales")
            message = "Saved to ", title
            messagebox.showinfo("Exported Successfully", "Saved to " + title)

        
        def reports_callback(event):
            export.config(state='normal', command=export_report)

            self.export_Table.delete(*self.export_Table.get_children())
            report_type = reports.get()
            date = scope.get_date()
            man = Manager.Manager()
            result = man.get_export_data(report_type, date)

            count = 0
            for item in result:
                self.export_Table.insert('', index='end', iid=count, text=item, values=(item))
                count += 1

        reports.bind('<<ComboboxSelected>>',reports_callback)
        scope.bind('<<DateEntrySelected>>',reports_callback)

        # Accidentally Replaced lines 843 and 844, which is essential ===========

        # self.Frame_ListN = Frame(self.Add_Notify, width=800, height=400, highlightbackground="black",
        #                          highlightthickness=1, padx=10, pady=10)
        # self.Frame_ListN.place(x=0, y=140)
        # self.frame_Table = ttk.Treeview(self.Frame_ListN, height=20)
        # self.frame_Table['columns'] = ("ID", "Name", "Days", "Expiration_Date")
        # self.frame_Table.column("#0", width=0, stretch=NO)
        # self.frame_Table.column("ID", anchor=W, width=73)
        # self.frame_Table.column("Name", anchor=W, width=403)
        # self.frame_Table.column("Days", anchor=CENTER, width=150)
        # self.frame_Table.column("Expiration_Date", anchor=W, width=150)
        # # Table Head
        # self.frame_Table.heading("#0")
        # self.frame_Table.heading("ID", text="ID", anchor=W)
        # self.frame_Table.heading("Name", text="Product Name", anchor=W)
        # self.frame_Table.heading("Days", text="Day", anchor=CENTER)
        # self.frame_Table.heading("Expiration_Date", text="Expiration Date", anchor=W)
        # self.frame_Table.pack(fill='both')
        # self.frame_Table.grid(row=1, column=0)

        # ====================================================
        
        self.Add_Notify.mainloop()
        # END

    # Chick ADD END!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def InvorGUI(self):
        self.InvorVal = Tk()
        self.InvorVal.title("Cresdel Pharmacy!!")
        width = self.InvorVal.winfo_screenwidth()
        height = self.InvorVal.winfo_screenheight()
        self.InvorVal.geometry("%dx%d" % (width, height))
        self.InvorVal.resizable(False, False)

        # For the Page 1 Detail
        self.Frame_Detail = Frame(self.InvorVal, width=1063, height=200, highlightbackground="black",
                                  highlightthickness=3, padx=10, pady=10)
        self.Frame_Detail.place(x=0, y=0)
        # self.img = PhotoImage(Image.open(r"C:\Users\Administrator\Documents\GitHub\Logo\123.jpg"))
        # self.label=Label(self.Frame_Detail,image=self.img,width=37,height=10)
        # self.label.place(x=0,y=0)

        # For the Page LIST
        self.Frame_main = Frame(self.InvorVal, width=1063, height=498, highlightbackground="black",
                                highlightthickness=3)
        self.Frame_main.place(x=0, y=199)
        self.Frame_List = Frame(self.Frame_main, width=1058, height=498, padx=10, pady=10)
        self.Frame_stack = Frame(self.Frame_main, width=1058, height=498, padx=10, pady=10)
        self.Frame_Empl = Frame(self.Frame_main, width=1058, height=498, padx=10, pady=10)
        self.Frame_Del = Frame(self.Frame_main, width=1058, height=498, padx=10, pady=10)

        # For the Side
        self.Frame_Side = Frame(self.InvorVal, width=300, height=697, highlightbackground="black", highlightthickness=3,
                                padx=10, pady=10)
        self.Frame_Side.place(x=1060, y=0)

        Detail = Label(self.Frame_Side, text="Detail Button", width=37, anchor=W).place(x=40, y=270)
        self.button_List = Button(self.Frame_Side, text="List", padx=10, pady=10, width=10, height=1, bg='#54FA9B',
                                  command=self.Click_List1)
        self.button_Stack = Button(self.Frame_Side, text="Stack", padx=10, pady=10, width=10, height=1, bg='#54FA9B',
                                   command=self.Click_Stack)
        self.button_Delivery = Button(self.Frame_Side, text="Delivery", padx=10, pady=10, width=10, height=1,
                                      bg='#54FA9B', command=self.Click_Delivery)
        self.button_Employee = Button(self.Frame_Side, text="Employeee", padx=10, pady=10, width=10, height=1,
                                      bg='#54FA9B', command=self.Click_Employee)

        label = Label(self.Frame_Side, text="IMAGE").place(x=100, y=10)
        Add = Label(self.Frame_Side, text="ADD Button", width=37, anchor=W).place(x=40, y=420)
        self.Add_Del = Button(self.Frame_Side, text="ADD Delivery", padx=10, pady=10, width=10, height=1, bg='#54FA9B',
                              command=self.Click_Add)
        self.button_Add_Em = Button(self.Frame_Side, text="ADD Employee", padx=10, pady=10, width=10, height=1,
                                    bg='#54FA9B', command=self.Click_Add_Em)
        self.button_Add_Pm = Button(self.Frame_Side, text="ADD Product", padx=10, pady=10, width=10, height=1,
                                    bg='#54FA9B', command=self.Click_Add_Product)
        self.btn_Notification = Button(self.Frame_Side, text="Export", padx=10, pady=10, width=10, height=1,
                                       bg='#54FA9B', command=self.notify_UI)

        self.button_List.place(x=40, y=300)
        self.button_Stack.place(x=160, y=300)
        self.button_Delivery.place(x=40, y=350)
        self.button_Employee.place(x=160, y=350)

        self.Add_Del.place(x=40, y=450)
        self.button_Add_Em.place(x=160, y=450)
        self.button_Add_Pm.place(x=40, y=500)
        # self.button_Add_prodref.place(x=160,y=500)
        self.btn_Notification.place(x=160, y=500)

        self.InvorVal.mainloop()

    def Click_Edit_Ref(self, var):
        self.Add_Stack = Toplevel()
        self.Add_Stack.title("Edit Product Reference")
        self.Add_Stack.geometry("700x350")

        self.Frame_Add_St = Frame(self.Add_Stack, width=700, height=350, )
        self.Frame_Add_St.grid(row=0, column=0)

        self.Frma = Label(self.Frame_Add_St, text="Edit Product!!", width=20, font=("Arial", 35), anchor=W)
        self.Frma.place(x=20, y=10)

        a = Product.product()

        global lst
        lst = a.return_one(var)

        idd = lst[0][0]
        namee = lst[0][1]
        pricee = lst[0][2]

        self.Old = Label(self.Frame_Add_St, text="Old Product Name", width=20, font=("Arial", 15), anchor=W)
        self.Old.place(x=50, y=70)

        global ref_id_entry, name, price
        ref_id_entry = StringVar()
        name = StringVar()
        price = StringVar()

        self.Stack_Product_ID_Label = Label(self.Frame_Add_St, text="ID:").place(x=50, y=110)
        self.Stack_Product_ID_EN = Entry(self.Frame_Add_St, width=10, borderwidth=5, textvariable=ref_id_entry,
                                         state="disabled")
        self.Stack_Product_ID_EN.place(x=50, y=130)

        self.Stack_Product_Item_Label = Label(self.Frame_Add_St, text="Product Name:", ).place(x=130, y=110)
        self.Stack_Product_Item_ENN = Entry(self.Frame_Add_St, width=70, textvariable=name, borderwidth=5,
                                            state="disabled")
        self.Stack_Product_Item_ENN.place(x=130, y=130)

        self.Stack_Product_ID_Label = Label(self.Frame_Add_St, text="Price:").place(x=570, y=110)
        self.Stack_Product_PRICE_EN = Entry(self.Frame_Add_St, textvariable=price, width=15, borderwidth=5,
                                            state="disabled")
        self.Stack_Product_PRICE_EN.place(x=570, y=130)

        self.Stack_Product_ID_EN.config(state='normal')
        self.Stack_Product_ID_EN.config(state='normal')
        self.Stack_Product_PRICE_EN.config(state='normal')

        ref_id_entry.set(idd)
        name.set(namee)
        price.set(pricee)

        self.Stack_Product_ID_EN.config(state='disabled')
        self.Stack_Product_ID_EN.config(state='disabled')
        self.Stack_Product_PRICE_EN.config(state='disabled')

        self.New = Label(self.Frame_Add_St, text="New Product Name", width=20, font=("Arial", 15), anchor=W)
        self.New.place(x=50, y=180)

        global ref_name_entry
        ref_name_entry = StringVar()
        self.Stack_Product_Name_Label = Label(self.Frame_Add_St, text="New Product Name:").place(x=50, y=210)
        self.Stack_Product_Name_ENN = Entry(self.Frame_Add_St, width=83, borderwidth=5,
                                            textvariable=ref_name_entry).place(x=50, y=230)

        global ref_price_entry
        ref_price_entry = StringVar()
        self.Stack_Product_Name_Label = Label(self.Frame_Add_St, text="New Product Price:").place(x=570, y=210)
        self.Stack_Product_Price_EN = Entry(self.Frame_Add_St, width=15, borderwidth=5,
                                            textvariable=ref_price_entry).place(x=570, y=230)

        self.submit = Button(self.Frame_Add_St, text="Submit Changes", padx=20, pady=5,
                             command=self.Click_ref_submit).place(x=450, y=280)

        self.button_Out = Button(self.Frame_Add_St, text="Cancel", padx=9, pady=5, bg="green",
                                 command=self.Add_Stack.destroy)
        self.button_Out.place(x=600, y=280)

    def Click_ref_submit(self):
        id = ref_id_entry.get()
        name = ref_name_entry.get()
        price = ref_price_entry.get()

        idd = int(id)
        pricee = int(price)
        priceee = float(pricee)

        Prod = Product.product()
        Prod.editReference(idd, name, priceee)

    def setRefVals(self, event):
        global choice
        choice = event.widget.get()
        res = [idx for idx, x in enumerate(lst) if x[1] == choice]
        item = lst[res[0]]
        price = item[2]
        name = item[1]
        id = item[0]

        ref_price_entry.set(price)
        ref_name_entry.set(name)
        ref_id_entry.set(id)

    def Click_Add_Ref(self):

        self.Add_Stack = Toplevel()
        self.Add_Stack.title("Add Product Reference")
        self.Add_Stack.geometry("700x543")

        self.Frame_Add_St = Frame(self.Add_Stack, width=700, height=350, )
        self.Frame_Add_St.grid(row=0, column=0)

        self.Frma = Label(self.Frame_Add_St, text="Add Product!!", width=20, font=("Arial", 40), anchor=W)
        self.Frma.place(x=20, y=10)

        self.Stack_Product_Name_Label = Label(self.Frame_Add_St, text="Product Name:").place(x=30, y=90)
        self.Stack_Product_Name_EN = Entry(self.Frame_Add_St, width=70, borderwidth=5)
        self.Stack_Product_Name_EN.place(x=30, y=110)

        global price_entry
        price_entry = tk.StringVar()
        self.Stack_Product_Price_Label = Label(self.Frame_Add_St, text="Price:").place(x=470, y=90)
        self.Stack_Product_Price_EN = Entry(self.Frame_Add_St, width=15, borderwidth=5, textvariable=price_entry).place(
            x=470, y=110)

        self.Frame_ListS = Frame(self.Add_Stack, width=800, height=320, highlightbackground="black",
                                 highlightthickness=3, padx=5, pady=5)
        self.Frame_ListS.place(x=0, y=200)
        # Table
        self.frame_Table = ttk.Treeview(self.Frame_ListS, height=15)
        self.frame_Table['columns'] = ("ID", "Name", "Price")
        self.frame_Table.column("#0", width=0, stretch=NO)
        self.frame_Table.column("ID", anchor=W, width=100)
        self.frame_Table.column("Name", anchor=W, width=482)
        self.frame_Table.column("Price", anchor=E, width=100)
        # Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID", text="ID", anchor=W)
        self.frame_Table.heading("Name", text="Product Name", anchor=W)
        self.frame_Table.heading("Price", text="Price", anchor=W)

        self.frame_Table.pack(fill='both')
        self.frame_Table.grid(row=1, column=0)

        self.button_Add = Button(self.Frame_Add_St, text="Add", padx=20, pady=5, command=self.reference_Done)
        self.button_Add.place(x=360, y=150)

        self.button_Delete = Button(self.Frame_Add_St, text="Delete", padx=20, pady=5, command=self.Delete)
        self.button_Delete.place(x=440, y=150)

        self.button_Finish = Button(self.Frame_Add_St, text="Finish", padx=20, pady=5, state='disabled')
        self.button_Finish.place(x=530, y=150)

        self.button_Cancel = Button(self.Frame_Add_St, text="Cancel", padx=9, pady=5, bg="green",
                                    command=self.Add_Stack.destroy)
        self.button_Cancel.place(x=620, y=150)

    def reference_Done(self):
        ProductName = self.Stack_Product_Name_EN.get()
        price = price_entry.get()
        id = randomNumGen.generateProductID()

        pricee = int(price)
        priceee = float(pricee)

        global vals
        vals = (id, ProductName, priceee)

        global count

        id = []
        name = []
        price = []

        if 'count' not in globals():
            count = 0
        else:
            count += 1
        self.frame_Table.insert(parent='', index='end', iid=count, text=vals, values=(vals))
        vals = ()

        for child in self.frame_Table.get_children():
            val = self.frame_Table.item(child)["values"]
            idd = randomNumGen.generateProductID()

            id.append(idd)
            name.append(val[1])
            price.append(val[2])

            vals = list(zip(id, name, price))

        self.button_Finish.config(state='normal', command=self.AddReference)

    def AddReference(self):
        self.frame_Table.delete(*self.frame_Table.get_children())
        Prod = Product.product()
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

    def close_window(self):
        self.Add_Del.config(state='normal')
        self.button_Add_Em.config(state='normal')
        self.button_Add_Pm.config(state='normal')
        self.btn_Notification.config(state='normal')
        frame.destroy()

    def start(self, id):
        self.InvorGUI()