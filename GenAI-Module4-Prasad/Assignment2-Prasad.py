# Task 1
try:
    order_amount = int(input("Enter Order Amount:"))
    if order_amount >= 2000:
      discount = 15
    elif order_amount < 2000 and order_amount >= 1500:
      discount = 10
    elif order_amount < 1500 and order_amount >= 1000:
      discount = 7
    else:
      discount = 0
    # Discount Amount
    discount_amount = order_amount * discount / 100
    subtotal = order_amount - discount_amount
    # Tax
    tax = subtotal * 0.05
    final_amount = subtotal + tax
    print(f'Order Amount is {order_amount}')
    print(f'Discount is {discount} %')
    print(f'Sub Total: {subtotal}')
    print(f'Tax: {tax}')
    print(f'Total Amount is {final_amount}')
except ValueError:
    print(f"Error: '{order_amount}' is not a valid integer.")

# Task 2
orders = [1200, 2500, 800, 1750, 3000]
total_revenue = 0
orders_with_discount = 0

print("Order Amount | Discount % | Final Amount")
for order_amount in orders:
  if order_amount >= 2000:
      discount = 15
  elif order_amount < 2000 and order_amount >= 1500:
    discount = 10
  elif order_amount < 1500 and order_amount >= 1000:
    discount = 7
  else:
    discount = 0

  discount_amount = order_amount * discount / 100
  final_amount = order_amount - discount_amount

  print(f"{order_amount} | {discount} % | {final_amount}")
  total_revenue += final_amount
  if discount > 0:
    orders_with_discount += 1

print(f"Total Revenue: {total_revenue}")
print(f"Orders with Discount: {orders_with_discount}")

# Task 3
orderList = []

while True:
    print("\n--- Menu ---")
    print("1: Add Order")
    print("2: View Orders")
    print("q: Quit")
    
    choice = input("Enter an action: ").strip()

    if choice.lower() == 'q':
        print("Exiting program")
        break
    elif choice == '1':
        order_amount = int(input("Enter Order Amount: "))
        orderList.append(order_amount)
        print(f"Added order of {order_amount}.")
    elif choice == '2':
        if not orderList:
            print("No orders added yet.")
            continue

        for order_amount in orderList:
            if order_amount >= 2000:
                discount = 15
            elif order_amount >= 1500:
                discount = 10
            elif order_amount >= 1000:
                discount = 7
            else:
                discount = 0

            discount_amount = order_amount * (discount / 100)
            subtotal = order_amount - discount_amount
            tax = subtotal * 0.05
            final_amount = subtotal + tax

            print(f"{order_amount} | {discount}% | Final: {final_amount:.2f}")
    else:
        print("Invalid input! Please select a valid option from the menu.")
        continue
    
# Task 4
daily = [250, 150, 0, 400, 50, -1, 300]
total_sales = 0
for sale in daily:
  if sale == -1:
    print("Corrupted Data")
    break
  elif sale == 0:
    print("No Sales")
    continue
  elif sale > 0:
    total_sales += sale
    print(f"Total Sales: {total_sales}")