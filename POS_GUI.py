from ast import Delete
import Manager
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# import sqlite3

root = Tk()
root.title('Point Of Sales!!')
tab = ttk.Treeview(root)


# root.geometry("400x520")

# data=[
#    [1,"l",3,4,52]
#    [2,"w",3,7,521]
#    [3,"d",32,8,51]
#    [4,"f",3,49,52]
# ]

def reverse(tuples):
    New_Tup = tuples[::-1]
    return New_Tup


# def data_delete():
#     con = sqlite3.connect("data.db")
#     cursor = con.cursor()
#
#     # cursor.execute("Delete FROM Product WHERE product_ID="'"+str(data)+"'"")
#     con.commit()


# def Search():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#
#     cursor.execute("SELECT * FROM inventory")
#     results = cursor.fetchall()
#     conn.commit()
#     return results
#

# Frame Receipt
frame_Receipt = Frame(root, width=250, height=500)
frame_Receipt.grid(row=0, column=0)
myLabel1 = Label(frame_Receipt, text="PRODUCT RECORD!")
myLabel1.grid(row=0, column=0)

# Table
frame_Table = ttk.Treeview(frame_Receipt, height=17)
frame_Table['columns'] = ("ID", "Name", "Price", "QTY", "Total")
frame_Table.column("#0", width=0, stretch=NO)
frame_Table.column("ID", anchor=W, width=50, minwidth=300, stretch=NO)
frame_Table.column("Name", anchor=W, width=300, minwidth=300, stretch=NO)
frame_Table.column("Price", anchor=E, width=80, stretch=NO)
frame_Table.column("QTY", anchor=CENTER, width=50, stretch=NO)
frame_Table.column("Total", anchor=E, width=80, stretch=NO)
# Table Head
frame_Table.heading("#0")
frame_Table.heading("ID", text="ID", anchor=W)
frame_Table.heading("Name", text="Product", anchor=W)
frame_Table.heading("Price", text="Prices", anchor=E)
frame_Table.heading("QTY", text="QTY", anchor=CENTER)
frame_Table.heading("Total", text="TOTAL", anchor=E)
frame_Table.grid(row=1, column=0)
#
# frame_Table.insert(parent='', index='end', iid=1, text="", values=(1, "Hello", 2, 3, 4))

# Frame Detail & Button of ProductList
frame_Detail = Frame(root, width=250, height=200)
frame_Detail.grid(row=0, column=1)
Product_PIMG = Label(frame_Detail, text="IMAGE")
Product_Name_LA = Label(frame_Detail, text="Product Name:")
Product_Name_EN = Entry(frame_Detail, width=40, borderwidth=3)
Product_Prices_LA = Label(frame_Detail, text="Product Prices:")
Product_Prices_EN = Entry(frame_Detail, width=40, borderwidth=3)
Product_CODE_LA = Label(frame_Detail, text="Enter Product Name/Code:")
Product_CODE_EN = Entry(frame_Detail, width=40, borderwidth=3)
# Frame Detail & Button of ProductList grid
Product_PIMG.grid(row=0, column=0, columnspan=3)
Product_Name_LA.grid(row=1, column=0, columnspan=3, sticky=W)
Product_Name_EN.grid(row=2, column=0, columnspan=5)
Product_Prices_LA.grid(row=3, column=0, columnspan=3, sticky=W)
Product_Prices_EN.grid(row=4, column=0, columnspan=5)
Product_CODE_LA.grid(row=5, column=0, columnspan=3, sticky=W)
Product_CODE_EN.grid(row=6, column=0, columnspan=5)


# Button logic
def Button_LOGIC(Number):
    current = Product_CODE_EN.get()
    # Quantity = Product_Quantity.get()
    Product_CODE_EN.delete(0, END)
    Product_CODE_EN.insert(0, str(current) + str(Number))


# Button List
def Click_List():
    window_list = Toplevel()
    window_list.title("PRODUCT LISTS!")
    window_list.geometry("400x320")

    def search():
        result = Entry_Search.get()

    window_Frame = Frame(window_list, width=400, height=100)
    window_Frame.grid(row=0, column=0)

    Label_Search = Label(window_Frame, text="Search:")
    Entry_Search = Entry(window_Frame, width=50, borderwidth=3)
    button_Search = Button(window_Frame, text="Search", padx=5, pady=0, command=search())

    Label_Search.grid(row=0, column=0, sticky=W)
    Entry_Search.grid(row=0, column=1)
    button_Search.grid(row=0, column=3)

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

    window_Frame3 = Frame(window_list, width=400, height=50, bg="blue")
    window_Frame3.grid(row=2, column=0)

    m=Manager.Manager()
    m1=m.viewInv()
    count=0
    for x in m1:
        count+=1
        Search_Table.insert(parent='', index='end', iid=count, text=x, values=x)


    button_Close = Button(window_Frame3, text="Close", command=window_list.destroy)
    button_Close.pack()


