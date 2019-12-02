from datetime import datetime

def line():
    print("-=" * 12)


line()
print(" == WORK REGISTRATION == ")
line()

data = dict()

data["Name"] = str(input("Type your name: "))
ybirth = int(input("Type your year of birth: "))
data["Age"] = datetime.now().year - ybirth
data["WPSS"] = int(input("Type your WPSS: "))
if data["WPSS"] != 0:
    data["Hiring"] = int(input("Type your year of hiring: "))
    data["Salary"] = float(input("Type your salary: "))
    data["Retirement"] = data["Hiring"] + 35

for p, v in data.items():
    print(f"{p} receab {v}")
