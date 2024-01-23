# Write your solution here


# Write your solution here

# Write your solution here



def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    block = []
    
    for row in range(row_no, (row_no+3)):
        for column in range(column_no, (column_no+3)):
            block.append(sudoku[row][column])
    for number in block:
        if block.count(number) > 1 and number != 0:
            return False
    return True
        
        
    # column = []
    # for row in range(len(sudoku)):
    #     column.append(sudoku[row][column_no])
    # for number in column:
    #     if column.count(number) > 1 and number != 0:
    #         return False
    # return True
        

    
    # for item in sudoku[column_no]:
    #     if item in numbers:
    #         x = sudoku[column_no].count(item)
    #         print(x)
    #         if  x > 1:
    #             return False
            













if __name__ == "__main__":
    
   sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]
   print(block_correct(sudoku, 0, 0))
   print(block_correct(sudoku, 1, 2))