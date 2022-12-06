import random
def game():
    user = input("Enter your choice: (r) for rock, (p) for paper and (s) for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "Its a tie!"
    
    if is_win(user, computer):
        return "You win!"
    
    return "You lose"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

print(game())