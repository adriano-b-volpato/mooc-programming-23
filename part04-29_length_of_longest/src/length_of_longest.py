# Write your solution here

def length_of_longest(list_of_str):
    longest = 0
    for item in list_of_str:
        if len(item) > longest:
            longest = len(item)
    return longest













if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)