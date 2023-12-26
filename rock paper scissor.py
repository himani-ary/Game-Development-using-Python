import random

# Initialize the turn counter
turns = 0

# Loop for three turns
while turns < 3:
    turns += 1 
    
    # Available options for the game
    option = ("rock", "paper", "scissors")
    
    # Computer randomly selects an option
    computer = random.choice(option)
    
    # Reset player choice within each iteration
    player = ()
    
    # Validate and prompt user for input until a valid choice is made
    while player not in option:
        player = input("Choose one - rock, paper, scissors: ")
    
    # Display player's and computer's choice
    print(f"Player's turn: {player}")
    print(f"Computer's turn: {computer}")

    # Game logic to determine the winner
    if player == computer:
        print("It's a tie")
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        print("You won")
    else:
        print("Computer won")

# Display game over message after three turns
print("Game's over")
