#Create a function with a default argument

def show_employee(name,salary=9000):
  print("Employee Name is :",name,"Salary is :",salary)

show_employee("Anil",20000)
show_employee("Amit")#There is only one argument so it take default parameter value