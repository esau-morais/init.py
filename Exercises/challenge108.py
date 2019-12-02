from module_108 import *

price = float(input("Type the product's price: R$"))
print(f"Increasing 10% to {money(price)}, you get: {money(increase(price))}")

print(f"Decreasing 13% to {money(price)}, you get {money(decrease(price))}")

print(f"The double of {money(price)}, you get: {money(double(price))}")

print(f"The half of {money(price)}, you get: {money(half(price))}")
