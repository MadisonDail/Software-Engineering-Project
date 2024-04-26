import pokemon
import moves
import moveList

# Types Abreviations
# GRS: Grass,   FIR: Fire,     WTR: Water,     BUG: Bug,       NRM: Normal, 
# PSN: Poison,  ELC: Electric, GRD: Ground,    FGT: Fighting, 
# PSY: Psychic, RCK: Rock,     GHT: Ghost,     ICE: Ice,       DRG: Dragon, 
# DRK: Dark,    STL: Steel,    FLY: Flying.

# idNum, name, type1, type2, xp, currentHp, hp, attack, defense, specAttack, specDefense, speed, move1=None, move2=None, move3=None, move4=None, status=0):

Bulbasaur = pokemon.Pokemon(1, "Bulbasaur", 'GRS', 'PSN', 0, 45, 45, 49, 49, 65, 65, 45, moveList.Tackle, moveList.Growl, moveList.Absorb, moveList.QuickAttack)
Ivysaur = pokemon.Pokemon(2, "Ivysaur", 'GRS', 'PSN', 0, 60, 60, 62, 63, 80, 80, 60, moveList.PoisonPowder, moveList.RazorLeaf, moveList.Tackle, moveList.Growl)
Venusaur = pokemon.Pokemon(3, "Venusaur", 'GRS', 'PSN', 0, 80, 80, 82, 83, 100, 100, 80, moveList.SwordsDance, moveList.RazorLeaf, moveList.PoisonPowder, moveList.Cut)

Charmander = pokemon.Pokemon(4, "Charmander", 'FIR', 'NONE', 0, 39, 39, 52, 43, 60, 50, 65, moveList.Scratch, moveList.Growl, moveList.Ember, moveList.QuickAttack)
Charmeleon = pokemon.Pokemon(5, "Charmeleon", 'FIR', 'NONE', 0, 58, 58, 64, 58, 80, 65, 80, moveList.DragonRage, moveList.Slash, moveList.Growl, moveList.Flamethrower)
Charizard = pokemon.Pokemon(6, "Charizard", 'FIR', 'FLY', 0, 78, 78, 84, 78, 109, 85, 100, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)

Squirtle = pokemon.Pokemon(7, "Squirtle", 'WTR', 'NONE', 0, 4400, 4400, 48, 65, 50, 64, 43, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)
Wartortle = pokemon.Pokemon(8, "Wartortle", 'WTR', 'NONE', 0, 59, 59, 63, 80, 65, 80, 58, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)
Blastoise = pokemon.Pokemon(9, "Blastoise", 'WTR', 'NONE', 0, 79, 79, 83, 100, 85, 105, 78, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)

Caterpie = pokemon.Pokemon(10, "Caterpie", "BUG", "NONE", 0, 45, 45, 30, 35, 20, 20, 45, moveList.Tackle, moveList.StringShot, moveList.Tackle, moveList.StringShot)
Metapod = pokemon.Pokemon(11, "Metapod", 'BUG', 'NONE', 0, 50, 50, 20, 55, 25, 25, 30, moveList.StringShot, moveList.BodySlam, moveList.Strength, moveList.Harden)
Butterfree = pokemon.Pokemon(12, "Butterfree", 'BUG', 'FLY', 0, 60, 60, 45, 50, 80, 80, 70, moveList.StringShot, moveList.QuickAttack, moveList.Gust, moveList.Swift)

Weedle = pokemon.Pokemon(13, "Weedle", 'BUG', 'PSN', 0, 40, 40, 35, 20, 20, 20, 50, moveList.Tackle, moveList.PoisonPowder, moveList.StringShot, moveList.Sludge)
Kakuna = pokemon.Pokemon(14, "Kakuna", 'BUG', 'PSN', 0, 45, 45, 25, 50, 25, 25, 35, moveList.BodySlam, moveList.PoisonGas, moveList.StringShot, moveList.Harden)
Beedrill = pokemon.Pokemon(15, "Beedrill", 'BUG', 'PSN', 0, 65, 65, 80, 40, 45, 80, 75, moveList.StringShot, moveList.PoisonGas, moveList.Smog, moveList.PoisonSting)

Pidgey = pokemon.Pokemon(16, "Pidgey", 'NRM', 'FLY', 0, 40, 40, 45, 40, 35, 35, 56, moveList.Peck, moveList.Gust, moveList.QuickAttack, moveList.Tackle)
Pidgeotto = pokemon.Pokemon(17, "Pidgeotto", 'NRM', 'FLY', 0, 63, 63, 60, 55, 50, 50, 71, moveList.DrillPeck, moveList.Gust, moveList.QuickAttack, moveList.BodySlam)
Pidgeot = pokemon.Pokemon(18, "Pidgeot", 'NRM', 'FLY', 0, 83, 83, 80, 75, 70, 70, 91, moveList.DrillPeck, moveList.Gust, moveList.Scratch, moveList.BodySlam)

Rattata = pokemon.Pokemon(19, "Rattata", 'NRM', 'NONE', 0, 30, 30, 56, 35, 25, 35, 72, moveList.Tackle, moveList.QuickAttack, moveList.TailWhip, moveList.Growl)
Raticate = pokemon.Pokemon(20, "Raticate", "NRM", "NONE", 0, 55, 55, 81, 60, 50, 70, 97, moveList.Tackle, moveList.Pound, moveList.BodySlam, moveList.Screech)

