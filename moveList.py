import moves
import pokemon

# Default move
NOMOVE = moves.Move("NOMOVE", 0, -10, "NONE", 0, "NRM", "ST")

# Normal type moves


BodySlam = moves.Move("BODYSLAM", 85, 0, "ENEMY PRZ 10", 100, "NRM", "PH");
Cut = moves.Move("CUT", 50, 0, "NONE", 95, "NRM", "PH");
DefenseCurl = moves.Move("DEFENSECURL", 0, 0, "USER DEF 1", 100, "NRM", "ST");
EggBomb = moves.Move("EGGBOMB", 100, 0, "NONE", 75, "NRM", "PH");
Explosion = moves.Move("EXPLOSION", 250, 0, "USER HP -10000", 100, "NRM", "PH");
Glare = moves.Move("GLARE", 0, 0, "ENEMY PRZ 100", 100, "NRM", "ST");
Growl = moves.Move("GROWL", 0, 0, "ENEMY ATK -1", 100, "NRM", "ST");
Harden = moves.Move("HARDEN", 0, 0, "USER DEF 1", 100, "NRM", "ST");
Headbutt = moves.Move("HEADBUTT", 70, 0, "NONE", 100, "NRM", "PH");
HornAttack = moves.Move("HORNATTACK", 65, 0, "NONE", 100, "NRM", "PH");
HyperFang = moves.Move("HYPERFANG", 80, 0, "NONE", 90, "NRM", "PH");
LovelyKiss = moves.Move("LOVELYKISS", 0, 0, "ENEMY SLP 100", 75, "NRM", "ST");
Pound = moves.Move("POUND", 40, 0, "NONE", 100, "NRM", "PH");
QuickAttack = moves.Move("QUICKATTACK", 40, 1, "NONE", 100 , "NRM", "PHY");
Scratch = moves.Move("SCRATCH", 40, 0, "NONE", 100,  "NRM", "PH");
Screech = moves.Move("SCREECH", 0, 0, "ENEMY DEF -2", 100, "NRM", "ST");
SelfDestruct = moves.Move("SELFDESTRUCT", 200, 0, "USER HP -10000", 100, "NRM", "PH");
Sharpen = moves.Move("SHARPEN", 0, 0, "USER ATK 1", 100, "NRM", "ST");
Slam = moves.Move("SLAM", 80, 0, "NONE", 75, "NRM", 'PH');
Slash = moves.Move("SLASH", 70, 0, "NONE", 100, "NRM", "PH");
SonicBoom = moves.Move("SONICBOOM", 0, 0, "ENEMY HP -20", 100, "NRM", "SP");
Stomp = moves.Move("STOMP", 65, 0, "NONE", 100, "NRM", "PH");
Strength = moves.Move("STRENGTH", 80, 0, "NONE", 100, "NRM", "PH");
Swift = moves.Move("SWIFT", 60, 0, "NONE", 100, "NRM", "SP");
SwordsDance = moves.Move("SWORDSDANCE", 0, 0, "USER ATK 2", 100, "NRM", "ST");
Tackle = moves.Move("TACKLE", 40, 0, "NONE", 100, "NRM", "PH");
TailWhip = moves.Move("TAILWHIP", 0, 0, "ENEMY DEF -1", 100, "NRM", "ST");


# Grass type moves

Absorb = moves.Move("ABSORB", 20, 0, "USER HP+", 100, "GRS", "SP");
RazorLeaf = moves.Move("RAZORLEAF", 55, 0, "NONE", 95, "GRS", "PH");
Spore = moves.Move("SPORE", 0, 0, "ENEMY SLP 100", 100, "GRS", "ST");
StunSpore = moves.Move("STUNSPORE", 0, 0, "ENEMY PRZ 75", 100, "GRS", "ST");

# Water type moves

WaterGun = moves.Move("WATERGUN", 40, 0, "NONE", 100 , "WTR", "SP");
HydroPump = moves.Move("HYDROPUMP", 110, 0, "NONE", 80, "WTR", "SP");
Bubble = moves.Move("BUBBLE", 40, 0, "ENEMY SPD -1 10", 100 , "WTR", "SP");
BubbleBeam = moves.Move("BUBBLEBEAM", 65, 0, "ENEMY SPD -1 10", 100 , "WTR", "SP");
CrabHammer = moves.Move("CRABHAMMER", 100, 0, "NONE", 90, "WTR", "PH");
Surf = moves.Move("SURF", 90, 0, "NONE", 100, "WTR", "SP");
# Fire type moves

