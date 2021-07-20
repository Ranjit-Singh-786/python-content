import os
print(os.getcwd())

# os.rmdir('new_folder')
print("output here !!")
for i in os.listdir():
    print(i)
os.mkdir('new_folder')

,,,,,,,,,,,,condition if present so dleate and nhi to create,,,,,,,,,,,,


if os.path.exists("new_folder"):
    os.rmdir("new_folder")
else:
    os.mkdir("new_folder")

,,,,,,,,another field create list all item,,,,,,,,,,

print(os.getcwd())
os.chdir((r'E:\ ' ))
for i in os.listdir():
    print(i)
,,,,,,,,,,,,,chek already exists or not,,,,,,,,,,

if os.path.exists("new_folder"):
    print("already exists")
else:
    os.mkdir("new_folder")
print(os.getcwd())

os.rmdir("new_folder")
print(os.path.exists("new_folder"))

os.makedirs('child/parent/grand')
os.removedirs('child/parent/grand')

import shutil
print(os.getcwd())
open("student.txt","a").close()
print(os.getcwd())
os.chdir(r'A:\pythn\child')
print(os.getcwd())
print(os.listdir()
shutil.move("student.txt",'A:\pythn\child\student3.txt')
shutil.move("student.txt",'child/student2.txt')
os.chdir(r'A:\pytoshn\child')
open("student2.txt","a").close()