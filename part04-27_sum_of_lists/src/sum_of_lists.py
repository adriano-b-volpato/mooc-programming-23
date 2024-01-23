# Write your solution here

def list_sum(list_ints_1, list_ints_2):
    sum = []
    for i in range(len(list_ints_1)):
        
        sum.append((list_ints_1[i] + list_ints_2[i]))
    
    return sum
        
    
    
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]