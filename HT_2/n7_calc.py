# 7. calculator 
  
# add two numbers  
def add(num1, num2): 
    return num1 + num2 
  
# subtract two numbers  
def subtract(num1, num2): 
    return num1 - num2 
  
# multiply two numbers 
def multiply(num1, num2): 
    return num1 * num2 
  
# divide two numbers 
def divide(num1, num2): 
    return num1 / num2 
  
print("Please select operation -\n", 
        "+. Add\n", 
        "-. Subtract\n", 
        "*. Multiply\n", 
        "/. Divide\n") 

# input data and operation from user  
oper = (input("Select operations: +, -, *, / ")) 
  
numb_1 = int(input("Enter first number: ")) 
numb_2 = int(input("Enter second number: ")) 

if oper == "+": 
    print(numb_1, "+", numb_2, "=", add(numb_1, numb_2)) 
  
elif oper == "-": 
    print(numb_1, "-", numb_2, "=", subtract(numb_1, numb_2)) 
  
elif oper == "*": 
    print(numb_1, "*", numb_2, "=", multiply(numb_1, numb_2)) 
  
elif oper == "/": 
    print(numb_1, "/", numb_2, "=", divide(numb_1, numb_2)) 
else: 
    print("invalid input") 