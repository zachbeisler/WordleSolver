import Controller as controller

def main():
    ls = load_words()
    while len(ls) > 1:
        guess = input(f"Enter guess (reccomended '{controller.choose_guess(ls)}'): ")
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