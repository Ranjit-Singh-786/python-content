class Mobile(object):
    def __init__(self):
        self.model = "realmi "
        self.brand = "C1"
    def show_method(self,p):
        price = p
        print("model: " ,self.model , self.brand ,price)
obj1 = Mobile()
obj1.brand = "C2"
obj1.show_method(2500)
print(id(obj1))