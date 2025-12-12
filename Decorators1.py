def User_input(func):
    def wrapper():
        print("Enter your Details :")
        S="\U0001F600"
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        print("Thank you for the details",S)
        print("Processing your details",S)
        return func(name, age)
        
    return wrapper

@User_input
def Person(name, age):
    print("Name:", name)
    print("Age:", age)

Person()
