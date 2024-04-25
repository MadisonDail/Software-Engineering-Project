import pokemon
import moves
import moveList

# Types Abreviations
# GRS: Grass,   FIR: Fire,     WTR: Water,     BUG: Bug,       NRM: Normal, 
# PSN: Poison,  ELC: Electric, GRD: Ground,    FGT: Fighting, 
# PSY: Psychic, RCK: Rock,     GHT: Ghost,     ICE: Ice,       DRG: Dragon, 
# DRK: Dark,    STL: Steel,    FLY: Flying.

# idNum, name, type1, type2, ability1, currentHp, hp, attack, defense, specAttack, specDefense, speed, move1=None, move2=None, move3=None, move4=None, status="None"):

Bulbasaur = pokemon.Pokemon(1, "Bulbasaur", 'GRS', 'PSN', 'Overgrow', 45, 45, 49, 49, 65, 65, 45, moveList.Tackle, moveList.Growl, moveList.Absorb, moveList.QuickAttack)
Ivysaur = pokemon.Pokemon(2, "Ivysaur", 'GRS', 'PSN', 'Overgrow', 60, 60, 62, 63, 80, 80, 60, moveList.PoisonPowder, moveList.RazorLeaf, moveList.Tackle, moveList.Growl)
Venusaur = pokemon.Pokemon(3, "Venusaur", 'GRS', 'PSN', 'Overgrow', 80, 80, 82, 83, 100, 100, 80, moveList.SwordsDance, moveList.RazorLeaf, moveList.PoisonPowder, moveList.Cut)

Charmander = pokemon.Pokemon(4, "Charmander", 'FIR', 'NONE', 'Blaze', 39, 39, 52, 43, 60, 50, 65, moveList.Scratch, moveList.Growl, moveList.Ember, moveList.QuickAttack)
Charmeleon = pokemon.Pokemon(5, "Charmeleon", 'FIR', 'NONE', 'Blaze', 58, 58, 64, 58, 80, 65, 80, moveList.DragonRage, moveList.Slash, moveList.Growl, moveList.Flamethrower)
Charizard = pokemon.Pokemon(6, "Charizard", 'FIR', 'FLY', 'Blaze', 78, 78, 84, 78, 109, 85, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)

Squirtle = pokemon.Pokemon(7, "Squirtle", 'WTR', 'NONE', 'Torrent', 44, 44, 48, 65, 50, 64, 43, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)
Wartortle = pokemon.Pokemon(8, "Wartortle", 'WTR', 'NONE', 'Torrent', 59, 59, 63, 80, 65, 80, 58, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)
Blastoise = pokemon.Pokemon(9, "Blastoise", 'WTR', 'NONE', 'Torrent', 79, 79, 83, 100, 85, 105, 78, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)

