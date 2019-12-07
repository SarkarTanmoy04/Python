from tkinter import *
import platform
master=Tk()
master.geometry("500x300")
master.title("Information Details")
a=(platform.processor(),"\n\n",
   platform.node(),"\n\n",
   platform.machine(),"\n\n",
   platform.system(),"\n\n",
   platform.platform(),"\n\n",
   platform.uname(),"\n\n",
   platform.version())
msg=Message(master,text=a, font="Bold")
msg.pack()
master.mainloop()

