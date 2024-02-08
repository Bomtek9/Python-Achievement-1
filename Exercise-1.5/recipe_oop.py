class Recipe:
    all_ingredients = set()  # Class variable to store all ingredients across all recipes

    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []  # Initialize ingredients as an empty list
        self.cooking_time = cooking_time
        self.difficulty = None  # Initialize difficulty as None initially

    def add_ingredients(self, ingredients):
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