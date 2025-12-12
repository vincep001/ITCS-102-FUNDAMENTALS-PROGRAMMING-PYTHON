#intro munaa like welcoming
#print welcome to py tutorials
#gumamit ng imports
#Bale 8 topics DAPAT ANG MAGAWA NA tutorials and EXAMPLES, tas 9 ay EXIT
#            TOPICS
        # 1.STRING
        # 2.statements, 
        # 3.variables, 
        # 4.operators: arithmetic, comparison, logical, assignment
        # 5.conditionals
        # 6.loops: triangle sample 
        # 7.lists  : append, pop, remove, insert, sort, reverse, len
        # 8.and functions: def greet and some calculation functions
        # 9.EXIT

#and after that next naman ay statement give examples again and then some example
#variable declaration is also isama naten
#operators din like give simple explanation and example like the arithmetic operators
#conditional statements din like if else and elif
#and loops and for loop din
#and list examples like the fruit list pakita ang append pop remove insert sort reverse len
#and functions din like DEF, example like greet name like that 


#dpat ang mangyayre, pag pinili EXAMPLE 1 STRING, lalabas si explanation and then example code, tas mag lalagay ka ng choices na like pag
# 1. Try string code, tas 2. BACK to menu na kung saan mag lalagay sya ng sarili nyang input na may nakafix na hello, so dpat ang result 
# ay magiging Hello name, and then lalabas ulit sila number 2
# BASTA LAHAT NG TOPICS AY MAG COCONTAIN NG TRY CODE AND BACK TO MENU OPTION(1 AND 2)

#- - - - - - - - - - -

import os
os.system('cls')

# print("WELCOME TO PYTHON TUTORIALS")
# print("HERE YOU CAN LEARN THE BASICS OF PYTHON PROGRAMMING LANGUAGE")
#import os


