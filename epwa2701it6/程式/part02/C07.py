class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
    self.graduationyear = 2000

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.sex = 'boy'
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear,x.sex)
