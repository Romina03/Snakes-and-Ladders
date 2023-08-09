import random

class Player:

    def __init__(self, name):
        self.name = name
        self.position = 0

    
def roll():
   return random.randint(1, 6)

# List which contains the numbers where there is a snake
snakeList = [17, 58, 62, 64, 87, 95, 98]

# List which contains the numbers where there is a ladder
ladderList = [4, 9, 21, 28, 51, 71, 80]

# Dictionary where the key is the where the snake is and the
# value is the number the user ends up in (tail of the snake)
snake = {
    17 : 7,
    58 : 34,
    62 : 19,
    64 : 60,
    87 : 24,
    95 : 75,
    98 : 79
}

# Dictionary where the key is where the ladder is positioned and the
# value is the number where the ladder takes the user to 
ladder = {
    4 : 14,
    9 : 31,
    21 : 42,
    28 : 84,
    51 : 67,
    71 : 91,
    80 : 99
}

# Welcome message
print("Welcome to Snakes and Ladders!")
print("This game is played between the user and computer.")
playerName = input("\nWhat is your name? ")

# Create player 1 which is the computer
player1 = Player("Computer")

# Create player 2 which is the user
player2 = Player(playerName)

print(f"\n{player1.name} vs {player2.name}\n")

# Computer rolls the dice first then the user
while True:
    number = roll()
    print(f"Computer rolled {number}.")
    player1.position = player1.position + number

    if player1.position in snake: 
        player1.position = snake[player1.position] 

    if player1.position in ladder:
        player1.position = ladder[player1.position]

    if player1.position > 100:
        player1.position = player1.position - number

    if player1.position == 100:
        print("\nComputer is the winner!!!!")
        break

    print(f"Computer is at {player1.position}.\n")

    enter = input("Press Enter to roll dice!\n")
    if enter == "":
        number = roll()
        print(f"{player2.name} rolled {number}.")
        player2.position = player2.position + number

        if player2.position in snake: 
            player2.position = snake[player2.position] 

        if player2.position in ladder:
            player2.position = ladder[player2.position]

        if player2.position > 100:
            player2.position = player2.position - number
        
        if player2.position == 100:
            print(f"\n{player2.name} is the winner!!!!")
            break

        print(f"{player2.name} is at {player2.position}.\n")






