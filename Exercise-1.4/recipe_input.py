import pickle

recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("What is the name of your recipe? ")
    cooking_time = int(input("How many minutes does it take to make your recipe? "))
    ingredients = input("List the ingredients, separated by commas: ").split(", ")
    
    recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients}
    
    return recipe

def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        return 'Easy'
    elif cooking_time < 10 and num_ingredients >= 4:
        return 'Medium'
    elif cooking_time >= 10 and num_ingredients < 4:
        return 'Intermediate'
    elif cooking_time >= 10 and num_ingredients >= 4:
        return 'Hard'

n = int(input("How many more recipes do you want to add? "))

for i in range(n):
    recipe = take_recipe()
    
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    
    cooking_time = recipe['cooking_time']
    num_ingredients = len(recipe['ingredients'])
    difficulty = calc_difficulty(cooking_time, num_ingredients)
    recipe['difficulty'] = difficulty
    
    recipes_list.append(recipe)

# Print All Ingredients in Alphabetical Order
ingredients_list.sort()
print("All Ingredients in Alphabetical Order:")
for ingredient in ingredients_list:
    print(f"- {ingredient}")

# Print Recipes List with Difficulty
print("\nRecipes List with Difficulty:")
for recipe in recipes_list:
    print("Recipe Name:", recipe['name'])
    print("Cooking Time:", recipe['cooking_time'])
    print("Ingredients:", recipe['ingredients'])
    print("Difficulty:", recipe['difficulty'])
    print("\n")

# Save Recipes List and Ingredients List to Binary File
data = {'recipes_list': recipes_list, 'all_ingredients': ingredients_list}
filename = input("Enter the filename for the binary file: ")

try:
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
        print(f"\nData has been saved to {filename}")
except FileNotFoundError:
    print("File not found. Failed to save data.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Script execution complete.")
    