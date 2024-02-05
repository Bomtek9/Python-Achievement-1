import pickle

recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("What is the name of your recipe? ")
    cooking_time = int(input("How many minutes does it take to make your recipe? "))
    ingredients = input("List the ingredients, serparated by commas: ").split(", ")
    
    recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients }
    
    return recipe

n = int(input("How many more recipes do you want to add? "))


for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)
        recipes_list.append(recipe)

# Determine Recipe Difficulty and Add to recipes_list
for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
      recipe['difficulty'] = 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
      recipe['difficulty'] = 'Medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
      recipe['difficulty'] = 'Intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
      recipe['difficulty'] = 'Hard'
    
    def print_ingredients():
        ingredients_list.sort()
        print('All Ingredients')
        print('_______________')
    for ingredient in ingredients_list:
     print(ingredient)

    print_ingredients()
    
    recipe = {
    'name': (recipe.name),
    'cooking_time' : (recipe.cooking_time),
    'ingredients' : (recipe.ingredients),
    'difficulty': (recipe.difficulty)
}

my_file = open('recipedetails.bin', 'wb')
pickle.dump(recipe, my_file)
my_file.close()