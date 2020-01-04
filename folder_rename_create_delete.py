import os
def makedir():
    askname=input("Please enter the folder name: ")
    os.mkdir(askname)
def deldir():
    folder_name=input("Please enter the folder name: ")
    os.removedirs(folder_name)
def renamedir():
    present_name=input("Please enter the present name of the folder:")
    update_name=input("Please enter the name to update: ")
    os.rename(present_name,update_name)
print("Program is to Create Folder and Delete Folder")
askfor=input("Please type your choice:\t1 for Make Directory\t2 for Delete Directory\t3 for Rename Folder\n")
if askfor==("1"):
    makedir()
elif askfor==("2"):
    deldir()
elif askfor==("3"):
    renamedir()
else:
    print("Wrong Input")
