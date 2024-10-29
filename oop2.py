#create a class person with  name, age and gender as the attribute constructor
#constructor method
class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
#method
    def display(self):
        print(f"my name is {self.name}, my age is {self.age}, my gender is {self.gender},")
#instance
myobj2=person("Robert",16,"male")
myobj2.display()
myobj2=person("Mary",36,"female")
myobj2.display()