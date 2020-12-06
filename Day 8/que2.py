try:
    
    n1,n2,operator = int(input("Enter First Number: ")), int(input("Enter Second Number: ")), input("Enter Arithmetic Operator: ")

    if operator == '+':
    
        print(n1,"+",n2,"=",n1+n2)
    
    elif operator == '-':
        
        print(n1,"-",n2,"=",n1-n2)
    
    elif operator == '*':
        
        print(n1,"*",n2,"=",n1*n2)
    
    elif operator == '/':
        
        try:
            
            print(n1,"/",n2,"=",n1/n2)
            
        except ZeroDivisionError:
            
            print("/ by zero")
    
    elif operator == '%':
    
        print(n1,"%",n2,"=",n1%n2)
    
    else:
        
        print("Invalid Operator")
        
except:
    
    raise Exception("Invalid Input")
