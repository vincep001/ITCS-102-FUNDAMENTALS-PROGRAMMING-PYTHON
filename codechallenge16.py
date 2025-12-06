#introduction ni vince punzalan 
#DONE
import json
import os
os.system("cls")


print("\n<--------------------------->")
print("STUDENT INFORMATION SYSTEM")
print("<--------------------------->")

#EMPTy dictionary
student_records = {}

while True:
#     print("============================\n\nSELECT FROM THE OPTIONS BELOW:\n\n============================ \nA - Add Information\nB - Print all record\nC - Search student record\nD - Delete student record\nE - Edit student Record")
    print("============================")
    print("SELECT FROM THE OPTIONS BELOW:")
    print("A - Add information\nB - Print student record")
    print("C - Search a record\nD - Delete a record")
    print("E - Modify a Record\nF - Export Student Record\nG - IMPORT record\n")
    print("X - EXIT")
    choice = input("============================\nYour choice  >>>>>>>   ").lower()

    #lagay na ng functions
    #DONE

    if choice == "a":
        print('============================')
        print('ADDING STUDENT INFORMATION📝')
        print('============================')
        search_id = input("Key search for this student/text >>>   ")

        first_name = input("Input student first name >>>   ").upper()
        last_name = input("Input student last name >>>   ").upper()
        course = input("Input student course >>>   ").upper()
        email =  input("Input student email >>>   ") 
        isSingle = input("Are you single? yes/no >>>   ")
        
        student_records[search_id] = [first_name, last_name, course, email, isSingle
                                      ]
        print("DATA SAVED")

        os.system("cls")
        continue
    

    #nakakalito na part
    #DONE
    elif choice == 'b':
        os.system('cls')
     #    print("============================")
        print("📇PRINTING STUDENT RECORD📇")
        print('============================')
        for id, search_id in student_records.items():
                print(f'STUDENT ID "{id}" IN STUDENT RECORD : {search_id}')
                
            
            
        continue


    elif choice == 'c':
        os.system('cls')
        print('SEARCH STUDENT RECORD')
        print('============================')

        search_id = input('Input ID to search --->>  ').lower()
        if search_id in student_records:
               print("==================")
               print('\nRECORD FOUND 🎉')
               print("==================")

               for i in student_records[search_id]:
                    print(f'--> {i}')
        else:
               print('====================')
               print('NO RECORD FOUND :(')
               print('====================')
               continue





     #    for id in student_records.keys():
     #      if search_id in student_records.keys():
     #           print("==================")
     #           print('\n\nRECORD FOUND🎉')
     #           for i in student_records[search_id]:
     #                print("\n==================")
     #                print(f'--> {i}')
     #      else:
     #           print('====================')
     #           print('NO RECORD FOUND:(')
     #           continue



    #UNFINISHED (PART D, E)

    elif choice == 'd':
         os.system('cls')
         print("DELETE EXISTING RECORD")

         search_id = input("Input ID to search ----->   ").lower()
         for id in student_records.keys():
               if search_id in student_records.keys():
                    print("===========================")
                    print('\n\nRECORD FOUND:)')
                    print("===========================")
                    #print the record of search student
                    for i in student_records[search_id]:
                         print(f'-- {i}')
                    student_records.pop(search_id)
                    print("===========================")
                    print("RECORD DELETED🗑")

               else:

                   print('====================================')
                   print('\n\nNO RECORD FOUND:(')
                   print('====================================')
               break
         continue
              #letter
    elif choice == 'e':
          os.system('cls')
          print('EDIT/MODIFY STUDENT RECORD')
          print('=============================')

          search_id = input('Input ID to search ----->   ').lower()

          for id in student_records.keys():
               if search_id in student_records.keys():
                    print("=========================")
                    #print the record of search student
                    for i in student_records[search_id]:
                         print(f'-- {i}')

                    
                    first_name = input("Input NEW student first name >>>   ").upper()
                    last_name = input("Input NEW student last name >>>   ").upper()
                    course = input("Input NEW student course >>>   ").upper()
                    email =  input("Input NEW student email >>>   ")

                    student_records[search_id][0] = first_name
                    student_records[search_id][1] = last_name
                    student_records[search_id][2] = course
                    student_records[search_id][3] = email

                    print("============================")
                    print("✨RECORD UPDATED SUCCESSFULLY✨")

               else:
                    print('============================')
                    print('\n\nNO RECORD FOUND:(')
                    print('============================')
               break
          continue
     
    elif choice == 'f':
           os.system('cls')
           print("EXPORTING STUDENT RECORD TO JSON FILE📁")
           print('============================')
     
           with open('student_records.json', 'w') as json_file:
            json.dump(student_records, json_file, indent=4)

           print("EXPORT SUCCESSFUL✅")
           continue
    elif choice == 'g':
               os.system('cls')
               print("IMPORTING STUDENT RECORD FROM JSON FILE📁")
               print('============================')
          
               with open('student_records.json', 'r') as json_file:
                    student_records = json.load(json_file)
               print("IMPORT SUCCESSFUL✅")
               continue
    
    elif choice == 'x':
            print("EXITING THE PROGRAM...👋")
            break

          

            



    