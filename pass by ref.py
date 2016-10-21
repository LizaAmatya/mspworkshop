def change_the_list(mylist):
    mylist = [1,2,3]
    print("Values inside function",mylist)
    return
mylist = [5,6,7]
print("values outside function",mylist)

    
change_the_list([1,5])


def change_the_list(name,age=19):
    mylist = [1,2,3]
    print("name:",name)
    print("age: ",age)
    return

change_the_list("liza")
change_the_list("rujeena")
change_the_list(name="liza")


argument = 3
def number():
    argument = 4
    print("local variable:",argument)

number()
print("global variable: ",argument)




