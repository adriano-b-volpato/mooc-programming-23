# Write your solution here

input_layers = 3 #int(input("Layers: "))
length = (input_layers*2) - 1
height = length 

letters = []

for i in range(65, 91):
    letters.append(chr(i))

layers = []
for i in range(input_layers):
    layers.append(letters[i])

layers.reverse()
outer_layer = layers[0]
#print(outer_layer*length)
    
#for h in range(height):
    
    # row = (f"{outer_layer}")
    # for l in range(1, length-2):
    #     row += (f"{layers[l]}")
    # row += (f"{outer_layer}")
    # print(row)
# row = (f"{outer_layer}")
    
        
        
     
# row += (f"{outer_layer}")
    
letter = 0
layer = 0

row = ""
# letters[0] * layers
# letters[1] * layers-2
# letters[1] * layers-3 + letters[2] + letters[1] * layers-3
# letters[1] * layers-2
# if letter != 0:
#   (f"{letter[0]})

print(row)  
    
    
    
    



# first row = lenght * letter[layers]
# second row = letter[layers] + (lenght-1) * letter[layers-1] + letter[layers]
# third row = letter[layers] + letter[layers-1] + (lenght-2) * letter[layers-2] + letter[layers-1] + letter[layers]
# fourth row = = lenght * letter[layers]

# CCCCC
# CBBBC
# CBABC
# CBBBC
# CCCCC


    







