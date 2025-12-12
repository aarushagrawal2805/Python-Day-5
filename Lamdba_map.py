#Use a lambda with the map() function to double each element in a list

numbers = [1, 2, 3, 4, 5]

def square():
    square1=list(map(lambda x:x+x,numbers))
    return square1

print(square())