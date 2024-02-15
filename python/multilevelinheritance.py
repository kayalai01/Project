class Brightservice():
    def __init__(self):
        print("welcome to our Bright service Association .")
    def ceo(self):
        print("Mr.Joes is a ceo of Bright service.")
    def manager(self):
        print("Mr.Jack is a manager of Bright services")
    def staff(self):
        print("Mis.Flores Nisha is HR of our company.")
    def coordinator(self):
        print("Mr. Karthick is a student coordinator.")
    def project(self):
        print("WE are trained a TNDSC program.")
    def batch(self):
        print("We training about a AI and CAD ")
    def AI(self):
        print("AI batch conduct a morning session .")
    def CAD(self):
        print("CAD batch is conduct Afternoon Session")
        
class BPO(Brightservice):
    def __init__(self):
        super().__init__()
        super().ceo()
        super().manager()
        super().staff()
        super().coordinator()
        super().project()
        super().batch()
        super().AI()
        super().CAD()
            
        print("our service is AR calling for US.")
        
    def emp(self):
        print("There are 40 members in Night shift.")
# x=BPO()
# x.emp()        
 
           
class Recquitors(BPO):
    def __init__(self):
        print("We are Recquiting A USA Candidates.")
        super().__init__()
        
R=Recquitors()
       