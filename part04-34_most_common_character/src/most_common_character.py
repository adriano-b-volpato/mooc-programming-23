# Write your solution here

def most_common_character(characters):
    counter = 0
    highest = ""
    for i in range(len(characters)):
        if characters.count(characters[i]) > counter:
            counter = characters.count(characters[i])
            highest = characters[i]
    return highest
        











if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
    