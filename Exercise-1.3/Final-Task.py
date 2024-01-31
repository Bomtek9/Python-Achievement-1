recipes_list = []
ingredients_list = []


def take_recipe():
    name = input("Enter the name of your recipe: ")
    cooking_time = int(input("Enter how many minutes it will take to complete: "))
    ingredients = input("Enter the list of ingredients, separated by commas: ").split(", ")

    # Call the function to take recipe input
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    
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

# Print Recipes List with Difficulty
for recipe in recipes_list:
   print('Recipe:', recipe['name'])
   print('Cooking time (min):', recipe['cooking_time'])
   print('Ingredients:')
   for ingredient in recipe['ingredients']:
      print(ingredient)
   print('Difficulty:', recipe['difficulty'])
    
def print_ingredients():
   ingredients_list.sort()
   print('All Ingredients')
   print('_______________')
   for ingredient in ingredients_list:
     print(ingredient)

print_ingredients()
