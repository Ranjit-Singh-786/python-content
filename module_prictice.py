# ,,,,,,,,,first type importing module,,,,,,,,,,

import modulo
obj = modulo.Student()
print(f"instence accessing :- ",obj.a)
print(obj.ins_show())
print()
print("class method call")
print()
print(obj.show())
print()
print(obj.add())
print()
print(f"static method call  : {obj.stat_add(5,5)} ")
print(Student.name)

# ,,,,,,,,,,,second type importing,,,,,,,,,,,

 import modulo as m
 # here i will created objec by using alias name and all function call by object
obj = m.Student()
print(f"instence accessing :- ",obj.a)
print(obj.ins_show())
print()
print("class method call")
print()
print(obj.show())
print()
print(obj.add())
print()
print(f"static method call  : {obj.stat_add(5,5)} ")

# ,,,,,,,,,,,third type importing module,,,,,,,,,,,,,,,,,,,
from modulo import Student
obj = Student()
print(obj.ins_show())
print(obj.show())
print(obj.stat_add(20,20))
print(obj.name)
print(obj.age)
print(obj.age2)
print(obj.skill)
obj.skill = "java"
print(obj.skill)

from modulo import Student as st
obj = st()
print(obj.stat_add(10,10))
print(obj.a)
print(st.age)     #here i am using alias name of class bczz this is class variable



# ,,,,,,,,,,,,fourth type of importing,,,,,,,,,,,,
# from modulo import Student as s
# obj = s()
# print(obj.ins_show())
# print(obj.show())
# print(obj.stat_add(20,20))
# print(obj.name)
# print(obj.age)
# print(obj.age2)
# print(obj.skill)
# obj.skill = "java"
# print(obj.skill)

# ,,,,,,,,,,,fifth type importing,,,,,,,,,,,,,,,,,,,,,,
# from modulo import*
# obj = Student()
# print("here i have changed class varieble value ")
# Student.name = "harshit vashishtha"
# print(obj.show())
# print(obj.name)
# print(obj.a)
# print(obj.skill)
# print(obj.age)
# print(obj.age2)
# print(obj.stat_add(25,25))
# print(obj.ins_show())
# print("all function has called according to this syntex")
