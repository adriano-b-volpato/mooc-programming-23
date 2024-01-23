# Write your solution here

words = []
i = 0

while True:
    word = input("Word: ")
    if i > 0 and word in words:
        print(f"You typed in {i} different words")
        break
    words.append(word)
    
    i += 1
    