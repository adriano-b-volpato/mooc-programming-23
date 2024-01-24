# Write your solution here


def histogram(string):
    letters = {}
    for letter in string:
        if letter not in letters:
            letters[letter] = 0
        
        letters[letter] += 1
    for key, value in letters.items():
        print(f"{key} {"*"*value}")
    









if __name__ == "__main__":
    histogram("statistically")