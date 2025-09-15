print("FACTORIAL PROGRAM")

blank = eval(input("place a number here >>>  "))
num = 1

for i in range(blank, 0, -1):
    num *= i
    print(num)