#main.py

import sqlite3
import os
from pokemon import Pokemon
from Items import Items
from pokeball import Pokeballs
from stores import Stores

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
    
    #Create a table for all stores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stores (
            id INTEGER PRIMARY KEY,
            item1_id INTEGER,
            item2_id INTEGER,
            item3_id INTEGER,
            item4_id INTEGER,
            item5_id INTEGER,
            item6_id INTEGER,
            item7_id INTEGER,
            item8_id INTEGER,
            item9_id INTEGER,
            item1_p INTEGER,
            item2_p INTEGER,
            item3_p INTEGER,
            item4_p INTEGER,
            item5_p INTEGER,
            item6_p INTEGER,
            item7_p INTEGER,
            item8_p INTEGER,
            item9_p INTEGER,
            pokeball1_id INTEGER,
            pokeball2_id INTEGER,
            pokeball3_id INTEGER,
            pokeball1_p INTEGER,
            pokeball2_p INTEGER,
            pokeball3_p INTEGER,
            money INTEGER,
            FOREIGN KEY (item1_id) REFERENCES items(id),
            FOREIGN KEY (item2_id) REFERENCES items(id),
            FOREIGN KEY (item3_id) REFERENCES items(id),
            FOREIGN KEY (item4_id) REFERENCES items(id),
            FOREIGN KEY (item5_id) REFERENCES items(id),
            FOREIGN KEY (item6_id) REFERENCES items(id),
            FOREIGN KEY (item7_id) REFERENCES items(id),
            FOREIGN KEY (item8_id) REFERENCES items(id),
            FOREIGN KEY (item9_id) REFERENCES items(id),
            FOREIGN KEY (pokeball1_id) REFERENCES pokeballs(id),
            FOREIGN KEY (pokeball2_id) REFERENCES pokeballs(id),
            FOREIGN KEY (pokeball3_id) REFERENCES pokeballs(id)
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
    
    #The data of items and money for all stores
    store_data = [
        (1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 300, 700, 1200, 2500, 3000, 300, 1200, 300, 2500, 1, 2, 3, 200, 600, 1200, 10000)
    ]

    #Insert pokemon_data into the Pokemon table
    cursor.executemany("INSERT INTO pokemon (id, name, type1, type2, ability1, ability2, ability3, hp, attack, defense, specAttack, specDefense, speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", pokemon_data)
    
    #Insert item_data into the Items table
    cursor.executemany("INSERT INTO items (id, name, description) VALUES (?, ?, ?)", item_data)
    
    #Insert item_data into the Poké Balls table
    cursor.executemany("INSERT INTO pokeballs (id, name, description, catchRateG, catchRateY, catchRateR) VALUES (?, ?, ?, ?, ?, ?)", pokeball_data)
    
    #Insert store_data into the Stores table
    cursor.executemany("INSERT INTO stores (id, item1_id, item2_id, item3_id, item4_id, item5_id, item6_id, item7_id, item8_id, item9_id, item1_p, item2_p, item3_p, item4_p, item5_p, item6_p, item7_p, item8_p, item9_p, pokeball1_id, pokeball2_id, pokeball3_id, pokeball1_p, pokeball2_p, pokeball3_p, money) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", store_data)

    #Commit changes to database file
    conn.commit()
    
    #Close database file
    conn.close()