Spearow = pokemon.Pokemon(21, "Spearow", 'NRM', 'FLY', 0, 40, 40, 60, 30, 31, 31, 70, moveList.Scratch, moveList.Growl, moveList.Peck, moveList.QuickAttack)
Fearow = pokemon.Pokemon(22, "Fearow", 'NRM', 'FLY', 0, 65, 65, 90, 65, 61, 61, 100, moveList.QuickAttack, moveList.Slash, moveList.Growl, moveList.DrillPeck)

Ekans = pokemon.Pokemon(23, "Ekans", 'PSN', 'NONE', 0, 35, 35, 60, 44, 40, 54, 55, moveList.PoisonSting, moveList.PoisonGas, moveList.Smog, moveList.Tackle)
Arbok = pokemon.Pokemon(24, "Arbok", 'PSN', 'NONE', 0, 60, 60, 85, 69, 65, 79, 80, moveList.PoisonSting, moveList.PoisonGas, moveList.Smog, moveList.AcidArmor)

Pikachu = pokemon.Pokemon(25, "Pikachu", 'ELC', 'NONE', 0, 35, 35, 55, 30, 50, 40, 90, moveList.ThunderShock, moveList.Agility, moveList.TailWhip, moveList.ThunderWave)
Raichu = pokemon.Pokemon(26, "Raichu", 'ELC', 'NONE', 0, 60, 60, 90, 55, 90, 80, 100, moveList.Thunder, moveList.QuickAttack, moveList.ThunderWave, moveList.TailWhip)

Sandshrew = pokemon.Pokemon(27, "Sandshrew", 'GRD', 'NONE', 0, 50, 50, 75, 85, 20, 30, 40, moveList.BoneClub, moveList.Tackle, moveList.TailWhip, moveList.Scratch)
Sandslash = pokemon.Pokemon(28, "Sandslash", 'GRD', 'NONE', 0, 75, 75, 100, 110, 45, 55, 65, moveList.BoneClub, moveList.Earthquake, moveList.BodySlam, moveList.TailWhip)

Nidoran = pokemon.Pokemon(29, "Nidoran", "PSN", "NONE", 0, 55, 55, 47, 52, 40, 40, 41, moveList.Tackle, moveList.PoisonPowder, moveList.TailWhip, moveList.Scratch)
Nidorina = pokemon.Pokemon(30, "Nidorina", 'PSN', 'NONE', 0, 70, 70, 62, 67, 55, 55, 56, moveList.PoisonSting, moveList.PoisonPowder, moveList.TailWhip, moveList.Scratch)
Nidoqueen = pokemon.Pokemon(31, "Nidoqueen", 'PSN', 'GRD', 0, 90, 90, 82, 87, 75, 85, 76, moveList.PoisonPowder, moveList.PoisonSting, moveList.BoneClub, moveList.Earthquake)

Nidoran = pokemon.Pokemon(32, "Nidoran", "PSN", "NONE", 0, 55, 55, 47, 52, 40, 40, 41, moveList.Tackle, moveList.PoisonPowder, moveList.TailWhip, moveList.Scratch)
Nidorino = pokemon.Pokemon(33, "Nidorino", 'PSN', 'NONE', 0, 70, 70, 62, 67, 55, 55, 56, moveList.PoisonSting, moveList.PoisonPowder, moveList.TailWhip, moveList.Scratch)
Nidoking = pokemon.Pokemon(34, "Nidoking", 'PSN', 'GRD', 0, 90, 90, 82, 87, 75, 85, 76, moveList.PoisonPowder, moveList.PoisonSting, moveList.BoneClub, moveList.Earthquake)
#32, 33, 34
Clefairy = pokemon.Pokemon(35, "Clefairy", 'NRM', 'NONE', 0, 70, 70, 45, 48, 60, 65, 35, moveList.Tackle, moveList.Pound, moveList.Screech, moveList.Headbutt)
Clefable = pokemon.Pokemon(36, "Clefable", 'NRM', 'NONE', 0, 95, 95, 70, 73, 85, 90, 60, moveList.Tackle, moveList.Pound, moveList.Harden, moveList.BodySlam)

Vulpix = pokemon.Pokemon(37, "Vulpix", 'FIR', 'NONE', 0, 38, 38, 41, 40, 50, 65, 65, moveList.Tackle, moveList.TailWhip, moveList.Ember, moveList.Flamethrower)
Ninetales = pokemon.Pokemon(38, "Ninetales", 'FIR', 'NONE', 0, 73, 73, 76, 75, 81, 100, 100, moveList.FirePunch, moveList.BodySlam, moveList.Flamethrower, moveList.FireBlast)

Jigglypuff = pokemon.Pokemon(39, "Jigglypuff", 'NRM', 'NONE', 0, 115, 115, 45, 20, 45, 25, 20, moveList.Tackle, moveList.Pound, moveList.TailWhip, moveList.Headbutt)
Wigglytuff = pokemon.Pokemon(40, "Wigglytuff", 'NRM', 'NONE', 0, 140, 140, 70, 45, 75, 50, 45, moveList.Tackle, moveList.Pound, moveList.Harden, moveList.BodySlam)

