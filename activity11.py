#input temperature
#1-20 = cold
#21-30 = warm
#31-40 = hot
#41-50 = very hot

temp = eval(input("enter temperature >>>   "))

if temp >= 1 and temp <= 20:
    print("the tenperature is cold")
elif temp >= 21 and temp <= 30:
    print("the temperature is warm")
elif temp >= 31 and temp <= 40:
    print("the temperature is hot")
elif temp >= 41 and temp <= 50:
    print("the temperature is very hot")
else:
    print("temperature is invalid...")