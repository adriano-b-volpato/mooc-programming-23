# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(word):     
        reverseword = ""
        for i in range(len(word), 0, -1):
            reverseword += word[i-1] 
        if word == reverseword:
            return True
        else:
            return False
        
            
while True:
    word = input("Please type in a palindrome: ")
    palindrome = palindromes(word)
    if palindrome == True:
        print(f"{word} is a palindrome!")
        break
    if palindrome == False:
        print("that wasn't a palindrome")
    
               
    
        
    
    


#if __name__ == "__main__":
    #palindromes("abba")