Zubat = pokemon.Pokemon(41, "Zubat", 'PSN', 'FLY', 0, 40, 40, 45, 35, 30, 40, 55, moveList.PoisonPowder, moveList.Sludge, moveList.Gust, moveList.TailWhip)
Golbat = pokemon.Pokemon(42, "Golbat", 'PSN', 'FLY', 0, 75, 75, 80, 70, 65, 75, 90, moveList.PoisonGas, moveList.Smog, moveList.DrillPeck, moveList.Gust)

Oddish = pokemon.Pokemon(43, "Oddish", 'GRS', 'PSN', 0, 45, 45, 50, 55, 75, 65, 30, moveList.Tackle, moveList.Growl, moveList.Absorb, moveList.QuickAttack)
Gloom = pokemon.Pokemon(44, "Gloom", 'GRS', 'PSN', 0, 60, 60, 65, 70, 85, 75, 40, moveList.PoisonPowder, moveList.RazorLeaf, moveList.Tackle, moveList.Growl)
Vileplume = pokemon.Pokemon(45, "Vileplume", 'GRS', 'PSN', 0, 75, 75, 80, 85, 110, 90, 50, moveList.SwordsDance, moveList.RazorLeaf, moveList.PoisonPowder, moveList.Cut)

Paras = pokemon.Pokemon(46, "Paras", 'BUG', 'GRS', 0, 35, 35, 70, 55, 45, 55, 25, moveList.Scratch, moveList.Growl, moveList.Ember, moveList.QuickAttack)
Parasect = pokemon.Pokemon(47, "Parasect", 'BUG', 'GRS', 0, 60, 60, 95, 80, 60, 80, 30, moveList.DragonRage, moveList.Slash, moveList.Growl, moveList.Flamethrower)

Venonat = pokemon.Pokemon(48, "Venonat", 'BUG', 'PSN', 0, 60, 60, 55, 50, 40, 55, 45, moveList.Flamethrower, moveList.Earthquake, moveList.Strength, moveList.SwordsDance)
Venomoth = pokemon.Pokemon(49, "Venomoth", 'BUG', 'PSN', 0, 70, 70, 65, 60, 90, 75, 90, moveList.Bubble, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)

Diglett = pokemon.Pokemon(50, "Diglett", 'GRD', 'NONE', 0, 10, 10, 55, 25, 35, 45, 95, moveList.WaterGun, moveList.Bite, moveList.TailWhip, moveList.BubbleBeam)
Dugtrio = pokemon.Pokemon(51, "Dugtrio", 'GRD', 'NONE', 0, 35, 35, 100, 50, 50, 70, 120, moveList.HydroPump, moveList.Surf, moveList.Blizzard, moveList.TailWhip)

Meowth = pokemon.Pokemon(52, "Meowth", 'NRM', 'NONE', 0, 40, 40, 45, 35, 40, 40, 90, moveList.Tackle, moveList.Growl, moveList.Absorb, moveList.QuickAttack)
Persian = pokemon.Pokemon(53, "Persian", 'NRM', 'NONE', 0, 65, 65, 70, 60, 65, 65, 115, moveList.PoisonPowder, moveList.RazorLeaf, moveList.Tackle, moveList.Growl)

Psyduck = pokemon.Pokemon(54, "Psyduck", 'WTR', 'NONE', 0, 50, 50, 52, 48, 65, 50, 55, moveList.WaterGun, moveList.BubbleBeam, moveList.Tackle, moveList.Growl)
Golduck = pokemon.Pokemon(55, "Golduck", 'WTR', 'NONE', 0, 80, 80, 82, 78, 95, 80, 85, moveList.HydroPump, moveList.Growl, moveList.Surf, moveList.BubbleBeam)

Mankey = pokemon.Pokemon(56, "Mankey", 'FGT', 'NONE', 0, 40, 40, 80, 35, 35, 45, 70, moveList.KarateChop, moveList.Pound, moveList.Tackle, moveList.BodySlam)
Primeape = pokemon.Pokemon(57, "Primeape", 'FGT', 'NONE', 0, 65, 65, 105, 60, 60, 70, 95, moveList.KarateChop, moveList.Headbutt, moveList.RollingKick, moveList.BodySlam)

Growlithe = pokemon.Pokemon(58, "Growlithe", 'FIR', 'NONE', 0, 55, 55, 70, 45, 70, 50, 60, moveList.Ember, moveList.Tackle, moveList.TailWhip, moveList.QuickAttack)
Arcanine = pokemon.Pokemon(59, "Arcanine", 'FIR', 'NONE', 0, 90, 90, 110, 80, 100, 80, 95, moveList.Flamethrower, moveList.FireBlast, moveList.FirePunch, moveList.BodySlam)

Poliwag = pokemon.Pokemon(60, "Poliwag", 'WTR', 'NONE', 0, 40, 40, 50, 40, 40, 40, 90, moveList.HydroPump, moveList.Surf, moveList.Tackle, moveList.TailWhip)
Poliwhirl = pokemon.Pokemon(61, "Poliwhirl", 'WTR', 'NONE', 0, 65, 65, 65, 65, 50, 50, 90, moveList.HydroPump, moveList.Surf, moveList.BodySlam, moveList.Growl)
Poliwrath = pokemon.Pokemon(62, "Poliwrath", 'WTR', 'FGT', 0, 90, 90, 95, 95, 70, 90, 70, moveList.HydroPump, moveList.RollingKick, moveList.KarateChop, moveList.CrabHammer)

