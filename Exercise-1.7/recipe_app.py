from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql.expression import or_

# Database Configuration: Set up connection parameters for the MySQL database.
USERNAME = "cf-python"
PASSWORD = "password"
HOST = "localhost"
DATABASE = "task_database"

# SQLAlchemy Engine: Create the engine to manage connections to the database.
engine = create_engine(f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}")

# Base Class: All model classes will inherit from this class.
Base = declarative_base()

# Session: Set up the mechanism to talk to the database. 
# The session will be used to query and commit transactions.
Session = sessionmaker(bind=engine)
session = Session()

class Recipe(Base):
    # Table Name: Define the name of the table in the database.
    __tablename__ = "final_recipes"

    # Schema:
    #|-----------------------------------------------------------------------------------|
    #| Field        | Type         | Null     | Key         | Default   | Extra          |
    #|--------------|--------------|----------|-------------|-----------|----------------|
    #| id           | int          | NOT NULL | PRIMARY KEY | NULL      | AUTO_INCREMENT |
    #| name         | varchar(50)  | NULLABLE |             | NULL      |                |
    #| ingredients  | varchar(255) | NULLABLE |             | NULL      |                |
    #| cooking_time | int          | NULLABLE |             | NULL      |                |
    #| difficulty   | varchar(20)  | NULLABLE |             | NULL      |                |
    #|-----------------------------------------------------------------------------------|

    # Columns: Define the structure of the table.
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        # Representation: Used for debugging purposes, showing a quick string representation of the object.
        return f"<Recipe(id={self.id}, name={self.name}, difficulty={self.difficulty})>"
    
    def __str__(self):
        # String Representation: Formats recipe details in a user-friendly way for printing.
        ingredients_list = self.ingredients.split(", ")
        formatted_ingredients = "\n ".join(f"  - {ingredient.title()}" for ingredient in ingredients_list)

        return (f"Recipe ID: {self.id}\n"
                f"  Name: {self.name.title()}\n"
                f"  Ingredients:\n {formatted_ingredients}\n"
                f"  Cooking Time: {self.cooking_time} minutes\n"
                f"  Difficulty: {self.difficulty}\n")