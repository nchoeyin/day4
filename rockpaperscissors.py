import random
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

def rockpaperscissor():
    '''User's Input'''
    print("For Rock enter R \nFor Paper enter P \nFor Scissors enter S: \n")
    user = input("Enter your choice: \t").lower()
    if user=='r':
        user=rock
        print(rock)
    elif user=='p':
        user=paper
        print(paper)
    elif user=='s':
        user=scissors
        print(scissors)
        
    '''Computer's choice'''
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        comp = rock
    elif computer_choice == 2:
        comp = paper
    else:
        comp = scissors
    print(f"The computer's choice is {comp}")
    
    '''Comparison'''
    if comp==user:
        print("Draw!!!")
    else:
        if comp==rock and user==paper:
            print("comp:rock | user:paper user wins!!")
        elif comp==rock and user==scissors:
            print("comp:rock | user:scissors computer wins!!")
        elif comp==paper and user==scissors:
            print("comp:paper | user:scissors user wins!!")
        elif comp==paper and user==rock:
            print("comp:paper | user:rock computer wins!!")
        elif comp==scissors and user==rock:
            print("comp:scissors | user:rock user wins!!")
        elif comp==scissors and user==paper:
            print("comp:scissors | user:paper comp wins!!")
rockpaperscissor()
'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1st Output:

For Rock enter R 
For Paper enter P 
For Scissors enter S: 

Enter your choice: 	r
  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  

The computer's choice is   
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  

Draw!!!
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2nd Output:
For Rock enter R 
For Paper enter P 
For Scissors enter S: 

Enter your choice: 	s
  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  

The computer's choice is   
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  

Draw!!!
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
