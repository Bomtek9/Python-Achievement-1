# Recipe App (Command Line Version)

## Objective

Build the command line version of a Recipe app as a precursor to its web app counterpart in Achievement 2. This project focuses on learning Python fundamentals, data structures, and object-oriented programming, preparing you for Django web framework development.

## Context

The project involves building a command line application in Python for managing recipes, including features like creating, reading, modifying, and searching for recipes based on ingredients. It serves as a demonstration of Python scripting skills and understanding of fundamental programming concepts.

## The 5 W’s

1. **Who:** My professional network and potential employers interested in my Python skills.
2. **What:** Command line application for a Recipe app with CRUD operations and ingredient-based searching.
3. **When:** Code available on GitHub, requiring a local Python 3.6+ installation for easy access by recruiters.
4. **Where:** Run on any machine with Python installed. Host the code on GitHub or my portfolio site.
5. **Why:** Showcase my Python skills and potential to work with web application frameworks like Django.

## User Goals

- Create and modify recipes with ingredients, cooking time, and auto-calculated difficulty.
- Search for recipes by ingredients.

## Key Features

- CRUD operations for user recipes stored in a locally hosted MySQL database.
- Ingredient-based recipe search.
- Automatic difficulty rating for recipes.
- Detailed recipe display including ingredients, cooking time, and difficulty.

## Technical Requirements

- Handle common exceptions and errors with user-friendly messages.
- Connect to a locally hosted MySQL database.
- Provide an easy-to-use interface with simple forms and concise instructions.
- Compatible with Python 3.6+.
- Well-formatted code following standardized guidelines.
- Include concise comments illustrating the program flow.

## Getting Started

1. Install Python 3.6 or higher.
2. Clone the repository.
3. Set up a local MySQL database.
4. Install required dependencies.
5. Run the application.

## Usage

- Follow on-screen instructions to manage recipes.
- Use the search option to find recipes based on ingredients.

## Contributions

No totallly sure why you would want to contribute but have at it! Feel free to open an issue or submit a pull request.

## Developer Decisions

- Exercise 1.2:
  Name (str): Contains the name of the recipe
  Cooking Time (int): Contains the cooking time in minutes
  Ingredients (list): Contains a number of ingredients, each of the str data type

  I used dictionaries for storing the above data for each recipe because of the different data types needing to be stored and the flexibility of dictionaries. Dictionaries can store the recipe names as strings, the ingredients as lists, and the cooking time as integers. Which I may switch the intgere to float given some ingredients may require 1.5 teaspoons for example.

- all_recipes = [ ]

  I decided to use a list as the outer structure to store the recipe dictionaries because lists are sequential and can store multiple recipes that can be modified if needed.