# Button quantity
def Click_QTY():
    window_Qty = Toplevel()
    window_Qty.title("Quantity!")
    window_Qty.geometry("300x120")

    window_Frame = Frame(window_Qty, width=400, height=100)
    window_Frame.pack()

    def search():
        result = Entry_Quantity.get()

    Label_Quantity = Label(window_Frame, text="Enter the Quantity of the Products!")
    Entry_Quantity = Entry(window_Frame, width=30, borderwidth=3)
    button_Quantity = Button(window_Frame, text="ENTER", padx=5, pady=5, command=search())

    Label_Quantity.pack()
    Entry_Quantity.pack()
    button_Quantity.pack()


# Button Enter/search the item
def Click_Enter():
    result = 0
    Product_ID = str(Product_CODE_EN.get())
    Product_Name = str(Product_CODE_EN.get())
    if Product_ID == "" or Product_Name == "":
        Errror_Message = messagebox.showerror("Product Search", "Please Enter the Product ID or Name")
    else:
        # Logic
        print("logic here")
    #     INSERT(str(Product_CODE_EN))
    #
    # for result in reverse(Search()):
    #     frame_Table.insert(parent='', index='end', iid=result, text="", values=(result))
    # result += 1


# Button Delete
def Click_Delete():
    selected_Product = frame_Table()[0]
    data_delete = str(frame_Table.item(selected_Product)['values'][0])
    data_delete(data_delete)


# Button List
button_1 = Button(frame_Detail, text="1", padx=20, pady=10, command=lambda: Button_LOGIC(1))
button_2 = Button(frame_Detail, text="2", padx=20, pady=10, command=lambda: Button_LOGIC(2))
button_3 = Button(frame_Detail, text="3", padx=20, pady=10, command=lambda: Button_LOGIC(3))
button_4 = Button(frame_Detail, text="4", padx=20, pady=10, command=lambda: Button_LOGIC(4))
button_5 = Button(frame_Detail, text="5", padx=20, pady=10, command=lambda: Button_LOGIC(5))
button_6 = Button(frame_Detail, text="6", padx=20, pady=10, command=lambda: Button_LOGIC(6))
button_7 = Button(frame_Detail, text="7", padx=20, pady=10, command=lambda: Button_LOGIC(7))
button_8 = Button(frame_Detail, text="8", padx=20, pady=10, command=lambda: Button_LOGIC(8))
button_9 = Button(frame_Detail, text="9", padx=20, pady=10, command=lambda: Button_LOGIC(9))
button_0 = Button(frame_Detail, text="0", padx=20, pady=10, command=lambda: Button_LOGIC(0))

# Button Grid frame_CAL
button_0.grid(row=10, column=0, sticky="ew")
button_1.grid(row=9, column=0, sticky="ew")
button_2.grid(row=9, column=1, sticky="ew")
button_3.grid(row=9, column=2, sticky="ew")
button_4.grid(row=8, column=0, sticky="ew")
button_5.grid(row=8, column=1, sticky="ew")
button_6.grid(row=8, column=2, sticky="ew")
button_7.grid(row=7, column=0, sticky="ew")
button_8.grid(row=7, column=1, sticky="ew")
button_9.grid(row=7, column=2, sticky="ew")

# FOR Button
button_Enter = Button(frame_Detail, text="ENTER", padx=16, pady=10, bg="green", command=Click_Enter)
button_DEL = Button(frame_Detail, text="DELETE", padx=14, pady=10, bg="green", command=Click_Delete)
button_Quan = Button(frame_Detail, text="Quantity", padx=10, pady=10, bg="green", command=Click_QTY)
button_List = Button(frame_Detail, text="List", padx=25, pady=10, bg="green", command=Click_List)

# Button Grid frame_CAL
button_Enter.grid(row=10, column=3)
button_DEL.grid(row=9, column=3)
button_Quan.grid(row=8, column=3)
button_List.grid(row=7, column=3)

root.mainloop()
