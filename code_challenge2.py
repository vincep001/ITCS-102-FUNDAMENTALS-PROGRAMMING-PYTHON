cashin = eval(input("Enter amount to deposit : "))


phd1 = cashin // 1000
cashin = cashin % 1000

phd2 = cashin // 500
cashin = cashin % 500

phd3 = cashin // 200
cashin = cashin % 200

phd4 = cashin // 100
cashin = cashin % 100

phd5 = cashin // 50
cashin = cashin % 50

phd6 = cashin // 20
cashin = cashin % 20

phd7 = cashin // 10
cashin = cashin % 10

phd8 = cashin // 5
cashin = cashin % 5

phd9 = cashin // 1
cashin = cashin % 1


print("\nHere is a brekdown, of PH denominantion : ")


print("1000 ", phd1)
print("500 ", phd2)
print("200 ", phd3)
print("100 ", phd4)
print("50 ", phd5)
print("20 ", phd6)
print("10 ", phd7)
print("5 ", phd8)
print("1 ", phd9) 

