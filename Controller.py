_wrong = "x"
_wrong_place = "?"
_correct = "o"

def read_pattern(pattern, guess, ls):
    for index in range(len(pattern)):
        status = pattern[index]
        char = guess[index]
        if status == _wrong:
            ls = list(filter(lambda s: char not in s, ls))
        elif status == _wrong_place:
            ls = list(filter(lambda s: char in s and s[index] != char, ls))
        elif status == _correct:
            ls = list(filter(lambda s: s[index] == char, ls))
    return ls
            
def choose_guess(ls):
    letter_weights = {}
    if len(ls) == 1:
        return ls[0]
    for word in ls:
        for char in word:
            if char not in letter_weights:
                letter_weights[char] = 0
            letter_weights[char] += 1
    weighted_words = map(lambda s: (s, sum([letter_weights[char] for char in set(s)])), ls)
    return sorted(weighted_words, key=lambda t: t[1], reverse=True)[0][0]

if __name__ == "__main__":
    s = "aabc"
    s = set(s)
    print(list(s))