from tkinter import *
from getmac import get_mac_address as gma
import platform,os,socket
def Shut():
    os.system("cmd /k shutdown /s")
def Rest():
    os.system("cmd /k shutdown /r")
def Sign_out():
    os.system("cmd /k shutdown /l")
def Hiber(self):
    os.system("cmd /k shutdown -h")
def check_ip():
    win2 = Toplevel(app)
    hostname=socket.gethostname()
    IP=socket.gethostbyname(hostname)
    label = Label(win2, text=IP, font="Times 20 bold")
    label.pack()
def sys_mac():
    win3=Toplevel(app)
    label=Label(win3,text=gma(),font="Times 20 bold")
    label.pack()
app=Tk()
app.geometry("450x200")
p=PhotoImage(file='icon.png')
app.iconphoto(False,p)
app.title("Application")
b1=Button(app,text="Shutdown",command=Shut,pady=5,padx=2,bg='#90d4a2',fg='black').grid(row=0,column=1)
b2=Button(app,text="Restart",command=Rest,pady=5,padx=2).grid(row=0,column=2)
b3=Button(app,text="Lock Screen",command=Sign_out,pady=5,padx=2).grid(row=0,column=3)
b4=Button(app,text="Hibernate",command=Hiber,pady=5,padx=2).grid(row=0,column=4)
b5=Button(app,text="Check_IP",command=check_ip,pady=5,padx=2).grid(row=0,column=5)
b6=Button(app,text="Sys_Mac",command=sys_mac,pady=5,padx=2).grid(row=0,column=6)
app.mainloop()