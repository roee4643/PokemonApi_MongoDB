#!/bin/bash

# start_app.sh

# Run the script to create the DynamoDB database
python create_Mongo_DataBase.py

# Then start the main application
python PokemonMainApi2.py
