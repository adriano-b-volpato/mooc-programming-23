# Copy here code of line function from previous exercise
def line(length, string):
    if string == "":
        print("*"*length)
    else:
        print(string[0]*length)

def triangle(size):
    # You should call function line here with proper parameters
    for i in range(size+1):
        line(i, "#")
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
