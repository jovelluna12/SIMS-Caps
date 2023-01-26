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
        global root
        
        root = tk.Tk()
        root.title("Delivery Detail")
        width=950
        height=630
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        root.protocol("WM_DELETE_WINDOW", self.on_Closing)
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        Title_Store=tk.Label(root,text="CRESDEL PHARMACY",font=('Arial',45,"bold"),justify=LEFT)
        Title_Store.place(x=10,y=10)

        Adrress=tk.Label(root,text="Ilaya Carmen, Cagayan de Oro City",font=('Arial',15),justify=LEFT)
        Adrress.place(x=10,y=85)

        Dstore=tk.Label(root,text="Purchase Order:",font=('Arial',12),justify=LEFT)
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
        Table.place(x=10,y=140,width=922,height=300)
        QTYIN_Table = ttk.Treeview(Table, height=25)
        QTYIN_Table['columns'] = ("ID","Name", "Price","QTY","QTYIN","QTYOUT","MARK","TotalQTY","TotalPrice")
        QTYIN_Table.column("#0", width=0, stretch=NO)
        QTYIN_Table.column("ID",anchor=W,width=80,stretch=NO)
        QTYIN_Table.column("Name",anchor=W,width=360,stretch=NO)
        QTYIN_Table.column("Price",anchor=CENTER,width=80,stretch=NO)
        QTYIN_Table.column("QTY",anchor=CENTER,width=40,stretch=NO)
        QTYIN_Table.column("QTYIN",anchor=CENTER,width=60,stretch=NO)
        QTYIN_Table.column("QTYOUT",anchor=CENTER,width=60,stretch=NO)
        QTYIN_Table.column("MARK",anchor=CENTER,width=100,stretch=NO)
        QTYIN_Table.column("TotalQTY",anchor=CENTER,width=60,stretch=NO)
        QTYIN_Table.column("TotalPrice",anchor=E,width=65,stretch=NO)

        # Table Head
        QTYIN_Table.heading("#0")
        QTYIN_Table.heading("ID", text="ID", anchor=W)
        QTYIN_Table.heading("Name", text="Product", anchor=W)
        QTYIN_Table.heading("Price", text="Unit Price", anchor=CENTER)
        QTYIN_Table.heading("QTY", text="QTY", anchor=CENTER)
        QTYIN_Table.heading("QTYIN", text="QTY IN", anchor=CENTER)
        QTYIN_Table.heading("QTYOUT", text="QTY OUT", anchor=CENTER)
        QTYIN_Table.heading("MARK", text="MARK", anchor=W)
        QTYIN_Table.heading("TotalQTY", text="Total QTY", anchor=CENTER)
        QTYIN_Table.heading("TotalPrice", text="Total Price", anchor=W)
        scrollbar = ttk.Scrollbar(Table, orient="vertical", command=QTYIN_Table.yview)
        scrollbar.place(relx=1.0, rely=0.0, anchor="ne")
        QTYIN_Table.configure(yscrollcommand=scrollbar.set)
        QTYIN_Table.pack(expand=1,fill=BOTH)

        emp=Employee.Employee()
        # CashName=emp.getEmployee_Name()
        GLabel_450=tk.Label(root,text="Name: ",font=('Arial',15),justify=LEFT)
        GLabel_450.place(x=600,y=440)

        GLabel_170=tk.Label(root,text="Subtotal: PHP ",font=('Arial',10),justify=LEFT)
        GLabel_170.place(x=600,y=470)

        # VAT=0.12*subtotal
        
        GLabel_139=tk.Label(root,text="12% VAT: PHP",font=('Arial',10),justify=LEFT)
        GLabel_139.place(x=600,y=490)

        GLabel_523=tk.Label(root,text="LESS: Other Discounts:",font=('Arial',10),justify=LEFT)
        GLabel_523.place(x=600,y=510)

        GLabel_524=tk.Label(root,text="Total Amount Due ",font=('Arial',10),justify=LEFT)
        GLabel_524.place(x=600,y=530)

        #VENDOR INFORMATION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        emp=Employee.Employee()
        # CashName=emp.getEmployee_Name()
        Vendor_ID=tk.Label(root,text="ID: ",font=('Arial',15),justify=LEFT)
        Vendor_ID.place(x=10,y=440)

        Vendor_Name=tk.Label(root,text="Name:",font=('Arial',10),justify=LEFT)
        Vendor_Name.place(x=10,y=470)
        
        Vendor_Address=tk.Label(root,text="Address:",font=('Arial',10),justify=LEFT)
        Vendor_Address.place(x=10,y=490)

        Vendor_Contact=tk.Label(root,text="Contact Number:",font=('Arial',10),justify=LEFT)
        Vendor_Contact.place(x=10,y=510)

        Vendor_Email=tk.Label(root,text="Email:",font=('Arial',10),justify=LEFT)
        Vendor_Email.place(x=10,y=530)

        Vendor_Ship=tk.Label(root,text="Total Amount Shipping: ",font=('Arial',10),justify=LEFT)
        Vendor_Ship.place(x=10,y=550)

        this=Button(root,text="this",command=self.Payment_GUI)
        this.place(x=1,y=2)

        root.mainloop()
    
    def on_Closing(self):
        if messagebox.askyesno("Warning","Closing this Window this Transaction.\nContinue Closing?"):
            root.destroy()
    
    def Payment_GUI(self):
        Payment_G = Toplevel()
        Payment_G.title("Amount Tendered")
        # Payment_G.protocol("WM_DELETE_WINDOW",on_close)
        Payment_G.wm_attributes("-topmost", 1)

        Payment_Frame=Frame(Payment_G)
        Total_pay=Label(Payment_G,text="Total Price is ",font=('Arial',15))
        Total_pay.pack()



if __name__ == "__main__":
    vdl = VDL()
