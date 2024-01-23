# Write your solution here

def shortest(list_of_str):
    short = 100000
    index = 0
    for i in range(len(list_of_str)):
        if len(list_of_str[i]) < short:
            short = len(list_of_str[i])
            index = i
    
    return list_of_str[index]
# def shortest(names: list): MUCH BETTEr

#     result = ""
#     for nimi in names:
#         if result == "" or len(nimi) < len(result):
#             result = nimi
#     return result












if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "hedy", "richard", "tim"]

    result = shortest(my_list)
    print(result)