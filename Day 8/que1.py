#Types of Errors and Exception

#1.Syntax error



myList = [1,2,3,4,5]

try:
    
    print(myList[6])
    
except:
    
    print("Array Index Out of Bound Exception")
    
finally:
    
    print("End of Code")



str = "Hello"

try:
    
    str[0] = 'h'

except:
    
    raise Exception("String are immutable")

a = "Hello"

try:
    
    print(b)
    
except:
    
    print("Name is not defined")
    
else:
    
    print("End of Code")


try:
    
    print(12/0)
    
except:
    
    raise Exception("Don't divide the numbers by zero")
    
finally:
    
    print("End of Program")
    
# Exception: Don't divide the numbers by zero    