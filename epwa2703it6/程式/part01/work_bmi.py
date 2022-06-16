import math
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, weight,height):
    super().__init__(fname, lname)
    self.weight = weight
    self.height = height


  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "your weight and height:", self.weight, self.height)
    height = float(self.height)
    weight = float(self.weight)
    bmi_value = round(self.weight / math.pow(self.height, 2), 2)
    if bmi_value < 18.5:
        myS= '體重過輕囉，多吃點！'
    elif bmi_value >= 18.5 and bmi_value < 24:
        myS= '體重剛剛好，繼續保持！'
    elif bmi_value >= 24 :
        myS= '體重有點過重囉，少吃多運動！'
    print('你的 BMI 指數為：{} {}'.format(bmi_value,myS))
 
x = Student("Mike", "Olsen", 60,1.8)
x.welcome()