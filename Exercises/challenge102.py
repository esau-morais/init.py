def fact(numb = 0, show = False):
    """
    Calculate a factorial of a number:
    n is the number 
    show (optional) is who shows the calculation
    return the value of factorial of the number "n"
    """
    f = 1
    for c in range(numb, 0, -1):
        if show == True:
            print(f"{c}", end=" ")
            if c > 1:
                print(f"x", end=" ")
            else:
                print("=", end=" ")
        f *= c
    return f

n = int(input("Type whole number: "))
print(fact(n, show=True))

help(fact)
