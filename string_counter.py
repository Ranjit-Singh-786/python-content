name = input("enter your name :- ")
temp = " "
i = 0
while i <= len(name):
    if name[i] not in temp :
        print(f' {name[i]} : {name.count(name[i])} ')
    i +=1
