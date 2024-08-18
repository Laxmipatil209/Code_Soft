import random

user_points = 0
computer_points = 0


def Play_Game():
    global user_points, computer_points
    computer_selection = ['Rock', 'Paper', 'Scissor']
    rand_int = random.randint(0, 2)
    computer_choice = computer_selection[rand_int]

    user_input = input("Enter your choice('Rock', 'Paper', 'Scissor'): ")

    if user_input.capitalize() == 'Rock' and computer_choice == 'Rock':
        print("Tie")
    elif user_input.capitalize() == 'Rock' and computer_choice == 'Paper':
        print("Computer Won")
        computer_points += 1
    elif user_input.capitalize() == 'Rock' and computer_choice == 'Scissor':
        print("User Won")
        user_points += 1
    elif user_input.capitalize() == 'Paper' and computer_choice == 'Rock':
        print("User Won")
        user_points += 1
    elif user_input.capitalize() == 'Paper' and computer_choice == 'Paper':
        print("Tie")
    elif user_input.capitalize() == 'Paper' and computer_choice == 'Scissor':
        print("Computer Won")
        computer_points += 1
    elif user_input.capitalize() == 'Scissor' and computer_choice == 'Rock':
        print("Computer Won")
        computer_points += 1
    elif user_input.capitalize() == 'Scissor' and computer_choice == 'Paper':
        print("User Won")
        user_points += 1
    elif user_input.capitalize() == 'Scissor' and computer_choice == 'Scissor':
        print("Tie")
    else:
        print("Invalid input")

    play_again = input("Do you want to play again?:(Y/N) ")
    if play_again.capitalize() == "Y":
        Play_Game()
    if play_again.capitalize() != "Y" and play_again.capitalize() != "N":
        print("Invalid input")
    else:
        if user_points > computer_points:
            print(f"User won the match!!\nUser points:{user_points}")
        elif user_points == computer_points:
            print(f"Match Tied!!\nUser points:{user_points}")

        else:
            print(f"Computer won the match!!\nComputer points:{computer_points}")


Play_Game()
