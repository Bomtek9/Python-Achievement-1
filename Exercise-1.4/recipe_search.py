import pickle

def display_recipe(recipe):
    print("\nRecipe Details:")
    print("--------------")
    print(f"Recipe Name: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f" - {ingredient}")
    print(f"Difficulty: {recipe['difficulty']}")

def search_ingredient(data):
    all_ingredients = data['all_ingredients']
    
    print("\nAvailable Ingredients:")
    print("----------------------")
    for index, ingredient in enumerate(all_ingredients):
        print(f"{index + 1}. {ingredient}")

    try:
        selected_index = int(input("\nEnter the number corresponding to the ingredient you want to search: ")) - 1
        ingredient_searched = all_ingredients[selected_index]
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")
        return

    print(f"\nRecipes containing {ingredient_searched}:")
    print("-------------------------------------")
    ingredient_found = False
    for recipe in data['recipes_list']:
        if ingredient_searched in recipe['ingredients']:
            display_recipe(recipe)
            ingredient_found = True

    if not ingredient_found:
        print(f"No recipes found containing {ingredient_searched}.")

def main():
    filename = input("Enter the filename containing recipe data: ")

    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    search_ingredient(data)

if __name__ == "__main__":
    main()
    