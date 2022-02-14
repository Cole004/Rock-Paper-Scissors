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
icons = [rock, paper, scissors]
user_types = int(input("What do you want to choose 0 for rock,1 for paper and 2 for scissors\n"))

if user_types >=3 or user_types <= 0 :
    print("You entered a invalid number.You lose")
else : 
    print(icons[user_types])

    computer_choice = random.randint(0, 2)
    print("Computer chose :")
    print(icons[computer_choice])


    if user_types == computer_choice :
        print("It's a draw mate!")
    elif user_types == 0 and computer_choice == 2 :
        print("You win")
    elif computer_choice > user_types :
        print("You lose")
    elif user_types > computer_choice :
        print("You win")
    elif user_types == 2 and computer_choice == 0 :
        print("You lose")

