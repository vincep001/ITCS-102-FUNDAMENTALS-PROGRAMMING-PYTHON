

print("diamond pattern")


for v in range(1, 11, 1):
    for i in range(11, v, -1):
        print(" ", end=" ")
    for n in range (1, v + 1, 1):
        print("*", end=" ")
    for s in range(1, v, 1):
        print("*", end=" ")
    print()

for p in range(11, 0, -1):
    for o in range(11, p, -1):
        print(" ", end=" ")
    for g in range (1, p + 1, 1):
        print("*", end=" ")
    for i in range(1, p, 1):
        print("*", end=" ")
    print()

