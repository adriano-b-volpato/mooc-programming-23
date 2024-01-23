# Write your solution here

def everything_reversed(list_str):
    reversed_list = []
    for item in reversed(list_str):
        reversed_list.append(item[::-1])
    return reversed_list

    








if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
    