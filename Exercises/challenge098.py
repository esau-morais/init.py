print("-=" * 16)
print("      == COUNT ON PYTHON == ")
print("-=" * 16)

from time import sleep

def counter(s, e, i):
    if i < 0:
        i *= -1 
    if i == 0:
        i = 1
    print(f"Count from {s} to {e}, from {i} in {i}")
    
    if s < e:
        c = s
        while c <= e:
            print(f"{c}", end=" ", flush=True)
            sleep(1.0)                
            c += s
        print("FIM")
    else:
        c = s
        while c >= e:
            print(f"{c}", end=" ", flush=True)
            sleep(1.0)
            c -= i
        print("FIM")

counter(1, 10, 1)
print("-=" * 16)

counter(10, 0, 2)
print("-=" * 16)

print("NOW, IT'S YOUR TURN! ")

start = int(input("Type the start number: "))

end = int(input("Type the final number: "))

interval = int(input("Type the interval between the numbers: "))

print("-=" * 16)

counter(start, end, interval)

print("-=" * 16)
