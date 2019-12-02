from time import  sleep

col = ("\033[m",
       "\033[33m",
        "\033[31m",
        "\033[30;44m")


def help_me(comm):
    title(f"Entering the system \{comm}\ ", 1)
    sleep(1.5)
    print((col[2]))
    help(comm)
    print(col[0], end=" ")


def title(mess, color=0):
    size = len(mess)
    print(col[color], end=" ")
    print("-" * size)
    print(mess)
    print("-" * size)
    print(col[0], end=" ")


command = ""
while True:
    title(" == HELP SYSTEM HELPME", 1)
    command = str(input(("Function or Library > ")))
    if command.upper() == "END":
        break
    else:
        help_me(command)
sleep(0.5)
title(" == CHECK BACK OFTEN! ", 1)
