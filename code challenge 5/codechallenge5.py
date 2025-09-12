#introduction
#genre input
#result of choices



genre =  input("welcome to manga recommender\nselect your genre\n (action, romance, horror) >>>>    ")

time = input("how long do you want it? (short, medium, long) >>>   ")

date = input("choice decade(1990, 2000)  ")



if genre == "action":
	if time == "short":
		if date == "1990":
			print("this is manga's i can recommend>\ndoraimon\ndragonball")

	else:
		print("we dont have manga at that duration/decade.")



elif genre == "romance":
	if time == "medium":
		if date == "1990":
			print("this is manga's i can recommend>\nkodocha\nboys over flower")

	else:
		print("we dont have manga at that duration/decade.")




elif genre == "horror":
	if time == "large":
		if date == "1990":
			print("this is manga's i can recommend>\nuzumaki\ntomie")

	else:
		print("we dont have manga at that duration/decade.")









		

		