Abra = pokemon.Pokemon(63, "Abra", 'PSY', 'NONE', 0, 25, 25, 20, 15, 105, 55, 90, moveList.Confusion, moveList.Meditate, moveList.Swift, moveList.TailWhip)
Kadabra = pokemon.Pokemon(64, "Kadabra", 'PSY', 'NONE', 0, 40, 40, 35, 30, 120, 70, 105, moveList.Confusion, moveList.Meditate, moveList.Amnesia, moveList.Psybeam)
Alakazam = pokemon.Pokemon(65, "Alakazam", 'PSY', 'NONE', 0, 55, 55, 50, 45, 135, 95, 120, moveList.Confusion, moveList.Psychic, moveList.Amnesia, moveList.Psybeam)

Machop = pokemon.Pokemon(66, "Machop", 'FGT', 'NONE', 0, 70, 70, 80, 50, 35, 35, 35, moveList.KarateChop, moveList.Tackle, moveList.Pound, moveList.Strength)
Machoke = pokemon.Pokemon(67, "Machoke", 'FGT', 'NONE', 0, 80, 80, 100, 70, 50, 60, 45, moveList.KarateChop, moveList.BodySlam, moveList.RollingKick, moveList.Stomp)
Machamp = pokemon.Pokemon(68, "Machamp", 'FGT', 'NONE', 0, 90, 90, 130, 80, 65, 85, 55, moveList.KarateChop, moveList.BodySlam, moveList.RollingKick, moveList.Slam)

Bellsprout = pokemon.Pokemon(69, "Bellsprout", 'GRS', 'PSN', 0, 50, 50, 75, 35, 70, 30, 40, moveList.Smog, moveList.Spore, moveList.TailWhip, moveList.Tackle)
Weepinbell = pokemon.Pokemon(70, "Weepinbell", 'GRS', 'PSN', 0, 65, 65, 90, 50, 85, 45, 55, moveList.Sludge, moveList.Spore, moveList.PoisonGas, moveList.RazorLeaf)
Victreebel = pokemon.Pokemon(71, "Victreebel", 'GRS', 'PSN', 0, 80, 80, 105, 65, 100, 60, 70, moveList.Sludge, moveList.Spore, moveList.StunSpore, moveList.RazorLeaf)

Tentacool = pokemon.Pokemon(72, "Tentacool", 'WTR', 'PSN', 0, 40, 40, 40, 35, 50, 100, 70, moveList.WaterGun, moveList.Bubble, moveList.PoisonSting, moveList.Smog)
Tentacruel = pokemon.Pokemon(73, "Tentacruel", 'WTR', 'PSN', 0, 80, 80, 70, 65, 80, 120, 100, moveList.HydroPump, moveList.BubbleBeam, moveList.PoisonGas, moveList.Sludge)

Geodude = pokemon.Pokemon(74, "Geodude", 'RCK', 'GRD', 0, 40, 40, 80, 100, 30, 30, 20, moveList.RockSlide, moveList.Tackle, moveList.BoneClub, moveList.Growl)
Graveler = pokemon.Pokemon(75, "Graveler", 'RCK', 'GRD', 0, 55, 55, 95, 115, 45, 45, 35, moveList.RockSlide, moveList.BodySlam, moveList.BoneClub, moveList.Earthquake)
Golem = pokemon.Pokemon(76, "Golem", 'RCK', 'GRD', 0, 80, 80, 120, 130, 55, 65, 45, moveList.RockSlide, moveList.Fissure, moveList.BoneClub, moveList.Earthquake)

Ponyta = pokemon.Pokemon(77, "Ponyta", 'FIR', 'NONE', 0, 50, 50, 85, 55, 65, 65, 90, moveList.Ember, moveList.Flamethrower, moveList.Tackle, moveList.BodySlam)
Rapidash = pokemon.Pokemon(78, "Rapidash", 'FIR', 'NONE', 0, 65, 65, 100, 70, 80, 80, 105, moveList.FireBlast, moveList.Flamethrower, moveList.BodySlam, moveList.FirePunch)

Slowpoke = pokemon.Pokemon(79, "Slowpoke", 'WTR', 'PSY', 0, 90, 90, 65, 65, 40, 40, 15, moveList.WaterGun, moveList.Bubble, moveList.TailWhip, moveList.Confusion)
Slowbro = pokemon.Pokemon(80, "Slowbro", 'WTR', 'PSY', 0, 95, 95, 75, 110, 100, 80, 30, moveList.HydroPump, moveList.Surf, moveList.BubbleBeam, moveList.Hypnosis)

Magnemite = pokemon.Pokemon(81, "Magnemite", 'ELC', 'STL', 0, 25, 25, 35, 70, 95, 55, 45, moveList.ThunderShock, moveList.ThunderWave, moveList.Tackle, moveList.Harden)
Magneton = pokemon.Pokemon(82, "Magneton", 'ELC', 'STL', 0, 50, 50, 60, 95, 120, 70, 70, moveList.ThunderShock, moveList.ThunderWave, moveList.Thunder, moveList.Harden)

Farfetchd = pokemon.Pokemon(83, "Farfetchd", 'NRM', 'FLY', 0, 52, 52, 90, 55, 58, 62, 60, moveList.Tackle, moveList.QuickAttack, moveList.Gust, moveList.DrillPeck)

Doduo = pokemon.Pokemon(84, "Doduo", 'NRM', 'FLY', 0, 35, 35, 85, 45, 35, 35, 75, moveList.Tackle, moveList.Gust, moveList.Scratch, moveList.Peck)
Dodrio = pokemon.Pokemon(85, "Dodrio", 'NRM', 'FLY', 0, 60, 60, 110, 70, 60, 60, 110, moveList.Slam, moveList.Gust, moveList.Slash, moveList.DrillPeck)

