# Task 1
products = ['Phone', 'AC', 'Cooler', 'Washing Machine', 'Toaster', 'AirFryer']
sample_product = ('Phone', 55000, 'Iphone')
print(f'2nd product is {products[1]}, Last product is {products[-1]}')
# lst.append(value)
products.append('Refrigerator')
products.append('Oven')
print('Products after append:', products)
sample_product = list(sample_product)
sample_product[1] = 75000
sample_product = tuple(sample_product)
print('Sample Product after changing price:', sample_product)

# Task 2
categories = [
    'Electronics', 
    'Home Appliances', 
    'Home Appliances', 
    'Home Appliances', 
    'Kitchen Appliances', 
    'Kitchen Appliances',
    'Home Appliances',
    'Kitchen Appliances'
]
# Create a set of categories
categories_set = set(categories)
print("Unique categories set:", categories_set)
categories_set.add('Electronics')
print('Checking Duplicates Ignore:', categories_set)
is_Electronics_in_set = 'Electronics' in categories_set
print('Electronics in set:', is_Electronics_in_set)
# Total Unique Categories
print('Total No.of Unique categories:', len(categories_set))

# Task 3
price_dict = {
    'Phone': 75000,
    'AC': 35000,
    'Cooler': 10000,
    'Washing Machine': 30000,
    'Toaster': 4000,
    'AirFryer': 6000,
    'Refrigerator': 60000,
    'Oven': 10000
}
print("Price Dictionary:", price_dict)
price_dict['Monitor'] = 10000
price_dict['Oven'] = 12000
try:
    del price_dict['Toaster']
except KeyError:
    print('Product does not exist in price dictionary')
print("Updated Price Dictionary:", price_dict)
# Average Price of all products
prices_list = [price for product, price in price_dict.items()]
print(f'Average prices of all products is {sum(prices_list)//len(prices_list)}')
# Get max and min values
max_price_product = max(price_dict, key=price_dict.get)
min_price_product = min(price_dict, key=price_dict.get)
print(f"Product with maximum price: {max_price_product} (${price_dict[max_price_product]})")
print(f"Product with minimum price: {min_price_product} (${price_dict[min_price_product]})")

# Task 4
catalog = []
for i, product_name in enumerate(products):
    # Get the category using the same index as product_name
    category = categories[i]
    # Get the price from price_dict
    price = price_dict.get(product_name)
    # Only add to catalog if a price was found
    if price is not None:
        catalog.append((product_name, price, category))
    else:
        print(f"Product {product_name} does not exist/does not have price in price_dict')")
print("Product Catalog:")
for item in catalog:
    print(item)

category_products = {}
for product_name, price, category in catalog:
    if category not in category_products:
        category_products[category] = []
    category_products[category].append(product_name)
print("Category to Products Dictionary:")
for category, products_in_category in category_products.items():
    print(f"{category}: {products_in_category}")
# Find the category with the max products
if category_products:
    max_category = max(category_products, key=lambda cat: len(category_products[cat]))
    products = category_products[max_category]
    print(f"\nCategory with most products: {max_category} ({len(products)} items)")
