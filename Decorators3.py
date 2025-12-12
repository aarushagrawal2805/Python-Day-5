def Decor(Add):
    def inner():
        result=Add()
        num3=int(input("Enter Third number :"))
        result += num3
        return result
    return inner



@Decor
def Add():
    num1=int(input("Enter First Number :"))
    num2=int(input("Enter Second Number :"))
    result=num1+num2
    return result

print(Add())