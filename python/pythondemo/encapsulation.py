

#a = 20 # public variable

#_b = 20 # protected variable

#__c = 20 # private variable


class sample:
    def encap(self):
        self.__a = 10 # private
        self._b = 20    # protected
        self.c = 30     #public

obj = sample()

obj.encap()

print(obj.__a)
print(obj._b)
print(obj.c)
