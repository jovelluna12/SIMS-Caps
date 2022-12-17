from ast import Delete
import Manager, Employee
import Product
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def start(m,id,user,time):
    global user_id
    user_id = id
    if (m=='pos'):

        global root
        root = Tk()
        root.title('Cresdel Pharmacy!!')
        tab = ttk.Treeview(root)
        width= root.winfo_screenwidth()
        height=root.winfo_screenheight()
        root.geometry("%dx%d"%(width,height))

        # Frame Receipt
        global frame_Receipt
        frame_Receipt = Frame(root, width=1000,height=560,highlightbackground="black", highlightthickness=3)
        frame_Receipt.grid(row=0, column=0)
        myLabel1 = Label(frame_Receipt, text="Cresdel Pharmacy!!",font=("Arial",30,'bold'))
        myLabel1.place(x=0,y=0)

        # Table
        style=ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")
        global frame_Table
        frame_Table = ttk.Treeview(frame_Receipt, height=24)
        frame_Table['columns'] = ("ID", "Name", "Price", "QTY", "Total")
        frame_Table.column("#0", width=0, stretch=NO)
        frame_Table.column("ID",anchor=W,stretch=NO)
        frame_Table.column("Name",anchor=W,width=500,stretch=NO)
        frame_Table.column("Price",anchor=E,width=100,stretch=NO)
        frame_Table.column("QTY",anchor=CENTER,width=100,stretch=NO)
        frame_Table.column("Total",anchor=E,width=93,stretch=NO)

        # Table Head
        frame_Table.heading("#0")
        frame_Table.heading("ID", text="ID", anchor=W)
        frame_Table.heading("Name", text="Product", anchor=W)
        frame_Table.heading("Price", text="Prices", anchor=E)
        frame_Table.heading("QTY", text="QTY", anchor=CENTER)
        frame_Table.heading("Total", text="TOTAL", anchor=E)
        frame_Table.pack(expand=True,fill=X)
        frame_Table.place(x=1,y=49)

        button_Out= Button(frame_Receipt,text="Time.OUT",padx=9,pady=5,bg="green",command=root.destroy)
        button_Out.place(x=910,y=8)

        #Detailed("This the new Update of the POS")
        global frame_Total
        frame_Total=Frame(root,width=1000,height=130,highlightbackground="black", highlightthickness=3)
        frame_Total.place(x=0,y=563)

        user_Em=Label(frame_Total,text="NAME:",width=0,height=0,font=("Arial",16,'bold')).place(x=10,y=10)
        user_FD=Label(frame_Total,text=user,width=25,height=0,anchor=W,font=("Arial",16,'bold')).place(x=80,y=10)

        user_Timein=Label(frame_Total,text="TIME IN:",width=10,height=0,anchor=W,font=("Arial",10,'bold')).place(x=10,y=50)
        user_FD=Label(frame_Total,text=time,width=50,height=0,anchor=W,font=("Arial",10,'bold')).place(x=90,y=50)

        # def temp_text(e):
        #     Totalprince_Entry.delete(0,"end")
        
        global Totalprince_Entry,Totalchange_Entry
        Totalprince_Entry=Label(frame_Total,text="",font=("Arial", 20,'bold'))
        Totalprince_Entry.place(x=800,y=40,height=35)
        Totalprince_Lbl=Label(frame_Total,text="Total:",font=("Arial", 20,'bold')).place(x=676,y=40)
        # Totalprince_Lbl.place(x=800,y=40,height=35)
        # Totalprince_Entry=Entry(frame_Total,width=8,borderwidth=3,fg='green',font=("Arial",30,'bold'))
        
        # Totalprince_Entry.insert(END,'0.00')
        # Totalprince_Entry.bind("<FocusIn>",temp_text)
        Totalchange_Label=Label(frame_Total,text="Change:",font=("Arial", 20,'bold')).place(x=676,y=80)
        Totalchange_Entry=Label(frame_Total,text="",font=("Arial", 20,'bold'))
        Totalchange_Entry.place(x=800,y=80,height=35)

        # Totalchange_Entry.insert(END,'0.00')
        # Totalchange_Entry.bind("<FocusIn>",temp_text)
        # END

        # Frame Detail & Button of ProductList
        global frame_Detail
        global ProductCODE_LA
        global Product_CODE_EN
        global ProductCODE
        global Product_Name_EN
        global Product_Name_LA
        global Product_Prices_EN
        global Product_Prices_LA

        frame_Detail = Frame(root, width=360, height=693,highlightbackground="black", highlightthickness=3)
        frame_Detail.place(x=1001,y=0)

        Product_PIMG = Label(frame_Detail, text="IMAGE")
        Product_Name_LA = Label(frame_Detail, text="Product Name:")

        ProductCODE_LA=Label(frame_Detail, text="Product Code")
        ProductCODE=Entry(frame_Detail,width=50, borderwidth=5,state="disabled")

        Product_Name_EN = Entry(frame_Detail,width=50, borderwidth=5,state="disabled")
        Product_Prices_LA = Label(frame_Detail, text="Product Prices:")
        Product_Prices_EN = Entry(frame_Detail, width=50, borderwidth=5,state="disabled")


        Product_CODE_LA = Label(frame_Detail, text="Enter Product Code:")
        Product_CODE_EN = Entry(frame_Detail, width=50, borderwidth=5)


        # Frame Detail & Button of ProductList grid
        #Disabled entry
        Product_PIMG.place(x=150,y=40)
        Product_Name_LA.place(x=20,y=140)
        Product_Name_EN.place(x=20,y=160)
        Product_Prices_LA.place(x=20,y=210)
        Product_Prices_EN.place(x=20,y=230)
        ProductCODE_LA.place(x=20,y=280)
        ProductCODE.place(x=20,y=300)

        #Able Entry
        Product_CODE_LA.place(x=20,y=360)
        Product_CODE_EN.place(x=20,y=380)



        # Button List
        button_1 = Button(frame_Detail, text="1", padx=22, pady=12, command=lambda: Button_LOGIC(1))
        button_2 = Button(frame_Detail, text="2", padx=22, pady=12, command=lambda: Button_LOGIC(2))
        button_3 = Button(frame_Detail, text="3", padx=22, pady=12, command=lambda: Button_LOGIC(3))
        button_4 = Button(frame_Detail, text="4", padx=22, pady=12, command=lambda: Button_LOGIC(4))
        button_5 = Button(frame_Detail, text="5", padx=22, pady=12, command=lambda: Button_LOGIC(5))
        button_6 = Button(frame_Detail, text="6", padx=22, pady=12, command=lambda: Button_LOGIC(6))
        button_7 = Button(frame_Detail, text="7", padx=22, pady=12, command=lambda: Button_LOGIC(7))
        button_8 = Button(frame_Detail, text="8", padx=22, pady=12, command=lambda: Button_LOGIC(8))
        button_9 = Button(frame_Detail, text="9", padx=22, pady=12, command=lambda: Button_LOGIC(9))
        button_0 = Button(frame_Detail, text="0", padx=22, pady=12, command=lambda: Button_LOGIC(0))

        # Button Grid frame_CAL
        button_0.place(x=50,y=600)
        button_1.place(x=50,y=550)
        button_2.place(x=110,y=550)
        button_3.place(x=170,y=550)
        button_4.place(x=50,y=500)
        button_5.place(x=110,y=500)
        button_6.place(x=170,y=500)
        button_7.place(x=50,y=450)
        button_8.place(x=110,y=450)
        button_9.place(x=170,y=450)


        # FOR Button
        global button_confirm
        global button_final_payment
        global button_List
        global button_Enter
        button_Enter = Button(frame_Detail, text="ENTER", padx=16, pady=12, bg="green",
                              command=lambda m="enter": SearchItem(m))
        button_DEL = Button(frame_Detail, text="DELETE", padx=14, pady=12, bg="green", command=Click_Delete)
        button_List = Button(frame_Detail, text="List", padx=25, pady=12, bg="green", command=Click_List)
        button_confirm = Button(frame_Detail, text="QTY", padx=3, pady=12, state="disabled")
        button_final_payment = Button(frame_Detail, text="Finish", padx=9, pady=12, command=payment, state="disabled")

        ButtonClear=Button(frame_Detail, text="Clear",padx=25, pady=12, bg="green",command=Click_Remove)
        
        # Button Grid frame_CAL
        button_Enter.place(x=230,y=600)
        button_DEL.place(x=230,y=550)
        button_List.place(x=230,y=500)
        ButtonClear.place(x=230,y=450)
        button_confirm.place(x=110,y=600)
        button_final_payment.place(x=170,y=600)

        root.mainloop()

