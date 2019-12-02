A = int(input()) # 0 <= A <= 100
if  0 > A or A > 100:
    exit()

M = int(input()) # 0 <= M <= 100
if  0 > M or M > 100:
    exit()

print((2 * M) - A)