Seel = pokemon.Pokemon(86, "Seel", 'WTR', 'NONE', 0, 65, 65, 45, 55, 45, 70, 45, moveList.WaterGun, moveList.Bubble, moveList.TailWhip, moveList.Tackle)
Dewgong = pokemon.Pokemon(87, "Dewgong", 'WTR', 'ICE', 0, 90, 90, 70, 80, 70, 95, 70, moveList.HydroPump, moveList.Surf, moveList.AuroraBeam, moveList.Blizzard)

Grimer = pokemon.Pokemon(88, "Grimer", 'PSN', 'NONE', 0, 80, 80, 80, 50, 40, 50, 25, moveList.Smog, moveList.Tackle, moveList.PoisonPowder, moveList.SwordsDance)
Muk = pokemon.Pokemon(89, "Muk", 'PSN', 'NONE', 0, 105, 105, 105, 75, 65, 100, 50, moveList.Sludge, moveList.Acid, moveList.PoisonGas, moveList.SwordsDance)

Shellder = pokemon.Pokemon(90, "Shellder", 'WTR', 'NONE', 0, 30, 30, 65, 100, 45, 25, 40, moveList.WaterGun, moveList.Bubble, moveList.Harden, moveList.Tackle)
Cloyster = pokemon.Pokemon(91, "Cloyster", 'WTR', 'ICE', 0, 50, 50, 95, 180, 85, 45, 70, moveList.HydroPump, moveList.Surf, moveList.AuroraBeam, moveList.Blizzard)

Gastly = pokemon.Pokemon(92, "Gastly", 'GHT', 'PSN', 0, 30, 30, 35, 30, 100, 35, 80, moveList.Lick, moveList.PoisonPowder, moveList.Tackle, moveList.Growl)
Haunter = pokemon.Pokemon(93, "Haunter", 'GHT', 'PSN', 0, 45, 45, 50, 45, 115, 55, 95, moveList.Lick, moveList.PoisonGas, moveList.PoisonPowder, moveList.Slash)
Gengar = pokemon.Pokemon(94, "Gengar", 'GHT', 'PSN', 0, 60, 60, 65, 60, 130, 75, 110, moveList.Lick, moveList.PoisonGas, moveList.Sludge, moveList.Acid)

Onix = pokemon.Pokemon(95, "Onix", 'RCK', 'GRD', 0, 35, 35, 45, 160, 30, 45, 70, moveList.RockSlide, moveList.BoneClub, moveList.Earthquake, moveList.Slam)

Drowzee = pokemon.Pokemon(96, "Drowzee", 'PSY', 'NONE', 0, 60, 60, 48, 45, 43, 90, 42, moveList.Agility, moveList.Barrier, moveList.BodySlam, moveList.Pound)
Hypno = pokemon.Pokemon(97, "Hypno", 'PSY', 'NONE', 0, 85, 85, 73, 70, 73, 115, 67, moveList.Agility, moveList.Amnesia, moveList.Psybeam, moveList.Psychic)

Krabby = pokemon.Pokemon(98, "Krabby", 'WTR', 'NONE', 0, 30, 30, 105, 90, 25, 25, 50, moveList.WaterGun, moveList.Bubble, moveList.TailWhip, moveList.Tackle)
Kingler = pokemon.Pokemon(99, "Kingler", 'WTR', 'NONE', 0, 55, 55, 130, 115, 50, 50, 75, moveList.HydroPump, moveList.Surf, moveList.BubbleBeam, moveList.CrabHammer)

Voltorb = pokemon.Pokemon(100, "Voltorb", 'ELC', 'NONE', 0, 40, 40, 30, 50, 55, 55, 100, moveList.Tackle, moveList.BodySlam, moveList.ThunderShock, moveList.ThunderWave)
Electrode = pokemon.Pokemon(101, "Electrode", 'ELC', 'NONE', 0, 60, 60, 50, 70, 80, 80, 150, moveList.ThunderShock, moveList.Slam, moveList.Thunder, moveList.ThunderPunch)

Exeggcute = pokemon.Pokemon(102, "Exeggcute", 'GRS', 'PSY', 0, 60, 60, 40, 80, 60, 45, 40, moveList.Agility, moveList.RazorLeaf, moveList.Tackle, moveList.Growl)
Exeggutor = pokemon.Pokemon(103, "Exeggutor", 'GRS', 'PSY', 0, 95, 95, 95, 85, 125, 75, 55, moveList.Agility, moveList.RazorLeaf, moveList.Psybeam, moveList.Hypnosis)

Cubone = pokemon.Pokemon(104, "Cubone", 'GRD', 'NONE', 0, 50, 50, 50, 95, 40, 50, 35, moveList.BoneClub, moveList.Growl, moveList.Tackle, moveList.QuickAttack)
Marowak = pokemon.Pokemon(105, "Marowak", 'GRD', 'NONE', 0, 60, 60, 80, 110, 50, 80, 45, moveList.BoneClub, moveList.Earthquake, moveList.Growl, moveList.Slam)

