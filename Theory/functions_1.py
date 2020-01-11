# Create a function to create a line
def line():
    print("-=" * 18)

# Create a function to create a message
def msg(message):
    print(message)

# Creating a title
line()
msg("    == SUM OF DIFFERENT VALUES == ")

# Create a function to sum of values
def sum(x, y):
    print(f"x = {x} and y = {y}")
    s = x + y
    print(f'The sum of the values is: {s}')

# Use the function
line()
sum(x=-4, y=5)

sum(y=-4, x=-4)

sum(y=-2, x=-15)
line()

# Creating a title
msg("        == MULTIPLE VALUES == ")
line()

# Create a function to sum of multiple values
def sum(*nums):
    print(f"The endered values were: ", end="")
    for n in nums:
        print(n, end=" ")

sum(2,4,6,8,10)
print()
line()

# Creating a title
msg("   == DOUBLING VALUES OF A LIST == ")
line()

# Create a function to double values of a list
def double(values):
        pos = 0
        while pos < len(values):
                values[pos] *= 2
                pos += 1

values = [2, 4, 6, 8, 10]
double(values)
print(values)
