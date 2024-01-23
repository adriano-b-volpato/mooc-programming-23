# Write your solution here


def spruce(size): 
    spaces = size - 1
    asterisks = 1
    print("a spruce!")
    
    
    for i in range(size):
        print(" " * spaces + "*" * asterisks + " " * spaces)
        spaces -= 1
        asterisks += 2
    
    print(" " * (size - 1) + "*" + " " * (size - 1))
        
        
        
    
    
    



# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)