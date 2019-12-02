from random import randint

from time import sleep


def line():
    print("-" * 26)


line()
print("   == SORTING VALUES == ")
line()


def lottery(nums):
    print("Drawn values: ", end="")
    for count in range(0, 5):
        n = randint(1, 10)
        nums.append(n)
        print(f"{n}", end=" ", flush=True)
        sleep(0.5)
    print("END")


def sume(nums):
    s = 0
    for values in nums:
        if values % 2 == 0:
            s += values
    print()
    print(f"The sum of the values {nums} is: {s}")


numbers = list()

lottery(numbers)

sume(numbers)
