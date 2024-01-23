# Copy here code of line function from previous exercise
def line(length, string):
    if string == "":
        print("*"*length)
    else:
        print(string[0]*length)

def square(size, character):
    # You should call function line here with proper parameters
    for i in range(size):
        line(size, character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")
    
    
    