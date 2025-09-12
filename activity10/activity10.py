#comments
#jeepney fare
#user would input their name
#if user is student, student discount will be applied
#20% discount for student, if not student, no discount.

name = input("input your name:)     ")
wasStudent =  input("Are you studen (YES/NO) >>>     ")
fare = eval(input("your bayad .....>   "))

if wasStudent == "YES":
         discount = fare * .2
         new_fare = fare - discount
         print("hi", name, " student discount is ", discount, "discount fare is ", new_fare)

else:
      print("Sorry", name, "you are not qualified for jeepney discount:(")


