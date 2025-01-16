while True:

    question_1 = input("\nis the movie playing?(y/n): ")
    question_2 = input("is the movie's ticket cheap?(y/n): ")
    question_3 = input("do you have free time?(y/n): ")
                
    if question_1.lower().strip() == "y" and question_3.lower().strip() == "y" and question_3.lower().strip() == "y":
        
        print("\nYou can go to the cinema!   :)")
    
    else:
        print("\nOh no! You can't go to the cinema...   :(")   

