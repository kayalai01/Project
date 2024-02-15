class tnsdc():
    def __init__(self):
        print("Welcome to TNSDC webpage.")
    def login(self):
        print("Enter Your USERNAME and Password.")
    def email(self):
        print("Enter u r Reg EMail ID.")
    def contact(self):
        print("Enter u r Reg Mobile no. ")
    def aadhar(self):
        print("Enter u r Aadhar No.")
    def batch(self):
        print("U have Choose a course batch.")
        
class AIbatch(tnsdc):
    def __init__(self):
        super(). __init__()
        super().login()
        super().email()
        super().contact()
        super().aadhar()
        super().batch()
        print("welcome to AI Batch Courses.")
    def C(self):
        print("i can study c")
    def cpp(self):
        print("i can study c++")
    
    def python(self):
        print("i can study python")

class CADbatch(tnsdc):
    def __init__(self):
        super(). __init__()
        super().login()
        super().email()
        super().contact()
        super().aadhar()
        super().batch()
        print("welcome to CAD Batch Courses.")
    def html(self):
        print("i can study html")
    def javascript(self):
        print("i can study javascript")
    
    def csharp(self):
        print("i can study C#")
    
#cad=CADbatch()
ai=AIbatch()
ai.C()
ai.cpp()
ai.python()