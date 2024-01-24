def dict_of_numbers():
    tens_done = False
    teens_done = False
    spelled_numbers = {}
    ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    counter = 1
    counter2 = 1
    
    for i in range(100):
        
        if i == 0:
            spelled_numbers[i] = "zero"
            continue
        if 0 < i < 10:
            spelled_numbers[i] = ones[i-1]
            continue
            
        if i % 10 == 0:
            if tens_done == False:
                for x in range(1, 10):
                    spelled_numbers[x*10] = tens[x-1]
            tens_done = True
            continue
        if 10 < i <= 20:
            if teens_done == False:
                for t in range(1, 10):
                    spelled_numbers[t+10] = teens[t-1]
            teens_done = True
            continue
                
            
            continue
        else:
            if counter2 == 10:
                counter +=1
                counter2 = 1
            spelled_numbers[i] = (f"{tens[counter]}-{ones[counter2 -1]}")
            counter2 += 1
            continue
            
            
            
                
                
            
            
    return spelled_numbers
    
    
    
    
    
    
    
    
    

    



















if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])