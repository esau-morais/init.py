def line():
    print("-=" * 16)


line()
print(" == APPROVED OR DESAPPROVED? == ")
line()

data = {"Name": str(input("Student's name: ")), "Mean": float(input("Student's mean: "))}

line()
name = data["Name"]
print(f"Name receab {name}")

line()
mean = data["Mean"]
print(f"Mean receab {mean}")

line()

if data["Mean"] >= 7:
    print("Student was Aproved! ")
elif 5 < data["Mean"] < 7:
    print("Student has Recovered ")
elif data["Mean"] < 5:
    print("Student is Disapproved")
