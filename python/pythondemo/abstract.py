from abc import ABC ,abstractmethod

class employee(ABC):
    @abstractmethod
    def attendance(self):
        pass
        
    def salary(self):
        print("Basic salary")
    
    def resign(self):
        print("employee resignation")