Caterpie = pokemon.Pokemon(10, "Caterpie", "BUG", "NONE", "None", 45, 45, 30, 35, 20, 20, 45, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Metapod = pokemon.Pokemon(11, "Metapod", 'BUG', 'NONE', 'Overgrow', 50, 50, 20, 55, 25, 25, 30, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)
Butterfree = pokemon.Pokemon(12, "Butterfree", 'BUG', 'FLY', 'Overgrow', 60, 60, 45, 50, 80, 80, 70, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)

Weedle = pokemon.Pokemon(13, "Weedle", 'BUG', 'PSN', 'Overgrow', 40, 40, 35, 20, 20, 20, 50, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Kakuna = pokemon.Pokemon(14, "Kakuna", 'BUG', 'PSN', 'Blaze', 45, 45, 25, 50, 25, 25, 35, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)
Beedrill = pokemon.Pokemon(15, "Beedrill", 'BUG', 'PSN', 'Blaze', 65, 65, 80, 40, 45, 80, 75, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)

Pidgey = pokemon.Pokemon(16, "Pidgey", 'NRM', 'FLY', 'Blaze', 40, 40, 45, 40, 35, 35, 56, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)
Pidgeotto = pokemon.Pokemon(17, "Pidgeotto", 'NRM', 'FLY', 'Torrent', 63, 63, 60, 55, 50, 50, 71, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)
Pidgeot = pokemon.Pokemon(18, "Pidgeot", 'NRM', 'FLY', 'Torrent', 83, 83, 80, 75, 70, 70, 91, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)

Rattata = pokemon.Pokemon(19, "Rattata", 'NRM', 'NONE', 'Torrent', 30, 30, 56, 35, 25, 35, 72, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)
Raticate = pokemon.Pokemon(20, "Raticate", "NRM", "NONE", "None", 55, 55, 81, 60, 50, 70, 97, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)

Spearow = pokemon.Pokemon(21, "Spearow", 'NRM', 'FLY', 'Blaze', 40, 40, 60, 30, 31, 31, 70, moveList.Scratch, moveList.Growl, moveList.Ember, moveList.QuickAttack)
Fearow = pokemon.Pokemon(22, "Fearow", 'NRM', 'FLY', 'Blaze', 65, 65, 90, 65, 61, 61, 100, moveList.DragonRage, moveList.Slash, moveList.Growl, moveList.Flamethrower)

Ekans = pokemon.Pokemon(23, "Ekans", 'PSN', 'NONE', 'Blaze', 35, 35, 60, 44, 40, 54, 55, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)
Arbok = pokemon.Pokemon(24, "Arbok", 'PSN', 'NONE', 'Torrent', 60, 60, 85, 69, 65, 79, 80, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)

Pikachu = pokemon.Pokemon(25, "Pikachu", 'ELC', 'NONE', 'Torrent', 35, 35, 55, 30, 50, 40, 90, moveList.ThunderShock, moveList.Agility, moveList.TailWhip, moveList.ThunderWave)
Raichu = pokemon.Pokemon(26, "Raichu", 'ELC', 'NONE', 'Torrent', 60, 60, 90, 55, 90, 80, 100, moveList.Thunder, moveList.QuickAttack, moveList.ThunderWave, moveList.TailWhip)

Sandshrew = pokemon.Pokemon(27, "Sandshrew", 'GRD', 'NONE', 'Torrent', 50, 50, 75, 85, 20, 30, 40, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)
Sandslash = pokemon.Pokemon(28, "Sandslash", 'GRD', 'NONE', 'Torrent', 75, 75, 100, 110, 45, 55, 65, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)

Nidoran = pokemon.Pokemon(29, "Nidoran", "PSN", "NONE", "None", 55, 55, 47, 52, 40, 40, 41, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Nidorina = pokemon.Pokemon(30, "Nidorina", 'PSN', 'NONE', 'Overgrow', 70, 70, 62, 67, 55, 55, 56, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)
Nidoqueen = pokemon.Pokemon(31, "Nidoqueen", 'PSN', 'GRD', 'Overgrow', 90, 90, 82, 87, 75, 85, 76, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)

Clefairy = pokemon.Pokemon(35, "Clefairy", 'NRM', 'NONE', 'Overgrow', 70, 70, 45, 48, 60, 65, 35, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Clefable = pokemon.Pokemon(36, "Clefable", 'NRM', 'NONE', 'Blaze', 95, 95, 70, 73, 85, 90, 60, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)

Vulpix = pokemon.Pokemon(37, "Vulpix", 'FIR', 'NONE', 'Blaze', 38, 38, 41, 40, 50, 65, 65, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)
Ninetales = pokemon.Pokemon(38, "Ninetales", 'FIR', 'NONE', 'Blaze', 73, 73, 76, 75, 81, 100, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)

Jigglypuff = pokemon.Pokemon(39, "Jigglypuff", 'NRM', 'NONE', 'Torrent', 115, 115, 45, 20, 45, 25, 20, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)
Wigglytuff = pokemon.Pokemon(40, "Wigglytuff", 'NRM', 'NONE', 'Torrent', 140, 140, 70, 45, 75, 50, 45, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)







#need stats for below 

Zubat = pokemon.Pokemon(41, "Zubat", 'PSN', 'FLY', 'Torrent', 40, 40, 45, 35, 30, 40, 55, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)
Golbat = pokemon.Pokemon(42, "Golbat", 'PSN', 'FLY', "None", 45, 45, 30, 35, 20, 20, 45, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)

Oddish = pokemon.Pokemon(43, "Oddish", 'GRS', 'PSN', 'Overgrow', 45, 45, 49, 49, 65, 65, 45, moveList.Tackle, moveList.Growl, moveList.Absorb, moveList.QuickAttack)
Gloom = pokemon.Pokemon(44, "Gloom", 'GRS', 'PSN', 'Overgrow', 60, 60, 62, 63, 80, 80, 60, moveList.PoisonPowder, moveList.RazorLeaf, moveList.Tackle, moveList.Growl)
Vileplume = pokemon.Pokemon(45, "Vileplume", 'GRS', 'PSN', 'Overgrow', 80, 80, 82, 83, 100, 100, 80, moveList.SwordsDance, moveList.RazorLeaf, moveList.PoisonPowder, moveList.Cut)

Paras = pokemon.Pokemon(46, "Paras", 'BUG', 'GRS', 'Blaze', 39, 39, 52, 43, 60, 50, 65, moveList.Scratch, moveList.Growl, moveList.Ember, moveList.QuickAttack)
Parasect = pokemon.Pokemon(47, "Parasect", 'BUG', 'GRS', 'Blaze', 58, 58, 64, 58, 80, 65, 80, moveList.DragonRage, moveList.Slash, moveList.Growl, moveList.Flamethrower)

Venonat = pokemon.Pokemon(48, "Venonat", 'BUG', 'PSN', 'Blaze', 78, 78, 84, 78, 109, 85, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)
Venomoth = pokemon.Pokemon(49, "Venomoth", 'BUG', 'PSN', 'Torrent', 44, 44, 48, 65, 50, 64, 43, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)

Diglett = pokemon.Pokemon(50, "Diglett", 'GRD', 'NONE', 'Torrent', 59, 59, 63, 80, 65, 80, 58, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)
Dugtrio = pokemon.Pokemon(51, "Dugtrio", 'GRD', 'NONE', 'Torrent', 79, 79, 83, 100, 85, 105, 78, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)

Meowth = pokemon.Pokemon(52, "Meowth", 'NRM', 'NONE', 'Overgrow', 45, 45, 49, 49, 65, 65, 45, moveList.Tackle, moveList.Growl, moveList.Absorb, moveList.QuickAttack)
Persian = pokemon.Pokemon(53, "Persian", 'NRM', 'NONE', 'Overgrow', 60, 60, 62, 63, 80, 80, 60, moveList.PoisonPowder, moveList.RazorLeaf, moveList.Tackle, moveList.Growl)

Psyduck = pokemon.Pokemon(54, "Psyduck", 'WTR', 'NONE', 'Overgrow', 80, 80, 82, 83, 100, 100, 80, moveList.SwordsDance, moveList.RazorLeaf, moveList.PoisonPowder, moveList.Cut)
Golduck = pokemon.Pokemon(55, "Golduck", 'WTR', 'NONE', 'Blaze', 39, 39, 52, 43, 60, 50, 65, moveList.Scratch, moveList.Growl, moveList.Ember, moveList.QuickAttack)

Mankey = pokemon.Pokemon(56, "Mankey", 'FGT', 'NONE', 'Blaze', 58, 58, 64, 58, 80, 65, 80, moveList.DragonRage, moveList.Slash, moveList.Growl, moveList.Flamethrower)
Primeape = pokemon.Pokemon(57, "Primeape", 'FGT', 'NONE', 'Blaze', 78, 78, 84, 78, 109, 85, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)

Growlithe = pokemon.Pokemon(58, "Growlithe", 'FIR', 'NONE', 'Torrent', 44, 44, 48, 65, 50, 64, 43, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)
Arcanine = pokemon.Pokemon(59, "Arcanine", 'FIR', 'NONE', 'Torrent', 59, 59, 63, 80, 65, 80, 58, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)

Poliwag = pokemon.Pokemon(60, "Poliwag", 'WTR', 'NONE', 'Torrent', 79, 79, 83, 100, 85, 105, 78, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)
Poliwhirl = pokemon.Pokemon(60, "Poliwhirl", 'WTR', 'NONE', 'Torrent', 79, 79, 83, 100, 85, 105, 78, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)
Poliwrath = pokemon.Pokemon(62, "Poliwrath", 'WTR', 'FGT', "None", 45, 45, 30, 35, 20, 20, 45, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)

Abra = pokemon.Pokemon(63, "Abra", 'PSY', 'NONE', 'Overgrow', 45, 45, 49, 49, 65, 65, 45, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)
Kadabra = pokemon.Pokemon(64, "Kadabra", 'PSY', 'NONE', 'Overgrow', 60, 60, 62, 63, 80, 80, 60, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)
Alakazam = pokemon.Pokemon(65, "Alakazam", 'PSY', 'NONE', 'Overgrow', 80, 80, 82, 83, 100, 100, 80, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)

Machop = pokemon.Pokemon(66, "Machop", 'FGT', 'NONE', 'Blaze', 39, 39, 52, 43, 60, 50, 65, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)
Machoke = pokemon.Pokemon(67, "Machoke", 'FGT', 'NONE', 'Blaze', 58, 58, 64, 58, 80, 65, 80, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)
Machamp = pokemon.Pokemon(68, "Machamp", 'FGT', 'NONE', 'Blaze', 78, 78, 84, 78, 109, 85, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)

Bellsprout = pokemon.Pokemon(69, "Bellsprout", 'GRS', 'PSN', 'Torrent', 44, 44, 48, 65, 50, 64, 43, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)
Weepinbell = pokemon.Pokemon(70, "Weepinbell", 'GRS', 'PSN', 'Torrent', 59, 59, 63, 80, 65, 80, 58, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)
Victreebel = pokemon.Pokemon(71, "Victreebel", 'GRS', 'PSN', 'Torrent', 79, 79, 83, 100, 85, 105, 78, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)

Tentacool = pokemon.Pokemon(72, "Tentacool", 'WTR', 'PSN', 'None', 45, 45, 30, 35, 20, 20, 45, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Tentacruel = pokemon.Pokemon(73, "Tentacruel", 'WTR', 'PSN', 'Blaze', 39, 39, 52, 43, 60, 50, 65, moveList.Scratch, moveList.Growl, moveList.Ember, moveList.QuickAttack)

Geodude = pokemon.Pokemon(74, "Geodude", 'RCK', 'GRD', 'Blaze', 58, 58, 64, 58, 80, 65, 80, moveList.DragonRage, moveList.Slash, moveList.Growl, moveList.Flamethrower)
Graveler = pokemon.Pokemon(75, "Graveler", 'RCK', 'GRD', 'Blaze', 78, 78, 84, 78, 109, 85, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)
Golem = pokemon.Pokemon(76, "Golem", 'RCK', 'GRD', 'Torrent', 44, 44, 48, 65, 50, 64, 43, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)

Ponyta = pokemon.Pokemon(77, "Ponyta", 'FIR', 'NONE', 'Torrent', 35, 35, 55, 30, 50, 40, 90, moveList.ThunderShock, moveList.Agility, moveList.TailWhip, moveList.ThunderWave)
Rapidash = pokemon.Pokemon(78, "Rapidash", 'FIR', 'NONE', 'Torrent', 60, 60, 90, 55, 90, 80, 100, moveList.Thunder, moveList.QuickAttack, moveList.ThunderWave, moveList.TailWhip)

Slowpoke = pokemon.Pokemon(79, "Slowpoke", 'WTR', 'PSY', 'Torrent', 59, 59, 63, 80, 65, 80, 58, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)
Slowbro = pokemon.Pokemon(80, "Slowbro", 'WTR', 'PSY', 'Torrent', 79, 79, 83, 100, 85, 105, 78, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)

Magnemite = pokemon.Pokemon(81, "Magnemite", 'ELC', 'STL', 'None', 45, 45, 30, 35, 20, 20, 45, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Magneton = pokemon.Pokemon(82, "Magneton", 'ELC', 'STL', 'Overgrow', 45, 45, 49, 49, 65, 65, 45, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)

Farfetchd = pokemon.Pokemon(83, "Farfetchd", 'NRM', 'FLY', 'Overgrow', 60, 60, 62, 63, 80, 80, 60, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)

Doduo = pokemon.Pokemon(84, "Doduo", 'NRM', 'FLY', 'Overgrow', 80, 80, 82, 83, 100, 100, 80, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Dodrio = pokemon.Pokemon(85, "Dodrio", 'NRM', 'FLY', 'Blaze', 39, 39, 52, 43, 60, 50, 65, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)

Seel = pokemon.Pokemon(86, "Seel", 'WTR', 'NONE', 'Blaze', 58, 58, 64, 58, 80, 65, 80, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)
Dewgong = pokemon.Pokemon(87, "Dewgong", 'WTR', 'ICE', 'Blaze', 78, 78, 84, 78, 109, 85, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)

Grimer = pokemon.Pokemon(88, "Grimer", 'PSN', 'NONE', 'Torrent', 44, 44, 48, 65, 50, 64, 43, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)
Muk = pokemon.Pokemon(89, "Muk", 'PSN', 'NONE', 'Torrent', 59, 59, 63, 80, 65, 80, 58, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)

Shellder = pokemon.Pokemon(90, "Shellder", 'WTR', 'NONE', "None", 45, 45, 30, 35, 20, 20, 45, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Cloyster = pokemon.Pokemon(91, "Cloyster", 'WTR', 'ICE', 'Overgrow', 45, 45, 49, 49, 65, 65, 45, moveList.Tackle, moveList.Growl, moveList.Absorb, moveList.QuickAttack)

Gastly = pokemon.Pokemon(92, "Gastly", 'GHT', 'PSN', 'Overgrow', 60, 60, 62, 63, 80, 80, 60, moveList.PoisonPowder, moveList.RazorLeaf, moveList.Tackle, moveList.Growl)
Haunter = pokemon.Pokemon(93, "Haunter", 'GHT', 'PSN', 'Overgrow', 80, 80, 82, 83, 100, 100, 80, moveList.SwordsDance, moveList.RazorLeaf, moveList.PoisonPowder, moveList.Cut)
Gengar = pokemon.Pokemon(94, "Gengar", 'GHT', 'PSN', 'Blaze', 39, 39, 52, 43, 60, 50, 65, moveList.Scratch, moveList.Growl, moveList.Ember, moveList.QuickAttack)

Onix = pokemon.Pokemon(95, "Onix", 'RCK', 'GRD', 'Blaze', 58, 58, 64, 58, 80, 65, 80, moveList.DragonRage, moveList.Slash, moveList.Growl, moveList.Flamethrower)

Drowzee = pokemon.Pokemon(96, "Drowzee", 'PSY', 'NONE', 'Blaze', 78, 78, 84, 78, 109, 85, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)
Hypno = pokemon.Pokemon(97, "Hypno", 'PSY', 'NONE', 'Torrent', 44, 44, 48, 65, 50, 64, 43, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)

Krabby = pokemon.Pokemon(98, "Krabby", 'WTR', 'NONE', 'Torrent', 59, 59, 63, 80, 65, 80, 58, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)
Kingler = pokemon.Pokemon(99, "Kingler", 'WTR', 'NONE', 'Torrent', 79, 79, 83, 100, 85, 105, 78, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)




Voltorb = pokemon.Pokemon(100, "Voltorb", 'ELC', 'NONE', 'Overgrow', 40, 40, 30, 50, 55, 55, 100, moveList.Tackle, moveList.Growl, moveList.Absorb, moveList.QuickAttack)

Electrode = pokemon.Pokemon(101, "Electrode", 'ELC', 'NONE', 'Overgrow', 60, 60, 50, 70, 80, 80, 150, moveList.Tackle, moveList.Growl, moveList.Absorb, moveList.QuickAttack)
Exeggcute = pokemon.Pokemon(102, "Exeggcute", 'GRS', 'PSY', 'Overgrow', 60, 60, 40, 80, 60, 45, 40, moveList.PoisonPowder, moveList.RazorLeaf, moveList.Tackle, moveList.Growl)
Exeggutor = pokemon.Pokemon(103, "Exeggutor", 'GRS', 'PSY', 'Overgrow', 95, 95, 95, 85, 125, 75, 55, moveList.SwordsDance, moveList.RazorLeaf, moveList.PoisonPowder, moveList.Cut)

Cubone = pokemon.Pokemon(104, "Cubone", 'GRD', 'NONE', 'Blaze', 50, 50, 50, 95, 40, 50, 35, moveList.Scratch, moveList.Growl, moveList.Ember, moveList.QuickAttack)
Marowak = pokemon.Pokemon(105, "Marowak", 'GRD', 'NONE', 'Blaze', 60, 60, 80, 110, 50, 80, 45, moveList.DragonRage, moveList.Slash, moveList.Growl, moveList.Flamethrower)
Hitmonlee = pokemon.Pokemon(106, "Hitmonlee", 'FGT', 'NONE', 'Blaze', 50, 50, 120, 53, 35, 110, 87, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)

Hitmonchan = pokemon.Pokemon(107, "Hitmonchan", 'FGT', 'NONE', 'Torrent', 50, 50, 105, 79, 35, 110, 76, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)
Lickitung = pokemon.Pokemon(108, "Lickitung", 'NRM', 'NONE', 'Torrent', 90, 90, 55, 75, 60, 45, 35, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)
Koffing = pokemon.Pokemon(109, "Koffing", 'PSN', 'NONE', 'Torrent', 40, 40, 65, 95, 60, 45, 35, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)

Weezing = pokemon.Pokemon(110, "Weezing", "PSN", "NONE", "None", 65, 65, 90, 120, 85, 70, 60, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Rhyhorn = pokemon.Pokemon(111, "Rhyhorn", "GRD", "RCK", "None", 80, 80, 85, 95, 30, 30, 25, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)
Rhydon = pokemon.Pokemon(112, "Rhydon", 'GRD', 'RCK', 'Overgrow', 105, 105, 130, 120, 45, 45, 40, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)

Chansey = pokemon.Pokemon(113, "Chansey", 'NRM', 'NONE', 'Overgrow', 250, 250, 5, 5, 35, 105, 50, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Tangela = pokemon.Pokemon(114, "Tangela", 'GRS', 'NONE', 'Blaze', 65, 65, 55, 115, 100, 40, 60, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)
Kangaskhan = pokemon.Pokemon(115, "Kangaskhan", 'NRM', 'NONE', 'Blaze', 105, 105, 95, 80, 40, 80, 90, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)

Horsea = pokemon.Pokemon(116, "Horsea", 'WTR', 'NONE', 'Blaze', 30, 30, 40, 70, 70, 25, 60, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)
Seadra = pokemon.Pokemon(117, "Seadra", 'WTR', 'NONE', 'Torrent', 55, 55, 65, 95, 95, 45, 85, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)
Goldeen = pokemon.Pokemon(118, "Goldeen", 'WTR', 'NONE', 'Torrent', 45, 45, 67, 60, 35, 50, 63, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)

Seaking = pokemon.Pokemon(119, "Seaking", 'WTR', 'NONE', 'Torrent', 80, 80, 92, 65, 65, 80, 68, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)
Staryu = pokemon.Pokemon(120, "Staryu", "WTR", "NONE", "None", 30, 30, 45, 55, 70, 55, 85, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)

Starmie = pokemon.Pokemon(121, "Starmie", 'WTR', 'PSY', 'Blaze', 60, 60, 75, 85, 100, 85, 115, moveList.Scratch, moveList.Growl, moveList.Ember, moveList.QuickAttack)
Mr_Mime = pokemon.Pokemon(122, "Mr. Mime", 'PSY', 'NRM', 'Blaze', 40, 40, 45, 65, 100, 120, 90, moveList.DragonRage, moveList.Slash, moveList.Growl, moveList.Flamethrower)

Scyther = pokemon.Pokemon(123, "Scyther", 'BUG', 'FLY', 'Blaze', 70, 70, 110, 80, 55, 80, 105, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)
Jynx = pokemon.Pokemon(124, "Jynx", 'ICE', 'PSY', 'Torrent', 65, 65, 50, 35, 115, 95, 95, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)

Electabuzz = pokemon.Pokemon(125, "Electabuzz", 'ELC', 'NONE', 'Torrent', 65, 65, 83, 57, 95, 85, 105, moveList.ThunderShock, moveList.Agility, moveList.TailWhip, moveList.ThunderWave)
Magmar = pokemon.Pokemon(126, "Magmar", 'FIR', 'NONE', 'Torrent', 65, 65, 95, 57, 100, 85, 93, moveList.Thunder, moveList.QuickAttack, moveList.ThunderWave, moveList.TailWhip)

Pinsir = pokemon.Pokemon(127, "Pinsir", 'BUG', 'NONE', 'Torrent', 65, 65, 125, 100, 55, 70, 75, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)
Tauros = pokemon.Pokemon(128, "Tauros", 'NRM', 'NONE', 'Torrent', 75, 75, 100, 95, 40, 70, 110, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)

Magikarp = pokemon.Pokemon(129, "Magikarp", "WTR", "NONE", "None", 20, 20, 10, 55, 15, 20, 80, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Gyarados = pokemon.Pokemon(130, "Gyarados", 'WTR', 'DRG', 'Overgrow', 95, 95, 125, 79, 60, 100, 81, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)
Lapras = pokemon.Pokemon(131, "Lapras", 'WTR', 'ICE', 'Overgrow', 130, 130, 85, 80, 85, 95, 60, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)

Ditto = pokemon.Pokemon(135, "Ditto", 'NRM', 'NONE', 'Overgrow', 48, 48, 48, 48, 48, 48, 48, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Clefable = pokemon.Pokemon(136, "Clefable", 'NRM', 'NONE', 'Blaze', 39, 39, 52, 43, 60, 50, 65, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)

Vulpix = pokemon.Pokemon(137, "Vulpix", 'FIR', 'NONE', 'Blaze', 58, 58, 64, 58, 80, 65, 80, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)
Ninetales = pokemon.Pokemon(138, "Ninetales", 'FIR', 'NONE', 'Blaze', 78, 78, 84, 78, 109, 85, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)

Jigglypuff = pokemon.Pokemon(139, "Jigglypuff", 'NRM', 'NONE', 'Torrent', 44, 44, 48, 65, 50, 64, 43, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)
Wigglytuff = pokemon.Pokemon(140, "Wigglytuff", 'NRM', 'NONE', 'Torrent', 59, 59, 63, 80, 65, 80, 58, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)

Zubat = pokemon.Pokemon(141, "Zubat", 'PSN', 'FLY', 'Torrent', 79, 79, 83, 100, 85, 105, 78, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)
Golbat = pokemon.Pokemon(142, "Golbat", 'PSN', 'FLY', "None", 45, 45, 30, 35, 20, 20, 45, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)

Oddish = pokemon.Pokemon(143, "Oddish", 'GRS', 'PSN', 'Overgrow', 45, 45, 49, 49, 65, 65, 45, moveList.Tackle, moveList.Growl, moveList.Absorb, moveList.QuickAttack)
Gloom = pokemon.Pokemon(144, "Gloom", 'GRS', 'PSN', 'Overgrow', 60, 60, 62, 63, 80, 80, 60, moveList.PoisonPowder, moveList.RazorLeaf, moveList.Tackle, moveList.Growl)
Vileplume = pokemon.Pokemon(145, "Vileplume", 'GRS', 'PSN', 'Overgrow', 80, 80, 82, 83, 100, 100, 80, moveList.SwordsDance, moveList.RazorLeaf, moveList.PoisonPowder, moveList.Cut)

Paras = pokemon.Pokemon(146, "Paras", 'BUG', 'GRS', 'Blaze', 39, 39, 52, 43, 60, 50, 65, moveList.Scratch, moveList.Growl, moveList.Ember, moveList.QuickAttack)
Parasect = pokemon.Pokemon(147, "Parasect", 'BUG', 'GRS', 'Blaze', 58, 58, 64, 58, 80, 65, 80, moveList.DragonRage, moveList.Slash, moveList.Growl, moveList.Flamethrower)

Venonat = pokemon.Pokemon(148, "Venonat", 'BUG', 'PSN', 'Blaze', 78, 78, 84, 78, 109, 85, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)
Venomoth = pokemon.Pokemon(149, "Venomoth", 'BUG', 'PSN', 'Torrent', 44, 44, 48, 65, 50, 64, 43, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)

Diglett = pokemon.Pokemon(150, "Diglett", 'GRD', 'NONE', 'Torrent', 59, 59, 63, 80, 65, 80, 58, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)
Dugtrio = pokemon.Pokemon(151, "Dugtrio", 'GRD', 'NONE', 'Torrent', 79, 79, 83, 100, 85, 105, 78, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)