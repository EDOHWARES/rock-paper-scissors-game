from random import choice

#r > s, s > p, p > r

def check(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
    or (player == "p" and opponent == "r"):
        return True
    else:
        return False


def game():
    computer = choice(["r", "p", "s"])
    user = input("Rock(r), Paper(p), or Scissors(s)? ")

    if computer == user:
        return "A Tie!"
    else:
        boole = check(user, computer)
        if boole:
            return f"Computer: {computer} \nYou: {user} \nYou Win!"
        else:
            return f"Computer: {computer} \nYou: {user} \nComputer wins!"

print(game())