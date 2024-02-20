class father:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def father_info(self):
        print("Hi my name is {} , I am the father class".format(self.name))


class son(father):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def son_info(self):
        print("Hi my name is {} , I am the son class".format(self.name))
        

son1 = son('sun',25)

son1.father_info()
son1.son_info()

