# Create a function with variable length of arguments
def func1(*n):
    print("Numbers are :")
    for i in n:
     print(i)

func1(10,20,30)
func1(20,30)