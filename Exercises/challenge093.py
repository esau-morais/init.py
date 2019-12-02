def line():
    print("-=" * 17)


line()
print(" == SOCCER PLAYER REGISTRATION == ")
line()

data = dict()
departures = list()

data["Name"] = str(input("Type the player's name: "))

total = int(input("Enter the number of matches {} has played: ".format(data["Name"])))

line()

for d in range(0, total):
    departures.append(int(input(f"Enter the number of goals in the match {d + 1}: ")))

line()

data["Goals"] = departures[:]

data["Sum"] = sum(departures)

print(data)

line()

for p, v in data.items():
    print(f"{p} receab {v}")

line()

print(f'{data["Name"]} has played {total} departures')

for i, v in enumerate(data["Goals"]):
    print(f" → Match {i}: {v} goals")
print(f'Total: {data["Sum"]} goals')