def Click_Remove():
    ProductCODE.config(state='normal')
    Product_Name_EN.config(state='normal')
    Product_Prices_EN.config(state='normal')

    ProductCODE.delete(0, END)
    Product_Name_EN.delete(0, END)
    Product_Prices_EN.delete(0, END)
    Product_CODE_EN.delete(0, END)

    ProductCODE.config(state='disabled')
    Product_Name_EN.config(state='disabled')
    Product_Prices_EN.config(state='disabled')

# Button logic
def Button_LOGIC(Number):
    current = Product_CODE_EN.get()
    Product_CODE_EN.delete(0, END)
    Product_CODE_EN.insert(0, str(current) + str(Number))

# Button List
def Click_List():
    global Entry_Search
    global Search_Table
    window_list = Toplevel()
    window_list.title("PRODUCT LISTS!")
    window_list.geometry("460x320")

    window_Frame = Frame(window_list, width=400, height=100)
    window_Frame.grid(row=0, column=0)

    window_Frame2 = Frame(window_list, width=400, height=250, bg="blue")
    window_Frame2.grid(row=1, column=0)

    Search_Table = ttk.Treeview(window_Frame2, height=12)
    Search_Table['column'] = ("ID", "Name", "Price",'Batch Number',"Stack")
    Search_Table.column("#0", width=0, stretch=NO, anchor=W)
    Search_Table.column("ID", width=50, stretch=NO, anchor=W)
    Search_Table.column("Name", width=148, stretch=NO, anchor=W)
    Search_Table.column("Batch Number", width=100, stretch=NO, anchor=W)
    Search_Table.column("Price", width=80, stretch=NO, anchor=E)
    Search_Table.column("Stack", width=80, stretch=NO, anchor=E)

    Search_Table.heading("#0")
    Search_Table.heading("ID", text="ID", anchor=W)
    Search_Table.heading("Name", text="Name", anchor=W)
    Search_Table.heading("Batch Number", text="Batch No", anchor=W)
    Search_Table.heading("Price", text="Price", anchor=W)
    Search_Table.heading("Stack", text="Stack", anchor=W)
    Search_Table.grid(row=0, column=0)

    def selectItem(a):
        global code,product,price,qty
        curItem = Search_Table.selection()[0]
        code=Search_Table.item(curItem)['values'][0]
        product=Search_Table.item(curItem)['values'][1]
        price=Search_Table.item(curItem)['values'][2]
        qty=Search_Table.item(curItem)['values'][3]
        ProductCODE.config(state='normal')
        Product_Name_EN.config(state='normal')
        Product_Prices_EN.config(state='normal')

        ProductCODE.insert(0,code)
        Product_Name_EN.insert(0,product)
        Product_Prices_EN.insert(0,price)

        ProductCODE.config(state='disabled')
        Product_Name_EN.config(state='disabled')
        Product_Prices_EN.config(state='disabled')

    Search_Table.bind('<Double-1>', selectItem)

    Label_Search = Label(window_Frame, text="Search:")
    Entry_Search = Entry(window_Frame, width=50, borderwidth=3)
    button_Search = Button(window_Frame, text="Search", padx=5, pady=0, command=search)

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

