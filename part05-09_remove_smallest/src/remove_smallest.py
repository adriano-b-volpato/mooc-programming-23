# Write your solution here


# Write your solution here

def remove_smallest(numbers: list):
    smallest = min(numbers)
    index = numbers.index(smallest)
    numbers.pop(index)
    # numbers.remove instead
    
    















if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
    