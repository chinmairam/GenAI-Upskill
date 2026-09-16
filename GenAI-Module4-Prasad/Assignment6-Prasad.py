# Task 1
try:
  numerator_ip = input('Enter Numerator: ')
  denominator_ip = input('Enter Denominator: ')

  numerator = float(numerator_ip)
  denominator = float(denominator_ip)

  result = numerator / denominator

except ValueError:
  print("Input is not a number.")
except ZeroDivisionError:
  print("Cannot divide by Zero.")
else:
  print(f"Result: {result}")
finally:
  print("Operation Complete")

# Task 2
prices = [120, 350, 'abc', 500, -200, 800]
total = 0

for price in prices:
  try:
    if not isinstance(price, (int, float)):
      raise TypeError(f"'{price}' is not a number")
    if price < 0:
      raise ValueError(f"Negative Price not allowed")
    total += price
    print(f"Running Total: {total}")

  except TypeError as e:
    print(f"Error: {e}")
  except ValueError as e:
    print(f"Error: {e}")

# Task 3
def check_age(age):
  try:
    if age < 1 or age > 120:
      raise ValueError("Age must be between 1 and 120")
  except ValueError as e:
    print(f"Error: {e}")
  else:
    print(f"Age: {age}")
age = int(input("Enter Age: "))
check_age(age)

# Task 4
def file_reader():
  file_name = input("Enter File Name: ")
  try:
    file = open(file_name, 'r')
  except FileNotFoundError:
    print(f"File '{file_name}' not found.")
  except PermissionError:
    print(f"Permission denied to open file '{file_name}'.")
  else:
    for i in range(3):
      line = file.readline()
      print(line.strip())
    file.close()
  finally:
    print("File operation attempted.")

file_reader()

# Task 5
def safe_shopping_cart():
    cart = []
    
    print("Welcome to Safe Shopping Cart!")
    print("Enter item prices. Enter 'q' to quit.\n")
    while True:
        user_input = input("Enter item price (or 'q' to quit): ").strip()
        if user_input.lower() == 'q':
            break
            
        try:
            price = float(user_input)
            
            if price < 0:
                raise ValueError("Price cannot be negative.")
            cart.append(price)
            
        except ValueError as e:
            if "negative" in str(e):
                print("Error: Invalid price. Price cannot be a negative number.")
            else:
                print("Error: Invalid input. Please enter a valid number or 'q'.")

    total_items = len(cart)
    total_bill = sum(cart)
    print(f"Total items: {total_items}")
    print(f"Total bill: {total_bill:.2f}")


safe_shopping_cart()