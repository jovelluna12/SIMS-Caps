import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import Manager

InvorVal = Tk()
Frame_main = Frame(InvorVal, width=1063, height=540, highlightbackground="black",
                                highlightthickness=2)
Frame_List = Frame(Frame_main, width=1058, height=540, padx=10, pady=10)
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview")
frame_Table = ttk.Treeview(Frame_List, height=23)
frame_Table['columns'] = ("Invoice Number","Purchase ID", "Item", "Quantity", "Total Price", "Discount", "Date Purchased")
frame_Table.column("#0", width=0, stretch=NO)
frame_Table.column("Invoice Number", anchor=W,)
frame_Table.column("Purchase ID", anchor=W,)
frame_Table.column("Item", anchor=W)
frame_Table.column("Quantity", anchor=E,)
frame_Table.column("Total Price", anchor=E,)
frame_Table.column("Discount", anchor=E,)
frame_Table.column("Date Purchased", anchor=E, )

frame_Table.heading("#0")
frame_Table.heading("Invoice Number", text="Invoice Number", anchor=W)
frame_Table.heading("Purchase ID", text="Purchase ID", anchor=W)
frame_Table.heading("Item", text="Item", anchor=W)
frame_Table.heading("Quantity", text="Quantity", anchor=W)
frame_Table.heading("Total Price", text="Total Price", anchor=W)
frame_Table.heading("Discount", text="Discount", anchor=W)
frame_Table.heading("Date Purchased", text="Date Purchased", anchor=W)
scrollbar = ttk.Scrollbar(frame_Table, orient="vertical", command=frame_Table)
scrollbar.pack(side="right", fill="y")

frame_Table.configure(yscrollcommand=scrollbar.set)    
frame_Table.pack()

m1 = Manager.Manager()
result = m1.inventoryList()
count = 0
for x in result:
    count += 1
    frame_Table.insert(parent='', index='end', iid=count, text=x, values=x)

InvorVal.mainloop()
