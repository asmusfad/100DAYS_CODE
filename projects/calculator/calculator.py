from art import logo


#Calculator
def add(num1, num2 ):
  """ takes to numbers and returns the sum """
  return num1 + num2

def subtract(num1, num2 ):
  """ takes to numbers and returns the difference """
  return num1 - num2

def multiply(num1, num2 ):
  """ takes to numbers and returns the product """
  return num1 * num2
def divide(num1, num2 ):
  """ takes to numbers and returns the quotient """
  return num1 / num2
def power(num1, num2):
  """ takes to numbers and returns the power """
  return num1 ** num2

operations = {'+': add, '-': subtract, '*': multiply, '/': divide, 'power': power}




def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for operation in operations:
    print(operation)
  
  end_of_calculation = False
  while not end_of_calculation:
    operation = input("Pick an operation from the line above: ")
    if operation not in operations:
      print("Invalid operation. Please try again.")
      continue
    num2 = float(input("What's the next number?: "))
    function = operations[operation]
    result = function(num1, num2)
    print(f"{num1} {operation} {num2} = {result}")
    
    if input(f"Type 'y' if  you like to continue calculating with the {result} or type 'n' to start a new calculation: ") == 'y':
      num1 = result
      
    else: 
      end_of_calculation = True
      calculator()
      
    

calculator()