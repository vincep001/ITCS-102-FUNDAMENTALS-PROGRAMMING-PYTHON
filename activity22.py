import random 
print("Let guess the number")
ran_num = random.randint(1,5)
tries = 0
tuloy = True

while tuloy == "True":
    num = int(input("Input an integer number"))

    tries += 1

    if num == ran_num:
        print("Winner !!")
        print("Your guess is CORRECT!")
        print(f"Only took you {tries} tries")
        break
    else:
        print("Wrong guess")
        print("Continue")
        continue