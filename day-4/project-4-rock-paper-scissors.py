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

# Add rock, paper and scissors to a list
game_choice = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# 1. Check if the user input is valid
if user_choice >= 0 and user_choice <= 2:
    print(game_choice[user_choice])

    # 2. MOVE COMPUTER LOGIC INSIDE THIS IF BLOCK
    # This only runs if the user choice was 0, 1, or 2
    computer_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(game_choice[computer_choice])

    # 3. MOVE CONDITIONS INSIDE THIS IF BLOCK
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif computer_choice == 2 and user_choice == 0:
        print("You win!")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice < computer_choice:
        print("You lose!")

# 4. The 'else' handles the invalid numbers
else:
    print("You chose an invalid option! You lose!")