def search():
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

def SearchItem(buttonpress):
    ProdCode = Product_CODE_EN

    var="itemsLIST"
    var2="quantityLIST"
    var3="ProdCodee"
    if var not in globals():
        if var2 not in globals():
            if var3 not in globals():
                global ProdCodee
                global itemsLIST
                global quantityLIST

                ProdCodee=[]
                itemsLIST=[]
                quantityLIST=[]

    if ProdCode.index("end")!=0:
        ProdCode=Product_CODE_EN.get()
        prod = Product.product()

        ProdCodee.append(ProdCode)
        result = prod.viewCode(ProdCode)

        if (buttonpress=="enter"):
            if (result == "empty"):
                messagebox.showerror("Product Search", "Item not in Inventory")
                Product_CODE_EN.delete(0, END)
            if (result != "empty"):

                result = prod.viewCode(ProdCode)
                Product_CODE_EN.delete(0, END)

                name = StringVar()
                pricee = StringVar()
                name.set(result[1])
                pricee.set(result[2])

                codee=StringVar()
                codee.set(ProdCode)

                ProductCODE.config(state='normal')
                Product_Name_EN.config(state='normal')
                Product_Prices_EN.config(state='normal')

                ProductCODE.insert(0,codee.get())
                Product_Name_EN.insert(0,name.get())
                Product_Prices_EN.insert(0,pricee.get())

                ProductCODE.config(state='disabled')
                Product_Name_EN.config(state='disabled')
                Product_Prices_EN.config(state='disabled')

                result1=(result[0],result[1],result[2],result[3])

                button_confirm.config(state="active",command=lambda m="confirm":Click_Enter(result1))
    elif ProdCode.index("end")==0 and ProductCODE.index('end')!=0 and Product_Name_EN.index('end')!=0 and Product_Prices_EN.index('end')!=0:
        ProdCodee.append(code)
        prod=Product.product()

        button_confirm.config(state="active",command=lambda m="confirm":Click_Enter((code,product,price,qty)))

    else: messagebox.showerror("Product Search", "Product Code Empty")

