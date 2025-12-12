#Create a recursive function
def addition(num):
    if num != 0:
        return num + addition(num - 1)
    else:
        return 0

res = addition(5)
print(res)

#Dry Run
#5+4+3+2+1