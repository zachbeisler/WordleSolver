import time
import Controller as controller

def load_words():
    ls = []
    with open("sgb-words.txt") as file:
        ls = [line.rstrip() for line in file]
    return ls
    
def make_pattern(guess, word):
    pattern = ""
    for i in range(len(guess)):
        if guess[i] == word[i]:
            pattern += "o"
        elif guess[i] in word:
            pattern += "?"
        else:
            pattern += "x"
    return pattern

def test_run(word, ls):
    newlist = ls[:]
    attempts = 0
    while True:
        attempts += 1
        guess = controller.choose_guess(newlist)
        pattern = make_pattern(guess, word)
        if guess == word:
            return attempts
        newlist = controller.read_pattern(pattern, guess, newlist)
        
if __name__ == "__main__":
    ls = load_words()
    runs = []
    n = 0
    for word in ls:
        print(f"{word} - {n} / {len(ls)}")
        runs.append(test_run(word, ls))
        n += 1
    print(f"Average Attempts: {sum(runs)/len(runs):.2f}")
    