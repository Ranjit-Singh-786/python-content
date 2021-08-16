# # def add_two(num1,num2):
# #     return num1 + num2
# # a = int(input("enter a first number "))
# # b = int(input("enter second number "))
# # total = add_two(a,b)
# # print(f"this is your addition of two number {total}")


# # ...............program............
# # def add_threenum(a,b,c):
# #     print(a + b + c)
# # add_threenum(5,5,5)


# # ...............program 3...............
def chek(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2
a = int(input("enter a first number  "))
b = int(input("enter a second number  "))
ok = chek(a,b)
print(ok)
# # # ...............program4..........
# # def chek(a,b):
# #     if a > b:
# #         return a
# #     else:
# #         return b
# # a = int(input("enter a first number  "))
# # b = int(input("enter a second number  "))
# # ok = chek(a,b)
# # print(ok)
# # ..........................program 5,,,,,,,,,,,,,,,,,,,,,,,
# def chek(a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
# a = int(input("enter a first numbr "))
# b = int(input("enter a second numbr "))
# c = int(input("enter a third numbr "))
# check =chek(a,b,c)
# print(f"this is greatest value  {check} ")
# ,,,,,,,,,,,,,,,,,,,,palindrom program,,,,,,,,,,,,,,,,,
# name = input("enter your strin : ")
# def chek(name):
#     # return name[::-1]
#     if name[::-1]==name:
#         print("this is palidrom")
#     else:
#         print("this is not palidrom")

# check = chek(name)
# print(check)
# ,,,,,,,,,,,,,,,,,,,,,,palindrome Example2,,,,,,,,,,,,,,,,,,
# name = input("enter your strin : ")
# def chek(name):
#     # return name[::-1]
#     if name[::-1]==name:
#         # print("this is palidrom")
#         return True
#     # else:
#         # print("this is not palidrom")
#     return False
# print(chek("madam"))
# print(chek("horse"))
# ,,,,,,,,,,,,,,,,,,,palindrom example3,,,,,,,,,,,,,,,,,,,
# def is_palindrom(word):
#     return word == word[::-1]
# print(is_palindrom("madam"))
# print(is_palindrom("horse"))
for i in range(1,11):
    print(i,end =",")

