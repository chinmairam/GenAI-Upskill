import math_utils
from math_utils import square
import string_utils
import shop_package.discount as disc
from shop_package.billing import calculate_total

print(math_utils.add(1, 2))
print(square(5))
print(string_utils.capitalize_words('Apple'))
print(string_utils.reverse_string('Tutedude'))
print(string_utils.word_count('Pawan Kalyan'))

print(disc.apply_discount(1000, 10))
print(disc.flat_discount(100))
print(calculate_total([100, 200, 300]))
