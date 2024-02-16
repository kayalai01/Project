class goggle():
    def __init__(self):
        print("Welcome to GOGGLE WORLD")
    def chrome(self):
        print("Lets Enter with words to search")
# g=goggle()
# g.chrome()

class gmail(goggle):
    def __init__(self):
        print("Welcome to login Gmail.")
        super().__init__()
        super().chrome()
    def login(self):
        print("Login mail wit user id and password:")
e=gmail()
e.login()



















