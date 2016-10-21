x= input("name")
print(x)
print("Hello world")

cars = 100
space_in_car = 4.0
driver = 30
passengers = 90
cars_not_driven = cars - driver
cars_driven = driver
carpool_capacity = cars_driven*space_in_car
average_passenger_per_car = passengers/cars_driven
print("there are" +  str(cars) + "cars available")		#convert int to string 
print("there are",cars,"cars available",sep = "-")		#prints combination of any data type using comma; sep used to 
														#separate between diff data types

newstring = " There are " + str(cars) + "cars available"
print(newstring)
print("there are",cars,"cars available",sep = "-")
values = (cars, "cars")
f = "there are %d %s available " % values
f = "there are %d %s available" %(cars, "cars")
print(f)