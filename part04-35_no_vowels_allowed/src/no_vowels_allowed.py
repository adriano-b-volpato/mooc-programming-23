# Write your solution here

def no_vowels(words):
    vowels = ["a", "e", "i", "o", "u"]
    vowelless = ""
    for i in range(len(words)):
        if words[i] in vowels:
            continue
        else:
            vowelless += words[i]
    return vowelless













if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
