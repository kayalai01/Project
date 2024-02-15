class solarfamily():
    def __init__(self):
        print("Welcome to solar family")
    
    def sun(self):
        print("sun rise on morning")
        
    def moon(self):
        print("moon upcoming night")
        
class glassy(solarfamily):
    def __init__(self):
        super().__init__()
        super().sun()
        super().moon()
        
    def star(self):
        print("present of milkyway glassy")
        
s=glassy()
s.star