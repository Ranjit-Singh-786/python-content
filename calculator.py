i = 0
while i <=10:
    num1 = int(input('enter your first number :- '))
    choice = input('enter your operation :- ')
    num2 = int(input('enter your first number :- '))

    def addi(num1,num2):
        print(num1+num2)
    def sub(num1,num2):
        print(num1-num2)
    def mult(num1,num2):
        print(num1*num2)
    def dive(num1,num2):
        print(num1/num2)
    def sqr(num1,num2):
        print(num1**num2)
    if choice =="+":
        addi(num1,num2)
    elif choice == "-":
        sub(num1,num2)
    elif choice == "*":
        mult(num1,num2)
    elif choice == "/":
        dive(num1,num2)
    elif choice == "**":
        sqr(num1,num2)
    i+=1
