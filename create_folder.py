import os       #importing os module
path=input("Please Enter any valid path: ")     #asking for a valid path, path will store into the valiable
os.chdir(path)  #will change directory to set the declared path
folder=input("Please enter a name: ")   #asking for folder name, name will stored into the path
os.mkdir(folder)    # command to create folder and passing the variable stored named as parameter
