recipes_list = []
ingredients_list = []


def take_recipe():
        name = input("Enter the name of your recipe: ")
        cooking_time = int(input("Enter how many minutes it will take to complete: "))
        ingredients = input("Enter the list of ingredients, separated by commas: ").split(", ")

        # Call the function to take recipe input
        recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
        return recipe

recipe_data = take_recipe()

# Access the recipe information using the dictionary keys
print("Recipe Name:", recipe_data['name'])
print("Cooking Time:", recipe_data['cooking_time'])
print("Ingredients:", recipe_data['ingredients'])

n = input(int("How many more recipes do you want to add? "))

