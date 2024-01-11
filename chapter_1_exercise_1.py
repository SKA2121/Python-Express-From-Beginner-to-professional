# Exercise 1: My first Calculator
def calculator():
    
    # defining variabthes that will be used by the user
    
    a = float(input("Enter the first nombre : "))
    b = float(input("Enter the second nombre : "))
    operator = input("Enter the operator (+, -, *, /) : ")
    
    
    # conditions

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a / b
    else:
        result = "invalid operator"

 # Displaying the results
    print("result :", result)

 # Calling the fonction
calculator()
