# M = Idade de Maria
# A = Idade de outro filho
# B = Idade de mais outro
M = int(input())

if 40 <= M <= 110:
    pass
else:
    print("Idade inválida")

A = int(input())

if 1 <= A < M:
    pass
else:
    print("Idade inválida")

B = int(input())

if 1 <= B < M:

    if A == B:
        print("Idade inválida")
    else:
        C = int(M - (A + B))
        if C > A and C > B:
            print(C)
        elif A > C and A > B:
            print(A)
        elif B > A and B > C:
            print(B)
else:
    print("Idade inválida")
