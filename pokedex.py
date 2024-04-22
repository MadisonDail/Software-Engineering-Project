import pokemon
import moves
import moveList

# Types Abreviations
# GRS: Grass, FIR: Fire, WTR: Water, BUG: Bug, NRM: Normal, 
# PSN: Poison, ELC: Electric, GRD: Ground, FGT: Fighting, 
# PSY: Psychic, RCK: Rock, GHT: Ghost, ICE: Ice, DRG: Dragon, 
# DRK: Dark, STL: Steel, FLY: Flying.



Bulbasaur = pokemon.Pokemon(1, "Bulbasaur", 'GRS', 'PSN', 'Overgrow', 45, 45, 49, 49, 65, 65, 45, moveList.Tackle, moveList.Growl, moveList.Absorb, moveList.QuickAttack)
Ivysaur = pokemon.Pokemon(2, "Ivysaur", 'GRS', 'PSN', 'Overgrow', 60, 60, 62, 63, 80, 80, 60, moveList.PoisonPowder, moveList.RazorLeaf, moveList.Tackle, moveList.Growl)
Venusaur = pokemon.Pokemon(3, "Venusaur", 'GRS', 'PSN', 'Overgrow', 80, 80, 82, 83, 100, 100, 80, moveList.SwordsDance, moveList.RazorLeaf, moveList.PoisonPowder, moveList.Cut)
Charmander = pokemon.Pokemon(4, "Charmander", 'FIR', 'NONE', 'Blaze', 39, 39, 52, 43, 60, 50, 65, moveList.Scratch, moveList.Growl, moveList.Ember, moveList.QuickAttack)
Charmeleon = pokemon.Pokemon(5, "Charmeleon", 'FIR', 'NONE', 'Blaze', 58, 58, 64, 58, 80, 65, 80, moveList.DragonRage, moveList.Slash, moveList.Growl, moveList.Flamethrower)
Charizard = pokemon.Pokemon(6, "Charizard", 'FIR', 'FLY', 'Blaze', 78, 78, 84, 78, 109, 85, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)
Squirtle = pokemon.Pokemon(7, "Squirtle", 'WTR', 'NONE', 'Torrent', 44, 44, 48, 65, 50, 64, 43, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)
Wartortle = pokemon.Pokemon(8, "Wartortle", 'WTR', 'NONE', 'Torrent', 59, 59, 63, 80, 65, 80, 58, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)
Blastoise = pokemon.Pokemon(9, "Blastoise", 'WTR', 'NONE', 'Torrent', 79, 79, 83, 100, 85, 105, 78, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)
