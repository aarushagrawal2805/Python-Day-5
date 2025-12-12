#Create a lambda function that squares a given number
def square(n):
    no = lambda n:n*n
    return no(n)

ans=square(10)
print(ans)