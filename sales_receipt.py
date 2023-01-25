import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkFont
import Employee
from datetime import datetime


class App:
    def __init__(self,discount,custom_discount,user_id, item_tuple):
        global root,u_id,items
        u_id=user_id
        items=item_tuple
        root = tk.Tk()
        #setting title
        root.title("Sales Summary")
        #setting window size
        width=700
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        root.protocol("WM_DELETE_WINDOW", self.on_Closing)
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        

        GLabel_602=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=22)
        GLabel_602["font"] = ft
        GLabel_602["fg"] = "#333333"
        GLabel_602["justify"] = "center"
        GLabel_602["text"] = "CRESDEL PHARMACY"
        GLabel_602.place(x=140,y=30)

        GLabel_899=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12)
        GLabel_899["font"] = ft
        GLabel_899["fg"] = "#333333"
        GLabel_899["justify"] = "center"
        GLabel_899["text"] = "Ilaya Carmen, Cagayan de Oro City"
        GLabel_899.place(x=120,y=60,width=329,height=40)

        GLabel_459=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_459["font"] = ft
        GLabel_459["fg"] = "#333333"
        GLabel_459["text"] = "Date Ordered: "+str(datetime.today().strftime('%Y-%m-%d'))
        GLabel_459.place(x=60,y=120)

        style=ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")

        global frame_Table
        frame_Table = ttk.Treeview(root, height=25)
        frame_Table['columns'] = ("Name", "Price", "QTY", "Total")
        frame_Table.column("#0", width=0, stretch=NO)
        frame_Table.column("Name",anchor=CENTER,width=200,stretch=NO)
        frame_Table.column("Price",anchor=CENTER,width=80,stretch=NO)
        frame_Table.column("QTY",anchor=CENTER,width=40,stretch=NO)
        frame_Table.column("Total",anchor=CENTER,width=93,stretch=NO)

        # Table Head
        frame_Table.heading("#0")
        frame_Table.heading("Name", text="Product", anchor=CENTER)
        frame_Table.heading("Price", text="Unit Price", anchor=CENTER)
        frame_Table.heading("QTY", text="QTY", anchor=CENTER)
        frame_Table.heading("Total", text="Total", anchor=CENTER)
        frame_Table.place(x=80,y=170,width=410,height=131)

        count=0
        subtotal=0
        for item in range(len(item_tuple)):
            frame_Table.insert('',index='end',iid=count,values=(item_tuple[item][0],item_tuple[item][2],item_tuple[item][1],item_tuple[item][2]*item_tuple[item][1]))
            count+=1
            subtotal=subtotal+item_tuple[item][2]*item_tuple[item][1]

        emp=Employee.Employee()
        CashName=emp.getEmployee_Name(user_id)
        GLabel_459=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_459["font"] = ft
        GLabel_459["fg"] = "#333333"
        GLabel_459["text"] = "Cashier: "+str(CashName[0])
        GLabel_459.place(x=60,y=300)

        GLabel_170=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_170["font"] = ft
        GLabel_170["fg"] = "#333333"
        GLabel_170["text"] = "Subtotal: PHP "+str(subtotal)
        GLabel_170.place(x=300,y=340)

        VAT=0.12*subtotal

        GLabel_139=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_139["font"] = ft
        GLabel_139["fg"] = "#333333"
        GLabel_139["text"] = "12% VAT: PHP "+str(format(VAT))
        GLabel_139.place(x=300,y=360)

        global disc1
        if discount=="Senior Citizen 20%" or discount =="PWD 20%":
            disc1=20/100*subtotal
        else: 
            disc1=0

        GLabel_522=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_522["font"] = ft
        GLabel_522["fg"] = "#333333"
        GLabel_522["text"] = "Senior/PWD Discount: PHP "+str(format(disc1))
        GLabel_522.place(x=300,y=380)

        global disc
        if not custom_discount:
            disc=0
        else:
            disc=custom_discount/100*subtotal

        GLabel_522=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_522["font"] = ft
        GLabel_522["fg"] = "#333333"
        GLabel_522["text"] = "LESS: Other Discounts: PHP "+str(format(disc))
        GLabel_522.place(x=300,y=400)

        global finalprice
        finalprice=subtotal-disc1-disc

        GLabel_522=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_522["font"] = ft
        GLabel_522["fg"] = "#333333"
        GLabel_522["text"] = "Total Amount Due "+str(finalprice)
        GLabel_522.place(x=300,y=420)

        amount=simpledialog.askfloat("Enter Amount Tendered","Enter Amount Tendered")
        if amount<finalprice:
            messagebox.showerror("Error","Amount Less than Actual Price")
        else:

            GLabel_522=tk.Label(root)
            ft = tkFont.Font(family='Arial',size=10)
            GLabel_522["font"] = ft
            GLabel_522["fg"] = "#333333"
            GLabel_522["text"] = "Cash: PHP"+str(amount)
            GLabel_522.place(x=300,y=440)

            
            change=amount-finalprice

            GLabel_522=tk.Label(root)
            ft = tkFont.Font(family='Arial',size=10)
            GLabel_522["font"] = ft
            GLabel_522["fg"] = "#333333"
            GLabel_522["text"] = "Change: PHP"+str(change)
            GLabel_522.place(x=300,y=460)


        Button(root,text="Close and Conclude Transaction",command=lambda: self.close()).place(x=250,y=490)

        root.mainloop()

    def close(self):
        e = Employee.Employee()
        discount_SC_PWD=disc1
        e.addNewTransaction(finalprice, discount_SC_PWD,disc, u_id, items)
        frame_Table.delete(*frame_Table.get_children())
        root.destroy()

    def on_Closing(self):
        if messagebox.askyesno("Warning","Warning! Closing this Window will not Save this Transaction.\nContinue Closing?"):
            root.destroy()


# if __name__ == "__main__":
#     app = App()
