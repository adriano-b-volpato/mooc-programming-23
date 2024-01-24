# Write your solution here

def factorials(n: int):
    factorial_dictionary = {}
    
    for number in range(1, n+1):
        factorial = number
        for i in range(number-1, 1, -1):
            factorial *= i
        
        factorial_dictionary[number] = factorial
        
        
            
    return factorial_dictionary
        
        