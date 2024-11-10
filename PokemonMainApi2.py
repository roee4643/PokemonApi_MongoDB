import requests
import random
import json
import os
from Pokemon_GetApi_Class import GetApi  # Import the GetApi class from pokemon_api.py
from Pokemon_Utilities_Class import Utilities  # Import the Utilities class        
from pymongo import MongoClient

# Main function
def main():
    # Define class variables
    get_api = GetApi()
    utilities = Utilities()

    # Create break flag
    flag = 0
    # Get Pokémon names list by API and store in pokemon_list
    pokemon_list = get_api.pokemon_list()  # Get Pokémon list

    print("----Welcome to the Pokémon generator!-----")
    while flag == 0:
        print("\n")
        print("-----------------------------------")
        ans = input("Do you want to generate a new Pokémon? (y/n): ")
        if ans == 'y':
            random_pokemon = get_api.Get_random_pokemon(pokemon_list)  # Get random Pokémon from the Pokémon list
            in_data_base = utilities.is_in_data_base(random_pokemon)  # Check if the random Pokémon is already in the database. If True, it will print the details with the relevant message

            if in_data_base == False:  # If the random Pokémon is not already in the database, do the next steps 
                Name, Height, Weight = get_api.get_pokemon_details(random_pokemon)  # Get Pokémon details info

                utilities.display(Name, Height, Weight)  # Display Pokémon details info
                utilities.insert_pokemon(Name, Height, Weight)  # Store the Pokémon details in MongoDB database

        elif ans == 'n':
            print("See you next time :)")
            flag = 1

# Call the main function
if __name__ == "__main__":
    main()
