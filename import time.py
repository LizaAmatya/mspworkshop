import time
print("this is python programming")
time.sleep(3)
print("thank you")

def sum(a,b):
    return a+b
def divide(number, divideby):
    return number/divideby
print(divide(10,5))
print(divide(50,10))
print(divide(10,50))
print(divide(divideby=10, number=50))

def sum(*numbers):
    print(numbers)
sum(1)
sum(1,2)
