# Write your solution here
phone_book = {}


while True:
    action = int(input("command (1 search, 2 add, 3 quit): "))
    if action == 1:
        name = input("name: ")
        if name not in phone_book:
            print("no number")
            continue
        print(phone_book[name])
        
        
        
    if action == 2:
        name = input("name: ")
        phone = input("number: ")
        phone_book[name] = phone
        print("ok!")
        
        
        
    if action == 3:
        print("quitting...")
        break
    
    
