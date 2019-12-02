def print_int(numb):
    ready = False
    value = 0
    while True:
        n = str(input(numb))
        if n.isnumeric():
            value = int(n)
            ready = True
        else:
            print("\033[31mERROR! Type only whole numbers\033[m")
        if ready:
            break
    return value


n = print_int("Type a number: ")
print(f"You have entered the number {n}")
