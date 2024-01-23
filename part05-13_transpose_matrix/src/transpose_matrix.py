# Write your solution here

def transpose(matrix: list):
    i = 0
    transposed_matrix = []
    for row in matrix:
        transposed_matrix.append(row[:])
    
    for row in range(len(transposed_matrix)):
        for column in range(len(transposed_matrix)):
            transposed_matrix[row][column] = matrix[column][row]
    for row in range(len(matrix)):
        matrix[row] = transposed_matrix[row]
            
            
        
















if __name__ == "__main__":
    matrix = [[1, 2, 3],[4,5,6],[7,8,9]]
    print(matrix)
    transpose(matrix)
    print(matrix)
    