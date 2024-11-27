from flask import Flask, jsonify
from Pokemon_Utilities_Class import Utilities
from Pokemon_GetApi_Class import GetApi  # Import your script

app = Flask(__name__)
pokemon_mongo = Utilities("54.149.108.64") # Instantiate my Utilitites class
pokemon_api = GetApi()  # Instantiate my GetApi class


@app.route('/pokemon/random', methods=['PUT'])
def put_pokemon_details():
    """Endpoint to insert a random Pokémon's details into the database."""
    pokemon_list = pokemon_api.pokemon_list()
    if not pokemon_list:
        return jsonify({"error": "Failed to retrieve Pokémon list"}), 500

    random_pokemon = pokemon_api.Get_random_pokemon(pokemon_list)
    name, height, weight = pokemon_api.get_pokemon_details(random_pokemon)

    if not name:
        return jsonify({"error": "Failed to retrieve Pokémon details"}), 500

    result = pokemon_mongo.insert_pokemon(name, height, weight)
    return jsonify(result), 201
    



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
