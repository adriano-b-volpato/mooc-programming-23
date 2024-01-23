# Write your solution here


def longest(strings: list):
    lenght = 0
    longest = ""
    for string in strings:
        if longest == "" or len(string)>lenght:
            longest = string
            lenght = len(string)
    return longest
            
    






if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))