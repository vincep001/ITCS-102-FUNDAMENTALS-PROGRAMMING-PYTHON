#using for loop, ask user to input 10 numbers
#after input, get the summation of all the numbers

num = 0
for x in range(1, 11):
    number = eval(input("enter a number"))
    num += number

print(num)