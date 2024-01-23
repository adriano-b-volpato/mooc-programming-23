# Write your solution here
def no_shouting(list_str):
    no_upper_list = []
    for item in list_str:
        if item.isupper() == False:
            no_upper_list.append(item)
        # if not string.isupper():
        #     without_upper.append(string)

            
    return no_upper_list
            














if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)