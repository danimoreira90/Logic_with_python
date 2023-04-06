def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

ops = {
      "+":add,
      "-":subtract,
      "*":multiply,
      "/":divide
}
def calculator():

  num1 = float(input("What's the first number?: "))
  for symbol in ops:
    print(symbol)

    while True:
      operations = input("Pick an operation: ")
      num2 = float(input("What's the next number?: "))
      calculation = ops[operations]
      answer = calculation(num1, num2)
      print(f"{num1} {operations} {num2} = {answer}")
      
      flag = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: [y/n]").lower()[0]

      if flag == 'n':
        break
      elif flag == 'y':
        num1 = answer
    calculator()
calculator()
      
      
      
        
    
  
  

# def operations(a, b, c):
#   if b == '+':
#     add(a, c)
#   elif b == '-':
#     return subtract(a, c)
#   elif b == '*':
#     return multiply(a, c)
#   elif b == '/':
#     return divide(a, c)
#answer = operations(num1, symbol, num2)
# print(f"{num1} {symbol} {num2} = {first_answer}")
# print('_' * 50)
# symbol = input("Pick another operation: ")
# print('_' * 50)
# num3 = int(input("What's the next number?: "))
# operations = ops[symbol]
# second_answer = operations(operations(num1, num2), num3)
# print('_' * 50)

# print(f"{first_answer} {symbol} {num3} = {second_answer}")
