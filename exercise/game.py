import random


def display_welcome_message():
    """Display welcome message and game rules."""
    print("=" * 50)
    print("🎮 NUMBER GUESSING GAME 🎮")
    print("=" * 50)
    print("\nI'm thinking of a number between 1 and 20.")
    print("Can you guess what it is?")
    print("\nLet's see how many attempts you need!")
    print("-" * 50)


def get_user_guess():
    """Get and validate user's guess."""
    while True:
        try:
            guess = input("\nWhat is your guess? (1-20): ").strip()
            guess = int(guess)
            
            if 1 <= guess <= 20:
                return guess
            else:
                print("⚠️  Please enter a number between 1 and 20.")
                
        except ValueError:
            print("⚠️  Invalid input! Please enter a valid number.")


def give_feedback(secret_number, user_guess):
    """Provide feedback based on user's guess."""
    if secret_number > user_guess:
        return "📈 My number is HIGHER than your guess!"
    elif secret_number < user_guess:
        return "📉 My number is LOWER than your guess!"
    else:
        return "🎉 CONGRATULATIONS! You guessed it right!"


def play_game():
    """Main game logic."""
    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 10
    
    print(f"\nI've chosen a number between 1 and 20.")
    print(f"You have maximum {max_attempts} attempts.")
    
    while attempts < max_attempts:
        attempts += 1
        guess = get_user_guess()
        feedback = give_feedback(secret_number, guess)
        
        print(f"\nAttempt #{attempts}: You guessed {guess}")
        print(feedback)
        
        if guess == secret_number:
            print(f"\n🏆 You found the number in {attempts} attempt(s)!")
            return attempts
        
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"💡 You have {remaining} attempt(s) remaining.")
    
    print(f"\n❌ Game Over! You've used all {max_attempts} attempts.")
    print(f"🤫 The secret number was: {secret_number}")
    return None


def ask_to_play_again():
    """Ask user if they want to play another round."""
    while True:
        choice = input("\n🔄 Would you like to play again? (y/n): ").strip().lower()
        
        if choice in ['y', 'yes', 'yeah', 'yep']:
            return True
        elif choice in ['n', 'no', 'nope']:
            return False
        else:
            print("⚠️  Please enter 'y' for yes or 'n' for no.")


def display_statistics(games_played, best_score):
    """Display game statistics."""
    print("\n" + "=" * 50)
    print("📊 GAME STATISTICS")
    print("=" * 50)
    print(f"Total games played: {games_played}")
    
    if best_score:
        print(f"Best score (fewest attempts): {best_score}")
    else:
        print("No wins yet. Keep trying!")
    print("=" * 50)


def main():
    """Main function to run the game."""
    display_welcome_message()
    
    games_played = 0
    best_score = None
    
    while True:
        games_played += 1
        
        print(f"\n{'='*50}")
        print(f"GAME #{games_played}")
        print(f"{'='*50}")
        
        attempts = play_game()
        
        # Update best score
        if attempts and (best_score is None or attempts < best_score):
            best_score = attempts
            print(f"🎖️  NEW BEST SCORE! {attempts} attempt(s)")
        
        display_statistics(games_played, best_score)
        
        if not ask_to_play_again():
            break
    
    print("\n" + "=" * 50)
    print("👋 Thanks for playing! Goodbye!")
    print("=" * 50)


if __name__ == "__main__":
    main()