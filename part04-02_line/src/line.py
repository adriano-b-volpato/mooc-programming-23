# Write your solution here
# You can test your function by calling it within the following block
def line(length, string):
    if string == "":
        print("*"*length)
    else:
        print(string[0]*length)
        
        
if __name__ == "__main__":
    line(5, "x")
    