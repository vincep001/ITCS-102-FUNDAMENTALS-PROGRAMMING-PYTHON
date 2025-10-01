#STRING FORMATTING
# firstname = "John"
# mid_name = "F."
# lname = "Kennedy"

#print("my name is ", firstname, " ", mid_name, " ", lname) 
# print("my name is {firstname ()} {mid_name()} {lname()}"
# inpu 10 numbers, get the summation of all the odd numbers

odds = 0

for i in range(1, 11, 1):
    num = eval(input(f"{i} - Enter number >>> "))

    if num % 2 == 1:
        odds += num

print(f"The summation of all given ODD numbers is: {odds}")
