class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sundar(self):
        print(self.name)
        print(self.age)
        
    def info(self):
        print("Hi my name is {} and my age is {}".format(self.name,self.age))

emp1 = employee('mogan',35)
emp2 = employee('jackson',50)
emp3 = employee('ragu',10)

emp1.info()
emp2.info()
emp3.info()
