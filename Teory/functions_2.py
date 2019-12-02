# Interactive Help
help()

# Alternative Interactive Help 
print(input.__doc__)

# Docstrings
def count(s,e,i):
    """
    It's a counter that show in the touch:
    s is the start of count;
    e is the end of count;
    i is the time's interval.
    no exist return
    by @e.mmmorais
    """
    c = s
    while c <= e:
        print(f"{c}", end=" ")
        c += i
    print("END ")


help(count)

# Optional Parameters
def nsum(x = 0,y = 0,z = 0):
    s = x + y + z
    print(f"The sum of the values is: {s}")


nsum(1,2,3)

nsum(1,2)

nsum(2,3)

nsum(1,3)

nsum()

print("-=" * 18)

# Scope of variables: global scope
def test():
    x = int(input("Type a value: "))
    print(f"In the function, the value receab {x}")


v = int(input("Type a value: "))
print(f"In the program, the value receab {v}")

# Scope of variables: local scope
test()

print("-=" * 18)

# Scope of variables: global and local scope
def test2():
    a = int(input("Type a value: "))
    print(f"In the function, a receab {a}")


a = int(input("Type a value: "))
test2()
print(f"In the program, a receab {a}")

print("-=" * 18)

# Scope of variables: treating two variables as global
def test3():
    global y
    y = 8
    print(f"In the function, y receab {y}")


y = 5
test3()
print(f"In the program, y receab {y}")

print("-=" * 18)

# Return values
def nsum2(x = 0,y = 0,z = 0):
    s = x + y + z
    return s


s1 = nsum2(1,2,3)

s2 = nsum2(1,2)

s3 = nsum2(2,3)

s4 = nsum2(1,3)

s5 = nsum2()

print(f"The obtained results were: {s1}, {s2}, {s3}, {s4} and {s5}")

print("-=" * 18)

# Practice: factorial of a number
def fact(numb = 0):
    f = 1
    for c in range(numb, 0, -1):
        f *= c
    return f


n = int(input("Type a whole number: "))
factorial = fact(n)
print(f"The factorial of {n} is {factorial}")

print("-=" * 18)

f1 = fact(5)

f2 = fact(3)

f3 = fact()

print(f"The obtained results were: {f1}, {f2} and {f3}")

# Practice 2: even or odd
def eo(number = 0):
    if number % 2 == 0:
        return True
    else:
        return False


number = int(input("Type a whole number: "))
if eo(number) == True:
    print("It's even")
else:
    print("It's odd")
