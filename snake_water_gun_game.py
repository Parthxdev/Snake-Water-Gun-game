import random

def get_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == 's' and computer == 'g') or \
         (user == 'w' and computer == 'w') or \
         (user == 'g' and computer == 's'):
             return "User"
    else:
        return "Computer"
    
def display_choice(short):
    return ("Choose s for Snake, w for Water, g for Gun").get(short, "Invalid")

user_score = 0
computer_score = 0
rounds = 0

print("🎮 Welcome to Snake 🐍 Water 💧 Gun 🔫 Game!")

while True:
    
    print("\n--------New Game--------")
    print("Choose s for Snake, w for Water, g for Gun")
    
    user_choice = input("Choose s/w/g: ")
    if user_choice not in ['s', 'w', 'g']:
        print("❌ Invalid choice. Try again.")
        continue
    
    computer_choice = random.choice(['s', 'w', 'g'])
    
    print(f"Your choice => {user_choice}")
    print(f"computer choice => {computer_choice}")
    
    winner = get_winner(user_choice, computer_choice)
    
    if winner == "User":
        print("✅ You win this round!")
        user_score += 1
    elif winner == "Computer":
        print("❌ Computer wins this round!")
        computer_score += 1
    else:
        print("🤝 It's a draw!")
    
    rounds += 1            
    print(f"Score = Your {user_score} | Computer {computer_score} | Rounds {rounds}")
    
    
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Game Over...")
        print(f"Final Score : your {user_score} | Computer {computer_score} | Total Rounds {rounds}")
        
        if user_score > computer_score:
            print("🏆 You are the overall winner!")
        elif computer_score > user_score:
            print("💻 Computer wins overall!")
        else:
            print("😐 It's a tie overall!")
        break