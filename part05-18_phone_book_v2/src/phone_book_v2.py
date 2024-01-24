# Write your solution here


phone_book = {"Adriano": [1166831828, 1166930174]}


while True:
    action = int(input("command (1 search, 2 add, 3 quit): "))
    if action == 1:
        name = input("name: ")
        if name not in phone_book:
            print("no number")
            continue
        for phone in phone_book[name]:
            print(phone)
        
        
        
        
    if action == 2:
        name = input("name: ")
        phone = input("number: ")
        if name not in phone_book:
            phone_book[name] = []
        phone_book[name].append(phone)
        print("ok!")
        
        
        
    if action == 3:
        print("quitting...")
        break
    
    
