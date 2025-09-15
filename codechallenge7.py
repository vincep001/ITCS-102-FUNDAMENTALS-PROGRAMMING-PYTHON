odd = 0
for i in range(10):
    no = eval(input("enter 10 numbers here >>>  "))
    
    if no % 2 != 0:
        odd += no
print("the sum of odd numbers summation is", odd)
