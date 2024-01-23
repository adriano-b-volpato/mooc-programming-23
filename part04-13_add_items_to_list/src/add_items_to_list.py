# Write your solution here

numbers = []

howMany = int(input("How many items:"))
i = 1
while i <= howMany:
    item = int(input(f"Item {i}: "))
    numbers.append(item)
    i += 1
    
print(numbers)