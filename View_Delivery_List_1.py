import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkFont
import Employee, Manager
from datetime import datetime

class VDL:
    def __init__(self,id):
        global root
        root = tk.Tk()
        root.title("Delivery Detail")
        width=1140
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        Title_Store=tk.Label(root,text="CRESDEL PHARMACY",font=('Arial',45,"bold"),justify=LEFT)
        Title_Store.place(x=10,y=10)

        Adrress=tk.Label(root,text="Ilaya Carmen, Cagayan de Oro City",font=('Arial',15),justify=LEFT)
        Adrress.place(x=10,y=85)

        man=Manager.Manager()
        res=man.getDateArrived_Purchased(id)

        Dstore=tk.Label(root,text="PO Number: "+str(id[0]),font=('Arial',12),justify=LEFT)
        Dstore.place(x=10,y=115)

        DateAr=tk.Label(root,text="Date Ordered: "+str(res[1]),font=('Arial',12),justify=LEFT)
        DateAr.place(x=310,y=115)

        if res[2]!="In Transit":
            DateRE=tk.Label(root,text="Date Received: "+str(res[0]),font=('Arial',12),justify=LEFT)
            DateRE.place(x=560,y=115)

        style=ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")

        global QTYIN_Table
        Table=Frame(root)
        Table.place(x=10,y=140,width=1125,height=300)
        QTYIN_Table = ttk.Treeview(Table, height=25)
        QTYIN_Table['columns'] = ("ID","Name", "Price","QTY","QTYIN","QTYOUT","MARK","TotalQTY","TotalPrice")
        QTYIN_Table.column("#0", width=0, stretch=NO)
        QTYIN_Table.column("ID",anchor=W,width=80,stretch=NO)
        QTYIN_Table.column("Name",anchor=W,width=360,stretch=NO)
        QTYIN_Table.column("Price",anchor=CENTER,width=80,stretch=NO)
        QTYIN_Table.column("QTY",anchor=CENTER,width=40,stretch=NO)
        QTYIN_Table.column("QTYIN",anchor=CENTER,width=60,stretch=NO)
        QTYIN_Table.column("QTYOUT",anchor=CENTER,width=60,stretch=NO)
        QTYIN_Table.column("MARK",anchor=CENTER,width=300,stretch=NO)
        QTYIN_Table.column("TotalQTY",anchor=CENTER,width=60,stretch=NO)
        QTYIN_Table.column("TotalPrice",anchor=E,width=65,stretch=NO)

        # Table Head
        QTYIN_Table.heading("#0")
        QTYIN_Table.heading("ID", text="ID", anchor=W)
        QTYIN_Table.heading("Name", text="Product", anchor=W)
        QTYIN_Table.heading("Price", text="Unit Price", anchor=CENTER)
        QTYIN_Table.heading("QTY", text="Qty", anchor=CENTER)
        QTYIN_Table.heading("QTYIN", text="Accepted", anchor=CENTER)
        QTYIN_Table.heading("QTYOUT", text="Returned", anchor=CENTER)
        QTYIN_Table.heading("MARK", text="Remark", anchor=W)
        QTYIN_Table.heading("TotalQTY", text="Total QTY", anchor=CENTER)
        QTYIN_Table.heading("TotalPrice", text="Total Price", anchor=W)
        scrollbar = ttk.Scrollbar(Table, orient="vertical", command=QTYIN_Table.yview)
        scrollbar.place(relx=1.0, rely=0.0, anchor="ne")
        QTYIN_Table.configure(yscrollcommand=scrollbar.set)
        QTYIN_Table.pack(expand=1,fill=BOTH)

        emp=Manager.Manager()
        res=emp.getPO_Items(id)

        count=0
        total1=[]
        for item in range(len(res)):
            total=res[item][3]-res[item][5]
            total1.append(res[item][2]*total)
            QTYIN_Table.insert('',index='end', iid=count,values=(res[item][0],res[item][1],res[item][2],res[item][3],res[item][4],res[item][5],res[item][6],res[item][3]-res[item][5],res[item][2]*total))
            count+=1

        res=emp.getPO_details(id[0])

        # GLabel_450=tk.Label(root,text="Purchase Details: ",font=('Arial',15),justify=LEFT)
        # GLabel_450.place(x=600,y=440)

        GLabel_170=tk.Label(root,text="Gross Amount w VAT: PHP {:.2f}".format(float(sum(total1))),font=('Arial',10),justify=LEFT)
        GLabel_170.place(x=600,y=450)
        
        GLabel_139=tk.Label(root,text="12% VAT: PHP {:.2f}".format(res[1]),font=('Arial',10),justify=LEFT)
        GLabel_139.place(x=600,y=470)

        GLabel_170=tk.Label(root,text="Gross Amount w/out VAT: PHP {:.2f}".format(float(sum(total1))-float(res[1])),font=('Arial',10),justify=LEFT)
        GLabel_170.place(x=600,y=490)

        GLabel_523=tk.Label(root,text="Discount: {:.2f}".format(res[2]),font=('Arial',10),justify=LEFT)
        GLabel_523.place(x=600,y=510)


        #VENDOR INFORMATION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        emp=Manager.Manager()
        res1=emp.getPO_Vendor(id[0])

        Vendor_ID=tk.Label(root,text="Vendor Details: ",font=('Arial',15),justify=LEFT)
        Vendor_ID.place(x=10,y=440)

        Vendor_Name=tk.Label(root,text="Vendor Name: "+str(res1[0]),font=('Arial',10),justify=LEFT)
        Vendor_Name.place(x=10,y=470)
        
        Vendor_Address=tk.Label(root,text="Vendor Address: "+str(res1[1]),font=('Arial',10),justify=LEFT)
        Vendor_Address.place(x=10,y=490)

        Vendor_Contact=tk.Label(root,text="Contact Number: "+str(res1[2]),font=('Arial',10),justify=LEFT)
        Vendor_Contact.place(x=10,y=510)

        Vendor_Email=tk.Label(root,text="Email: "+str(res1[3]),font=('Arial',10),justify=LEFT)
        Vendor_Email.place(x=10,y=530)

        Vendor_Ship=tk.Label(root,text="Shipping Fee: "+str(res1[4]),font=('Arial',10),justify=LEFT)
        Vendor_Ship.place(x=600,y=530)
        print(total1)
        print(sum(total1))
        print(float(res[2]))
        print(float(res1[4]))

        GLabel_524=tk.Label(root,text="NET Amount: PHP {:.2f}".format(float(sum(total1))-float(res[2])-float(res1[4])),font=('Arial',10),justify=LEFT)
        GLabel_524.place(x=600,y=550)


# if __name__=="__main__":
#     VDL(1234)