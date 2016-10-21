def add(a,b):
    c=a+b
    print(c)

def subtract(a,b):
    c=a-b
    print(c)

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
print(sum(1))
print(sum(1,2))


def sum(*numbers):
    sum=0
    for number in numbers:
        if number < 0:
            continue
        sum += number
    return sum

print(sum(1))
print(sum(1,2))
print(sum(1,2,-5))


