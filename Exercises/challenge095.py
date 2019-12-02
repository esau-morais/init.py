def line():
    print("-=" * 17)


line()
print(" == SOCCER PLAYER REGISTRATION == ")
line()

data = dict()
departures = list()
team = list()

while True:
    data.clear()

    data["Name"] = str(input("Type the player's name: "))

    total = int(input("Enter the number of matches {} has played: ".format(data["Name"])))

    departures.clear()

    line()

    for d in range(0, total):
        departures.append(int(input(f"Enter the number of goals in the match {d + 1}: ")))

    data["Goals"] = departures[:]

    data["Sum"] = sum(departures)

    team.append(data.copy())

    while True:
        answer = str(input("Do you want to continue? [Y/N] ")).upper()[0]
        if answer in "YN":
            break
        print("ERROR! Type only Y or N ")
    if answer == "N":
        break
    line()

line()
for e in data.keys():
    print(f"{e:<13}",end=" ")
print()

for p, v in enumerate(team):
    print(f'{p:>2}: ', end=" ")
    for d in v.values():
        print(f'{str(d):<10}', end=" ")
    print()

while True:
    search = int(input("Do you want to display the data of which player? "))
    if search == 999:
        break
    if search >= len(team):
        print(f"ERROR! There is no player with the number {search}")
    else:
        print(f'Player Survey {team[search]["Name"]}')
        for p, g in enumerate(team[search]["Goals"]):
            print(f"On the match {p + 1}, the player was {g} goals")
