import sys

def menu():
    """menu"""
    print("*" * 50)
    print("Here are your game menu: ".center(50))
    print("1. Create new player".center(50))
    print("2. Start new game".center(50))
    print("3. Change existing player name".center(50))
    print("4. Show highscore".center(50))
    print("5. Show rules of the game".center(50))
    print("6.Quit game".center(50))
    print("*" * 50)
    return input("choice:")

def welcome():
    """Welcome message"""
    print("*" * 50)
    print("Welcome to Pig Dice!" .center(50))
    print("*" * 50)

def rules():
    """rules of the game"""
    print("*" * 100)
    print("* The The objective of the game is to be the first one to reach 100 points".center(30))
    print("* Each turn, a player will roll a die".center(30))
    print("* until either a 1 is rolled or the player decides to hold".center(30))
    print("* If the player rolls any other number, it is added to their turn total and the player's turn continues".center(30))
    print("* If a player chooses to hold, their turn total is added to their score, and it becomes the next player's turn".center(30))
    print("*" * 100)

if __name__ == "__main__":
    # Call the main function.