#print muna mga choices
while True:
    print("🙋 WELCOME TO PYTHON TUTORIALS BY Punzalan, Vince anton M | BSIT-1A")
    print("HERE YOU CAN LEARN THE BASICS OF PYTHON PROGRAMMING LANGUAGE🧑‍💻")
    print('- - - - - - - - - - -')
    print('🐍 PYTHON TUTORIALS MENU 🐍')
    print('1. STRING\n2. STATEMENTS\n3. VARIABLES\n4. OPERATORS\n5. CONDITIONALS\n6. LOOPS\n7. LISTS\n8. FUNCTIONS\n9. EXIT')
    choice = input("CHOOSE THE NUMBER OF TOPIC YOU WANT TO LEARN 🔍 >>>   ")
    os.system('cls')

    #STRING TOPIC MAG LAGAY NG EXPLANATION AND EXAMPLE and 2 OPTIONS sa loob
    if choice == '1':
        print('STRING DEFINITION:')
        print('A string is a sequence of characters enclosed within \nsingle or double quotes. It is used to represent text in Python.')
        print('\nExample:')
        print('''   Input:
        name = "Vince" <-- this is the string variable
            print(name) 
        
        output:
            Vince''')
        
        #interaction sa user
        print('\n1. TRY STRING CODE\n2. BACK TO MENU')
        string_choice = input("YOUR CHOICE 👉   ")
        os.system('cls')

        if string_choice == '1':
            name = input("Enter your name: ")
            print(f"Hello, {name}! <--- uppercase letters".upper()) 
            print(f"Hello, {name}! <--- lowercase letters".lower())
            print(' '.join(reversed(name)) + "     <--- reversed letters")
            print(' '.join(name) + '     <--- spaced letters')
            
            print('\n2. BACK TO MENU')
            back_choice = input("YOUR CHOICE 👉   ")
            os.system('cls')
        
        elif string_choice == '2':
            os.system('cls')
            continue
        
        
        #STATEMENTS TOPIC MAG LAGAY NG EXPLANATION AND EXAMPLE and 2 OPTIONS sa loob
    elif choice == '2':
        print('STATEMENTS DEFINITION:')
        print('''A statement is a single line of code that tells Python to do something.
Every line that performs an action is a statement. so i show you the basic input and print statements.''')
        
        print('\nExample:')
        print('''              Input:
              username = input("Enter your username: ")
                print("Welcome,", username)
              
              output:
                Enter your username: Vince
                Welcome, Vince''')
        #interaction sa user
        print('\n1. TRY STATEMENT CODE\n2. BACK TO MENU')
        statement_choice = input("YOUR CHOICE 👉   ")
        os.system('cls') 
        if statement_choice == '1':
            username = input("Enter your username: ")
            print("Welcome", username, "to starting point of python basic tutorials!")
            print('\n2. BACK TO MENU')
            back_choice = input("YOUR CHOICE 👉   ")
            os.system('cls')
            
        elif statement_choice == '2':
            os.system('cls')
            continue
        
        
        #Variables topic naman mag lagay ng explanation and example and 2 OPTIONS sa loob
    elif choice == '3':
            print('VARIABLES DEFINITION:')
            print('''A variable is the named location that stores data in the memory. 
It acts as a container for values that can be changed during program execution.''')
            print('\nExample:')
            print('''          Input:
              age = 21
              print("I am", age, "years old.")
                  
                  output:
                  I am 21 years old.''')
            #interaction sa user
            print('\n1. TRY VARIABLE CODE W INPUT FUNCTION\n2. BACK TO MENU')
            variable_choice = input("YOUR CHOICE 👉   ")
            os.system('cls')
            if variable_choice == '1':
                while True:
                    age = input("Enter your age: ")
                    #isdigit verifying if tama yung input
                    if age.isdigit():
                        print("I am", age, "years old.")
                        print('\n2. BACK TO MENU')
                    else:
                        print('Letters are not allowed, please enter a valid age number.\n')
                        print('ENTER to try again\n2. BACK TO MENU')    
                    back_choice = input("YOUR CHOICE 👉   ")
                    os.system('cls')
                    if back_choice == '2':
                        break
                
            elif variable_choice == '2':
                os.system('cls')
                continue
    #OPERATORS TOPIC naman and mag lagay ng explanation and example at options inside the elif
    #Mag lagay ng 5 options including the back to menu option
    #1 arithmetic operators
    #2 comparison operators
    #3 logical operators
    #4 assignment operators
    #and each option dpat is may example and try simple code
    elif choice == '4':
        while True:
            print('OPERATORS DEFINITION:')
            print(''' 
In Python, operators help us compute values, compare data, make decisions, and assign information to 
variables. There are several operator types: ARITHMETIC, COMPARISON, LOGICAL, and ASSIGNMENT OPERATORS.''')
            print('\n1 > ARITHMETIC OPERATORS\n2 > COMPARISON OPERATORS\n3 > LOGICAL OPERATORS\n4 > ASSIGNMENT OPERATORS\n5 > BACK TO MAIN MENU')
            operator_choice = input('YOUR CHOICE 👉   ')
            os.system('cls')
            #arithmetic operators
            if operator_choice == '1':
                print('ARITHMETIC OPERATORS DEFINITION:')
                print('''Arithmetic operators are used to perform mathematical operations such as addition, subtraction, 
multiplication, and division. (+, -, *, /, %, **, // are examples of arithmetic operators).''')
                print('\nExample:')
                print('''               Input:
                      num1 = int(input("Enter a number: ")) <--- example number : 10
                      num2 = int(input("Enter another number: ")) <--- example number : 5
                      
                      result = num1 + num2
                      
                        print("The sum is:", result)
                        
                    output:
                        
                      The sum is: 15
 ''')
                print('\n1.TRY ARITHMETIC OPERATOR CODE\n2.BACK TO MENU')
                back_choice = input("YOUR CHOICE 👉   ")
                os.system('cls')
                if back_choice == '1':
                    

                    n1 = eval(input("Enter the first number : "))
                    n2 = eval(input("Enter the second number : "))
                    s = n1 + n2
                    d = n1 - n2
                    p = n1 * n2
                    q = n1 / n2

                    solution = ((n1 / n2) * 100 - 5 ) // 300
                    print("\nThe sum (+) of", n1, "and", n2, "is", s, "✔️\n")
                    
                    print("The difference (-) of", n1, "and", n2, "is", d, "✔️\n")
                    
                    print("The product (*) of", n1, "and", n2, "is", p, "✔️\n")
                    
                    print("The quotient (/) of", n1, "and", n2, "is", q, "✔️\n")
                    
                    print(n1, "exponent (**) by", n2, "is", n1**2, "✔️\n")
                    
                    print("The remainder (%) of", n1, "and", n2, "is",n1 % n2, "✔️\n")
                    
                    print("The floor division (//) of", n1, "and", n2, "is", n1//n2, "✔️\n")
                    
                    print('\n2.BACK TO MENU')
                    back_choice = input("YOUR CHOICE 👉   ")
                    os.system('cls')
                elif back_choice == '2':
                    os.system('cls')
                    continue
                #Comparison Operators
            elif operator_choice == '2':
                print('COMPARISON OPERATORS DEFINITION:')
                print('Comparison operators are used to compare two values and check if the condition is "True or False".')
                print('\nExample:')
                print('''                   Input:
                      age = int(input("Enter your age: ")) <--- example number : 20

                        is_adult = age >= 18 

                        if age >= 18:   <--- check if age is 18 or older
    
                            print("legally an adult")
                        else:
   
                            print("Your a minor")
                        
                      output:
                            
                            legally an adult
 ''')
                print('\n1.TRY COMPARISON OPERATOR CODE\n2.BACK TO MENU')
                back_choice = input("YOUR CHOICE 👉   ")
                os.system('cls')
                if back_choice == '1':
                    while True:
                        age1 = int(input("Enter 1st age(Try 18 above): "))
                        os.system('cls')

                        is_adult = age1 >= 18 

                        if age1 >= 18:   # validate kung age is 18 or older
                            
                            print("legally an adult✅")
                            break
                        else:
                            print("Incorrect input, only input 18 above...")
                    
                    while True:
                        age2 = int(input("Enter 2nd age(Try 17 below): "))
                        os.system('cls')

                        is_minor = age2 <= 17

                        if age2 <= 17:
                            break
                            
                        else:
                            print("Incorrect input, only input 17 below...")
                    print("SUMMARY:")
                    print(f"----->  You're 1st age '{age1}' is legally adult ✅\n")
                    print(f"----->  You're 2nd age '{age2}' is a minor ❌\n")
                    print('\n2.BACK TO MENU')
                    back_choice = input("YOUR CHOICE 👉   ")
                    os.system('cls')
                    continue
                elif back_choice == '2':
                    os.system('cls')
                    continue
            elif operator_choice == '3':
                print('LOGICAL OPERATORS DEFINITION:')
                print('Logical operators are used to combine multiple conditions and return a boolean value (True or False).')
                print('\nExample:')
                print('''                   Input: 
                      score = int(input("Enter your score: ")) #<--- example number : 15
                       
                      has_id = input("Did you pass the paper in google classroom (yes/no): ") #<--- example input : yes
                        
                      passed = score >= 12 and has_id.lower() == 'yes'
                        
                      if passed:
                        print("You passed the quiz!")

                    else:
                        print("You failed the quiz:( better luck next time! / Make sure to passed the paper in google classroom")
                        output:
                                
                                You passed the quiz!
''')
                #interaction sa user
                print('\n1.TRY LOGICAL OPERATOR CODE\n2.BACK TO MENU')
                back_choice = input("YOUR CHOICE 👉   ")
                os.system('cls')
                if back_choice == '1':
                    score = int(input("Imagine you done at your QUIZ 1-20 items and the passing score is '12', and it is online quiz\nEnter your score: ")) #<--- example number : 22
                     
                    has_id = input("Did you pass the paper in google classroom (yes/no): ") #<--- example input : yes
                    passed = score >= 12 and has_id.lower() == 'yes'
                    if passed:
                        print("You passed the quiz 🥳")

                    else:
                        print("You failed the quiz:( better luck next time 😔 / Make sure to passed the paper in google classroom")
                    
                    print('\n2.BACK TO MENU')
                    back_choice = input("YOUR CHOICE 👉   ")
                    os.system('cls')
                
                elif back_choice == '2':
                    os.system('cls')
                    continue
                #assignment operators
            elif operator_choice == '4':
                    print('ASSIGNMENT OPERATORS DEFINITION:')
                    print('Assignment operators are used to assign values to variables. The most common assignment operator is the equal sign (=).')
                    print('\nExample:')
                    print('''                   Input:
                          x = 10 <--- eto yung assigned value
                          y = 5  <--- eto yung assigned value
                          
                          x += y  <--- it means x = x + y / it adds the value of y to x
                          
                          print("The value of x is:", x)
                          
                          output:
                                
                                The value of x is: 15 ''')
                    
                    #interaction sa user
                    print('\n1.TRY ASSIGNMENT OPERATOR CODE W INPUT FUNCTION\n2.BACK TO MENU')
                    back_choice = input("YOUR CHOICE 👉   ")
                    os.system('cls')
                    if back_choice == '1':

                        
                        a = int(input("Enter a starting number: ")) #<--- ask ng value for a

                        print("The value of a is", a)

                        a += 5
                        print("After a += 5, the value of a is", a)

                        a = +5
                        print("After a = +5, the value of a is", a)

                        a += 3
                        print("After a += 3, the value of a is", a)

                        a += 8
                        print("After a += 8, the value of a is", a)

                        a *= 2
                        print("After a *= 2, the value of a is", a)

                        a -= 3
                        print("After a -= 3, the value of a is", a)
                                                
                        
                        print('\n2.BACK TO MENU')
                        back_choice = input("YOUR CHOICE 👉   ")
                        os.system('cls')

                    elif back_choice == '2':
                        os.system('cls')
                        continue
            elif operator_choice == '5':
                os.system('cls')
                break
            continue
        #Conditional statements TOPIC naman mag lagay ng explanation and example and 2 OPTIONS sa loob
    elif choice == '5':
        print('CONDITIONAL STATEMENTS DEFINITION:')
        print('Conditional statements allow us to make decisions in our code based on certain conditions. Common examples in Python are if, elif, and else.')
        print('\nExample:')
        print('''                   Input:
                        num = int(input("Enter a number: ")) <-- example number: 7
              
                        if num > 0:    <--- if true 
                            print("The number is positive.")
                        
                        elif num < 0:    <--- if the 1st condition is false and this is true
                            print("The number is negative.")    <--- neither the conditions is true
                        
                        else:
                            print("The number is zero.")
                                    output:
                                        
                                        The number is positive.
 ''')
        #interaction sa user
        print('\n1. TRY CONDITIONAL STATEMENT CODE\n2. BACK TO MENU')
        back_choice = input("YOUR CHOICE >>>   ")
        os.system('cls')
        if back_choice == '1':
            num = int(input("Enter a number: ")) 
              
            if num > 0:   
                print(num,"is positive.")
            
            elif num < 0:    
                print(num,"is negative.")    
            
            else:
                print("The number is zero.")
            
            if num % 2 == 0:
                print(num,"is even.")
            
            else:
                print(num,"is odd.")
            
            print('\n2.BACK TO MENU')
            back_choice = input("YOUR CHOICE 👉   ")
            os.system('cls')
        elif back_choice == '2':
            os.system('cls')
            continue
        #LOOP topic naman guysss mag lagay ng explanation and example and 2 OPTIONS sa loob
    elif choice == '6':
        print('LOOPS DEFINITION:')
        print('A loop is a programming structure that repeats a block of code again and again\nuntil a certain condition is met or for a specific number of times.')
        print('\nExample:')
        print('''           input:
            print("diamond pattern")

            for v in range(1, 11, 1): <--- this part is the half top of the diamond
                for i in range(11, v, -1): <--- eto naman yung nag aadjust ng spaces sa left side
                    print(" ", end=" ")
              
                for n in range (1, v + 1, 1): <--- eto naman yung nag aadjust ng bilang ng stars sa left side ng diamond
                    print("*", end=" ")
              
                for s in range(1, v, 1): <--- eto naman yung nag aadjust ng bilang ng stars sa right side
                    print("*", end=" ")
                print() 
              
           
        output:
                    * 
                  * * * 
                * * * * * 
              * * * * * * * 
            * * * * * * * * * 
          * * * * * * * * * * * 
        * * * * * * * * * * * * * 
      * * * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * * * 
  * * * * * * * * * * * * * * * * * * *''')
        #interaction sa user
        print('\n1. TRY LOOP CODE W INPUT FUNCTION\n2. BACK TO MENU')
        back_choice = input("YOUR CHOICE 👉   ")  
        os.system('cls')
        if back_choice == '1':
            rows = int(input("Enter number of rows: ")) #<--- example we input: 5

            for i in range(1, rows + 1):
                 spaces = " " * (rows - i)
                 stars = "*" * (2*i - 1)
                 print(spaces + stars)

              
            print('\n2.BACK TO MENU')
            back_choice = input("YOUR CHOICE 👉   ")
            os.system('cls')
        elif back_choice == '2':
            os.system('cls')
            continue
    # #List operator namann mag lagay ng explanation and 2 options
    elif choice == '7':
            my_list = []
            while True:   
                print('LIST DEFINITION:')
                print('A list is a collection of items that are ordered and changeable. Lists are used to store multiple items in a single variable.\nand here are some examples of list methods like append, pop, remove, insert, sort, reverse, and len.')
                print('\n1. APPEND METHOD\n2. POP METHOD\n3. REMOVE METHOD\n4. INSERT METHOD\n5. SORT METHOD\n6. REVERSE METHOD\n7. LEN METHOD\n8. SHOW LIST\nX. BACK TO MAIN MENU')
                list_choice = input("YOUR CHOICE 👉   ")
                os.system('cls')
                if list_choice == '1':
                    #append part
                    print('APPEND METHOD DEFINITION:')
                    print('The append() method adds an item to the end of the list.')
                    
                    # Loop to allow adding multiple items
                    while True:
                        item = input("Enter an item: ")
                        my_list.append(item)
                        print(f"{item} is added to the list.")
                        print("Current list:", my_list)
                        
                        # Ask if user wants to add more
                        print('\nA. ADD MORE\nX. BACK TO MAIN MENU')
                        add_choice = input("YOUR CHOICE 👉   ").upper()
                        os.system('cls')
                        
                        if add_choice == 'A':
                            continue  # Go back to add another item
                        
                        if add_choice == 'X':
                            break                   
                    os.system('cls')
                elif list_choice == '2':
                    print('POP METHOD DEFINITION:')
                    print('The pop() method removes and returns the last item from the list.')
                    if my_list:
                        popped_item = my_list.pop()
                        print(f"Popped item: {popped_item}", "is now gone from the list.")
                    else:
                        print("List is empty!")
                    print("Current list:", my_list)
                    print('\nX. BACK TO MAIN MENU')
                    back_choice = input("YOUR CHOICE 👉   ")
                    os.system('cls')
                elif list_choice == '3':
                    #remove part
                    print('REMOVE METHOD DEFINITION:')
                    print('The remove() method removes the first occurrence of a specified item from the list.')
                    print('current list:', my_list)
                    if my_list:
                        remove = input("Enter the item to remove: ")
                        os.system('cls')
                        if remove in my_list:
                            my_list.remove(remove)
                            print(f"{remove} removed from the list.")
                        else:
                            print("Item not found.")
                    else:
                        print("List is empty!")
                    print("Current list:", my_list)
                    print('\nX. BACK TO MAIN MENU')
                    back_choice = input("YOUR CHOICE 👉   ")
                    os.system('cls')
                elif list_choice == '4':
                    #insert part
                    print('INSERT METHOD DEFINITION:')
                    print('The insert() method inserts an item at a specified index in the list.')
                    insert = input("Enter an item to insert: ")
                    index = int(input("Enter the index (0-based): "))
                    my_list.insert(index, insert)
                    print(f"{insert} inserted at index {index}.")
                    print("Current list:", my_list)
                    print('\nX. BACK TO MAIN MENU')
                    back_choice = input("YOUR CHOICE 👉   ")
                    os.system('cls')
                elif list_choice == '5':
                    #sort part
                    print('SORT METHOD DEFINITION:')
                    print('The sort() method sorts the items of the list in ascending order, like A to Z or 0 to 9.')
                    try:
                        my_list = [int(i) for i in my_list]
                        my_list.sort()
                    except ValueError:
                        my_list.sort()
                    print("List sorted.")
                    print("Current list:", my_list)
                    print('\nX. BACK TO MAIN MENU')
                    back_choice = input("YOUR CHOICE 👉   ")
                    os.system('cls')
                elif list_choice == '6':
                    #reverse part
                    print('REVERSE METHOD DEFINITION:')
                    print('The reverse() method reverses the order of the items in our list.')
                    my_list.reverse()
                    print("List reversed.")
                    print("Current list:", my_list)
                    print('\nX. BACK TO MAIN MENU')
                    back_choice = input("YOUR CHOICE 👉   ")
                    os.system('cls')
                elif list_choice == '7':
                    #len part
                    print('LEN METHOD DEFINITION:')
                    print('The len() function returns the number of items in a list.')
                    length = len(my_list)
                    print(f"\nThe length of the list is: {length}")
                    print("Current list:", my_list)
                    print('\nX. BACK TO MAIN MENU')
                    back_choice = input("YOUR CHOICE 👉   ")
                    os.system('cls')
                elif list_choice == '8':
                    #show list part
                    print('CURRENT LIST:', my_list)
                    print('\nX. BACK TO MAIN MENU')
                    back_choice = input("YOUR CHOICE 👉   ")
                    os.system('cls')
                elif list_choice.upper() == 'X':
                    os.system('cls')
                    break
                continue
    #FUNCTIONS TOPIC naman mag lagay ng explanation and example and 2 OPTIONS sa loob
    elif choice == '8':
        print('FUNCTIONS DEFINITION:')
        print('A function is like mini-program within a program. Defining a function makes your program\nmore ogranize and you can re-use it in any part of your program. Use the "def" keyword to define a function. ')
        print('\nExample:')
        print('''           Input: 
              def sum (num1, num2): #<--- num1 and num2 are parameters
    
                total = num1 + num2 #<-- the calculation
                print ("The sum of",num1,"and",num2,"is",total) 

              def act(): 
                first = eval(input("Enter a number: "))
                second = eval(input("Enter a number: "))
                sum(first, second)
                act()
              output:
                    Enter a number: 20
                    Enter a number: 15
                    The sum of 20 and 15 is 35''')
        #interaction sa user
        print('\n1. TRY FUNCTION CODE W INPUT\n2. BACK TO MENU')
        back_choice = input("YOUR CHOICE 👉   ")
        os.system('cls')
        if back_choice == '1':
            
            print('=== TEXT SECTION ===')
            while True:
                user_name = input("Enter your name: ")
                os.system('cls')

                if user_name.isalpha():
                    break
                else:
                    print("Letters only please 😁")
            
            def greet_ppl(name):
                print(f"Hello again, {name}😁 We are almost there, keep going until the end!")
            
            greet_ppl(user_name)
            
            print('\n=== MATH SECTION ===')
            num = int(input("Enter a random number from 1-100: "))
            print(f'\n> Original number: {num}\n')

            def multiply_to_two(num):
                return num * 2
            print(f'> Multiply to 2: {multiply_to_two(num)}\n')

            def plus_ten(n):
                return n + 10
            print(f'> Add 10: {plus_ten(num)}\n')

            def squareRoot(n):
                return n ** 2
            print(f'> Square Root: {squareRoot(num)}\n')
            
            
            print('\n2.BACK TO MENU')
            back_choice = input("YOUR CHOICE 👉   ")
            os.system('cls')
        elif back_choice == '2':
            os.system('cls')
        continue
    #Last optionnnnn
    elif choice == '9':
        os.system('cls')
        import time

        thankyuumessage = "YOU HAVE EXITED AND REACHED THE END OF MY PYTHON TUTORIALS 🥳 🥳\nI HOPE YOU ENJOY TO MY LITTLE PROGRAM, HOPE TO SEE YOU AGAIN USER 🤝\nTHANKYOU SO MUCH AND ADVANCE MERRY CHRISTMAS  ❤️ 🧑‍🎄   \n\n-VAMP\n\n"
        
        ascii_hart = r""" 
                          ⣴⠶⢦⣤⠶⠶⣄⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⣇⠀⠀⠁⠀⢀⣿⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠙⢧⣄⠀⣠⠞⠁⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⣀⡀⠀⠉⠛⠃⣠⣄⡀⠀⠀⠀
                    ⠀⠀⠀⠀⡞⠉⠙⢳⣄⢀⡾⠁⠈⣿⠀⠀⠀
                    ⠀⠀⠀⠀⢻⡄⠀⠀⠙⢿⡇⠀⢰⠇⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠙⣦⡀⠀⠀⠹⣦⡟⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠈⢳⣄⠀⠀⠈⠻⣄⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⡞⠋⠛⢧⡀⠀⠀⠘⢷⡀⠀
                    ⠀⠀⠀⢠⡴⠾⣧⡀⠀⠀⠹⣦⠀⠀⠈⢿⡄
                    ⠀⠀⣀⣿⠀⠀⠈⠻⣄⠀⠀⠀⠀⠀⠀⠈⣷
                    ⢠⡟⠉⠛⢷⣄⠀⠀⠈⠀⠀⠀⠀⠀⠀⣰⠏
                    ⠀⢷⡀⠀⠀⠉⠃⠀⠀⠀⠀⠀⠀⠀⣴⠏⠀
                    ⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⠀⠀
                    ⠀⠀⠀⠈⠙⠶⣤⣤⣤⡤⠶⠋⠁⠀⠀
"""

        speed = 0.05

        for char in thankyuumessage:
            print(char, end='', flush=True)
            time.sleep(speed)

        print(ascii_hart)
        break
       
    
       

        



            
            
            
            
                  
        
  












   
