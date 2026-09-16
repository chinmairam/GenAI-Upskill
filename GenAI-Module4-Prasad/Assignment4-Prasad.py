# Task 1
sales = [1200, 450, 980, 1500, 3000]
with open('sales_data.txt', 'w') as file:
  # file.write(','.join(str(sale) for sale in sales))
  file.writelines(f"{str(sale)}\n" for sale in sales)
with open('sales_data.txt', 'r') as file:
  content = file.read()
  print(content)

# Task 2
with open('sales_data.txt', 'r') as file:
  content = file.read()
  print(content)
  file.seek(0)
  first_line = file.readline()
  print(first_line)
  sales = [int(sale) for sale in content.split()]
  print(sales)

# Task 3
with open('sales_data.txt', 'a') as file:
  new_sales = [5000, 2500, 1700]
  file.writelines(f"{str(sale)}\n" for sale in new_sales)

with open('sales_data.txt', 'r') as file:
  content = file.read()
  print(content)
  file.seek(0)
  print('Total Lines: ', len(file.readlines()))

# Task 4
with open('sales_data.txt', 'r') as file:
  content = file.read()
  sales = [int(sale) for sale in content.split()]
  print(sales)
  print(f"Total Sales: {sum(sales)}")
  print(f"Average Sales: {sum(sales)/len(sales)}")
  print(f"Highest Sale: {max(sales)}")
  print(f"Lowest Sale: {min(sales)}")

# Task 5
product_data = []
for i in range(3):
    product_name = input(f"Enter product name {i+1}: ")
    product_price = input(f"Enter price for {product_name}: ")
    product_data.append(f"{product_name} | {product_price}")
with open('products.txt', 'w') as file:
    for line in product_data:
        file.write(line + '\n')
with open('products.txt', 'r') as file:
    content = file.read()
    print(content)

# Task 6
file_input = input('Enter file name to open: ')
try:
    with open(file_input, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the filename.")

# Task 7
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount_percent = float(input("Enter discount percentage (e.g., 10 for 10%): "))
multiplier = 1 - (discount_percent / 100)

filename = "discount_report.txt"
total_discounted_price = 0

with open(filename, "w") as file:
    file.write("Product | Original Price | Discounted Price\n")
    file.write("-" * 45 + "\n")
    
    for item, price in prices.items():
        discounted_price = price * multiplier
        total_discounted_price += discounted_price
        file.write(f"{item:<10} | {price:>14.2f} | {discounted_price:>16.2f}\n")
    
    total_items = len(prices)
    avg_discounted_price = total_discounted_price / total_items
    
    file.write("-" * 45 + "\n")
    file.write(f"Total Items: {total_items}\n")
    file.write(f"Average Discounted Price: {avg_discounted_price:.2f}\n")

with open(filename, "r") as file:
    content = file.read()
    print("\n" + content)
