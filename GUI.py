import Employee, Manager
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from tkinter.ttk import Treeview
from datetime import date, datetime
## pip install pillow
from PIL import Image, ImageTk

import POS_GUI,InventoryGUI

#declare GUI var
class GUI():

    def __init__(self):
        self.loginGui = None
        self.session_user = None
        self.inTime = "Not Yet Timed In"
        self.outTime = None

    def login(self):
        global result
        usernameVal = self.username.get()
        passwordVal = self.password.get()

        self.employee = Employee.Employee()

        result = self.employee.login(usernameVal, passwordVal)

        if (result['user']):
            print("Setting Session")
            self.setSession('setUser', {"username": usernameVal, "password": passwordVal, "userID" : result['user'][0],"role":result["user"][4]})
            print("Session Set:")
            print(self.getSession('getUser'))
            self.showDashboard()
        else:
            messagebox.showerror(title="No User found", message="Incorrect user or password!")

    def setSession(self, action, *arg):
        if (action == 'setUser'):
            self.session_user = {
                "user" : arg[0]['username'],
                "password": arg[0]['password'],
                "userID": arg[0]['userID'],
                "role":arg[0]["role"]
            }
    
    def getSession(self, action):
        if (action == 'getUser'):
            return self.session_user

    def showDashboard(self):

        if (self.loginGui):
            self.loginGui.destroy()

        attendanceRows = self.employee.getAttendance(self.getSession('getUser')['userID'])

       
        self.dashboardGUI = Tk()
        #set title
        self.dashboardGUI.title('Cresdel Pharmacy')
        #set size
        self.dashboardGUI.geometry("1000x600")
        self.dashboardGUI.resizable(False,False)
        self.employeePage = Label(self.dashboardGUI, text=f"Employee Page", font=("Arial", 40)).place(x=230, y=12)

        self.scroll_CP=Frame(self.dashboardGUI)
        self.scroll_CP.place(x=230, y=90)
        
        self.tv = Treeview(self.scroll_CP, height= 20)
        self.tv['columns']=('ID','Name', 'Date', 'Working Time')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('ID', anchor=CENTER, width=190)
        self.tv.column('Name', anchor=CENTER, width=190)
        self.tv.column('Date', anchor=CENTER, width=190)
        self.tv.column('Working Time', anchor=CENTER, width=180)
        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('ID', text='ID', anchor=CENTER)
        self.tv.heading('Name', text='Name', anchor=CENTER)
        self.tv.heading('Date', text='Date', anchor=CENTER)
        self.tv.heading('Working Time', text='Working Time', anchor=CENTER)
        scrollbar = ttk.Scrollbar(self.scroll_CP, orient="vertical", command=self.tv.yview)
        scrollbar.pack(side="right", fill="y")
        self.tv.configure(yscrollcommand=scrollbar.set)    
        self.tv.pack()

        self.logoutButton = Button(self.dashboardGUI, text="Logout", command=self.logout, width=10, font=("Arial", 15), bg='#54FA9B').place(x=50, y=535) 
        
        self.startButton = Button(self.dashboardGUI, text="Start", width=10, font=("Arial", 15), bg='#54FA9B')
        self.startButton['command'] = lambda idx="Start", binst=self.startButton: self.timeIn(idx, binst)
        self.startButton.place(x=850, y=535)  

        self.NotifyButton=Button(self.dashboardGUI, text="Notification", width=10, font=("Arial", 15), bg='#54FA9B',command=self.Notification)
        self.NotifyButton.place(x=50, y=270)

        pos=POS_GUI
        self.POSButton=Button(self.dashboardGUI, text="Point of Sale", width=10, font=("Arial", 15), bg='#54FA9B',command = lambda m="pos": pos.start(m,result['user'][0],result['user'][1],self.inTime))
        self.POSButton.place(x=50, y=320)

        if result['user'][4]=="Manager" or result['user'][4]=="Owner":
            self.inventoryButton=Button(self.dashboardGUI, text="Inventory", width=10, font=("Arial", 15), bg='#54FA9B',command = lambda: self.startInventory())
            self.inventoryButton.place(x=50, y=370)


        print("userID ",result['user'][0])
        img_path="user.png"
        self.load = Image.open(img_path)
        self.load = self.load.resize((150, 150), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.dashboardGUI, image=self.render)
        self.img.image = self.render
        self.img.place(x=35, y=10)

        
        self.employeeName = Label(self.dashboardGUI, text=f"{self.session_user['user']}", font=("Arial", 15)).place(x=50, y=170)

        for i in attendanceRows:
            
            self.tv.insert(parent='', index=self.getTreeLength(self.tv), iid=self.getTreeLength(self.tv), 
            values=( i[0],  i[1], i[2], (f"{i[3]} - {i[4]} ") ))


        self.dashboardGUI.mainloop()
    
    global is_closing
    is_closing = FALSE
    global PageOpen
    PageOpen = 1

    def bring_to_front(self,event):
        global is_closing
        if not is_closing:
            self.NotifGUI.bell()
            self.NotifGUI.focus_force()

    def on_close(self):
            global PageOpen
            global is_closing
            is_closing = True
            self.NotifGUI.wm_attributes("-topmost", 0)
            if messagebox.askokcancel('Close', 'Close this Window?'):
                self.dashboardGUI.grab_release()
                PageOpen=1
                is_closing = FALSE
                self.NotifGUI.destroy()
            else:
                is_closing = False
                self.NotifGUI.wm_attributes("-topmost", 1)
    

    def Notification(self):
        global PageOpen
        if PageOpen<2:
            self.NotifGUI=Toplevel(self.dashboardGUI)
            self.NotifGUI.title("Notification")
            self.NotifGUI.geometry("500x520")
            self.NotifGUI.resizable(False,False)
            self.NotifGUI.protocol("WM_DELETE_WINDOW",self.on_close)
            self.NotifGUI.wm_attributes("-topmost", 1)
            self.NotifGUI.bind("<FocusOut>", self.bring_to_front)          
            self.NotifGUI.grab_set()

            self.Noti_Frame=Frame(self.NotifGUI,width=405,height=35)
            self.Noti_Frame.grid(row=0,column=0)

            self.Noti_Label=Label(self.Noti_Frame,text="Notification",font=("Arial", 20))
            self.Noti_Label.grid(row=0,column=0)


            #BOX
            self.Noti_BOX=Frame(self.NotifGUI,width=520,height=460,highlightbackground="black", highlightthickness=1,padx=5,pady=5)
            self.Noti_BOX.place(x=0,y=35)

            self.Noti_canvas=Canvas(self.Noti_BOX,width=465,height=460)
            self.Noti_canvas.pack(side=LEFT,fill=BOTH,expand=1)

            self.my_scrollbar= ttk.Scrollbar(self.Noti_BOX,orient=VERTICAL,command=self.Noti_canvas.yview)
            self.my_scrollbar.pack(side=RIGHT,fill=Y)

            self.Noti_canvas.configure(yscrollcommand=self.my_scrollbar.set)
            self.Noti_canvas.bind('<Configure>',lambda e: self.Noti_canvas.configure(scrollregion= self.Noti_canvas.bbox("all")))

            self.Noti_post=Frame(self.Noti_canvas)
            self.Noti_canvas.create_window((0,0), window=self.Noti_post,anchor=NW)

            a=Manager.Manager()
            message,name=a.notify_expiry()

            widgets=[]
            ids=[]
            x=0
            
            for thing in message:
                
                self.Noti_NotiBOX=Frame(self.Noti_post,width=570,height=70,padx=5,pady=5)
                self.Noti_NotiBOX.grid(row=x,column=0)
                widgets.append(self.Noti_NotiBOX)
                self.Noti_MessageBOX=Frame(self.Noti_NotiBOX,width=410,height=100,highlightbackground="black", highlightthickness=1,padx=5,pady=5)
                self.Noti_MessageBOX.grid(row=0,column=0)

                self.Noti_MTitle=Label(self.Noti_MessageBOX,text=name[x],font=("Arial", 12),width=43,height=2,anchor=W,wraplength=400)
                ids.append(id[x])
                self.Noti_MTitle.place(x=0,y=0)
                self.Noti_MBody=Label(self.Noti_MessageBOX,text=thing,font=("Arial", 10),wraplength=400,)
                self.Noti_MBody.place(x=0,y=50)

                for widget in widgets:
                    # for i in ids:
                        # wid=lambda w=widget: check(w)
                        # noted=lambda id=i: noteChecked(id)
                        
                    self.Noti_NotiButton=Button(self.Noti_NotiBOX,text="Close",command=lambda w=widget: (check(w), noteChecked(name[x])))
                    self.Noti_NotiButton.grid(row=0,column=1,padx=10)

                x+=1
            def check(w):
                w.destroy()
            
            def noteChecked(i):
                man=Manager.Manager()
                man.addNote(("Checked",i))

            PageOpen+=1
        else:
            messagebox.showinfo("Error","The Window is already Open!")

    def startInventory(self):
        INVOR=InventoryGUI.InvortoryGUI()
        INVOR.start(result['user'][0], result['user'][4])

    def timeIn(self, idx, binst):
        print(idx)
        print(binst)
        binst.place_forget()
        now = datetime.now()
        self.inTime = now.strftime("%Y-%m-%d %H:%M:%S")
        self.inTimeLang = now.strftime("%H:%M:%S") 
        self.stopButton = Button(self.dashboardGUI, text="Stop", command=self.timeOut, width=10, font=("Arial", 15), bg='#54FA9B')
        self.stopButton['command'] = lambda idx="Stop", binst=self.stopButton: self.timeOut(idx, binst)
        self.stopButton.place(x=850, y=535)  
        pos=POS_GUI
        m="pos"
        pos.start(m, result['user'][0],result['user'][1],self.inTime)

    def timeOut(self,idx,binst):
        today = date.today()
        dateNow = today.strftime("%Y-%m-%d")
        print(date)
        
        now = datetime.now()
        self.outTime = now.strftime("%Y-%m-%d %H:%M:%S")
        self.outTimeLang = now.strftime("%H:%M:%S") 

        insertId = self.employee.attendance(dateNow, self.inTime, self.outTime, self.getSession('getUser')['userID'])
    
        self.tv.insert(parent='', index=self.getTreeLength(self.tv), iid=self.getTreeLength(self.tv), 
        values=( insertId,  self.getSession('getUser')['user'], dateNow, (f"{self.inTimeLang} - {self.outTimeLang} ") ))
        binst.place_forget()

        
    def getTreeLength(self, tree):
        counter = 0
        for i in tree.get_children():
            counter += 1
        return counter
    
    def logout(self):
        if (self.outTime  == None):
            messagebox.showerror(title="Not Timed In", message="You Haven't Timed Out Yet")

        else:
            self.session_user = None
            self.dashboardGUI.destroy()
            self.showLogin()


    def showLogin(self):
        self.loginGui = Tk()
        #set title
        self.loginGui.title('Cresdel Pharmacy!!')
        #set size
        self.loginGui.geometry("1000x600")

        loginLabel = Label(self.loginGui, text="Login", font=("Arial", 55)).place(x=100, y=50)

        usernameLabel = Label(self.loginGui, text="Username:", font=("Arial", 25)).place(x=250, y=150)
        self.username = StringVar()
        usernameEntry = Entry(self.loginGui, textvariable=self.username, width=25, font=("Arial", 25)).place(x=250, y=200)

        passwordLabel = Label(self.loginGui, text="Password:", font=("Arial", 25)).place(x=250, y=250)
        self.password = StringVar()
        passwordEntry = Entry(self.loginGui, textvariable=self.password, show="*", width=25, font=("Arial", 25)).place(x=250, y=300)

        
        loginButton = Button(self.loginGui, text="Login", command=self.login, width=10, font=("Arial", 25), bg='#54FA9B').place(x=500, y=400)  
        
        self.loginGui.mainloop()

    def start(self):
        self.showLogin()