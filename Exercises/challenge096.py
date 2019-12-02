# Creting a title
print("-=" * 19)
print(" == CALCULATING THE AREA OF A LAND == ")
print("-=" * 19)

# Create the variables to the width and length
width = float(input("Type the width of the land: "))
length = float(input("Type the length of the land: "))

# Create a program that create a function that calculate the area of land
def area(w,l):
    a = w * l
    print(f"The area of the land {width} x {length} is {a} m²")


area(width,length)
