# Write your solution here


def create_tuple(x: int, y: int, z: int):
    
    temp = [x, y, z]
    sorted_temp = sorted(temp)
    temp = []
    temp.append(sorted_temp[0])
    temp.append(sorted_temp[1])
    temp.append(sorted_temp[2])
    temp.append(sorted_temp[0] + sorted_temp[1] + sorted_temp[2])
    coordinates = (temp[0], temp[2], temp[-1])
    return coordinates







if __name__ == "__main__":
    print(create_tuple(1, 4, 2))