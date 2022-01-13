import os
import Controller as controller

def print_help():
    print()
    with open("help.txt") as help_file:
        for line in help_file:
            print(line, end="")
    print()
    input("Press any key to continue...")
    print()

def main():
    os.system('cls')
    print("Welcome to WordleSolver. Guess \"help\" to display a help menu.")
    ls = load_words()
    while len(ls) > 1:
        guess = input(f"Enter guess (reccomended '{controller.choose_guess(ls)}'): ")
        if guess == "*":
            print(ls)
            continue
        elif guess == "help":
            print_help()
            continue
        elif guess == "restart":
            return main()
        pattern = input(f"Enter pattern: ")
        ls = controller.read_pattern(pattern, guess, ls)
    input(f"Congratulations, the word is {ls[0]}! Press any key to close...")

def load_words():
    ls = []
    with open("sgb-words.txt") as file:
        ls = [line.rstrip() for line in file]
    return ls

if __name__ == "__main__":
    main()