# write your solution here

def form_matrix():
    matrix = []
    with open("matrix.txt") as matrix_file:
        for line in matrix_file:
            line = (line.replace("\n", ""))
            line = line.split(",")
            row = []
            for number in line:
                row.append(int(number))
            matrix.append(row)
    return matrix



def matrix_sum():
    matrix = form_matrix()
    sum = 0
    for row in matrix:
        for number in row:
            sum += number
            
    return sum
        
        

    
def matrix_max():
    matrix = form_matrix()
    biggest = 0
    for row in matrix:
        for number in row:
            if number > biggest:
                biggest = number
    return biggest            
    
    

def row_sums():
    matrix = form_matrix()
    sums = []
    
    for row in matrix:
        sum = 0
        for number in row:
            sum += number
        sums.append(sum)
    return sums










if __name__ == "__main__":
    
    
    print(row_sums())
   #print(form_matrix())
   #print(matrix_sum())
   #print(matrix_max())