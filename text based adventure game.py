import time

def introduction():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest...")
    time.sleep(1)

def make_choice(options):
    print("Choose your action:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

def forest_path():
    print("You come across a fork in the path.")
    time.sleep(1)

    options = ["Take the left path", "Take the right path"]
    choice = make_choice(options)

    if choice == 1:
        print("You venture down the left path.")
        time.sleep(1)
        print("You encounter a friendly creature.")
        time.sleep(1)
        print("It leads you to a hidden treasure!")
    else:
        print("You choose the right path.")
        time.sleep(1)
        print("You stumble upon a trap and fall into a pit.")
        time.sleep(1)
        print("Game over. You have failed.")

def main():
    introduction()
    forest_path()

if __name__ == "__main__":
    main()
