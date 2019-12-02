def line():
    print("-=" * 14)


line()
print(" == PEOPLES REGISTRATION == ")
line()

people = dict()
peoples = list()
sum = mean = 0

while True:
    people.clear()
    people["Name"] = str(input("Type the people's name: "))

    while True:
        people['Sex'] = str(input("Type the people's sex [M/F]: ")).upper()[0]
        if people['Sex'] in "MF":
            break
        print("ERROR! Type only M or F ")
    people['Age'] = int(input("Type people's age: "))
    sum += people['Age']
    peoples.append(people.copy())

    while True:
        answer = str(input("Do you want continue? [Y/N] ")).upper()[0]
        if answer in "YN":
            break
        print("ERROR! Type only Y or N ")
    if answer == "N":
        break

line()
print(f"Total of registered people: {len(peoples)}")
line()

mean = sum / len(peoples)

print(f"The people's age mean is: {mean:5.1f} ")
line()

print("The registred women were:\n", end=" ")
for p in peoples:
    if p['Sex'] in "Ff":
        print(f'{p["Name"]}', end="\n")
line()

print("List of people who are above average: ")
for p in peoples:
    if p["Age"] >= mean:
        for k, v in p.items():
            print(f'{k} → {v}')
line()
