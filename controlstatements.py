num=int(input("Enter a number: "))

if num%2==0:
    print(f"{num} is an Even number")
else:
    print(f"{num}is an Odd number")

#create a program that checks if someone can vote or not using age above 18

num1=int(input("Enter your age: "))

if num1>=18:
    print(f"Your age is {num1}yrs you can vote")
else:
    print(f"Your age is {num1}yrs you are under age")

#create a program to grade students from A to Fail

mark=int(input("Enter your mark: "))
if mark<=100 and mark>=80:
    print("you have an A")
elif mark<=79 and mark>=60:
    print("you have an B")
elif mark>=40 and mark<=59:
    print("you have an C")
elif mark==0 and mark>=39:
    print("you have Failed terribly")
else:
    print("invalid marks entered")
