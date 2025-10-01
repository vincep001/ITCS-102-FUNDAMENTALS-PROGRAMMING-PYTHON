print("\t\t\t*")

for x in range(1, 11, 1):
    for y in range(10, x, -1):
        print(" ", end=" ")
    for z in range(1, x, 1):
        print("*", end=" ")
    for v in range(0, x, 1):
        print("*", end=" ")
    print()