Hitmonlee = pokemon.Pokemon(106, "Hitmonlee", 'FGT', 'NONE', 0, 50, 50, 120, 53, 35, 110, 87, moveList.KarateChop, moveList.Tackle, moveList.Strength, moveList.SwordsDance)
Hitmonchan = pokemon.Pokemon(107, "Hitmonchan", 'FGT', 'NONE', 0, 50, 50, 105, 79, 35, 110, 76, moveList.KarateChop, moveList.Slam, moveList.RollingKick, moveList.SwordsDance)

Lickitung = pokemon.Pokemon(108, "Lickitung", 'NRM', 'NONE', 0, 90, 90, 55, 75, 60, 45, 35, moveList.BodySlam, moveList.LovelyKiss, moveList.Stomp, moveList.Headbutt)

Koffing = pokemon.Pokemon(109, "Koffing", 'PSN', 'NONE', 0, 40, 40, 65, 95, 60, 45, 35, moveList.Smog, moveList.PoisonPowder, moveList.Tackle, moveList.TailWhip)
Weezing = pokemon.Pokemon(110, "Weezing", "PSN", "NONE", 0, 65, 65, 90, 120, 85, 70, 60, moveList.Smog, moveList.Sludge, moveList.PoisonGas, moveList.Slam)

Rhyhorn = pokemon.Pokemon(111, "Rhyhorn", "GRD", "RCK", 0, 80, 80, 85, 95, 30, 30, 25, moveList.RockSlide, moveList.Harden, moveList.BoneClub, moveList.Tackle)
Rhydon = pokemon.Pokemon(112, "Rhydon", 'GRD', 'RCK', 0, 105, 105, 130, 120, 45, 45, 40, moveList.RockSlide, moveList.Earthquake, moveList.BoneClub, moveList.BodySlam)

Chansey = pokemon.Pokemon(113, "Chansey", 'NRM', 'NONE', 0, 250, 250, 5, 5, 35, 105, 50, moveList.Tackle, moveList.EggBomb, moveList.Harden, moveList.LovelyKiss)

Tangela = pokemon.Pokemon(114, "Tangela", 'GRS', 'NONE', 0, 65, 65, 55, 115, 100, 40, 60, moveList.RazorLeaf, moveList.Spore, moveList.Tackle, moveList.Harden)

Kangaskhan = pokemon.Pokemon(115, "Kangaskhan", 'NRM', 'NONE', 0, 105, 105, 95, 80, 40, 80, 90, moveList.BodySlam, moveList.HornAttack, moveList.Growl, moveList.Strength)

Horsea = pokemon.Pokemon(116, "Horsea", 'WTR', 'NONE', 0, 30, 30, 40, 70, 70, 25, 60, moveList.WaterGun, moveList.Bubble, moveList.Strength, moveList.SwordsDance)
Seadra = pokemon.Pokemon(117, "Seadra", 'WTR', 'NONE', 0, 55, 55, 65, 95, 95, 45, 85, moveList.BubbleBeam, moveList.HydroPump, moveList.Surf, moveList.SwordsDance)

Goldeen = pokemon.Pokemon(118, "Goldeen", 'WTR', 'NONE', 0, 45, 45, 67, 60, 35, 50, 63, moveList.WaterGun, moveList.Bubble, moveList.Swift, moveList.SwordsDance)
Seaking = pokemon.Pokemon(119, "Seaking", 'WTR', 'NONE', 0, 80, 80, 92, 65, 65, 80, 68, moveList.HydroPump, moveList.Surf, moveList.BubbleBeam, moveList.Screech)

Staryu = pokemon.Pokemon(120, "Staryu", "WTR", "NONE", 0, 30, 30, 45, 55, 70, 55, 85, moveList.WaterGun, moveList.Bubble, moveList.Screech, moveList.Tackle)
Starmie = pokemon.Pokemon(121, "Starmie", 'WTR', 'PSY', 0, 60, 60, 75, 85, 100, 85, 115, moveList.HydroPump, moveList.BubbleBeam, moveList.Psybeam, moveList.Agility)

MrMime = pokemon.Pokemon(122, "MrMime", 'PSY', 'NRM', 0, 40, 40, 45, 65, 100, 120, 90, moveList.Confusion, moveList.QuickAttack, moveList.Psychic, moveList.Agility)

Scyther = pokemon.Pokemon(123, "Scyther", 'BUG', 'FLY', 0, 70, 70, 110, 80, 55, 80, 105, moveList.DrillPeck, moveList.Gust, moveList.StringShot, moveList.SwordsDance)
Jynx = pokemon.Pokemon(124, "Jynx", 'ICE', 'PSY', 0, 65, 65, 50, 35, 115, 95, 95, moveList.AuroraBeam, moveList.Blizzard, moveList.Psychic, moveList.Confusion)

Electabuzz = pokemon.Pokemon(125, "Electabuzz", 'ELC', 'NONE', 0, 65, 65, 83, 57, 95, 85, 105, moveList.ThunderShock, moveList.Sharpen, moveList.ThunderShock, moveList.ThunderWave)

Magmar = pokemon.Pokemon(126, "Magmar", 'FIR', 'NONE', 0, 65, 65, 95, 57, 100, 85, 93, moveList.Ember, moveList.FireBlast, moveList.Growl, moveList.BodySlam)

Pinsir = pokemon.Pokemon(127, "Pinsir", 'BUG', 'NONE', 0, 65, 65, 125, 100, 55, 70, 75, moveList.StringShot, moveList.QuickAttack, moveList.LovelyKiss, moveList.SelfDestruct)

