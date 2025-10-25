

animelist = []


while True:
    askT = (input("Emter the title of an anime ( or type 'exit' to finish):  "))

    if askT.lower() == 'exit':
        break

    animelist.append(askT)
    print(f'"{askT}" has been added to your anime list.\n')

print("\nYou have exited the anime entry program.")
print("Your anime list includes:")

for anime in animelist:
    print(f" - {anime}")


