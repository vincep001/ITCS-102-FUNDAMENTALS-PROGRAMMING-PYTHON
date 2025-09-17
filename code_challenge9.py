print("COUNTDOWN TIMER SIMULATOR")
timer = eval(input("Enter a number for countdown >>>  "))
print("Countdown started...")

for i in range(timer, 0, -1):
    print(i)
    
    import time
    time.sleep(1)
print("LIFTOFF!")