Ember = moves.Move("EMBER", 40, 0, "ENEMY BRN 10", 100 ,"FIR", "SP");
Flamethrower = moves.Move("FLAMETHROWER", 90, 0, "ENEMY BRN 10", 100, "FIR", "SP");
FireBlast = moves.Move("FIREBLAST", 110, 0, "ENEMY BRN 10", 85, "FIR", "SP");
FirePunch = moves.Move("FIREPUNCH", 75, 0, "ENEMY BRN 10", 100, "FIR", "PH");

# Bug type moves

StringShot = moves.Move("STRINGSHOT", 0, 0, "ENEMY SPD -1", 95, "BUG", "ST");

# Poison type moves

PoisonSting = moves.Move("POISONSTING", 15, 0, "ENEMY PSN 30", 100, "PSN", "PH");
Acid = moves.Move("ACID", 40, 0, "ENEMY SPDEF -1 10", 100, "PSN", "SP");
AcidArmor = moves.Move("ACIDARMOR", 0, 0, "USER DEF 2", 100, "PSN", "ST");
PoisonGas = moves.Move("POISONGAS", 0, 0, "ENEMY PSN 90", 100, "PSN", "ST");
PoisonPowder = moves.Move("POISONPOWDER", 0, 0, "ENEMY PSN 75", 100, "PSN", "ST");
Sludge = moves.Move("SLUDGE", 65, 0, "ENEMY PSN 30", 100, "PSN", "SP");
Smog = moves.Move("SMOG", 30, 0, "ENEMY PSN 40", 70, "PSN", "SP");


# Electric type moves

Thunder = moves.Move("THUNDER", 110, 0, "ENEMY PRZ 30", 70, "ELC", "SP");
ThunderPunch = moves.Move("THUNDERPUNCH", 75, 0, "ENEMY PRZ 10", 100, "ELC", "PH");
ThunderShock = moves.Move("THUNDERSHOCK", 40, 0, "ENEMY PRZ 10", 100, "ELC", "SP");
ThunderWave = moves.Move("THUNDERWAVE", 0, 0, "ENEMY PRZ 100", 90, "ELC", "ST");

# Ground type moves

Earthquake = moves.Move("EARTHQUAKE", 100, 0, "NONE", 100, "GRD", "PH");
BoneClub = moves.Move("BONECLUB", 65, 0, "NONE", 85, "GRD", "PH");
Fissure = moves.Move("FISSURE", 0, 0, "ENEMY HP -10000", 30, "GRD", "PH");

# Fighting type moves
KarateChop = moves.Move("KARATECHOP", 50, 0, "NONE", 100, "FGT", "PH");
RollingKick = moves.Move("ROLLINGKICK", 60, 0, "NONE", 85, "FGT", "PH");

# Psychic type moves

Agility = moves.Move("AGILITY", 0, 0, "USER SPD 2", 100, "PSY", "ST");
Hypnosis = moves.Move("HYPNOSIS", 0, 0, "ENEMY SLP 100", 60, "PSY", "ST");
Amnesia = moves.Move("AMNESIA", 0, 0, "USER SPDEF 2", 100, "PSY", "ST");
Barrier = moves.Move("BARRIER", 0, 0, "USER DEF 2", 100, "PSY", "ST");
Confusion = moves.Move("CONFUSION", 50, 0, "NONE", 100, "PSY", "SP");
Meditate = moves.Move("MEDITATE", 0, 0, "USER ATK 1", 100, "PSY", "ST");
Psybeam = moves.Move("PSYBEAM", 65, 0, "NONE", 100, "PSY", "SP");
Psychic = moves.Move("PSYCHIC", 90, 0, "ENEMY SPDEF -1 10", 100, "PSY", "SP");


# Rock type moves
RockSlide = moves.Move("ROCKSLIDE", 75, 0, "NONE", 90, "RCK", "PH");


# Ghost type moves
Lick = moves.Move("LICK", 30, 0, "ENEMY PRZ 10", 100, "GHT", "PH");


# Ice type moves
AuroraBeam = moves.Move("AURORABEAM", 65, 0, "ENEMY ATK -1 10", "100", "ICE", "SP");
Blizzard = moves.Move("BLIZZARD", 110, 0, "ENEMY FRZ 10", 70, "ICE", "SP");


# Dragon type moves
DragonRage = moves.Move("DRAGONRAGE", 0, 0, "ENEMY HP -40", 100, "DRG", "SP");


# Dark type moves
Bite = moves.Move("BITE", 60, 0, "NONE", 100, "DRK", "PH");


# Steel type moves



# Flying type moves
DrillPeck = moves.Move("DRILLPECK", 80, 0, "NONE", 100, "FLY", "PH");
Gust = moves.Move("GUST", 40, 0, "NONE", 100, "FLY", "SP");
Peck = moves.Move("PECK", 35, 0, "NONE", 100, "FLY", "PH");

