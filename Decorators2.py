import time
def validate(func):
    def wrapper():
        star_time=time.time()
        name = input("Enter your name: ")
        age = input("Enter your age: ")

        if not age.isdigit():
            print("Invalid age! Please enter a number.")
            

        end_time=time.time()
        execute=end_time-star_time
        print("Time taken To Execute The Code :",execute,"Seconds")
        return func(name, int(age))
    return wrapper

@validate
def show(name, age):
    print("Details Proccesed Succesfully")
    print("Welcome", name, "Your age is", age)

show()
