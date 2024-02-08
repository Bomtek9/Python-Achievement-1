class Recipe:
    all_ingredients = set()  # Class variable to store all ingredients across all recipes

    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []  # Initialize ingredients as an empty list
        self.cooking_time = cooking_time
        self.difficulty = None  # Initialize difficulty as None initially

    def add_ingredients(self, *ingredients):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)
            self.update_all_ingredients()  # Update all_ingredients after adding each ingredient

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def calculate_difficulty(self):
        num_ingredients = len(self.ingredients)
        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = 'Easy'
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = 'Medium'
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = 'Intermediate'
        elif self.cooking_time >= 10 and num_ingredients >= 4:
            self.difficulty = 'Hard'

    def get_difficulty(self):
        if not self.difficulty:  # If difficulty hasn't been calculated, calculate it first
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        Recipe.all_ingredients.update(self.ingredients)

    def __str__(self):
        return f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}\nCooking Time: {self.cooking_time} minutes\nDifficulty: {self.get_difficulty()}"
    
    def recipe_search(data, search_term):
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)
                

# Main code

# Creating instances of the Recipe class and adding ingredients
tea = Recipe("Tea", 5)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
print(tea)

coffee = Recipe("Coffee", 5)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
print(coffee)

cake = Recipe("Cake", 50)
cake.add_ingredients(
    "Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"
)
print(cake)

banana_smoothie = Recipe("Banana Smoothie", 5)
banana_smoothie.add_ingredients(
    "Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"
)
print(banana_smoothie)

# Creating a list of recipes
recipes_list = [tea, coffee, cake, banana_smoothie]

# Using recipe_search function to find recipes containing specific ingredients
print("\nRecipes containing Water:")
Recipe.recipe_search(recipes_list, "Water")

print("\nRecipes containing Sugar:")
Recipe.recipe_search(recipes_list, "Sugar")

print("\nRecipes containing Bananas:")
Recipe.recipe_search(recipes_list, "Bananas")