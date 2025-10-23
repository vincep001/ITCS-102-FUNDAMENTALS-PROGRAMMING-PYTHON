name = input("Hi ! What is your name? >>> ")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
print("ODD number compiler, type '0' to terminate the loop ")

sum = 0
odd = ""
tuloy = True

while tuloy == True:
    num = eval(input("Please input a number >>>  "))

    if num % 2 == 1:
        print("ODD number detected")
        odd += str(num) + ","
        sum += num
        continue
    elif num == 0:
        print("Loop terminated")
        break
    else:
        print("Invalid number")