# Button Enter/search the item
def Click_Enter(result):

    window_Qty = Toplevel()
    window_Qty.title("Quantity!")
    window_Qty.geometry("300x120")

    window_Frame = Frame(window_Qty, width=400, height=100)
    window_Frame.pack()

    Label_Quantity = Label(window_Frame, text="Enter the Quantity of the Products!")

    Entry_Quantity = Entry(window_Frame, width=30, borderwidth=3)
    button_Quantity = Button(window_Frame, text="ENTER", padx=5, pady=5, command=lambda m=Entry_Quantity.get():setQTY(Entry_Quantity.get()))

    ProdID=result[0]
    ProdName=result[1]
    ProdPrice=result[2]
    # ProdQTY=result[3]
    RemainingQTY=result[3]
    def setQTY(val):
        call=0
        global ProdQTY
        try:
            ProdQTY=int(val)
        except ValueError:
            call=1
            messagebox.showerror("Product Search", "Invalid Input")
            Click_Enter(result)
            window_Qty.destroy()

        if call==0:
            if (ProdQTY>RemainingQTY):
                messagebox.showerror("POS Transaction", "Not Enough QTY in Stock")
            else:
                itemsLIST.append(ProdName)
                quantityLIST.append(ProdQTY)


                Product_ID = str(ProductCODE.get())
                Product_Name = str(Product_Name_EN.get())
                if Product_ID == "" or Product_Name == "":
                    messagebox.showerror("Product Search", "Please Enter the Product ID or Name")
                else:
                    try:
                        ProductCODE.config(state='normal')
                        Product_Name_EN.config(state='normal')
                        Product_Prices_EN.config(state='normal')

                        ProductCODE.delete(0, 'end')
                        Product_Name_EN.delete(0, 'end')
                        Product_Prices_EN.delete(0, 'end')

                        ProductCODE.config(state='disabled')
                        Product_Name_EN.config(state='disabled')
                        Product_Prices_EN.config(state='disabled')

                        frame_Table.insert(parent='', index='end', iid=ProdID, text=(ProdID, ProdName, ProdPrice, ProdQTY),
                                           values=(ProdID, ProdName, ProdPrice, ProdQTY))
                        button_confirm.config(state="disabled")

                    except:
                        messagebox.showerror("Product Search", "Item Already Existed")

                    subtotal=[]
                    for x in frame_Table.get_children():
                        subtotal.append(frame_Table.item(x)["values"][2]*frame_Table.item(x)["values"][3])

                    global totalprice
                    totalprice = sum(subtotal)
                    
                    Totalprince_Entry.config(text=totalprice)
                    button_final_payment.config(state='active')

                    window_Qty.destroy()

    Label_Quantity.pack()
    Entry_Quantity.pack()
    button_Quantity.pack()

