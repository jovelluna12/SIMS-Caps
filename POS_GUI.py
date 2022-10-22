from ast import Delete
import Manager, Employee
import Product
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class PointOfSale_GUI:

    def __init__(self):
        self.POSGUI = None

        #global user_id
        #def start(id):
        #    user_id=id

        # Button logic
    def Button_LOGIC(self,Number):
        current = self.Product_CODE_EN.get()
        self.Product_CODE_EN.delete(0, END)
        self.Product_CODE_EN.insert(0, str(current) + str(Number))

        # Button List
    def Click_List(self):
        global Entry_Search
        global Search_Table
        window_list = Toplevel()
        window_list.title("PRODUCT LISTS!")
        window_list.geometry("400x320")

        window_Frame = Frame(window_list, width=400, height=100)
        window_Frame.grid(row=0, column=0)

        window_Frame2 = Frame(window_list, width=400, height=250, bg="blue")
        window_Frame2.grid(row=1, column=0)

        Search_Table = ttk.Treeview(window_Frame2, height=12)
        Search_Table['column'] = ("ID", "Name", "Price", "Stack")
        Search_Table.column("#0", width=0, stretch=NO, anchor=W)
        Search_Table.column("ID", width=50, stretch=NO, anchor=W)
        Search_Table.column("Name", width=148, stretch=NO, anchor=W)
        Search_Table.column("Price", width=100, stretch=NO, anchor=E)
        Search_Table.column("Stack", width=80, stretch=NO, anchor=E)

        Search_Table.heading("#0")
        Search_Table.heading("ID", text="ID", anchor=W)
        Search_Table.heading("Name", text="Name", anchor=W)
        Search_Table.heading("Price", text="Price", anchor=W)
        Search_Table.heading("Stack", text="Stack", anchor=W)
        Search_Table.grid(row=0, column=0)

        Label_Search = Label(window_Frame, text="Search:")
        Entry_Search = Entry(window_Frame, width=50, borderwidth=3)
        button_Search = Button(window_Frame, text="Search", padx=5, pady=0, command=self.search)

        Label_Search.grid(row=0, column=0, sticky=W)
        Entry_Search.grid(row=0, column=1)
        button_Search.grid(row=0, column=3)

        window_Frame3 = Frame(window_list, width=400, height=50, bg="blue")
        window_Frame3.grid(row=2, column=0)

        m = Manager.Manager()
        m1 = m.viewInv()
        count = 0
        if len(m1) == 0:
             for item in Search_Table.get_children():
                 Search_Table.delete(item)
        else:
             for x in m1:
                 count += 1
                 Search_Table.insert(parent='', index='end', iid=count, text=x, values=x)

        button_Close = Button(window_Frame3, text="Close", command=window_list.destroy)
        button_Close.pack()

    def search(self):
        search_field = Entry_Search.get()
        search = Product.product()

        if (not(search_field and search_field.strip())):
            for item in Search_Table.get_children():
                Search_Table.delete(item)

            m = Manager.Manager()
            m1 = m.viewInv()
            count = 0
            if len(m1)==0:
                for item in Search_Table.get_children():
                    Search_Table.delete(item)
            else:
                for x in m1:
                    count += 1
                    Search_Table.insert(parent='', index='end', iid=count, text=x, values=x)
        else:
            for item in Search_Table.get_children():
                Search_Table.delete(item)

            result = search.viewALL(search_field)
            count = 0
            if result=="empty":
                for item in Search_Table.get_children():
                    Search_Table.delete(item)
            else:
                for x in result:
                    count += 1
                    Search_Table.insert(parent='', index='end', iid=count, text=x, values=x)

    def SearchItem(self,buttonpress):
        ProdCode = self.Product_CODE_EN
        if ProdCode.index("end")!=0:
            ProdCode=self.Product_CODE_EN.get()
            print(ProdCode)
            prod = Product.product()

            var="itemsLIST"
            var2="quantityLIST"
            if var not in globals():
                if var2 not in globals():
                    global itemsLIST
                    global quantityLIST
                    itemsLIST=[]
                    quantityLIST=[]

            result = prod.view(ProdCode)
            if (buttonpress=="enter"):
                if (result == "empty"):
                    messagebox.showerror("Product Search", "Item not in Inventory")
                    self.Product_CODE_EN.delete(0, END)
                if (result != "empty"):

                    result = prod.view(ProdCode)
                    self.Product_CODE_EN.delete(0, END)
                    name = StringVar()
                    price = StringVar()
                    name.set(result[1])
                    price.set(result[2])
                    print(result)

                    code=StringVar()
                    code.set(ProdCode)
                    self.ProductCODE.config(textvariable=code.get())
                    self.Product_Name_EN.config(textvariable=name.get())
                    self.Product_Prices_EN.config(textvariable=price.get())

                    print(name.get())
                    quantity = 1
                    result1=(result[0],result[1],result[2],quantity,result[3])
                    print(result1)
                    self.button_confirm.config(state="active",command=lambda m="confirm":self.Click_Enter(result1))


        else: messagebox.showerror("Product Search", "Product Code Empty")

    # Button Enter/search the item
    def Click_Enter(self,result):

        window_Qty = Toplevel()
        window_Qty.title("Quantity!")
        window_Qty.geometry("300x120")

        window_Frame = Frame(window_Qty, width=400, height=100)
        window_Frame.pack()

        Label_Quantity = Label(window_Frame, text="Enter the Quantity of the Products!")

        Entry_Quantity = Entry(window_Frame, width=30, borderwidth=3)
        button_Quantity = Button(window_Frame, text="ENTER", padx=5, pady=5, command=lambda m=Entry_Quantity.get():setQTY(Entry_Quantity.get()))

        self.ProdID=result[0]
        self.ProdName=result[1]
        self.ProdPrice=result[2]
        self.ProdQTY=result[3]
        self.RemainingQTY=result[4]
        def setQTY(val):
            call=0
            global ProdQTY
            try:
                ProdQTY=int(val)
            except ValueError:
                call=1
                messagebox.showerror("Product Search", "Invalid Input")
                self.Click_Enter(result)
                window_Qty.destroy()
            if call==0:
                if (ProdQTY>self.RemainingQTY):
                    messagebox.showerror("POS Transaction", "Not Enough QTY in Stock")
                else:
                    itemsLIST.append(self.ProdName)
                    quantityLIST.append(ProdQTY)
                    Product_ID = str(self.ProductCODE.get())
                    Product_Name = str(self.Product_Name_EN.get())
                    if Product_ID == "" or Product_Name == "":
                        messagebox.showerror("Product Search", "Please Enter the Product ID or Name")
                    else:
                        try:
                            self.frame_Table.insert(parent='', index='end', iid=self.ProdID, text=(self.ProdID, self.ProdName, self.ProdPrice, ProdQTY),
                                            values=(self.ProdID, self.ProdName, self.ProdPrice, ProdQTY))

                        except:
                            messagebox.showerror("Product Search", "Item Already Existed")

                        subtotal=[]
                        for x in self.frame_Table.get_children():
                            subtotal.append(self.frame_Table.item(x)["values"][2]*self.frame_Table.item(x)["values"][3])
                        global totalprice
                        totalprice = sum(subtotal)
                        self.button_final_payment.config(state='active')

                        window_Qty.destroy()

        Label_Quantity.pack()
        Entry_Quantity.pack()
        button_Quantity.pack()

    def payment(self):
        global Entry_Amount
        global Labell
        global Discount_Entry
        global windowASK

        windowASK=Toplevel()
        windowASK.title("Payment")
        windowASK.geometry("200x180")
        window = Frame(windowASK)
        window.pack()

        totalpricelabel=Label(windowASK,text=totalprice)
        Labell = Label(windowASK, text="Total Price")
        Entry_Amount = Entry(windowASK, width=30, borderwidth=3,state="disabled")
        global button_Quantity
        button_Quantity = Button(windowASK, text="Compute Discount", padx=5, pady=5, command=self.discount)

        Discount_LBL=Label(windowASK, text="Enter Discount, Leave Blank if None")
        Discount_Entry=Entry(windowASK, width=30, borderwidth=3)
                
        Labell.pack()
        totalpricelabel.pack()
        Entry_Amount.pack()

        Discount_LBL.pack()
        Discount_Entry.pack()
        button_Quantity.pack()

    def discount(self):
        if not Discount_Entry.get():
            discount = 0
            self.calculatechange(discount)
        else:

            disc=int(float(Discount_Entry.get()))/100

            discount=totalprice*disc

            self.calculatechange(discount)
    def calculatechange(self,discount):
        disc=discount

        Entry_Amount.config(state="normal")
        Discount_Entry.config(state="disabled")
        button_Quantity.config(text="Enter", command=lambda m=disc: self.record(disc))

        global total
        global finalprice

        fprice = StringVar()
        finalprice=totalprice-discount

        fprice.set(str(finalprice))
        Labell.config(text=fprice.get())


    def record(self,discount):

        totalamounttendered = Entry_Amount.get()
        # try:
        total = int(float(totalamounttendered.strip()))
        change = total - finalprice


        if (total < finalprice):
            Labell.config(text="Entered Amount Not Enough!")
        else:
            Labell.config(text="Change: " + "{:.2f}".format(change))

            # get treeview data in list of tuple
            item_tuple = list(zip(itemsLIST, quantityLIST))
            attendedBy = "11"

            e = Employee.Employee()
            e.addNewTransaction(finalprice, discount, attendedBy, item_tuple)

            # close this window here
            Entry_Amount.config(state="disabled")
            Discount_Entry.config(state="disabled")

            button_Quantity.config(text="Done", command=windowASK.destroy)

            for x in self.frame_Table.get_children():
                self.frame_Table.delete(x)

    # Button Delete
    def Click_Delete(self):
        selected_Product = self.frame_Table.get_children()
        self.frame_Table.delete(selected_Product)
        
    def POS_Window(self):

        self.POSGUI = Tk()
        self.POSGUI.title('Point Of Sales!!')
        self.tab = ttk.Treeview(self.POSGUI)

        # Frame Receipt
        self.frame_Receipt = Frame(self.POSGUI, width=250, height=500)
        self.frame_Receipt.grid(row=0, column=0)
        self.myLabel1 = Label(self.frame_Receipt, text="PRODUCT RECORD!")
        self.myLabel1.grid(row=0, column=0)

        # Table
        self.frame_Table = ttk.Treeview(self.frame_Receipt, height=17)
        self.frame_Table['columns'] = ("ID", "Name", "Price", "QTY", "Total")
        self.frame_Table.column("#0", width=0, stretch=NO)
        self.frame_Table.column("ID", anchor=W, width=50, minwidth=300, stretch=NO)
        self.frame_Table.column("Name", anchor=W, width=300, minwidth=300, stretch=NO)
        self.frame_Table.column("Price", anchor=E, width=80, stretch=NO)
        self.frame_Table.column("QTY", anchor=CENTER, width=50, stretch=NO)

        # Table Head
        self.frame_Table.heading("#0")
        self.frame_Table.heading("ID", text="ID", anchor=W)
        self.frame_Table.heading("Name", text="Product", anchor=W)
        self.frame_Table.heading("Price", text="Prices", anchor=E)
        self.frame_Table.heading("QTY", text="QTY", anchor=CENTER)
        self.frame_Table.heading("Total", text="TOTAL", anchor=E)
        self.frame_Table.grid(row=1, column=0)

        # Frame Detail & Button of ProductList
        self.frame_Detail = Frame(self.POSGUI, width=250, height=200)
        self.frame_Detail.grid(row=0, column=1)
        Product_PIMG = Label(self.frame_Detail, text="IMAGE")
        Product_Name_LA = Label(self.frame_Detail, text="Product Name:")

        ProductCODE_LA=Label(self.frame_Detail, text="Product Code")
        self.ProductCODE=Entry(self.frame_Detail,width=40, borderwidth=3,state="disabled")

        self.Product_Name_EN = Entry(self.frame_Detail,width=40, borderwidth=3,state="disabled")
        Product_Prices_LA = Label(self.frame_Detail, text="Product Prices:")
        self.Product_Prices_EN = Entry(self.frame_Detail, width=40, borderwidth=3,state="disabled")


        Product_CODE_LA = Label(self.frame_Detail, text="Enter Product Name/Code:")
        self.Product_CODE_EN = Entry(self.frame_Detail, width=40, borderwidth=3)
        # Frame Detail & Button of ProductList grid
        Product_PIMG.grid(row=0, column=0, columnspan=3)
        Product_Name_LA.grid(row=3, column=0, columnspan=3, sticky=W)
        self.Product_Name_EN.grid(row=4, column=0, columnspan=5)
        Product_Prices_LA.grid(row=5, column=0, columnspan=3, sticky=W)
        self.Product_Prices_EN.grid(row=6, column=0, columnspan=5)
        Product_CODE_LA.grid(row=9, column=0, columnspan=3, sticky=W)
        self.Product_CODE_EN.grid(row=10, column=0, columnspan=5)

        ProductCODE_LA.grid(row=1, column=0, columnspan=3, sticky=W)
        self.ProductCODE.grid(row=2, column=0, columnspan=5, sticky=W)

        # Button List
        self.button_1 = Button(self.frame_Detail, text="1", padx=20, pady=10, command=lambda: self.Button_LOGIC(1))
        self.button_2 = Button(self.frame_Detail, text="2", padx=20, pady=10, command=lambda: self.Button_LOGIC(2))
        self.button_3 = Button(self.frame_Detail, text="3", padx=20, pady=10, command=lambda: self.Button_LOGIC(3))
        self.button_4 = Button(self.frame_Detail, text="4", padx=20, pady=10, command=lambda: self.Button_LOGIC(4))
        self.button_5 = Button(self.frame_Detail, text="5", padx=20, pady=10, command=lambda: self.Button_LOGIC(5))
        self.button_6 = Button(self.frame_Detail, text="6", padx=20, pady=10, command=lambda: self.Button_LOGIC(6))
        self.button_7 = Button(self.frame_Detail, text="7", padx=20, pady=10, command=lambda: self.Button_LOGIC(7))
        self.button_8 = Button(self.frame_Detail, text="8", padx=20, pady=10, command=lambda: self.Button_LOGIC(8))
        self.button_9 = Button(self.frame_Detail, text="9", padx=20, pady=10, command=lambda: self.Button_LOGIC(9))
        self.button_0 = Button(self.frame_Detail, text="0", padx=20, pady=10, command=lambda: self.Button_LOGIC(0))

        # Button Grid frame_CAL
        self.button_0.grid(row=14, column=0, sticky="ew")
        self.button_1.grid(row=13, column=0, sticky="ew")
        self.button_2.grid(row=13, column=1, sticky="ew")
        self.button_3.grid(row=13, column=2, sticky="ew")
        self.button_4.grid(row=12, column=0, sticky="ew")
        self.button_5.grid(row=12, column=1, sticky="ew")
        self.button_6.grid(row=12, column=2, sticky="ew")
        self.button_7.grid(row=11, column=0, sticky="ew")
        self.button_8.grid(row=11, column=1, sticky="ew")
        self.button_9.grid(row=11, column=2, sticky="ew")

        # FOR Button
        self.button_Enter = Button(self.frame_Detail, text="ENTER", padx=16, pady=10, bg="green", command=lambda m="enter":self.SearchItem(m))
        self.button_DEL = Button(self.frame_Detail, text="DELETE", padx=14, pady=10, bg="green", command=self.Click_Delete)

        self.button_List = Button(self.frame_Detail, text="List", padx=25, pady=10, bg="green", command=self.Click_List)
        self.button_confirm = Button(self.frame_Detail, text="Confirm", padx=5, pady=10, state="disabled")
        self.button_final_payment= Button(self.frame_Detail, text="Finish", padx=8, pady=10,command=self.payment, state="disabled")

        # Button Grid frame_CAL
        self.button_Enter.grid(row=14, column=3)
        self.button_DEL.grid(row=13, column=3)

        self.button_List.grid(row=11, column=3)
        self.button_confirm.grid(row=14, column=2)
        self.button_final_payment.grid(row=14, column=1)

        self.POSGUI.mainloop()
        
    def start(self,m,id):
        if (m=="pos"):
            self.POS_Window()