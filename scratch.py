from tkinter import *
import platform,os
class msg(Toplevel):
    def __init__(self,app=None):
        super().__init__(app=app)
        i = PhotoImage(file='icon.png')
        self.iconphoto(False, i)
        self.title("System status")
        self.geometry("400x250")
        os.system("cmd /k shutdown /l")
        sys_details=Label(self,text=platform.release()).pack()
app=Tk()
app.geometry("300x200")
p=PhotoImage(file='icon.png')
app.iconphoto(False,p)
app.title("Application")
b1=Button(app,text="Shutdown",command=msg,pady=5,padx=2,bg='#90d4a2',fg='black').grid(row=0,column=1)
b2=Button(app,text="Restart",command="",pady=5,padx=2).grid(row=0,column=2)
b3=Button(app,text="Lock Screen",command="",pady=5,padx=2).grid(row=0,column=3)
b3=Button(app,text="Hibernate",command="",pady=5,padx=2).grid(row=0,column=4)
mainloop()