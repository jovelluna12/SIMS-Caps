from tkinter import *
from tkinter import messagebox
from functools import partial
import Employee
#decalre GUI var
class GUI():
    def login(self):
        usernameVal = self.username.get()
        passwordVal = self.password.get()
        print(usernameVal, passwordVal)

        employee = Employee.Employee()

        result = employee.login(usernameVal, passwordVal)

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

        self.loginGui.destroy()

        self.dashboardGUI = Tk()
        #set title
        self.dashboardGUI.title('Mafaith')
        #set size
        self.dashboardGUI.geometry("1000x600")

        loggedInUser = Label(self.dashboardGUI, text=f"Logged In User is : {self.session_user['user']}", font=("Arial", 55)).place(x=100, y=50)

        
        logoutButton = Button(self.dashboardGUI, text="Logout", command=self.logout, width=10, font=("Arial", 25), bg='#54FA9B').place(x=500, y=400)  


        self.dashboardGUI.mainloop()
    
    def logout(self):
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
