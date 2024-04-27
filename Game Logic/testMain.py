#main.py

import sqlite3
import os
from pokemon import Pokemon
from Items import Items
from pokeball import Pokeballs

#Save the route for the database file in 'file'
file = "pokemongame.db"

#If db file exists, don't open
if not os.path.exists(file):
    #Connect to sqlite database
    conn = sqlite3.connect("pokemongame.db")

    #Create an obj to interact with db file
    cursor = conn.cursor()

    #Create a table for Pokémon
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY,
            name STRING,
            type1 STRING,
            type2 STRING,
            ability1 STRING,
            ability2 STRING,
            ability3 STRING,
            hp INTEGER,
            attack INTEGER,
            defense INTEGER,
            specAttack INTEGER,
            specDefense INTEGER,
            speed INTEGER
        )
    ''')

    #Create a table for Items
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name STRING,
            description STRING
        )
    ''')
    
    #Create a table for Poké Balls
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pokeballs (
            id INTEGER PRIMARY KEY,
            name STRING,
            description STRING,
            catchRateG INTEGER,
            catchRateY INTEGER,
            catchRateR INTEGER
        )
    ''')
    
    #The data of Pokemon for the database
    pokemon_data = [
        (1, "Bulbasaur", "Grass", "Poison", "Overgrow", "Chlorophyll", None, 45, 49, 49, 65, 65, 45),
        (2, "Ivysaur", "Grass", "Poison", "Overgrow", "Chlorophyll", None, 60, 62, 63, 80, 80, 60),
        (3, "Venusaur", "Grass", "Poison", "Overgrow", "Chlorophyll", None, 80, 82, 83, 100, 100, 80),
        (4, "Charmander", "Fire", None, "Blaze", "Solar Power", None, 39, 52, 43, 60, 50, 65),
        (5, "Charmeleon", "Fire", None, "Blaze", "Solar Power", None, 58, 64, 58, 80, 65, 80),
        (6, "Charizard", "Fire", "Flying", "Blaze", "Solar Power", None, 78, 84, 78, 109, 85, 100),
        (7, "Squirtle", "Water", None, "Torrent", "Rain Dash", None, 44, 48, 65, 50, 64, 43),
        (8, "Wartortle", "Water", None, "Torrent", "Rain Dash", None, 59, 63, 80, 65, 80, 58),
        (9, "Blastoise", "Water", None, "Torrent", "Rain Dash", None, 79, 83, 100, 85, 105, 78)
    ]

    #The data of items for the database
    item_data = [
        (1, "Potion", "Heals 20 HP!"),
        (2, "Super Potion", "Heals 50 HP!"),
        (3, "Hyper Potion", "Heals 200 HP!"),
        (4, "Max Potion", "Heals to Max HP!"),
        (5, "Full Restore", "Heals to Max HP and cures non-volatile status effects and confusion!"),
        (6, "Ether", "Restores 10 PP for one of a Pokémon's moves!"),
        (7, "Max Ether", "Fully restores PP for one of a Pokémon's moves!"),
        (8, "Elixir", "Restores 10 PP for all of a Pokémon's moves!"),
        (9, "Max Elixir", "Fully restores PP for all of a Pokémon's moves!")
    ]
    
    #The data of pokeballs for the database
    pokeball_data = [
        (1, "Poké Ball", "Catch Pokémon with these!", 5, 10, 25),
        (2, "Great Ball", "Higher capture rate than Poké Balls!", 35, 45, 50),
        (3, "Ultra Ball", "Higher capture rate than Great Balls!", 55, 65, 75),
        (4, "Master Ball", "Guaranteed capture of a Pokémon!", 100, 100, 100)
    ]

    #Insert pokemon_data into the Pokemon table
    cursor.executemany("INSERT INTO pokemon (id, name, type1, type2, ability1, ability2, ability3, hp, attack, defense, specAttack, specDefense, speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", pokemon_data)
    
    #Insert item_data into the Items table
    cursor.executemany("INSERT INTO items (id, name, description) VALUES (?, ?, ?)", item_data)
    
    #Insert item_data into the Poké Balls table
    cursor.executemany("INSERT INTO pokeballs (id, name, description, catchRateG, catchRateY, catchRateR) VALUES (?, ?, ?, ?, ?, ?)", pokeball_data)

    #Commit changes to database file
    conn.commit()
    
    #Close database file
    conn.close()