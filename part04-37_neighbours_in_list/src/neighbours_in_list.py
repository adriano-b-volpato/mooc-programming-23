# Write your solution here


# def longest_series_of_neighbours(list_int):
#    counter = 1
#    highest = 1
#    for i in range(len(list_int)-1):
       
#        if list_int[(i)] == (list_int[i+1]-1) or list_int[(i)] == (list_int[i+1]+1):
#            counter += 1
#            continue
#        if counter > highest:
#                highest = counter
#        if list_int[(i)] != (list_int[i+1]-1) and list_int[(i)] != (list_int[i+1]+1):
#            counter = 1   
    
           
#    return highest
           
def longest_series_of_neighbours(list_int):
    counter = 1
    highest = 1

    for i in range(len(list_int) - 1):
        if list_int[i + 1] == (list_int[i] - 1) or list_int[i + 1] == (list_int[i] + 1):
            counter += 1
        else:
            counter = 1

        if counter > highest:
            highest = counter

    # Check the last element
    if counter > highest:
        highest = counter  # This part was added to update the counter for the last element

    return highest
        
            
            
       
       
        
    
if __name__ == "__main__":
    my_list = [1, 2, 3, 5, 6, 9, 10]
    print(longest_series_of_neighbours(my_list))