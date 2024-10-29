class fruits:
    def __init__(self, name,price,color):
        self.name = name
        self.price = price
        self.color = color

       #method
    def display(self):
        print(f"i love eating {self.name}, it costs {self.price}, and its color is {self.color}")


#instance
myobj=fruits("apple",35,"green")
myobj.display()
myobj=fruits("banana",20,"yellow")
myobj.display()