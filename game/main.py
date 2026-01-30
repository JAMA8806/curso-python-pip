import random



def choose_option():
    option = ('rock', 'paper', 'scissors')
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in option:
        print("Invalid choice. Please try again.")
        return choose_option()
    computer_choice = random.choice(option)
    print(f"Computer chose: {computer_choice}")
    return user_choice, computer_choice

def determine_winner(user_choice, computer_choice, user_wins, computer_wins):
    if user_choice == computer_choice:
        return "It's a tie!", user_wins, computer_wins
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        user_wins += 1
        return "You win!", user_wins, computer_wins
    else:
        computer_wins += 1
        return "Computer wins!", user_wins, computer_wins

def play_game():
    user_wins = 0
    computer_wins = 0
    round_number = 1
    print("Welcome to Rock, Paper, Scissors!")
    print("First to 3 wins is the champion!")

    while user_wins < 3 and computer_wins < 3:
        print(f"Round {round_number}!")
        print("**********************************")
        round_number += 1
        user_choice, computer_choice = choose_option()
        result, user_wins, computer_wins = determine_winner(user_choice, computer_choice, user_wins, computer_wins)
        print(result)
        print(f"Score - You: {user_wins}, Computer: {computer_wins}")

if __name__ == "__main__":
    play_game()
  