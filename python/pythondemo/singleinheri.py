class grandparents():
    def __init__(self,grandpa,grandma,familyname):
     self.grandfather=grandpa
     self.grandmother=grandma
     self.familyname=familyname
    
    def welcome(self):
     print ( "welcome to ",self.familyname, "wishes from ", self.grandfather, "and" , self.grandmother)
     
#x=grandparents("Nateshan","palambal","Nateshanfam") 
#x.welcome()

class mahendhran(grandparents):
    def __init__(self,grandpa,grandma,familyname,fathername,mothername):
     self.fathername=fathername
     self.mothername=mothername
     super().__init__(grandpa,grandma,familyname)
        
    def thanks(self):
        print("Hi grandpa", self.grandfather, "and grandma", self.grandmother,"we", self.fathername, "and" , self.mothername, "thank you for warm welcome to our ", self.familyname, "family")
        
x=mahendhran("Nateshan","palambal","Nateshanfam","mahendhran","Ragini mahendhran")
x.welcome()
x.thanks() 

   
      
