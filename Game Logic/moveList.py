import moves
import pokemon

# Default move
NOMOVE = moves.Move("Nomove", 0, -10, "NONE", 0, "NRM", "ST")

# Normal type moves


BodySlam = moves.Move("Bodyslam", 85, 0, "ENEMY PRZ 10", 100, "NRM", "PH")
Cut = moves.Move("Cut", 50, 0, "NONE", 95, "NRM", "PH")
DefenseCurl = moves.Move("Defensecurl", 0, 0, "USER DEF 1", 100, "NRM", "ST")
EggBomb = moves.Move("Eggbomb", 100, 0, "NONE", 75, "NRM", "PH")
Explosion = moves.Move("Explosion", 250, 0, "USER HP -10000", 100, "NRM", "PH")
Glare = moves.Move("Glare", 0, 0, "ENEMY PRZ 100", 100, "NRM", "ST")
Growl = moves.Move("Growl", 0, 0, "ENEMY ATK -1", 100, "NRM", "ST")
Harden = moves.Move("Harden", 0, 0, "USER DEF 1", 100, "NRM", "ST")
Headbutt = moves.Move("Headbutt", 70, 0, "NONE", 100, "NRM", "PH")
HornAttack = moves.Move("Hornattack", 65, 0, "NONE", 100, "NRM", "PH")
HyperFang = moves.Move("Hyperfang", 80, 0, "NONE", 90, "NRM", "PH")
LovelyKiss = moves.Move("Lovelykiss", 0, 0, "ENEMY SLP 100", 75, "NRM", "ST")
Pound = moves.Move("Pound", 40, 0, "NONE", 100, "NRM", "PH")
QuickAttack = moves.Move("Quickattack", 40, 1, "NONE", 100 , "NRM", "PH")
Scratch = moves.Move("Scratch", 40, 0, "NONE", 100,  "NRM", "PH")
Screech = moves.Move("Screech", 0, 0, "ENEMY DEF -2", 100, "NRM", "ST")
SelfDestruct = moves.Move("Selfdestruct", 200, 0, "USER HP -10000", 100, "NRM", "PH")
Sharpen = moves.Move("Sharpen", 0, 0, "USER ATK 1", 100, "NRM", "ST")
Slam = moves.Move("Slam", 80, 0, "NONE", 75, "NRM", 'PH')
Slash = moves.Move("Slash", 70, 0, "NONE", 100, "NRM", "PH")
SonicBoom = moves.Move("Sonicboom", 0, 0, "ENEMY HP -20", 100, "NRM", "SP")
Stomp = moves.Move("Stomp", 65, 0, "NONE", 100, "NRM", "PH")
Strength = moves.Move("Strength", 80, 0, "NONE", 100, "NRM", "PH")
Swift = moves.Move("Swift", 60, 0, "NONE", 100, "NRM", "SP")
SwordsDance = moves.Move("Swordsdance", 0, 0, "USER ATK 2", 100, "NRM", "ST")
Tackle = moves.Move("Tackle", 40, 0, "NONE", 100, "NRM", "PH")
TailWhip = moves.Move("Tailwhip", 0, 0, "ENEMY DEF -1", 100, "NRM", "ST")
# Grass type move
Absorb = moves.Move("Absorb", 20, 0, "USER HP+", 100, "GRS", "SP")
RazorLeaf = moves.Move("Razorleaf", 55, 0, "NONE", 95, "GRS", "PH")
Spore = moves.Move("Spore", 0, 0, "ENEMY SLP 100", 100, "GRS", "ST")
StunSpore = moves.Move("Stunspore", 0, 0, "ENEMY PRZ 75", 100, "GRS", "ST")
# Water type move
WaterGun = moves.Move("Watergun", 40, 0, "NONE", 100 , "WTR", "SP")
HydroPump = moves.Move("Hydropump", 110, 0, "NONE", 80, "WTR", "SP")
Bubble = moves.Move("Bubble", 40, 0, "ENEMY SPD -1 10", 100 , "WTR", "SP")
BubbleBeam = moves.Move("Bubblebeam", 65, 0, "ENEMY SPD -1 10", 100 , "WTR", "SP")
CrabHammer = moves.Move("Crabhammer", 100, 0, "NONE", 90, "WTR", "PH")
Surf = moves.Move("Surf", 90, 0, "NONE", 100, "WTR", "SP")
# Fire type move
Ember = moves.Move("Ember", 40, 0, "ENEMY BRN 10", 100 ,"FIR", "SP")
Flamethrower = moves.Move("Flamethrower", 90, 0, "ENEMY BRN 10", 100, "FIR", "SP")
FireBlast = moves.Move("Fireblast", 110, 0, "ENEMY BRN 10", 85, "FIR", "SP")
FirePunch = moves.Move("Firepunch", 75, 0, "ENEMY BRN 10", 100, "FIR", "PH")
# Bug type move
StringShot = moves.Move("Stringshot", 0, 0, "ENEMY SPD -1", 95, "BUG", "ST")
# Poison type move
PoisonSting = moves.Move("Poisonsting", 15, 0, "ENEMY PSN 30", 100, "PSN", "PH")
Acid = moves.Move("Acid", 40, 0, "ENEMY SPDEF -1 10", 100, "PSN", "SP")
AcidArmor = moves.Move("Acidarmor", 0, 0, "USER DEF 2", 100, "PSN", "ST")
PoisonGas = moves.Move("Poisongas", 0, 0, "ENEMY PSN 90", 100, "PSN", "ST")
PoisonPowder = moves.Move("Poisonpowder", 0, 0, "ENEMY PSN 75", 100, "PSN", "ST")
Sludge = moves.Move("Sludge", 65, 0, "ENEMY PSN 30", 100, "PSN", "SP")
Smog = moves.Move("Smog", 30, 0, "ENEMY PSN 40", 70, "PSN", "SP")
# Electric type move
Thunder = moves.Move("Thunder", 110, 0, "ENEMY PRZ 30", 70, "ELC", "SP")
ThunderPunch = moves.Move("Thunderpunch", 75, 0, "ENEMY PRZ 10", 100, "ELC", "PH")
ThunderShock = moves.Move("Thundershock", 40, 0, "ENEMY PRZ 10", 100, "ELC", "SP")
ThunderWave = moves.Move("Thunderwave", 0, 0, "ENEMY PRZ 100", 90, "ELC", "ST")
# Ground type move
Earthquake = moves.Move("Earthquake", 100, 0, "NONE", 100, "GRD", "PH")
BoneClub = moves.Move("Boneclub", 65, 0, "NONE", 85, "GRD", "PH")
Fissure = moves.Move("Fissure", 0, 0, "ENEMY HP -10000", 30, "GRD", "PH")
# Fighting type move
KarateChop = moves.Move("Karatechop", 50, 0, "NONE", 100, "FGT", "PH")
RollingKick = moves.Move("Rollingkick", 60, 0, "NONE", 85, "FGT", "PH")
# Psychic type move
Agility = moves.Move("Agility", 0, 0, "USER SPD 2", 100, "PSY", "ST")
Hypnosis = moves.Move("Hypnosis", 0, 0, "ENEMY SLP 100", 60, "PSY", "ST")
Amnesia = moves.Move("Amnesia", 0, 0, "USER SPDEF 2", 100, "PSY", "ST")
Barrier = moves.Move("Barrier", 0, 0, "USER DEF 2", 100, "PSY", "ST")
Confusion = moves.Move("Confusion", 50, 0, "NONE", 100, "PSY", "SP")
Meditate = moves.Move("Meditate", 0, 0, "USER ATK 1", 100, "PSY", "ST")
Psybeam = moves.Move("Psybeam", 65, 0, "NONE", 100, "PSY", "SP")
Psychic = moves.Move("Psychic", 90, 0, "ENEMY SPDEF -1", 100, "PSY", "SP")
# Rock type move
RockSlide = moves.Move("Rockslide", 75, 0, "NONE", 90, "RCK", "PH")
# Ghost type move
Lick = moves.Move("Lick", 30, 0, "ENEMY PRZ 10", 100, "GHT", "PH")
# Ice type move
AuroraBeam = moves.Move("Aurorabeam", 65, 0, "ENEMY ATK -1 10", "100", "ICE", "SP")
Blizzard = moves.Move("Blizzard", 110, 0, "ENEMY FRZ 10", 70, "ICE", "SP")
# Dragon type move
DragonRage = moves.Move("Dragonrage", 0, 0, "ENEMY HP -40", 100, "DRG", "SP")
# Dark type move
Bite = moves.Move("Bite", 60, 0, "NONE", 100, "DRK", "PH")
# Steel type move
# Flying type move
DrillPeck = moves.Move("Drillpeck", 80, 0, "NONE", 100, "FLY", "PH")
Gust = moves.Move("Gust", 40, 0, "NONE", 100, "FLY", "SP")
Peck = moves.Move("Peck", 35, 0, "NONE", 100, "FLY", "PH")