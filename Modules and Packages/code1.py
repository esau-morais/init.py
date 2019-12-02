# Before
def  fact(numb):
    f = 1
    for c in range(1, numb + 1):
        f *= c
    return f


def double(numb):
    return numb * 2


def triple(numb):
    return numb * 3


n = int(input("Type a whole number: "))
f1 = fact(n)
print(f"The factorial of {n} is {f1}")

print(f"The double of {n} is {double(n)}")

print(f"The triple of {n} is {triple(n)}")

print("-" * 25)

# After
from module1 import * # * means all that exist on module1
n = int(input("Type a whole number: "))
f1 = fact(n)
print(f"The factorial of {n} is {f1}")

print(f"The double of {n} is {double(n)}")

print(f"The triple of {n} is {triple(n)}")

print("-" * 25)

# Packages
# import numbers
from Packages import numbers
n = int(input("Type a whole number: "))
f1 = fact(n)
print(f"The factorial of {n} is {f1}")

print(f"The double of {n} is {double(n)}")

print(f"The triple of {n} is {triple(n)}")
