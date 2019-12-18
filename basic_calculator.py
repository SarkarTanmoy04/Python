def add(x,y):
    return x+y
def mul(x,y):
    return x*y
def sub(x,y):
    return(x-y)
def div(x,y):
    return(x/y)

x=float(input("Enter the first value: "))
y=float(input("Enter the second value: "))

print("1. Addition 2. Subtraction 3.Multiplication 4.Division\t")
val=input("Please enter your choice: ")
if (val=="1"):
        print(x,"+",y,"=",add(x,y))
elif(val=="2"):
    print(x,"-",y,"=",sub(x,y))
elif(val=="3"):
    print(x,"*",y,"=",mul(x,y))
elif(val=="4"):
    print(x,"/",y,"=",div(x,y))
else:
    print("Invalid Input")
