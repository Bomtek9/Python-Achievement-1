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