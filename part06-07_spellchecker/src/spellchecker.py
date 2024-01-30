# write your solution here


text_input = input("Write text: ")
text_list = text_input.split()
feedback = ""
wordlist = []
misspelled = []


with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        wordlist.append(line.strip())
    

for index, word in enumerate(text_list):
    
    if word.lower() not in wordlist:
        misspelled.append(word)    
    
for word in text_list:
    if word in misspelled:
        feedback += f"*{word}* "
    else:
        feedback += f"{word} "
print(feedback)
   
### Part of the model solution

# for word in sentence.split(' '): ***** 

#     if word.lower() in words:

#         print(word + " ", end="")

#     else:

#         print("*" + word + "* ", end="")   
    
    
    
            
    
    
        
        
    