def payment():
        global Entry_Amount
        global Labell
        global Discount_Entry
        global windowASK

        windowASK=Toplevel()
        windowASK.title("Payment")
        windowASK.geometry("200x180")
        window = Frame(windowASK)
        window.pack()

        global totalpricelabel
        totalpricelabel=Label(windowASK,text=totalprice)
        Labell = Label(windowASK, text="Total Price")
        Entry_Amount = Entry(windowASK, width=30, borderwidth=3,state="disabled")
        global button_Quantity
        button_Quantity = Button(windowASK, text="Compute Discount", padx=5, pady=5, command=discount)

        Discount_LBL=Label(windowASK, text="Enter Discount, Leave Blank if None")
        Discount_Entry=Entry(windowASK, width=30, borderwidth=3)
        
        Labell.pack()
        totalpricelabel.pack()
        Entry_Amount.pack()

        Discount_LBL.pack()
        Discount_Entry.pack()
        button_Quantity.pack()

def discount():
    if not Discount_Entry.get():
        discount = 0
        calculatechange(discount)
    else:
        disc=int(float(Discount_Entry.get()))/100
        discount=totalprice*disc
        calculatechange(discount)

def calculatechange(discount):
    disc=discount

    Entry_Amount.config(state="normal")
    Discount_Entry.config(state="disabled")
    button_Quantity.config(text="Enter", command=lambda m=disc: record(disc))

    global total
    global finalprice

    fprice = StringVar()
    finalprice=totalprice-discount

    finalpricee = "Final Price: " + str(finalprice)

    fprice.set(str(finalprice))
    Labell.config(text=finalpricee)


def record(discount):

    totalamounttendered = Entry_Amount.get()
    total = int(float(totalamounttendered.strip()))
    change = total - finalprice
    

    if (total < finalprice):
        totalpricelabel.config(text="Entered Amount Not Enough!")
    else:
        Labell.config(text="Change: " + "{:.2f}".format(change))
        Totalchange_Entry.config(text=change)

        # get treeview data in list of tuple
        item_tuple = list(zip(itemsLIST, quantityLIST, ProdCodee))
        attendedBy = user_id
        
        e = Employee.Employee()
        e.addNewTransaction(finalprice, discount, attendedBy, item_tuple)
        # close this window here
        Entry_Amount.config(state="disabled")
        Discount_Entry.config(state="disabled")

        windowASK.destroy()
        Button(frame_Total,text="Next Transaction", command=newTransact).place(x=550,y=80)
        # button_Quantity.config(text="Done", command=windowASK.destroy)
    
        for x in frame_Table.get_children():
            frame_Table.delete(x)


def newTransact():
    Totalprince_Entry.config(text="")
    Totalchange_Entry.config(text="")

    itemsLIST.clear()
    quantityLIST.clear()

    Click_Remove()

# Button Delete
def Click_Delete():
    selected_Product = frame_Table.get_children()
    frame_Table.delete(selected_Product)