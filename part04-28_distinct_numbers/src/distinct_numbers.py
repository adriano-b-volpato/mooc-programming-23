# Write your solution here
def distinct_numbers(list_of_ints):
    new_list = []
    for item in list_of_ints:
        if item in new_list:
            continue
        else:
            new_list.append(item)
    return sorted(new_list)
















if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]