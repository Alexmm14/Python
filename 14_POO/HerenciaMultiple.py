from msilib.schema import SelfReg


class A():
    def primera(self):
        return "Esta es la sentencia A"

class B():
    def segunda (self):
        return "Esta es la sentencia B"

class C (A, B): #se le hereda de dos padres
    pass


c= C()
print(c.primera())
print(c.segunda())