import csv
import os
print(os.getcwd())
os.chdir(r"A:\pythn\pandas")
print(os.getcwd())
print(os.listdir())
with open("friend.csv","r") as csv_file:
        csv_reder=csv_file.read()
print(csv_reder)
print(os.listdir(r"a:\pythn"))

open(r"a:\pythn\csv_operation.py","x")
for i in os.listdir(r"a:\pythn"):
        if i=="csv_operation.py":
                print("this file is exists")
        else:
                print("this file is not your exists")



# print(type(data))
# if os.path.exists(r"a:\\pythn\\csv_operation.py"):
#         with open(r"a:\\pythn\\csv_operation.py","w") as pythn_file:
#                 pythn_file.write(data)
#                 print("write your all data")
# else:
#         print("this file is not present")
with open(r"a:\\pythn\\csv_operation.py","r") as pythn_file:
        print("file reading started")
        print()
        print(pythn_file.read())