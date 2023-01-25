import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkFont
import Employee
from datetime import datetime

class VDL:
    def __init__(self):
        
        root = tk.Tk()
        root.title("Delivery Detail")
        width=1000
        height=730
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        # root.protocol("WM_DELETE_WINDOW", self.on_Closing)
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        Title_Store=tk.Label(root,text="CRESDEL PHARMACY",font=('Arial',45,"bold"),justify=LEFT)
        Title_Store.place(x=10,y=10)

        Adrress=tk.Label(root,text="Ilaya Carmen, Cagayan de Oro City",font=('Arial',15),justify=LEFT)
        Adrress.place(x=10,y=85)

        Dstore=tk.Label(root,text="Delivery Store:",font=('Arial',12),justify=LEFT)
        Dstore.place(x=10,y=115)

        DateAr=tk.Label(root,text="Date Arravil:",font=('Arial',12),justify=LEFT)
        DateAr.place(x=310,y=115)

        DateRE=tk.Label(root,text="Date Receive:",font=('Arial',12),justify=LEFT)
        DateRE.place(x=560,y=115)

        style=ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")

        global QTYIN_Table
        Table=Frame(root)
        Table.place(x=10,y=140,width=763,height=300)
        QTYIN_Table = ttk.Treeview(Table, height=25)
        QTYIN_Table['columns'] = ("ID","Name", "Price","QTY","QTYIN","TotalQTY","TotalPrice")
        QTYIN_Table.column("#0", width=0, stretch=NO)
        QTYIN_Table.column("ID",anchor=W,width=80,stretch=NO)
        QTYIN_Table.column("Name",anchor=W,width=360,stretch=NO)
        QTYIN_Table.column("Price",anchor=CENTER,width=80,stretch=NO)
        QTYIN_Table.column("QTY",anchor=CENTER,width=40,stretch=NO)
        QTYIN_Table.column("QTYIN",anchor=CENTER,width=60,stretch=NO)
        QTYIN_Table.column("TotalQTY",anchor=CENTER,width=60,stretch=NO)
        QTYIN_Table.column("TotalPrice",anchor=E,width=65,stretch=NO)

        # Table Head
        QTYIN_Table.heading("#0")
        QTYIN_Table.heading("ID", text="ID", anchor=W)
        QTYIN_Table.heading("Name", text="Product", anchor=W)
        QTYIN_Table.heading("Price", text="Unit Price", anchor=CENTER)
        QTYIN_Table.heading("QTY", text="QTY", anchor=CENTER)
        QTYIN_Table.heading("QTYIN", text="QTY IN", anchor=CENTER)
        QTYIN_Table.heading("TotalQTY", text="Total QTY", anchor=CENTER)
        QTYIN_Table.heading("TotalPrice", text="Total Price", anchor=E)
        scrollbar = ttk.Scrollbar(Table, orient="vertical", command=QTYIN_Table.yview)
        scrollbar.place(relx=1.0, rely=0.0, anchor="ne")
        QTYIN_Table.configure(yscrollcommand=scrollbar.set)
        QTYIN_Table.pack(expand=1,fill=BOTH)

        Retrun=tk.Label(root,text="Product To Retrun:",font=('Arial',12),justify=LEFT)
        Retrun.place(x=10,y=444)

        global QTYOUT_Table
        TableOUT=Frame(root)
        TableOUT.place(x=10,y=470,width=863,height=250)
        QTYOUT_Table = ttk.Treeview(TableOUT, height=25)
        QTYOUT_Table['columns'] = ("ID","Name", "Price","QTY","QTYOUT","TotalQTY","TotalPrice","MARK")
        QTYOUT_Table.column("#0", width=0, stretch=NO)
        QTYOUT_Table.column("ID",anchor=W,width=80,stretch=NO)
        QTYOUT_Table.column("Name",anchor=W,width=360,stretch=NO)
        QTYOUT_Table.column("Price",anchor=CENTER,width=80,stretch=NO)
        QTYOUT_Table.column("QTY",anchor=CENTER,width=40,stretch=NO)
        QTYOUT_Table.column("QTYOUT",anchor=CENTER,width=60,stretch=NO)
        QTYOUT_Table.column("TotalQTY",anchor=CENTER,width=60,stretch=NO)
        QTYOUT_Table.column("TotalPrice",anchor=E,width=65,stretch=NO)
        QTYOUT_Table.column("MARK",anchor=E,width=100,stretch=NO)

        # TableOUT Head
        QTYOUT_Table.heading("#0")
        QTYOUT_Table.heading("ID", text="ID", anchor=W)
        QTYOUT_Table.heading("Name", text="Product", anchor=W)
        QTYOUT_Table.heading("Price", text="Unit Price", anchor=CENTER)
        QTYOUT_Table.heading("QTY", text="QTY", anchor=CENTER)
        QTYOUT_Table.heading("QTYOUT", text="QTY OUT", anchor=CENTER)
        QTYOUT_Table.heading("TotalQTY", text="Total QTY", anchor=CENTER)
        QTYOUT_Table.heading("TotalPrice", text="Total Price", anchor=CENTER)
        QTYOUT_Table.heading("MARK", text="Mark", anchor=W)
        scrollbar = ttk.Scrollbar(TableOUT, orient="vertical", command=QTYOUT_Table.yview)
        scrollbar.place(relx=1.0, rely=0.0, anchor="ne")
        QTYOUT_Table.configure(yscrollcommand=scrollbar.set)
        QTYOUT_Table.pack(expand=1,fill=BOTH)

        emp=Employee.Employee()
        # CashName=emp.getEmployee_Name()
        GLabel_450=tk.Label(root,text="Cashier: ",font=('Arial',15),justify=LEFT)
        GLabel_450.place(x=780,y=240)

        GLabel_170=tk.Label(root,text="Subtotal: PHP ",font=('Arial',10),justify=LEFT)
        GLabel_170.place(x=780,y=270)

        # VAT=0.12*subtotal
        
        GLabel_139=tk.Label(root,text="12% VAT: PHP",font=('Arial',10),justify=LEFT)
        GLabel_139.place(x=780,y=290)

        GLabel_522=tk.Label(root,text="Senior/PWD Discount: PHP",font=('Arial',10),justify=LEFT)
        GLabel_522.place(x=780,y=310)

        GLabel_523=tk.Label(root,text="LESS: Other Discounts:",font=('Arial',10),justify=LEFT)
        GLabel_523.place(x=780,y=330)

        # global finalprice
        # finalprice=subtotal-disc1-disc

        GLabel_524=tk.Label(root,text="Total Amount Due ",font=('Arial',10),justify=LEFT)
        GLabel_524.place(x=780,y=350)

        GLabel_525=tk.Label(root,text="Cash: ",font=('Arial',10),justify=LEFT)
        GLabel_525.place(x=780,y=370)            

        GLabel_526=tk.Label(root,text="Change: ",font=('Arial',10),justify=LEFT)
        GLabel_526.place(x=780,y=390)


        root.mainloop()

if __name__ == "__main__":
    vdl = VDL()
