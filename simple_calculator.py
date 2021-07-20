def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def division(a,b):
    return a // b
def pow(a,b):
    return a ** b
num = int(input("enter your first number "))
# num2 = int(input("enter your second number "))
choice = input("enter your operation ")
if choice == "+" :
    print(add(num,num2))
elif choice== "-" :
    print(sub(num,num2))
elif choice== "*" :
    print(mult(num,num2))
elif choice== "/" :
    print(division(num,num2))