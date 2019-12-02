from module_109 import *

price = float(input("Type the product's price: R$"))
print(f"Increasing 10% to {money(price)}, you get: {increase(price, True)}")

print(f"Decreasing 13% to {money(price)}, you get {decrease(price, False)}")

print(f"The double of {money(price)}, you get: {double(price, False)}")

print(f"The half of {money(price)}, you get: {half(price, True)}")
