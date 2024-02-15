class student():
    def __init__(self):
        print("Hii kayal!!..welcome to u r studies")   
    def sslc(self):
        print("you got a first class.")
    def hsc(self):
        print("choose a Bio_maths group.")   
    def school(self):
        print("she is completed a school with a 60 percentage.")   
    def Engineering(self):
        print("She is a selected a ENGINEER course.")   
    def specification(self):
        print("she is choose a Mechnical engineering.")
        
class carrer():
    def __init__(self):
        print("Lets see about carrer.")
    def Developer(self):
        print("I am software Engineer.")
    def officer(self):
        print("I am become a IAS officer.")
    
class extracurriculum(student,carrer):
    def __init__(self):
        print("I am completed a Autocad, solidworks, catia,windows,network,linux,unix,devops,cloudcomputing,c programming, c++ language, mysql, python, github")

        super().__init__()
        super().sslc()
        super().hsc()
        super().school()
        super().Engineering()
        super().specification()
        super().Developer()
        super().officer()
        
E= extracurriculum()
        