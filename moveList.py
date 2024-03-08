import moves
import pokemon


# Normal type moves

QuickAttack = moves.Move("QUICKATTACK", 40, 1, "NONE", 100 , "NRM", "PHY")
Scratch = moves.Move("SCRATCH", 40, 0, "NONE", 100,  "NRM", "PH")
TailWhip = moves.Move("TAILWHIP", 0, 0, "ENEMY DEF -1", 100 "NRM", "ST")
SwordsDance = moves.Move("SWORDSDANCE", 0, 0, "SELF ATTACK 2", 100, "NRM", "ST")
# Grass type moves

Absorb = moves.Move("ABSORB", 20, 0, "HP+", 100, "GRS", "SP")

# Water type moves

WaterGun = moves.Move("WATERGUN", 40, 0, "NONE", 100 , "WTR" "SP")
HydroPump = moves.Move("HYDROPUMP", 110, 0, "NONE", 80, "WTR", "SP")

# Fire type moves

Ember = moves.Move("EMBER", 40, 0, "ENEMY BRN 10", 100 ,"FIR", "SP")
Flamethrower = moves.Move("FLAMETHROWER", 90, 0, "ENEMY BRN 10", 100 "FIR", "SP")

# Bug type moves



# Poison type moves

PoisonSting = moves.Move("POISONSTING", 15, 0, "ENEMY PSN 30", 100, "PSN", "PH")

# Electric type moves

ThunderWave = moves.Move("THUNDERWAVE", 0, 0, "ENEMY PRZ 100", 90 , "ST")

# Ground type moves

Earthquake = moves.Move("EARTHQUAKE", 100, 0, "NONE", 100, "GRD", "PH")

# Fighting type moves



# Psychic type moves

Agility = moves.Move("AGILITY", 0, 0, "SELF SPEED 2", 100, "PSY", "ST")
Hypnosis = moves.Move("HYPNOSIS", 0, 0, "ENEMY SLP 100", 60, "PSY", "ST")

# Rock type moves



# Ghost type moves



# Ice type moves



# Dragon type moves



# Dark type moves



# Steel type moves



# Flying type moves
