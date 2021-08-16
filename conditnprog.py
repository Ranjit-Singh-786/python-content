num1 = int(input("enter your first number:"))
oper = str(input("select your operation number:"))
num2 = int(input("enter your second number:"))
if oper=='+':
	print("this is your addition:",num1,"+",num2,"=",num1+num2)
elif oper=='-':
	print("this is your subtraction:",num1,"-",num2,"=",num1-num2)
elif oper=='*':
	print("this is your multiplication:",num1,"*",num2,"=",num1*num2)
elif oper=='/':
	print("this is your division:",num1,"/",num2,"=",num1/num2)
else :
	print("invalid operation")

