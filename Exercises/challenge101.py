# Create a function for the line
def line():
    print("-" * 25)


# Creating the title
line()
print("      == VOTING ==")
line()

# Create a function for the voting
def voting():
    from datetime import date
    year = int(input("Type the year of birth: "))
    a = date.today().year - year
    if a < 16:
        return f"You are {a} years → You can't vote "
    elif 16 > a > 18 or a > 65:
        return f"You are {a} years → Voting is optional "
    else:
        return f"You are {a} years → Vote is required "

print(voting())
