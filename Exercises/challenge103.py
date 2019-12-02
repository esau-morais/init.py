def data(n = "unknown", g = 0):
    print(f"The player {n} done {g} goals")


player = str(input("Type the name of player: "))
goals = str(input("Enter the number of goals scored: "))
if goals.isnumeric():
    goals = int(goals)
else:
    goals = "nothing goals informated"
if player.strip() == "":
    data(g = goals)
else:
    data(player, goals)
