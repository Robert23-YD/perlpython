# list data structure, mutable/changable, ordered

cars=["toyota","nissan","subaru",]
cars[1]="BMW"
cars.append("Mazda")
cars.pop(1)
cars.insert(1,"volvo")

num=[6,8,1,6,78,12,0]
print(f"the largest number is {max(num)}")




print(cars)
print(f"i love {cars[1]}")

#tuple, ordered, immutable
fruits=("mangoes","banana","watermelon","pinneapple")


print(fruits)
print(f"i love eating {fruits[1]}")
print(f"i love {fruits[2]}")

#set, unordered, non index
comp={"hp","lenovo","ibm"}
print(comp)

#dictionaries
employee={"name":"Robert","age":58,"salary":3000}
print(employee)
print(f"The name of the employee is {employee['name']}")
print(f"the age of the employee is {employee['age']}")