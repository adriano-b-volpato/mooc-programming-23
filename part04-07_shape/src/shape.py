# Copy here code of line function from previous exercise and use it in your solution
def line(length, string):
    if string == "":
        print("*"*length)
    else:
        print(string[0]*length)
        
def shape(width, character1, height, character2):
    # You should call function line here with proper parameters
    for i in range(width+1):
            line(i, character1)
    x = 0
    while x < height:
        line(width, character2)
        x+=1
        
        
        
    
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")