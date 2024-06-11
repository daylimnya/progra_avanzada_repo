import random

def rock_paper_scissors_lizard_spock(choice: str) -> str:
    """
    Recieves a choice as a string: rock, paper, scissors, lizard, spock. 
    And the computer will choose, randomly, another play. The winner is given by the following rules:

    scissors cuts paper
    paper covers rock
    rock crushes lizard
    lizard poisons spock
    spock smashes scissors
    scissors decapitates lizard
    lizard eats paper
    paper disproves spock
    spock vaporizes rock
    (and as it always has) rock crushes scissors
    """
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    if choice not in choices:
        return "Invalid choice! Choose one of: rock, paper, scissors, lizard, spock."

    computer_choice = random.choice(choices)
    
    outcomes = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }
    
    if choice == computer_choice:
        result = "It's a tie!"
    elif computer_choice in outcomes[choice]:
        result = f"You win! {choice} beats {computer_choice}."
    else:
        result = f"You lose! {computer_choice} beats {choice}."
    
    return f"Player chose: {choice}\nComputer chose: {computer_choice}\n{result}"

# Tests:
print("Executing tests...")
print(rock_paper_scissors_lizard_spock("rock"))
print(rock_paper_scissors_lizard_spock("spock"))
print(rock_paper_scissors_lizard_spock("lizard"))