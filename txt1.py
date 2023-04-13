import time

def display_intro():
    print("Welcome to the Adventure Game!")
    time.sleep(2)
    print("You wake up in a dark room with no memory of how you got there.")
    time.sleep(2)
    print("There are three doors in front of you - which one will you choose?")
    time.sleep(2)

def choose_door():
    choice = input("Enter 1, 2, or 3 to choose a door: ")
    while choice not in ['1', '2', '3']:
        choice = input("Invalid choice. Please enter 1, 2, or 3: ")
    return int(choice)

def play_game():
    display_intro()
    door = choose_door()
    print("You chose door", door)
    time.sleep(2)
    print("You open the door and step through...")
    time.sleep(2)
    print("You find yourself in a maze!")
    time.sleep(2)
    print("You need to find your way out. Good luck!")
    time.sleep(2)

# Run the game
play_game()