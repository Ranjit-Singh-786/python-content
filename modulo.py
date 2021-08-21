class Student:
    name = "RANJIT SINGH"
    age = 24
    age2 = 24
    skill = "PYTHON"
    
    def __init__(self):
        self.a = "instence varieble"
    def ins_show(self):
        return f"this is your instence method acess :- {self.a} "
    @classmethod
    def show(cls):
        return f"NAME :{cls.name} age :{cls.age} skill : {cls.skill} "
    @classmethod
    def add(cls):
        return f"this is your class mehod add return := {cls.age + cls.age2} "
    @staticmethod
    def stat_add(a,b):
        return a * b
# print(Student.name)
    

