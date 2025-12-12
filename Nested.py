#Create a program with nested functions to perform an addition calculation 
# outer function
def outer_fun(a, b):
    pass

    # inner function
    def addition(a, b):
        return a + b

    add = addition(a, b)
    return add + 10

result = outer_fun(50, 10)
print("Sum is :",result)