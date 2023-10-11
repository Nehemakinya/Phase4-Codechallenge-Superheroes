## Superheroes
**Description:**
This is a Flask application that provides an API for managing superheroes, their superpowers, and the relationships between heroes and powers. You can use this API to retrieve a list of heroes, powers, update power descriptions, and create associations between heroes and powers.

# Table of Contents
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Seed Data](#seed-data)
- [Running the Application](#running-the-application)


# Requirements
Make sure you have the following requirements installed:

- Python (3.6 or higher)
- Flask (>=1.1.2)
- Flask-SQLAlchemy (>=2.5.1)
- Flask-Migrate (>=2.9.1) - for database migrations
- SQLite (should come pre-installed with Python)

You can install these packages using `pip`. 

# Getting Started
1. Clone this repository to your local machine:

git clone https://github.com/Nehemakinya/Phase4-Codechallenge-Superheroes

2. Navigate to the project directory:

cd Phase4-Codechallenge-Superheroes

3. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

4. Install the required dependencies:

pipenv install

5. Configure the database URI in the app.py file:

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Superheroes.db' 

6. Initialize the database and apply migrations:

flask db init
flask db migrate
flask db upgrade

# API Endpoints
GET /heroes: Get a list of hero IDs.
GET /powers: Get a list of powers with their descriptions.
PATCH /powers/<int:id>: Update the description of a specific power.
POST /hero_powers: Create a relationship between a hero and a power.


# Seed Data
To seed the database with initial data, you can run the provided seed_data() function. This function creates sample hero and power records and establishes associations between them using the HeroPower model.

**if __name__ == '__main__':**
    **with app.app_context():**
        **db.create_all()**
        **seed_data()**


# Data Seeding
To populate the database with initial data, you use the seed.py script. Run it as follows:

python seed.py


# Running the Application
To run the application, execute the following command:

python app.py

The application will start on port 5555 by default. You can access the API using a tool like curl or a web client of your choice.


# Acknowledgments
This project was created as a simple example of building a RESTful API with Flask and SQLAlchemy.

# License
This project is licensed under the MIT License.

# Author 
Nehema Kinya.
