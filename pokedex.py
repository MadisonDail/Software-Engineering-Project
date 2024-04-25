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
Metapod = pokemon.Pokemon(11, "Metapod", 'BUG', 'NONE', 'Overgrow', 45, 45, 49, 49, 65, 65, 45, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)
Butterfree = pokemon.Pokemon(12, "Butterfree", 'BUG', 'FLY', 'Overgrow', 60, 60, 62, 63, 80, 80, 60, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)

Weedle = pokemon.Pokemon(13, "Weedle", 'BUG', 'PSN', 'Overgrow', 80, 80, 82, 83, 100, 100, 80, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Kakuna = pokemon.Pokemon(14, "Kakuna", 'BUG', 'PSN', 'Blaze', 39, 39, 52, 43, 60, 50, 65, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)
Beedrill = pokemon.Pokemon(15, "Beedrill", 'BUG', 'PSN', 'Blaze', 58, 58, 64, 58, 80, 65, 80, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)

Pidgey = pokemon.Pokemon(16, "Pidgey", 'NRM', 'FLY', 'Blaze', 78, 78, 84, 78, 109, 85, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)
Pidgeotto = pokemon.Pokemon(17, "Pidgeotto", 'NRM', 'FLY', 'Torrent', 44, 44, 48, 65, 50, 64, 43, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)
Pidgeot = pokemon.Pokemon(18, "Pidgeot", 'NRM', 'FLY', 'Torrent', 59, 59, 63, 80, 65, 80, 58, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)

Rattata = pokemon.Pokemon(19, "Rattata", 'NRM', 'NONE', 'Torrent', 79, 79, 83, 100, 85, 105, 78, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)
Raticate = pokemon.Pokemon(20, "Raticate", "NRM", "NONE", "None", 45, 45, 30, 35, 20, 20, 45, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)

Spearow = pokemon.Pokemon(21, "Spearow", 'NRM', 'FLY', 'Blaze', 39, 39, 52, 43, 60, 50, 65, moveList.Scratch, moveList.Growl, moveList.Ember, moveList.QuickAttack)
Fearow = pokemon.Pokemon(22, "Fearow", 'NRM', 'FLY', 'Blaze', 58, 58, 64, 58, 80, 65, 80, moveList.DragonRage, moveList.Slash, moveList.Growl, moveList.Flamethrower)

Ekans = pokemon.Pokemon(23, "Ekans", 'PSN', 'NONE', 'Blaze', 78, 78, 84, 78, 109, 85, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)
Arbok = pokemon.Pokemon(24, "Arbok", 'PSN', 'NONE', 'Torrent', 44, 44, 48, 65, 50, 64, 43, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)

Pikachu = pokemon.Pokemon(25, "Pikachu", 'ELC', 'NONE', 'Torrent', 35, 35, 55, 30, 50, 40, 90, moveList.ThunderShock, moveList.Agility, moveList.TailWhip, moveList.ThunderWave)
Raichu = pokemon.Pokemon(26, "Raichu", 'ELC', 'NONE', 'Torrent', 60, 60, 90, 55, 90, 80, 100, moveList.Thunder, moveList.QuickAttack, moveList.ThunderWave, moveList.TailWhip)

Sandshrew = pokemon.Pokemon(27, "Sandshrew", 'GRD', 'NONE', 'Torrent', 59, 59, 63, 80, 65, 80, 58, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)
Sandslash = pokemon.Pokemon(28, "Sandslash", 'GRD', 'NONE', 'Torrent', 79, 79, 83, 100, 85, 105, 78, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)

Nidoran = pokemon.Pokemon(29, "Nidoran", "PSN", "NONE", "None", 45, 45, 30, 35, 20, 20, 45, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Nidorina = pokemon.Pokemon(30, "Nidorina", 'PSN', 'NONE', 'Overgrow', 45, 45, 49, 49, 65, 65, 45, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)
Nidoqueen = pokemon.Pokemon(31, "Nidoqueen", 'PSN', 'GRD', 'Overgrow', 60, 60, 62, 63, 80, 80, 60, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)

Clefairy = pokemon.Pokemon(35, "Clefairy", 'NRM', 'NONE', 'Overgrow', 80, 80, 82, 83, 100, 100, 80, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Clefable = pokemon.Pokemon(36, "Clefable", 'NRM', 'NONE', 'Blaze', 39, 39, 52, 43, 60, 50, 65, moveList.Harden, moveList.Harden, moveList.Harden, moveList.Harden)

Vulpix = pokemon.Pokemon(37, "Vulpix", 'BUG', 'PSN', 'Blaze', 58, 58, 64, 58, 80, 65, 80, moveList.PoisonPowder, moveList.StunSpore, moveList.Gust, moveList.Psybeam)
Ninetales = pokemon.Pokemon(38, "Ninetales", 'NRM', 'FLY', 'Blaze', 78, 78, 84, 78, 109, 85, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)

Jigglypuff = pokemon.Pokemon(39, "Jigglypuff", 'NRM', 'FLY', 'Torrent', 44, 44, 48, 65, 50, 64, 43, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)
Wigglytuff = pokemon.Pokemon(40, "Wigglytuff", 'NRM', 'FLY', 'Torrent', 59, 59, 63, 80, 65, 80, 58, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)

Zubat = pokemon.Pokemon(41, "Zubat", 'NRM', 'NONE', 'Torrent', 79, 79, 83, 100, 85, 105, 78, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)
Golbat = pokemon.Pokemon(42, "Golbat", "NRM", "NONE", "None", 45, 45, 30, 35, 20, 20, 45, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)

Oddish = pokemon.Pokemon(43, "Oddish", 'GRS', 'PSN', 'Overgrow', 45, 45, 49, 49, 65, 65, 45, moveList.Tackle, moveList.Growl, moveList.Absorb, moveList.QuickAttack)
Gloom = pokemon.Pokemon(44, "Gloom", 'GRS', 'PSN', 'Overgrow', 60, 60, 62, 63, 80, 80, 60, moveList.PoisonPowder, moveList.RazorLeaf, moveList.Tackle, moveList.Growl)
Vileplume = pokemon.Pokemon(45, "Vileplume", 'GRS', 'PSN', 'Overgrow', 80, 80, 82, 83, 100, 100, 80, moveList.SwordsDance, moveList.RazorLeaf, moveList.PoisonPowder, moveList.Cut)

Paras = pokemon.Pokemon(46, "Paras", 'FIR', 'NONE', 'Blaze', 39, 39, 52, 43, 60, 50, 65, moveList.Scratch, moveList.Growl, moveList.Ember, moveList.QuickAttack)
Parasect = pokemon.Pokemon(47, "Parasect", 'FIR', 'NONE', 'Blaze', 58, 58, 64, 58, 80, 65, 80, moveList.DragonRage, moveList.Slash, moveList.Growl, moveList.Flamethrower)

Venonat = pokemon.Pokemon(48, "Venonat", 'FIR', 'FLY', 'Blaze', 78, 78, 84, 78, 109, 85, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)
Venomoth = pokemon.Pokemon(49, "Venomoth", 'WTR', 'NONE', 'Torrent', 44, 44, 48, 65, 50, 64, 43, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)

Diglett = pokemon.Pokemon(50, "Diglett", 'WTR', 'NONE', 'Torrent', 59, 59, 63, 80, 65, 80, 58, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)
Dugtrio = pokemon.Pokemon(51, "Dugtrio", 'WTR', 'NONE', 'Torrent', 79, 79, 83, 100, 85, 105, 78, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)

