from tkinter import *
from tkinter import messagebox
from functools import partial
from tkinter.ttk import Treeview
import Employee
from datetime import date, datetime
## pip install pillow
from PIL import Image, ImageTk

import POS_GUI


#declare GUI var
class GUI():

    def __init__(self):
        self.loginGui = None
        self.session_user = None
        self.inTime = None
        self.outTime = None

    def login(self):
        global result
        usernameVal = self.username.get()
        passwordVal = self.password.get()
        print(usernameVal, passwordVal)

        self.employee = Employee.Employee()

        result = self.employee.login(usernameVal, passwordVal)

        if (result['user']):
            print("Setting Session")
            self.setSession('setUser', {"username": usernameVal, "password": passwordVal, "userID" : result['user'][0]})
            print("Session Set:")
            print(self.getSession('getUser'))
            messagebox.showinfo(title="Success", message="Login Successful!")
            self.showDashboard()
        else:
            messagebox.showerror(title="No User found", message="Incorrect user or password!")


    def setSession(self, action, *arg):
        if (action == 'setUser'):
            self.session_user = {
                "user" : arg[0]['username'],
                "password": arg[0]['password'],
                "userID": arg[0]['userID']
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
        self.dashboardGUI.title('Mafaith')
        #set size
        self.dashboardGUI.geometry("1000x600")
        self.employeePage = Label(self.dashboardGUI, text=f"Employee Page", font=("Arial", 25)).place(x=10, y=5)

        self.tv = Treeview(self.dashboardGUI, height= 20)
        self.tv['columns']=('ID','Name', 'Date', 'Working Time')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('ID', anchor=CENTER, width=190)
        self.tv.column('Name', anchor=CENTER, width=190)
        self.tv.column('Date', anchor=CENTER, width=190)
        self.tv.column('Working Time', anchor=CENTER, width=190)
        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('ID', text='ID', anchor=CENTER)
        self.tv.heading('Name', text='Name', anchor=CENTER)
        self.tv.heading('Date', text='Date', anchor=CENTER)
        self.tv.heading('Working Time', text='Working Time', anchor=CENTER)

        # self.tv.insert(parent='', index=0, iid=0, values=("vineet", "e11", 1000000.00, 'test'))

        # print(self.getTreeLength(self.tv))

        
        # self.tv.insert(parent='', index=1, iid=1, values=("vineet", "e11", 1000000.00, 'test'))

        
        # print(self.getTreeLength(self.tv))

        self.tv.place(x=230, y=90)

        
        self.logoutButton = Button(self.dashboardGUI, text="Logout", command=self.logout, width=10, font=("Arial", 15), bg='#54FA9B').place(x=50, y=535) 
        
        self.startButton = Button(self.dashboardGUI, text="Start", width=10, font=("Arial", 15), bg='#54FA9B')
        self.startButton['command'] = lambda idx="Start", binst=self.startButton: self.timeIn(idx, binst)
        self.startButton.place(x=850, y=535)  
        self.POSButton=Button(self.dashboardGUI, text="Point of Sale", width=10, font=("Arial", 15), bg='#54FA9B',command = POS_GUI.start(result['user'][0]))



        print("userID ",result['user'][0])

        self.POSButton.place(x=50, y=400)


        self.load = Image.open("user.png")
        self.load = self.load.resize((150, 150), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.dashboardGUI, image=self.render)
        self.img.image = self.render
        self.img.place(x=35, y=90)

        
        self.employeeName = Label(self.dashboardGUI, text=f"{self.session_user['user']}", font=("Arial", 15)).place(x=50, y=250)

        for i in attendanceRows:
            
            self.tv.insert(parent='', index=self.getTreeLength(self.tv), iid=self.getTreeLength(self.tv), 
            values=( i[0],  i[1], i[2], (f"{i[3]} - {i[4]} ") ))


        self.dashboardGUI.mainloop()

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
        if (self.inTime and self.outTime == None):
            messagebox.showerror(title="No Timeout Found", message="Please Timeout")
        else:
            self.session_user = None
            self.dashboardGUI.destroy()
            self.showLogin()



    def showLogin(self):
        self.loginGui = Tk()
        #set title
        self.loginGui.title('Mafaith')
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
