# Write your solution here
# recipe list
# Separate the different recipes by " "
# Make sure the recipes are lists
# Add the recipes to the recipe list


def read_file(filename :str):
    recipes = []
    parts = []
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            parts.append(line)
        
        for item in parts:
            recipe = []
            if item == "" or item == " ":
                recipes.append(recipe)
                continue
            recipe.append(item)
        recipes.append(recipe)
                
    print(recipes)
        
        
read_file("recipes1.txt")            
            
            
            
            
            
            
            
            
            
    # recipes = []
    # with open(filename) as new_file:
    #     parts = ""
    #     for line in new_file:
    #         line = line.replace("\n", "")
    #         parts += line + " "
    #         recipe_list = parts.split("  ")
        
    #     for item in recipe_list:
            
    #         recipes.append(item.split())
    # return recipes
    


    
def search_by_name(filename: str, word: str):
    recipes = read_file(filename)
    print(recipes)
    recipes_found = []
    for recipe in recipes:
        if word.lower() in recipe[0].lower():
            recipes_found.append(recipe[0])
    
    return recipes_found
    
            


#print(search_by_name("recipes1.txt", "Cake"))
    

      
# if type(recipe_list[1]) != int:
            #     recipe_list[0] += recipe_list.pop(1)
        
