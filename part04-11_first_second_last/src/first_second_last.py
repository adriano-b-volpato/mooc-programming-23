# Write your solution here
def first_word(sentence):
    for i in range(len(sentence)):
        if sentence[i] == " ":
            return(sentence[0:i])
            
    
    
def second_word(sentence):
    x = len(first_word(sentence))
    for i in range(len(sentence)):
        if i == (len(sentence)-1):
                return(sentence[x+1:i+1])
        if sentence[i] == " " and i > x:
            return(sentence[x+1:i])
    
def last_word(sentence):
    for (i) in reversed(range(len(sentence))):
        if sentence[i] == " ":
            return(sentence[i+1:])
    
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "it was a good day"
    print(second_word(sentence))
    print(last_word(sentence))