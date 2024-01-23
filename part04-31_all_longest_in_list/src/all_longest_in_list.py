# Write your solution here

def all_the_longest(list_str):
    longest = ""
    new_list = []
    
    for item in list_str:
        if longest == "" or len(item) > len(new_list[0]):
            new_list = []
            new_list.append(item)
            longest = len(item)
            continue
            
        if len(item) == len(new_list[0]):
            new_list.append(item)
    return new_list
        
    # def all_the_longest(names: list):

    # result = []

 

    # for name in names:

    #     if result == [] or len(name) > len(result[0]):

    #         result = [name]

    #     elif len(name) == len(result[0]):

    #         result.append(name)

 

    # return result
    












if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']