# cars=["toyota","suzuki","Hyundai","Honda"]
# cars.insert(0,"BMW")
# print(cars)


cars=("toyota","honda","suzuki")

vehicle=list(cars)
vehicle[0]="Nissan"
cars=tuple(vehicle)
# print(cars)

# sets atre unordered,unchangable, unindexed, non-duplicate
fruits={"mango","orange","apple","banana","apple"}
# if "banana" in fruits:
    # print("banana")
    # fruits.remove("banana")
    # print(fruits)

fruits.add("avocado")
# print(fruits)
Dict ={cars}
print(Dict)