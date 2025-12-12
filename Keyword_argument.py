#(**) means multiple keyword argument in calling function
def deco(func):
      def decorate(*args,**kwargs):
            print("Here Are the Information of Person")
            func(*args,**kwargs)
            
            print("Thank you for Coding here")
            
      return decorate
@deco
def Keyword(**kargs): 
    if kargs:
     print("-------Information------\n")    

     for key,value in kargs.items():
        print(key,":",value)
    else:
        print("\n No information ")
    
Keyword(Name="Amit",Age=20,City="Indore")
Keyword(Job="Doctor",Salary=20000)
Keyword()