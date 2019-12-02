from time import sleep

def line():
    print("-" * 32)


line()
print("       == HIGHEST VALUE == ")
line()

def highest(*nums):
    c = h = 0
    print("Entered values: ", end="")
    for v in nums:
        print(f"{v}", end=" ", flush=True)
        sleep(0.5)
        if c == 0:
            h = v
        else:
            if v > h:
                h = v
        c += 1
    print()
    print(f"In all, we have {c} values")
    print(f"The highest value entered was: {h}")
    line()

highest(1, 2, 3, 4 , 5)

highest(2, 4, 6, 8, 10)

highest(0)
