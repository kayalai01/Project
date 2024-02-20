from abstract import employee


class digitalmarket(employee):
    def attendance(self):
        print("market emp attendance")
    
    def salary(self):
        super().salary()
        print("sales increment")
        
        
digit = digitalmarket()

digit.attendance()

digit.salary()

digit.resign()
