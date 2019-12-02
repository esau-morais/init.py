# Error Handling
try:
    x = int(input("Numerator: "))
    y = int(input("Denominator: "))
    answer = x / y
except Exception as error:
    print(f"Error found: {error.__class__}")
else:
    print(f"The result of calculation {x} / {y} is: {answer}")
finally:
    print("Thank you for using our program. Check back often!")

# Error Handling 2
try:
    a = int(input("Numerator: "))
    b = int(input("Denominator: "))
    answer2 = a / b
except (TypeError, ValueError):
    print("Entered values error ):")
except KeyboardInterrupt:
    print("The user didn't want to continue the program ):")
except ZeroDivisionError:
    print("Unable to divide a number by zero ):")
except Exception as error2:
    print(f"Error found: {error2.__cause__}")
else:
    print(f"The result of calculation {a} / {a} is: {answer2}")

# Error Handling 3
