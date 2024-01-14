'''
# travel log
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

travel_log["France"] = {"cities_visited": ["Paris", "Lille", "Dijon"]}

print(travel_log)


# format name function
# better to use method title()
def format_name(name):
  words = name.split(' ')

  for word in range(len(words)):
    words[word] = words[word].capitalize()

  return ' '.join(words)


print(format_name('aLVAurO GuiMaraeS CALDAS'))
'''

# calculator
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
  }

num1 = int(input('First Number?\n'))
num2 = int(input('Second Number?\n'))

operation_symbol = operations[input('Which operation do you want?')]

print(f"{operation_symbol(num1, num2)}")