Tauros = pokemon.Pokemon(128, "Tauros", 'NRM', 'NONE', 0, 75, 75, 100, 95, 40, 70, 110, moveList.Glare, moveList.QuickAttack, moveList.HornAttack, moveList.TailWhip)

Magikarp = pokemon.Pokemon(129, "Magikarp", "WTR", "NONE", 0, 20, 20, 10, 55, 15, 20, 80, moveList.Bubble, moveList.Surf, moveList.Tackle, moveList.Harden)
Gyarados = pokemon.Pokemon(130, "Gyarados", 'WTR', 'FLY', 0, 95, 95, 125, 79, 60, 100, 81, moveList.DrillPeck, moveList.Gust, moveList.HydroPump, moveList.WaterGun)

Lapras = pokemon.Pokemon(131, "Lapras", 'WTR', 'ICE', 0, 130, 130, 85, 80, 85, 95, 60, moveList.AuroraBeam, moveList.Blizzard, moveList.HydroPump, moveList.Surf)

Ditto = pokemon.Pokemon(132, "Ditto", 'NRM', 'NONE', 0, 48, 48, 48, 48, 48, 48, 48, moveList.Tackle, moveList.QuickAttack, moveList.Headbutt, moveList.DefenseCurl)

Eevee = pokemon.Pokemon(133, "Eevee", 'NRM', 'NONE', 0, 550, 550, 55, 50, 45, 65, 55, moveList.Pound, moveList.Harden, moveList.SwordsDance, moveList.Growl)
Vaporeon = pokemon.Pokemon(134, "Vaporeon", 'WTR', 'NONE', 0, 130, 130, 65, 60, 110, 95, 65, moveList.BubbleBeam, moveList.WaterGun, moveList.Headbutt, moveList.QuickAttack)
Jolteon = pokemon.Pokemon(135, "Jolteon", 'ELC', 'NONE', 0, 65, 65, 65, 60, 110, 95, 130, moveList.SwordsDance, moveList.LovelyKiss, moveList.Thunder, moveList.ThunderShock)
Flareon = pokemon.Pokemon(136, "Flareon", 'FIR', 'NONE', 0, 65, 65, 130, 60, 95, 110, 65, moveList.Swift, moveList.FireBlast, moveList.FirePunch, moveList.Slash)

Porygon = pokemon.Pokemon(137, "Porygon", 'NRM', 'NONE', 0, 65, 65, 60, 70, 85, 75, 40, moveList.QuickAttack, moveList.EggBomb, moveList.SwordsDance, moveList.HornAttack)

Omanyte = pokemon.Pokemon(138, "Omanyte", 'RCK', 'WTR', 0, 35, 35, 40, 100, 90, 55, 35, moveList.Bubble, moveList.CrabHammer, moveList.Surf, moveList.RockSlide)
Omastar = pokemon.Pokemon(139, "Omastar", 'RCK', 'WTR', 0, 70, 70, 60, 125, 115, 70, 55, moveList.Bubble, moveList.CrabHammer, moveList.Surf, moveList.RockSlide)

Kabuto = pokemon.Pokemon(140, "Kabuto", 'RCK', 'WTR', 0, 30, 30, 80, 90, 55, 45, 55, moveList.RockSlide, moveList.Surf, moveList.HydroPump, moveList.BubbleBeam)
Kabutops = pokemon.Pokemon(141, "Kabutops", 'RCK', 'WTR', 0, 60, 60, 115, 105, 65, 70, 80, moveList.RockSlide, moveList.Surf, moveList.HydroPump, moveList.BubbleBeam)

Aerodactyl = pokemon.Pokemon(142, "Aerodactyl", 'RCK', 'FLY', 0, 80, 80, 105, 65, 60, 75, 130, moveList.DrillPeck, moveList.Gust, moveList.RockSlide, moveList.Peck)

Snorlax = pokemon.Pokemon(143, "Snorlax", 'NRM', 'NONE', 0, 160, 160, 110, 65, 65, 110, 30, moveList.Tackle, moveList.Tackle, moveList.Glare, moveList.SelfDestruct)

Articuno = pokemon.Pokemon(144, "Articuno", 'ICE', 'FLY', 0, 90, 90, 85, 100, 95, 125, 85, moveList.Gust, moveList.DrillPeck, moveList.AuroraBeam, moveList.Blizzard)

Zapdos = pokemon.Pokemon(145, "Zapdos", 'ELC', 'FLY', 0, 90, 90, 90, 85, 125, 85, 90, moveList.Gust, moveList.Peck, moveList.ThunderShock, moveList.ThunderWave)

Moltres = pokemon.Pokemon(146, "Moltres", 'FIR', 'FLY', 0, 90, 90, 100, 90, 125, 85, 90, moveList.DrillPeck, moveList.Flamethrower, moveList.Gust, moveList.FireBlast)

Dratini = pokemon.Pokemon(147, "Dratini", 'DRG', 'NONE', 0, 41, 41, 64, 45, 50, 50, 50, moveList.DragonRage, moveList.QuickAttack, moveList.Swift, moveList.SwordsDance)
Dragonair = pokemon.Pokemon(148, "Dragonair", 'DRG', 'NONE', 0, 61, 61, 84, 65, 70, 70, 70, moveList.DragonRage, moveList.QuickAttack, moveList.Swift, moveList.SwordsDance)
Dragonite = pokemon.Pokemon(149, "Dragonite", 'DRG', 'FLY', 0, 91, 91, 134, 95, 100, 100, 80, moveList.DragonRage, moveList.DrillPeck, moveList.Gust, moveList.Peck)

