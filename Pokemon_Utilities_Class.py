# pokemon_utilities.py

from pymongo import MongoClient

class Utilities:
    def __init__(self, filename='PokemonDB.json'):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["mydatabase"]  # Specify the database
        self.collection = self.db["Pokemon"]

    def insert_pokemon(self, pokemon_name, weight, height):
        pokemon = {
        "PokemonName": pokemon_name,
        "Weight": weight,
        "Height": height
        }
          # Specify the collection

        result = self.collection.insert_one(pokemon)
        
    
    def display(self, name, height, weight):
        print(f"The pokemon is: {name}\nweights: {weight}\nheights is: {height}")
        if not name or not height or not weight:
            print("Error: Missing Pokémon details.")
    
    def is_in_data_base(self, pokemon_name):
        query = {"PokemonName": pokemon_name}
        existing_pokemon = self.collection.find_one(query)

        if existing_pokemon:
            print("Pokémon already exists:", existing_pokemon)    
            return True
        else:
            return False
