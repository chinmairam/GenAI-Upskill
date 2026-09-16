# Task 1
class Product:
  def __init__(self, name, price, category):
    self.name = name
    self.price = price
    self.category = category
  
  def get_info(self):
    print(f"Product Name: {self.name}")
    print(f"Price: {self.price}")
    print(f"Category: {self.category}")
  
  def apply_discount(self, discount_percent):
    return self.price - (self.price * (discount_percent / 100))

p1 = Product('Mouse', 500, 'Electronics')
p1.get_info()

p2 = Product('Keyboard', 800, 'Electronics')
p2.get_info()
print("Discounted Price: ", p2.apply_discount(10))

# Task 2
class Product:
  def __init__(self, name, price, category):
    self.name = name
    self.__price = price
    self.category = category
  
  def get_info(self):
    print(f"Product Name: {self.name}")
    print(f"Price: {self.price}")
    print(f"Category: {self.category}")
  
  def apply_discount(self, discount_percent):
    return self.price - (self.price * (discount_percent / 100))

  def get_price(self):
    return self.__price

  def set_price(self, new_price):
    if new_price < 0:
      print("Price cannot be negative")
    else:
      self.__price = new_price

p1 = Product('Mouse', 500, 'Electronics')
print("Product 1 Price is: ", p1.get_price())
p1.set_price(1000)
print("Updated Product 1 Price is: ", p1.get_price())

# Task 3
class ElectronicProduct(Product):
  def __init__(self, name, price, category, warranty_years):
    super().__init__(name, price, category)
    self.warranty_years = warranty_years

  def get_info(self):
    print(f"Product Name: {self.name}")
    print(f"Price: {self.get_price()}")
    print(f"Category: {self.category}")
    print(f"Warranty: {self.warranty_years} years")

p1 = ElectronicProduct('Mouse', 500, 'Electronics', 2)
p1.get_info()

# Task 4
class Laptop(Product):
  def __init__(self, name, price, category, ram, storage):
    super().__init__(name, price, category)
    self.ram = ram
    self.storage = storage

  def get_info(self):
    print(f"Product Name: {self.name}")
    print(f"Price: {self.get_price()}")
    print(f"Category: {self.category}")
    print(f"RAM: {self.ram}")
    print(f"Storage: {self.storage}")

class Mobile(Product):
  def __init__(self, name, price, category, camera_quality):
    super().__init__(name, price, category)
    self.camera_quality = camera_quality

  def get_info(self):
    print(f"Product Name: {self.name}")
    print(f"Price: {self.get_price()}")
    print(f"Category: {self.category}")
    print(f"Camera Quality: {self.camera_quality}")

lap = Laptop('Mac', '1500000', 'Pro', '32GB', '512GB')
mob = Mobile('Samsung', '100000', 'Fold 4', '200MP')

for product_item in [lap, mob]:
  product_item.get_info()
  print("-"*20)

# Task 5
from abc import ABC, abstractmethod

class Payment(ABC):
  @abstractmethod
  def process_payment(self, amount):
    pass 

class CreditCardPayment(Payment):
  def process_payment(self, amount):
     print(f"Processing Credit Card Payment of ${amount}")

class UPIPayment(Payment):
  def process_payment(self, amount):
    print(f"Processing UPI Payment of ${amount}")

cp = CreditCardPayment()
cp.process_payment(10000)
up = UPIPayment()
up.process_payment(2000)

# Task 6
class Product:
  def __init__(self, name, price, category):
    self.name = name
    self.__price = float(price)
    self.category = category

  def get_info(self):
    print(f"Product Name: {self.name}")
    print(f"Price: {self.get_price()}")
    print(f"Category: {self.category}")

  def apply_discount(self, discount_percent):
    return self.get_price() - (self.get_price() * (discount_percent / 100))

  def get_price(self):
    return self.__price

  def set_price(self, new_price):
    if new_price < 0:
      print("Price cannot be negative")
    else:
      self.__price = float(new_price)

  def __str__(self):
    return f"Product Name: {self.name}\nPrice: {self.get_price()}\nCategory: {self.category}"

  def __add__(self, other):
    return self.get_price() + other.get_price()

p1 = Product('Mouse', 500, 'Electronics')
print(p1)
print("Discounted Price: ", p1.apply_discount(10))

p1 = Product('Mouse', 500, 'Electronics')
print("Product 1 Price is: ", p1.get_price())
p1.set_price(1000)
print("Updated Product 1 Price is: ", p1.get_price())

p2 = Product('Keyboard', 800, 'Electronics')
print(p2)
total_price = p1 + p2
print('Total Price is: ', total_price)

# Task 7
class Inventory:
  def __init__(self):
    self.products = []

  def add_product(self, product):
    self.products.append(product)

  def remove_product(self, name):
    product_found = False
    for product in self.products:
      if product.name == name:
        self.products.remove(product)
        product_found = True
        break
    if not product_found:
      print(f"{name} not found in inventory.")

  def find_product_by_name(self, name):
    for product in self.products:
      if product.name == name:
        return product
    return None

  def get_total_value(self):
    total_value = 0
    for product in self.products:
      total_value += int(product.get_price())
    return total_value

  def show_all_products(self):
    if not self.products:
      print("Inventory is empty.")
      return
    for product in self.products:
      print(f"Product Name: {product.name}")
      print(f"Price: {product.get_price()}")
      print(f"Category: {product.category}")
      print("-"*20)

  def sum_prices_of_two_products(self, product_name1, product_name2):
    product1 = self.find_product_by_name(product_name1)
    product2 = self.find_product_by_name(product_name2)

    if product1 and product2:
      combined_price = product1 + product2
      print(f"Combined price of {product_name1} and {product_name2}: {combined_price}")
      return combined_price
    else:
      missing_products = []
      if not product1: missing_products.append(product_name1)
      if not product2: missing_products.append(product_name2)
      print(f"Could not find product(s): {', '.join(missing_products)} in inventory.")
      return None

class Store:
  def __init__(self, store_name):
    self.store_name = store_name
    self.inventory = Inventory()

  def add_new_product(self, name, price, category):
    new_product = Product(name, price, category)
    self.inventory.add_product(new_product)
    print(f"Added {name} to {self.store_name}'s inventory.")

  def show_summary(self):
    print(f"Store Name: {self.store_name}")
    print("-"*20)
    self.inventory.show_all_products()

st = Store('Dmart')
st.add_new_product('PS5', '55000', 'Gaming')
st.add_new_product('Mouse', '500', 'Electronics')
st.add_new_product('Keyboard', '800', 'Electronics')
print()
st.show_summary()
print()
p1 = st.inventory.find_product_by_name('PS5')
p2 = st.inventory.find_product_by_name('Keyboard')
st.inventory.sum_prices_of_two_products(p1.name, p2.name)
print()
st.inventory.remove_product('Mouse')
st.show_summary()
print()
print("Total Value of Inventory: ", st.inventory.get_total_value())