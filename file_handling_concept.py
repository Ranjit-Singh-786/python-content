import os
print(os.getcwd())
f = open("A:\\pythn\\decorator.py")
obj = f.readlines()          # this functionreturan ['dhkshkjs','jdhkd','ddfdf']
print(obj)
f.close()                    # close the file 


# #,,,,,print the first three line
s = f.readline()
print(s)
s1 = f.readline()
print(s1)
s2 = f.readline()
print(s2)



obj = f.read()             #read the file 
obj = f.read(30)           # define with the char size
print(obj)
obj2 = f.read(10)
print(obj2)
print(os.getcwd())
f = open("C:\\Users\Dell\Desktop\\radhey.py","x") 
print(os.getcwd())
os.chdir("C:\\Users\Dell\Desktop")
file = open("C:\\Users\Dell\Desktop\\file.txt", "w+")
t = file.read()
print(t)

print(os.getcwd())
print(os.listdir())        #for remove the file
os.rmdir("nesfolder")
os.remove("sqllchek.py")
print(os.getcwd())
t = open("C:\\Users\Dell\Desktop\\radhey.py","w+")
s = "this is my string"
t.write(s)
sw = t.read()
t.close()
print(sw)






def fuc(l):
#indentation problem occure here	
    for item in l:
#         return lambda itme: l[itme]
#     print(a(student))
# print(fuc(student))


# valu = []


# for i in student.values():
#     valu.append(i)
# print(type(valu))
# print(type(student))
# print(student.values())

# ,,,,,,,,successfully work,,,,,,




