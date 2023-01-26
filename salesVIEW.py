import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkFont
import Employee
from datetime import datetime

class App:
    def __init__(self):
        root = tk.Tk()
        root.title("Sales Summary")
        width=600
        height=700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_602=tk.Label(root,text="CRESDEL PHARMACY",font=('Arial',35,"bold"),justify=LEFT)
        GLabel_602.place(x=20,y=20)

        GLabel_899=tk.Label(root,text="Ilaya Carmen, Cagayan de Oro City",font=('Arial',15),justify=LEFT)
        GLabel_899.place(x=20,y=85)

        GLabel_459=tk.Label(root,text="Date Ordered: "+str(datetime.today().strftime('%Y-%m-%d')),font=('Arial',15),justify=LEFT)
        GLabel_459.place(x=20,y=120)

        style=ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")

        global frame_Table
        Table=Frame(root)
        Table.place(x=20,y=150,width=550,height=300)
        frame_Table = ttk.Treeview(Table, height=25)
        frame_Table['columns'] = ("Name", "Price", "QTY", "Total")
        frame_Table.column("#0", width=0, stretch=NO)
        frame_Table.column("Name",anchor=W,width=360,stretch=NO)
        frame_Table.column("Price",anchor=CENTER,width=80,stretch=NO)
        frame_Table.column("QTY",anchor=CENTER,width=40,stretch=NO)
        frame_Table.column("Total",anchor=E,width=45,stretch=NO)

        # Table Head
        frame_Table.heading("#0")
        frame_Table.heading("Name", text="Product", anchor=W)
        frame_Table.heading("Price", text="Unit Price", anchor=CENTER)
        frame_Table.heading("QTY", text="QTY", anchor=CENTER)
        frame_Table.heading("Total", text="Total", anchor=E)
        scrollbar = ttk.Scrollbar(Table, orient="vertical", command=frame_Table.yview)
        scrollbar.place(relx=1.0, rely=0.0, anchor="ne")
        frame_Table.configure(yscrollcommand=scrollbar.set)
        frame_Table.place(x=0,y=0,width=530,height=300)
        
        # global subtotal
        # count=0
        # subtotal=0
        # for item in range(len(item_tuple)):
        #     frame_Table.insert('',index='end',iid=count,values=(item_tuple[item][0],item_tuple[item][2],item_tuple[item][1],item_tuple[item][2]*item_tuple[item][1]))
        #     count+=1
        #     subtotal=subtotal+item_tuple[item][2]*item_tuple[item][1]
        
       
        # emp=Employee.Employee()
        # CashName=emp.getEmployee_Name(user_id)
        
        GLabel_450=tk.Label(root,text="Cashier: ",font=('Arial',15),justify=LEFT)
        GLabel_450.place(x=20,y=470)

        GLabel_450=tk.Label(root,text="Invoice No: ",font=('Arial',15),justify=LEFT)
        GLabel_450.place(x=20,y=500)

        GLabel_170=tk.Label(root,text="Subtotal: PHP {:.2f}",font=('Arial',10),justify=LEFT)
        GLabel_170.place(x=350,y=510)

        # VAT=0.12*subtotal
        
        GLabel_139=tk.Label(root,text="12% VAT: PHP {:.2f}",font=('Arial',10),justify=LEFT)
        GLabel_139.place(x=350,y=530)

        GLabel_522=tk.Label(root,text="Senior/PWD Discount: PHP {:.2f}",font=('Arial',10),justify=LEFT)
        GLabel_522.place(x=350,y=550)

        GLabel_523=tk.Label(root,text="LESS: Other Discounts: PHP {:.2f}",font=('Arial',10),justify=LEFT)
        GLabel_523.place(x=350,y=570)


        GLabel_524=tk.Label(root,text="Total Amount Due {:.2f}",font=('Arial',10),justify=LEFT)
        GLabel_524.place(x=350,y=590)

        GLabel_525=tk.Label(root,text="Cash: PHP {:.2f}",font=('Arial',10),justify=LEFT)
        GLabel_525.place(x=350,y=610)            

        GLabel_526=tk.Label(root,text="Change: PHP {:.2f}",font=('Arial',10),justify=LEFT)
        GLabel_526.place(x=350,y=630)


        root.mainloop()


if __name__ == "__main__":
    app = App()
