class grandparents():
    def __init__(self,grandpa,grandma,familyname):
     self.grandfather=grandpa
     self.grandmother=grandma
     self.familyname=familyname
    
    def welcome(self):
     print ( "welcome to ",self.familyname, "wishes from ", self.grandfather, "and" , self.grandmother)
     
x=grandparents("Nateshan","palambal","Nateshanfam") 
x.welcome()

   
      
