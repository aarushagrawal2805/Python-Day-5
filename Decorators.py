def deco(func):
    def wrap(func1):
      def wrapper(*args):
        print("Hello Coder")
        func(*args)
        func1(*args)
        print("Thank you")
      return wrapper
    return wrap

def Add(a,b):
    print("Sum is :",a+b)
@deco(Add)
def Sub(a,b):
    print("Subtraction is :",a-b)

Sub(10,5)