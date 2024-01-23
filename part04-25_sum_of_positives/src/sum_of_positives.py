# Write your solution here

def sum_of_positives(list_of_ints):
    sum = 0
    for i in list_of_ints:
        if i > 0:
            sum += i
    return sum     
        











if __name__ == "__main__":
        my_list = [1, -2, 3, -4, 5]
        result = sum_of_positives(my_list)
        print("The result is", result)



    