import random

# 0 = rock, 1 = paper, 2 = scissors
user_choice = int(input("Enter 0 for rock, 1 for paper, 2 for scissors: "))
computer_choice = random.randint(0, 2)

print("Computer chose:", computer_choice)

if user_choice >= 3 or user_choice < 0:
    print("Invalid choice")
elif user_choice == computer_choice:
    print("Draw")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")
