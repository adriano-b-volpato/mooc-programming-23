# Write your solution here

def row_correct(sudoku: list, row_no: int):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for item in sudoku[row_no]:
        if item in numbers:
            x = sudoku[row_no].count(item)
            if  x > 1:
                return False
    return True

def column_correct(sudoku: list, column_no: int):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    column = []
    for row in range(len(sudoku)):
        column.append(sudoku[row][column_no])
    for number in column:
        if column.count(number) > 1 and number != 0:
            return False
    return True

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


def sudoku_grid_correct(sudoku: list):
    indexes = [[0, 0], [0,3],[0, 6], [3,0],[3,3], [3,6],[6, 0], [6, 3],[6, 6]]
    for row in range(len(sudoku)-1):
        if row_correct(sudoku, row) == False:
            return False
    for column in range(len(sudoku)-1):
        if column_correct(sudoku, column) == False:
            return False
    for index in indexes:
        if block_correct(sudoku, index[0], index[1]) == False:
            return False
    return True
    
    
    
def print_sudoku(sudoku: list):
    for row in range(len(sudoku)):
        if row == 3 or row == 6:
                print("")
        for number in range(len(sudoku)):
            if number == 3 or number == 6:
                print(" ", end="")
                
            if sudoku[row][number] == 0:
                print("_", end=" ")
                continue
            
            print(sudoku[row][number],end=" ")
        print(" ")
        
 
 
 
 
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number
      









if __name__ == "__main__":
    sudoku  = [
    [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
    [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
    [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
    [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
    [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
    [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
    [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],]
    # add_number(sudoku, 0, 0, 2)
    # add_number(sudoku, 1, 2, 7)
    # add_number(sudoku, 5, 7, 3)
    print_sudoku(sudoku)
    
    # print()
    # print("Three numbers added:")
    # print()
    # print_sudoku(sudoku)
    
    


