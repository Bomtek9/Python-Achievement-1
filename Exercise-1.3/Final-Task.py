recipes_list = []
ingredients_list = []


def take_recipe():
        name = input("Enter the name of your recipe: ")
        cooking_time = int(input("Enter how many minutes it will take to complete: "))
        ingredients = input("Enter the list of ingredients, separated by commas: ").split(", ")

        # Call the function to take recipe input
        recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
        return recipe



n = input(int("How many more recipes do you want to add? "))

# Run a for loop to take n recipes
for _ in range(n):

    # Run take_recipe() and store its return output in a variable called recipe
    recipe_data = take_recipe()

    # Access the recipe information using the dictionary keys
    print("Recipe Name:", recipe_data['name'])
    print("Cooking Time:", recipe_data['cooking_time'])
    print("Ingredients:", recipe_data['ingredients'])

    # Run another loop to check and add new ingredients to ingredients_list
    for ingredient in recipe_data['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

# Print the final ingredients list
print("Ingredients List:", ingredients_list)

for recipe in recipes_list:
    cooking_time = recipe["cooking_time"]
    num_ingredients = len(recipe["ingredients"])

    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"

        recipe["difficulty"] = difficulty
        
        print("Recipes List with Difficulty:")
        
    for recipe in recipes_list:
        print(recipe)
