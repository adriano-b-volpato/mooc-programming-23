# Write your solution here

numbers = []



while True:
    print(f"The list is now {numbers}")
    action = input("a(d)d, (r)emove or e(x)it: ")
    if action == "d":
        if len(numbers) != 0:
            numbers.append((numbers[-1])+1)
            continue
        else:
            numbers.append(1)
        
    if action == "r":
        numbers.pop(-1)
    if action == "x":
        print("Bye!")
        break