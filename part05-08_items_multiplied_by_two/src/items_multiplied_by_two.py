# Write your solution here

def double_items(numbers: list):
    doubled_numbers = []
    for number in numbers:
        doubled_numbers.append(2*number)
    
    
    return doubled_numbers















if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
    