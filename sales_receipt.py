import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkFont
import Employee, Product, Manager
from datetime import datetime
import os
from dotenv import load_dotenv
import randomNumGen

class App:
    def __init__(self,discount,custom_discount,user_id, item_tuple):
        global root,u_id,items, discounted,discounted_custom,disc1,disc,sub,amount
        u_id=user_id
        items=item_tuple
        discounted=discount
        discounted_custom=custom_discount
        sub=self.computeSubtotal()
        disc1,disc=self.determineDiscount()
        # amount,change=self.Payment_GUI(sub)
        # amount,change=self.calculate(sub)

        root = tk.Tk()
        root.title("Sales Summary")
        width=600
        height=700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        root.protocol("WM_DELETE_WINDOW", self.on_Closing)
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_602=tk.Label(root,text="CRESDEL PHARMACY",font=('Arial',35,"bold"),justify=LEFT)
        GLabel_602.place(x=20,y=20)

        GLabel_899=tk.Label(root,text="Ilaya Carmen, Cagayan de Oro City",font=('Arial',15),justify=LEFT)
        GLabel_899.place(x=20,y=85)

        GLabel_459=tk.Label(root,text="Date Ordered: "+str(datetime.today().strftime('%Y-%m-%d')),font=('Arial',15),justify=LEFT)
        GLabel_459.place(x=20,y=120)
        
        global invo
        invo=randomNumGen.generateInvoice()
        GLabel_459=tk.Label(root,text="Invoice: "+str(invo),font=('Arial',15),justify=LEFT)
        GLabel_459.place(x=400,y=120)

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

        man=Manager.Manager()

        global subtotal,total1
        count=0
        subtotal=0
        total1=[]
        sub_tot=[]
        total_disc=[]
        essentials=[]

        percent=os.getenv('SC_DISCOUNT')
        for item in range(len(item_tuple)):
            print(item_tuple[item][0])
            ess=man.check_ifEssential(item_tuple[item][0])
            sub_tot.append(float(item_tuple[item][2])*int(item_tuple[item][1]))
            if ess[0]=='Yes' and discounted=="Senior Citizen 20%" or discounted=="PWD 20%":
                price=int(percent)/100*float(item_tuple[item][2])
                total=price*int(item_tuple[item][1])
                total1.append(float(item_tuple[item][2])*int(item_tuple[item][1])-total) 
                total_disc.append(total)
            else: 
                price=item_tuple[item][1]
                total=price
                total1.append(float(item_tuple[item][2])*int(item_tuple[item][1])) 
                total_disc.append(total)
                
            print(price,int(item_tuple[item][1]))
        
            frame_Table.insert('',index='end',iid=count,values=(item_tuple[item][0],item_tuple[item][2],item_tuple[item][1],float(item_tuple[item][2])*int(item_tuple[item][1])-total))
            count+=1
            subtotal=subtotal+float(item_tuple[item][2])*float(item_tuple[item][1])
                     
        emp=Employee.Employee()
        CashName=emp.getEmployee_Name(user_id)
        GLabel_450=tk.Label(root,text="Cashier: "+str(CashName[0]),font=('Arial',15),justify=LEFT)
        GLabel_450.place(x=20,y=470)

        GLabel_170=tk.Label(root,text="Subtotal: PHP {:.2f}".format(sum(sub_tot)),font=('Arial',10),justify=LEFT)
        GLabel_170.place(x=350,y=470)

        VAT=int(os.getenv('VAT'))/100*sum(sub_tot)
        
        GLabel_139=tk.Label(root,text="12% VAT: PHP {:.2f}".format(VAT),font=('Arial',10),justify=LEFT)
        GLabel_139.place(x=350,y=490)

        GLabel_522=tk.Label(root,text="Senior/PWD Discount: PHP {:.2f}".format(sum(total_disc)),font=('Arial',10),justify=LEFT)
        GLabel_522.place(x=350,y=510)

        GLabel_523=tk.Label(root,text="LESS: Other Discounts: PHP {:.2f}".format(disc),font=('Arial',10),justify=LEFT)
        GLabel_523.place(x=350,y=530)

        global finalprice
        finalprice=subtotal-disc1-disc

        GLabel_524=tk.Label(root,text="Total Amount Due {:.2f}".format(sum(total1)),font=('Arial',10),justify=LEFT)
        GLabel_524.place(x=350,y=550)

        amount,change=self.calculate(sub)

        GLabel_525=tk.Label(root,text="Cash: PHP {:.2f}".format(amount),font=('Arial',10),justify=LEFT)
        GLabel_525.place(x=350,y=570)            

        GLabel_526=tk.Label(root,text="Change: PHP {:.2f}".format(change),font=('Arial',10),justify=LEFT)
        GLabel_526.place(x=350,y=590)

        Button(root,text="Close and Conclude Transaction",bg="green",borderwidth=3,command=lambda: self.close()).place(x=190,y=640)

        root.mainloop()


    def close(self):
        e = Employee.Employee()
        p=Product.product()
        discount_SC_PWD=disc1
        e.addNewTransaction(finalprice, discount_SC_PWD,disc,amount,change, u_id, items,invo)
        ite=frame_Table.get_children()
        for i in range(len(ite)):
            rem=p.getRemainingBal(items[i][0])
            rem=[x[0] for x in rem]
            InventItems=(items[i][0],items[i][2],'-',datetime.today().strftime('%Y-%m-%d'),'-',items[i][1],rem[0]-items[i][1])
            p.Inventory(InventItems,'Sale')

            itemlist=list(items)
            itemlist.clear()
            
        # itemlist=list(items)
        # itemlist=[]
        # items=tuple(itemlist)

        frame_Table.delete(*frame_Table.get_children())
        
        root.destroy()

    def computeSubtotal(self):
        subtotal=0
        for item in range(len(items)):
            print(items) 
            print(float(items[item][2]),float(items[item][1]))
            subtotal=subtotal+float(items[item][2])*float(items[item][1])
        return subtotal

    def determineDiscount(self):
        if discounted=="Senior Citizen 20%":
            percent=os.getenv('SC_DISCOUNT')

            disc1=float(int(percent)/100*sub)

        elif discounted =="PWD 20%":
            percent=os.getenv('PWD_DISCOUNT')
            disc1=float(int(percent)/100*sub)
        else: 
            disc1=0

        if not discounted_custom:
            disc=0
        else:
            disc=float(discounted_custom)/100*subtotal

        return disc1, disc

    def Payment_GUI(self,sub):
        self.Payment_G = Toplevel()
        self.Payment_G.title("Amount Tendered")
        width=300
        height=200
        screenwidth = self.Payment_G.winfo_screenwidth()
        screenheight = self.Payment_G.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.Payment_G.geometry(alignstr)
        self.Payment_G.protocol("WM_DELETE_WINDOW",self.pay_on_closing)
        self.Payment_G.wm_attributes("-topmost", 1)
        self.Payment_G.resizable(False,False)

        Total_=Label(self.Payment_G,text=" ",font=('Arial',10))
        Total_.pack()

        Total_pay=Label(self.Payment_G,text="Total Price is "+str(sub),font=('Arial',20,"bold"))
        Total_pay.pack()

        Total_EAT=Label(self.Payment_G,text="Enter Amount Tendered ",font=('Arial',15))
        Total_EAT.pack()

        Total_Entry=Entry(self.Payment_G,width=20,font=('Arial',15))
        Total_Entry.pack()
        
        Total_1=Label(self.Payment_G,text=" ",font=('Arial',10))
        Total_1.pack()

        
        Payment_Button=Button(self.Payment_G,text="Enter",width=20,borderwidth=5,bg="green",command= self.calculate(amount))
        Payment_Button.pack()

        Total_2=Label(self.Payment_G,text=" ",font=('Arial',10))
        Total_2.pack()

    def pay_on_closing(self):
        self.Payment_G.wm_attributes("-topmost", 0)
        if messagebox.askyesno("Warning","Closing this Window this Transaction.\nContinue Closing?"):
            frame_Table.delete(*frame_Table.get_children())
            itemlist=list(items)
            itemlist=[]
            items=tuple(itemlist)
            root.destroy()


    def calculate(self,sub):
        global finalprice,change
        finalprice=sub-disc1-disc
        try:
            amount=simpledialog.askfloat("Enter Amount Tendered","Total Price is "+str(sum(total1))+"\nEnter Amount Tendered")
            if amount is None:
                messagebox.showinfo("Closed","Closed Without Saving")
            elif amount<sum(total1) and amount is not None:
                messagebox.showerror("Error","Amount Less than Actual Price")
                
            else:
                change=float(amount-sum(total1))
        except(ValueError):
            messagebox.showerror("Input Error","Enter a Valid Number")
        return amount, change

    def on_Closing(self):
        if messagebox.askyesno("Warning","Warning! Closing this Window will not Save this Transaction.\nContinue Closing?"):
            frame_Table.delete(*frame_Table.get_children())
            global items
            root.destroy()
            items = []


# if __name__ == "__main__":
#     app = App()