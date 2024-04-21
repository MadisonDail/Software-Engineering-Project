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
        (9, "Blastoise", "Water", None, "Torrent", "Rain Dash", None, 79, 83, 100, 85, 105, 78),
        (10, "Caterpie", "Bug", None, "Shield Dust", "Run Away", None, 45, 30, 35, 20, 20, 45),
        (11, "Metapod", "Bug", None, "Shed Skin", None, None, 50, 20, 55, 25, 25, 30),
        (12, "Butterfree", "Bug", "Flying", "Compoundeyes", "Tinted Lens", None, 60, 45, 50, 90, 80, 70),
        (13, "Weedle", "Bug", "Poison", "Shield Dust", "Run Away", None, 40, 35, 30, 20, 20, 50),
        (14, "Kakuna", "Bug", "Poison", "Shed Skin", None, None, 45, 25, 50, 25, 25, 35),
        (15, "Beedrill", "Bug", "Poison", "Swarm", "Sniper", None, 65, 90, 40, 45, 80, 75),
        (16, "Pidgey", "Normal", "Flying", "Keen Eye", "Big Pecks", None, 40, 45, 40, 35, 35, 56),
        (17, "Pidgeotto", "Normal", "Flying", "Keen Eye", "Big Pecks", None, 63, 60, 55, 50, 50, 71),
        (18, "Pidgeot", "Normal", "Flying", "Keen Eye", "Big Pecks", None, 83, 80, 75, 70, 70, 101),
        (19, "Rattata", "Normal", None, "Run Away", "Guts", "Hustle", 30, 56, 35, 25, 35, 72),
        (20, "Raticate", "Normal", None, "Run Away", "Guts", "Hustle", 55, 81, 60, 50, 70, 97),
        (21, "Spearow", "Normal", "Flying", "Keen Eye", "Sniper", None, 40, 60, 30, 31, 31, 70),
        (22, "Fearow", "Normal", "Flying", "Keen Eye", "Sniper", None, 65, 90, 65, 61, 61, 100),
        (23, "Ekans", "Poison", None, "Intimidate", "Shed Skin", "Unnerve", 35, 60, 44, 40, 54, 55),
        (24, "Arbok", "Poison", None, "Intimidate", "Shed Skin", "Unnerve", 60, 95, 69, 65, 79, 80),
        (25, "Pikachu", "Electic", None, "Static", "Lightning Rod", None, 35, 55, 40, 50, 50, 90),
        (26, "Raichu", "Electic", None, "Static", "Lightning Rod", None, 60, 90, 55, 90, 80, 110),
        (27, "Sandshrew", "Ground", None, "Sand Veil", "Sand Rush", None, 50, 75, 85, 20, 30, 40),
        (28, "Sandslash", "Ground", None, "Sand Veil", "Sand Rush", None, 75, 100, 110, 45, 55, 65),
        (29, "Nidoran (F)", "Poison", None, "Poison Point", "Rivalry", "Hustle", 55, 47, 52, 40, 40, 41),
        (30, "Nidorina", "Poison", None, "Poison Point", "Rivalry", "Hustle", 70, 62, 67, 55, 55, 56),
        (31, "Nidoqueen", "Poison", "Ground", "Poison Point", "Rivalry", "Sheer Force", 90, 92, 87, 75, 85, 76),
        (32, "Nidoran (M)", "Poison", None, "Poison Point", "Rivalry", "Hustle", 46, 57, 40, 40, 40, 50),
        (33, "Nidorino", "Poison", None, "Poison Point", "Rivalry", "Hustle", 61, 72, 57, 55, 55, 65),
        (34, "Nidoking", "Poison", "Ground", "Poison Point", "Rivalry", "Sheer Force", 81, 102, 77, 85, 75, 85),
        (35, "Clefairy", "Fairy", None, "Cute Charm", "Magic Guard", "Friend Guard", 70, 45, 48, 60, 65, 35),
        (36, "Clefable", "Fairy", None, "Cute Charm", "Magic Guard", "Unaware", 95, 70, 73, 95, 90, 60),
        (37, "Vuplix", "Fire", None, "Flash Fire", "Drought", None, 38, 41, 40, 50, 65, 65),
        (38, "Ninetails", "Fire", None, "Flash Fire", "Drought", None, 73, 76, 75, 81, 100, 100),
        (39, "Jigglypuff", "Normal", "Fairy", "Cute Charm", "Competitive", "Friend Guard", 115, 45, 20, 45, 25, 20),
        (40, "Wigglytuff", "Normal", "Fairy", "Cute Charm", "Competitive", "Frisk", 140, 70, 45, 85, 50, 45),
        (41, "Zubat", "Poison", "Flying", "Inner Focus", "Infiltartor", None, 40, 45, 35, 30, 40, 55),
        (42, "Golbat", "Poison", "Flying", "Inner Focus", "Infiltartor", None, 75, 80, 70, 65, 75, 90),
        (43, "Oddish", "Grass", "Poison", "Chlorophyll", "Run Away", None, 45, 50, 55, 75, 65, 30),
        (44, "Gloom", "Grass", "Poison", "Chlorophyll", "Stench", None, 60, 65, 70, 85, 75, 40),
        (45, "Vileplume", "Grass", "Poison", "Chlorophyll", "Effect Spore", None, 75, 80, 85, 110, 90, 50),
        (46, "Paras", "Bug", "Grass", "Effect Spore", "Dry Skin", "Damp", 35, 70, 55, 45, 55, 25),
        (47, "Parasect", "Bug", "Grass", "Effect Spore", "Dry Skin", "Damp", 60, 95, 80, 60, 80, 30),
        (48, "Venonat", "Bug", "Poison", "Compoundeyes", "Tinted Lens", "Run Away", 60, 55, 50, 40, 55, 45),
        (49, "Venomoth", "Bug", "Poison", "Shield Dust", "Tinted Lens", "Wonder Skin", 70, 65, 60, 90, 75, 90),
        (50, "Diglett", "Ground", None, "Sand Veil", "Arena Trap", "Sand Force", 10, 55, 25, 35, 45, 95),
        (51, "Dugtrio", "Ground", None, "Sand Veil", "Arena Trap", "Sand Force", 35, 100, 50, 50, 70, 120),
        (52, "Meowth", "Normal", None, "Pickup", "Technician", "Unnerve", 40, 45, 35, 40, 40, 90),
        (53, "Persian", "Normal", None, "Limber", "Technician", "Unnerve", 65, 70, 60, 65, 65, 115),
        (54, "Psyduck", "Water", None, "Damp", "Cloud Nine", "Swift Swarm", 50, 52, 48, 65, 50, 55),
        (55, "Golduck", "Water", None, "Damp", "Cloud Nine", "Swift Swarm", 80, 82, 78, 95, 80, 85),
        (56, "Mankey", "Fighting", None, "Vital Spirit", "Anger Point", "Defiant", 40, 80, 35, 35, 45, 70),
        (57, "Primeape", "Fighting", None, "Vital Spirit", "Anger Point", "Defiant", 65, 105, 60, 60, 70, 95),
        (58, "Growlithe", "Fire", None, "Intimidate", "Flash Fire", "Justified", 55, 70, 45, 70, 50, 60),
        (59, "Arcanine", "Fire", None, "Intimidate", "Flash Fire", "Justified", 90, 110, 80, 100, 80, 95),
        (60, "Poliwag", "Water", None, "Water Absorb", "Damp", "Swift Swim", 40, 50, 40, 40, 40, 90),
        (61, "Poliwhirl", "Water", None, "Water Absorb", "Damp", "Swift Swim", 65, 65, 65, 50, 50, 90),
        (62, "Poliwrath", "Water", "Fighting", "Water Absorb", "Damp", "Swift Swim", 90, 95, 95, 70, 90, 70),
        (63, "Abra", "Psychic", None, "Synchronize", "Inner Focus", "Magic Guard", 25, 20, 15, 105, 55, 90),
        (64, "Kadabra", "Psychic", None, "Synchronize", "Inner Focus", "Magic Guard", 40, 35, 30, 120, 70, 105),
        (65, "Alakazam", "Psychic", None, "Synchronize", "Inner Focus", "Magic Guard", 55, 50, 45, 135, 95, 120),
        (66, "Machop", "Fighting", None, "Guts", "No Guard", "Steadfast", 70, 80, 50, 35, 35, 35),
        (67, "Machoke", "Fighting", None, "Guts", "No Guard", "Steadfast", 80, 100, 70, 50, 60, 45),
        (68, "Machamp", "Fighting", None, "Guts", "No Guard", "Steadfast", 90, 130, 80, 65, 85, 55),
        (69, "Bellsprout", "Grass", "Poison", "Chlorophyll", "Gluttony", None, 50, 75, 35, 70, 30, 40),
        (70, "Weepinbell", "Grass", "Poison", "Chlorophyll", "Gluttony", None, 65, 90, 50, 85, 45, 55),
        (71, "Victreebell", "Grass", "Poison", "Chlorophyll", "Gluttony", None, 50, 75, 35, 70, 30, 40),
        (72, "Tentacool", "Water", "Poison", "Clear Body", "Liquid Ooze", "Rain Dish", 40, 40, 35, 50, 100, 70),
        (73, "Tentacruel", "Water", "Poison", "Clear Body", "Liquid Ooze", "Rain Dish", 80, 70, 65, 80, 120, 100),
        (74, "Geodude", "Rock", "Ground", "Rock Head", "Sturdy", "Sand Veil", 40, 80, 100, 30, 30, 20),
        (75, "Graveler", "Rock", "Ground", "Rock Head", "Sturdy", "Sand Veil", 55, 95, 115, 45, 45, 35),
        (76, "Golem", "Rock", "Ground", "Rock Head", "Sturdy", "Sand Veil", 80, 120, 130, 55, 65, 45),
        (77, "Ponyta", "Fire", None, "Run Away", "Flash Fire", "Flame Body", 50, 85, 55, 65, 65, 90),
        (78, "Rapidash", "Fire", None, "Run Away", "Flash Fire", "Flame Body", 65, 100, 70, 80, 80, 105),
        (79, "Slowpoke", "Water", "Psychic", "Oblivious", "Own Tempo", "Regenerator", 90, 65, 65, 40, 40, 15),
        (80, "Slowbro", "Water", "Psychic", "Oblivious", "Own Tempo", "Regenerator", 95, 75, 110, 100, 80, 30),
        (81, "Magnemite", "Electric", "Steel", "Magnet Pull", "Sturdy", "Analytic", 25, 35, 70, 95, 55, 45),
        (82, "Magneton", "Electric", "Steel", "Magnet Pull", "Sturdy", "Analytic", 50, 60, 95, 120, 70, 70),
        (83, "Farfetch'd", "Normal", "Flying", "Keen Eye", "Inner Focus", "Defiant", 52, 90, 55, 58, 62, 60),
        (84, "Doduo", "Normal", "Flying", "Run Away", "Early Bird", "Tangled Feet", 35, 85, 45, 35, 35, 75),
        (85, "Dodrio", "Normal", "Flying", "Run Away", "Early Bird", "Tangled Feet", 60, 110, 70, 60, 60, 110),
        (86, "Seel", "Water", None, "Thick Fat", "Hydration", "Ice Body", 65, 45, 55, 45, 70, 45),
        (87, "Dewgong", "Water", "Ice", "Thick Fat", "Hydration", "Ice Body", 90, 70, 80, 70, 95, 70),
        (88, "Grimer", "Poison", None, "Stench", "Sticky Hold", "Poison Touch", 80, 80, 50, 40, 50, 25),
        (89, "Muk", "Poison", None, "Stench", "Sticky Hold", "Poison Touch", 105, 105, 75, 65, 100, 50),
        (90, "Shellder", "Water", None, "Shell Armor", "Skill Link", "Overcoat", 30, 65, 100, 45, 25, 40),
        (91, "Cloyster", "Water", "Ice", "Shell Armor", "Skill Link", "Overcoat", 50, 95, 180, 85, 45, 70),
        (92, "Gastly", "Ghost", "Poison", "Levitate", None, None, 30, 35, 30, 100, 35, 80),
        (93, "Haunter", "Ghost", "Poison", "Levitate", None, None, 45, 50, 45, 115, 55, 95),
        (94, "Gengar", "Ghost", "Poison", "Cursed Body", None, None, 60, 65, 60, 130, 75, 110),
        (95, "Onix", "Rock", "Ground", "Rock Head", "Sturdy", "Weak Armor", 35, 45, 160, 30, 45, 70),
        (96, "Drowzee", "Psychic", None, "Insomnia", "Forewarn", "Inner Focus", 60, 48, 45, 43, 90, 42),
        (97, "Hypno", "Psychic", None, "Insomnia", "Forewarn", "Inner Focus", 85, 73, 70, 73, 115, 67),
        (98, "Krabby", "Water", None, "Hyper Cutter", "Shell Armor", "Sheer Force", 30, 105, 90, 25, 25, 50),
        (99, "Kingler", "Water", None, "Hyper Cutter", "Shell Armor", "Sheer Force", 55, 130, 115, 50, 50, 75),
        (100, "Voltorb", "Electric", None, "Soundproof", "Static", "Aftermath", 40, 30, 50, 55, 55, 100),
        (101, "Electrode", "Electric", None, "Soundproof", "Static", "Aftermath", 60, 50, 70, 80, 80, 150),
        (102, "Exeggcute", "Grass", "Psychic", "Chlorophyll", "Harvest", None, 60, 40, 80, 60, 45, 40),
        (103, "Exeggutor", "Grass", "Psychic", "Chlorophyll", "Harvest", None, 95, 95, 85, 125, 75, 55),
        (104, "Cubone", "Ground", None, "Rock Head", "Lightning Rod", "Battle Armor", 50, 50, 95, 40, 50, 35),
        (105, "Marowak", "Ground", None, "Rock Head", "Lightning Rod", "Battle Armor", 60, 80, 110, 50, 80, 45),
        (106, "Hitmonlee", "Fighting", None, "Limber", "Reckless", "Unburden", 50, 120, 53, 35, 110, 87),
        (107, "Hitmonchan", "Fighting", None, "Limber", "Reckless", "Unburden", 50, 105, 79, 35, 110, 76),
        (108, "Lickitung", "Normal", None, "Own Tempo", "Oblivious", "Cloud Nine", 90, 55, 75, 60, 45, 35),
        (109, "Koffing", "Poison", None, "Levitate", "Neutralizing Gas", "Stench", 40, 65, 95, 60, 45, 35),
        (110, "Weezing", "Poison", None, "Levitate", "Neutralizing Gas", "Stench", 65, 90, 120, 85, 70, 60),
        (111, "Rhyhorn", "Ground", "Rock", "Lightning Rod", "Rock Head", "Reckless", 80, 85, 95, 30, 30, 25),
        (112, "Rhydon", "Ground", "Rock", "Lightning Rod", "Rock Head", "Reckless", 105, 130, 120, 45, 45, 40),
        (113, "Chansey", "Normal", None, "Natural Cure", "Serene Grace", "Healer", 250, 5, 5, 35, 105, 50),
        (114, "Tangela", "Grass", None, "Chlorophyll", "Leaf Guard", "Regenerator", 65, 55, 115, 100, 40, 60),
        (115, "Kangaskhan", "Normal", None, "Early Bird", "Scrappy", "Inner Focus", 105, 95, 80, 40, 80, 90),
        (116, "Horsea", "Water", None, "Swift Swim", "Sniper", "Damp", 30, 40, 70, 70, 25, 60),
        (117, "Seadra", "Water", None, "Poison Point", "Sniper", "Damp", 55, 65, 95, 95, 45, 85),
        (118, "Goldeen", "Water", None, "Swift Swim", "Water Veil", "Lightning Rod", 45, 67, 60, 35, 50, 63),
        (119, "Seaking", "Water", None, "Swift Swim", "Water Veil", "Lightning Rod", 80, 92, 65, 65, 80, 68),
        (120, "Staryu", "Water", None, "Illuminate", "Natural Cure", "Analytic", 30, 45, 55, 70, 55, 85),
        (121, "Starmie", "Water", "Psychic", "Illuminate", "Natural Cure", "Analytic", 60, 75, 85, 100, 85, 115),
        (122, "Mr. Mime", "Psychic", "Fairy", "Soundproof", "Filter", "Technician", 40, 45, 65, 100, 120, 90),
        (123, "Scyther", "Bug", "Flying", "Swarm", "Technician", "Steadfast", 70, 110, 80, 55, 80, 105),
        (124, "Jynx", "Ice", "Psychic", "Oblivious", "Forewarn", "Dry Skin", 65, 50, 35, 115, 95, 95),
        (125, "Electabuzz", "Electric", None, "Static", "Vital Spirit", None, 65, 83, 57, 95, 85, 105),
        (126, "Magmar", "Fire", None, "Flame Body", "Vital Spirit", None, 65, 95, 57, 100, 85, 93),
        (127, "Pinsir", "Bug", None, "Hyper Cutter", "Mold Breaker", "Moxie", 65, 125, 100, 55, 70, 75),
        (128, "Tauros", "Normal", None, "Intimidate", "Anger Point", "Sheer Force", 75, 100, 95, 40, 70, 110),
        (129, "Magikarp", "Water", None, "Swift Swim", "Rattled", None, 20, 10, 55, 15, 20, 80),
        (130, "Gyarados", "Water", "Dragon", "Intimidate", "Moxie", None, 95, 125, 79, 60, 100, 81),
        (131, "Lapras", "Water", "Ice", "Water Absorb", "Shell Armor", "Hydration", 130, 85, 80, 85, 95, 60),
        (132, "Ditto", "Normal", None, "Limber", "Imposter", None, 48, 48, 48, 48, 48, 48),
        (133, "Eevee", "Normal", None, "Run Away", "Adaptability", "Anticipation", 55, 55, 50, 45, 65, 55),
        (134, "Vaporeon", "Water", None, "Water Absorb", "Hydration", None, 130, 65, 60, 110, 95, 65),
        (135, "Jolteon", "Electric", None, "Volt Absorb", "Quick Feet", None, 65, 65, 60, 110, 95, 130),
        (136, "Flareon", "Fire", None, "Flash Fire", "Guts", None, 65, 130, 60, 95, 110, 65),
        (137, "Porygon", "Normal", None, "Trace", "Download", "Analytic", 65, 60, 70, 85, 75, 40),
        (138, "Omanyte", "Rock", "Water", "Swift Swim", "Shell Armor", "Weak Armor", 35, 40, 100, 90, 55, 35),
        (139, "Omastar", "Rock", "Water", "Swift Swim", "Shell Armor", "Weak Armor", 70, 60, 125, 115, 70, 55),
        (140, "Kabuto", "Rock", "Water", "Swift Swim", "Battle Armor", "Weak Armor", 30, 80, 90, 55, 45, 55),
        (141, "Kabutops", "Rock", "Water", "Swift Swim", "Battle Armor", "Weak Armor", 60, 115, 105, 65, 70, 80),
        (142, "Aerodactyl", "Rock", "Flying", "Rock Head", "Pressure", "Unnerve", 80, 105, 65, 60, 75, 130),
        (143, "Snorlax", "Normal", None, "Immunity", "Thick Fat", "Gluttony", 160, 110, 65, 65, 110, 30),
        (144, "Articuno", "Ice", "Flying", "Pressure", "Snow Cloak", None, 90, 85, 100, 95, 125, 85),
        (145, "Zapdos", "Electric", "Flying", "Pressure", "Static", None, 90, 90, 85, 125, 85, 90),
        (146, "Moltres", "Fire", "Flying", "Pressure", "Flame Body", None, 90, 100, 90, 125, 85, 90),
        (147, "Dratini", "Dragon", None, "Shed Skin", "Marvel Scale", None, 41, 64, 45, 50, 50, 50),
        (148, "Dragonair", "Dragon", None, "Shed Skin", "Marvel Scale", None, 61, 84, 65, 70, 70, 70),
        (149, "Dragonite", "Dragon", "Flying", "Inner Focus", "Multiscale", None, 91, 134, 95, 100, 100, 80),
        (150, "Mewtwo", "Psychic", None, "Pressure", "Unnerve", None, 106, 110, 90, 154, 90, 130),
        (151, "Mew", "Psychic", None, "Synchronize", None , None, 100, 100, 100, 100, 100, 100)
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