#Assign a different name to function and call it through the new name

def Person(name,age):
      print("Name is :",name,"Age is :",age)

#Calling with Same Name:
Person("Anil",20)

#Calling Same function But with another name:
Person2=Person
Person2("Amit",18)
