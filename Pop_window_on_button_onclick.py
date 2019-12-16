from tkinter import *
import platform
master=Tk()
master.geometry("300x100")
master.title("Button Window")
def new_window():
    newwin=Toplevel(master)
    newwin.geometry("550x200")
    newwin.title("Display Window")
    quote="This is just a popup window"
    w1=Label(newwin,text=quote,font="Helvetica 12 bold")
    w1.pack()
b1=Button(master,text="Click Me..!",font='calibri 10 bold',pady='5',command=new_window)
b1.pack()
master.mainloop()