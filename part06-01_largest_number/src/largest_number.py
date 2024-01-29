# write your solution here

def largest():
    with open("numbers.txt") as numbers_file:
        largest_number = 0
        for line in numbers_file:
            line = line.replace("\n", "")
            number = int(line)
                                    
            if number > largest_number:
                largest_number = number
                
    return largest_number