Mewtwo = pokemon.Pokemon(150, "Mewtwo", 'PSY', 'NONE', 0, 106, 106, 110, 90, 154, 90, 130, moveList.Hypnosis, moveList.Psychic, moveList.QuickAttack, moveList.Headbutt)

Mew = pokemon.Pokemon(151, "Mew", 'PSY', 'NONE', 0, 100, 100, 100, 100, 100, 100, 100, moveList.Hypnosis, moveList.Psychic, moveList.Amnesia, moveList.Confusion)

Pokedex = [Bulbasaur, Ivysaur, Venusaur, Charmander, Charmeleon, Charizard, Squirtle, Wartortle, Blastoise, Caterpie, Metapod, Butterfree, Weedle, Kakuna, Beedrill, Pidgey, Pidgeotto, Pidgeot, Rattata, Raticate, Spearow, Fearow, Ekans, Arbok, Pikachu, Raichu, Sandshrew, Sandslash, Nidoran, Nidorina, Nidoqueen, Nidoran, Nidorina, Nidoking, Clefairy, Clefable, Vulpix, Ninetales, Jigglypuff, Wigglytuff, Zubat, Golbat, Oddish, Gloom, Vileplume, Paras, Parasect, Venonat, Venomoth, Diglett, Dugtrio, Meowth, Persian, Psyduck, Golduck, Mankey, Primeape, Growlithe, Arcanine, Poliwag, Poliwhirl, Poliwrath, Abra, Kadabra, Alakazam, Machop, Machoke, Machamp, Bellsprout, Weepinbell, Victreebel, Tentacool, Tentacruel, Geodude, Graveler, Golem, Ponyta, Rapidash, Slowpoke, Slowbro, Magnemite, Magneton, Farfetchd, Doduo, Dodrio, Seel, Dewgong, Grimer, Muk, Shellder, Cloyster, Gastly, Haunter, Gengar, Onix, Drowzee, Hypno, Krabby, Kingler, Voltorb, Electrode, Exeggcute, Exeggutor, Cubone, Marowak, Hitmonlee, Hitmonchan, Lickitung, Koffing, Weezing, Rhyhorn, Rhydon, Chansey, Tangela, Kangaskhan, Horsea, Seadra, Goldeen, Seaking, Staryu, Starmie, MrMime, Scyther, Jynx, Electabuzz, Magmar, Pinsir, Tauros, Magikarp, Gyarados, Lapras, Ditto, Eevee, Vaporeon, Jolteon, Flareon, Porygon, Omanyte, Omastar, Kabuto, Kabutops, Aerodactyl, Snorlax, Articuno, Zapdos, Moltres, Dratini, Dragonair, Dragonite, Mewtwo, Mew]

first_gen = [Bulbasaur, Charmander, Squirtle, 
            Caterpie, Weedle, Pidgey, Rattata,
            Spearow, Ekans, Pikachu, Sandshrew, 
            Nidoran,Nidoran, Clefairy, Vulpix, Jigglypuff,
            Zubat, Oddish, Paras, Venonat, Diglett, 
            Meowth, Psyduck, Mankey, Growlithe, 
            Poliwag, Abra, Machop, Bellsprout, 
            Tentacool, Geodude, Ponyta, Slowpoke,
            Magnemite, Seel, Grimer, Shellder,
            Gastly, Drowzee, Krabby, Voltorb,
            Exeggcute, Cubone, Hitmonlee, 
            Koffing, Rhyhorn, Horsea, Goldeen,
            Staryu, Scyther, Magikarp, Eevee, 
            Omanyte, Kabuto, Dratini, Doduo
]
second_gen = [Ivysaur, Charmeleon, Wartortle,
              Metapod, Kakuna, Pidgeotto, 
              Nidorina,Nidorino, Gloom, Poliwhirl, 
              Machoke, Weepinbell, Graveler,
              Haunter, Dragonair
]

third_gen = [Venusaur, Charizard, Blastoise,
            Butterfree, Beedrill, Nidoqueen, Nidoking,
            Vileplume, Poliwrath, Alakazam, 
            Machamp, Victreebel, Golem, 
            Gengar, Dragonite
]

second_final_gen = [Raticate, Fearow, Arbok,
                    Raichu, Sandslash, Clefable,
                    Ninetales, Wigglytuff, Golbat,
                    Parasect, Venomoth, Dugtrio,
                    Persian, Golduck, Primeape,
                    Slowbro, Magneton, Dewgong,
                    Muk, Cloyster, Hypno, Kingler,
                    Electrode, Exeggutor, Marowak, 
                    Hitmonchan, Weezing, Rhydon, 
                    Seadra, Seaking, Starmie, 
                    Jynx, Gyarados, Omastar, 
                    Kabutops, Dodrio
]
 
only_gen = [Farfetchd, Onix, Lickitung, Chansey, 
            Tangela, Kangaskhan, MrMime,
            Electabuzz, Magmar, Pinsir, 
            Tauros, Lapras, Ditto, Porygon, 
            Aerodactyl, Snorlax, Articuno, 
            Zapdos, Moltres, Mewtwo, Mew
]

eevee_evol = [Vaporeon, Jolteon, Flareon]