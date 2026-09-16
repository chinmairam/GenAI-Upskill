#Task 1
def apply_discount(price, discount_percent=None):
  if discount_percent is None:
    discount_percent = 5
  if discount_percent > 60:
    print("Discount can't exceed 60%")
    return
  discount_amount = price * (discount_percent / 100)
  final_price = price - discount_amount
  return final_price
print(apply_discount(1000, 10))
print(apply_discount(500))

# Task 2
def factorial(n):
  if n in [0,1]:
    return 1
  if n < 0:
    print("Factorial is not defined for negative numbers")
    return
  else:
    return n*factorial(n-1)
print(factorial(5))
print(factorial(0))
print(factorial(-3))

# Task 3
gst = lambda price: price+(0.18*price)
print(gst(100))
final_price = lambda price, discount_percent: gst(price) - (price * (discount_percent / 100))
print(final_price(100, 10))

# Task 4
prices = [100, 250, 400, 1200, 50]
prices_with_gst = list(map(gst, prices))
print(prices_with_gst)

# Task 5
prices = [100, 250, 400, 1200, 50, 2000, 850]
prices_gt_500 = list(filter(lambda price: price > 500, prices))
prices_leq_500 = list(filter(lambda price: price <= 500, prices))
print(prices_gt_500)
print(prices_leq_500)

# Task 6
def process_prices(prices):
  discounted_prices = list(map(lambda price: price-(price*0.1), prices))
  filtered_prices = list(filter(lambda price: price > 300, discounted_prices))
  return discounted_prices, filtered_prices
print(process_prices([100, 500, 900, 50, 750]))

# Task 7
def add_prices(prices_list, price):
  prices_list.append(price)
def get_average_price(prices_list):
  return sum(prices_list)/len(prices_list)
def get_max_price(prices_list):
  return max(prices_list)

prices_list = []
while True:
    print("\n--- Menu ---")
    print("1: Add Price")
    print("2: Get Average")
    print("3: Get Max Price")
    print("q: Quit")

    choice = input("Enter an action: ").strip()

    if choice.lower() == 'q':
        print("Exiting program")
        break
    elif choice == '1':
        price = int(input("Enter Price: "))
        add_prices(prices_list, price)
        print(f"Added price of {price}.")
    elif choice == '2':
        if not prices_list:
            print("No prices added yet.")
            continue
        average = get_average_price(prices_list)
        print(f"Avg. of all prices is {average}")
    elif choice == '3':
        if not prices_list:
            print("No prices added yet.")
            continue
        max_price = get_max_price(prices_list)
        print(f"Max Price is {max_price}")
    else:
        print("Invalid input! Please select a valid option from the menu.")
        continue