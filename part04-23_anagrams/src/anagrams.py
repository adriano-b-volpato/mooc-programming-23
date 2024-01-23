# Write your solution here

def anagrams(word1, word2):
    ordered1 = sorted(word1)
    ordered2 = sorted(word2)
    
    if ordered1 == ordered2:
        return True
    else:
        return False
    
    







if __name__ == "__main__":
    print(anagrams("tame", "meta"))