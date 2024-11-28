from flask import Flask, jsonify
from Pokemon_GetApi_Class import GetApi  # Import your script


app = Flask(__name__)
pokemon_api = GetApi()  # Instantiate my GetApi class


@app.route('/pokemon_list', methods=['GET'])
def get_pokemon_list():
    """Endpoint to fetch the list of Pokémon."""
    pokemon_list = pokemon_api.pokemon_list()
    if pokemon_list:
        return jsonify(pokemon_list), 200
    else:
        return jsonify({"error": "Failed to retrieve Pokémon list"}), 500

@app.route('/pokemon/random', methods=['GET'])
def get_random_pokemon_details():
    """Endpoint to fetch a random Pokémon with details."""
    pokemon_list = pokemon_api.pokemon_list()
    if not pokemon_list:
        return jsonify({"error": "Failed to retrieve Pokémon list"}), 500

    random_pokemon = pokemon_api.Get_random_pokemon(pokemon_list)
    name, height, weight = pokemon_api.get_pokemon_details(random_pokemon)

    if name:
        return jsonify({
            "name": name,
            "height": height,
            "weight": weight
        }), 200
    else:
        return jsonify({"error": "Failed to retrieve Pokémon details"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
