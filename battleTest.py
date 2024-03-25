import pokemon
import Items
import pokeball
import pokedex
import moves
import random
import math

# Choosing the move for a battle
def BattleMenu():
    print("1. Move 1\n2. Move 2\n3. Move 3\n4. Move 4\n")
    choice = 0
    while(choice < 1 or choice > 4):
        choice = int(input())
        if(choice < 1 or choice > 4):
            print("Invalid")
        else:
            return choice
        
def CheckPriority(userMove, enemyMove):
    # Checks if user's move has higher priority
    if(userMove.priority > enemyMove.priority):
        return userMove
    # Checks if enemy's move has higher priority
    elif(enemyMove.priority > userMove.priority):
        return enemyMove
    # If the priority of the moves are the same, returns 0 to lead to CheckSpeed() where the pokemons' speeds are checked
    else:
        return 0

def CheckSpeed(userPokemon, enemyPokemon):
    # Will return 0 if user's pokemon is faster, will return 1 if enemy's pokemon is faster
    # Checks if the user's pokemon is faster
    if(userPokemon.currentSpeed > enemyPokemon.currentSpeed):
        return 0
    # Checks if the enemy's pokemon is faster
    elif(enemyPokemon.currentSpeed > userPokemon.currentSpeed):
        return 1
    # If the user's pokemon and enemy's pokemon have the same speed, a random one will be chosen
    else:
        if(random.randint(1, 2) == 1):
            return 0
        else:
            return 1
        
def UseMove(move):
    # Checks if the move is a status, physical, or special move
    # If it is a status move, check effect
    # If it is a physical or special move, calculate damage and apply secondary effect
    pass

def CheckEffect(move, userPokemon, enemyPokemon):
    splitEffect = move.secondaryEffect.split()
    if(splitEffect[0] == "NONE"):
        return
    if(splitEffect[0] == "SELF"):
        # Apply Effect to userPokemon
        ApplyEffect(splitEffect, userPokemon)
        pass
    elif(splitEffect[0] == "ENEMY"):
        # Apply Effect to enemyPokemon
        ApplyEffect(splitEffect, enemyPokemon)
        pass

def ApplyEffect(effect, pkmn):
    # Will apply effect on the pokemon
    if(effect[1] == "PRZ"):
        if(random.randint(1, 100) < int(effect[2])):
            # Apply Paralysis to Pokemon
            pass
    elif(effect[1] == "BRN"):
        if(random.randint(1, 100) < int(effect[2])):
            # Apply Burn to Pokemon
            pass
    elif(effect[1] == "PSN"):
        if(random.randint(1, 100) < int(effect[2])):
            # Apply Poison to Pokemon
            pass
    elif(effect[1] == "SLP"):
        if(random.randint(1, 100) < int(effect[2])):
            # Apply Sleep to Pokemon
            pass
    elif(effect[1] == "ATK"):
        # Will have to adjust multiplier for attack
        # pkmn.attack += int(effect[2])
        pass
    elif(effect[1] == "DEF"):
        # pkmn.defense += int(effect[2])
        pass
    elif(effect[1] == "SPATK"):
        # pkmn.specAttack += int(effect[2])
        pass
    elif(effect[1] == "SPDEF"):
        # pkmn.specDefense += int(effect[2])
        pass
    elif(effect[1] == "SPD"):
        # pkmn.speed += int(effect[2])
        pass
    elif(effect[1] == "HP"):
        # UNFININSHED
        pass

def ResetStats(currentPokemon):
    currentPokemon.currentAttack = currentPokemon.attack;
    currentPokemon.currentDefense = currentPokemon.defense
    currentPokemon.currentSpecAttack = currentPokemon.specAttack;
    currentPokemon.currentSpecDefense = currentPokemon.specDefense
    currentPokemon.currentSpeed = currentPokemon.speed
    


# Battle function that will be looped until either party reaches 0
def Battle(userP, enemyP):
    userTargetFainted = len(enemyP)
    enemyTargetFainted = len(userP)
    userFaints = 0
    enemyFaints = 0
    print(userTargetFainted)
    print(enemyTargetFainted)
    while(userFaints != userTargetFainted and enemyFaints != enemyTargetFainted):
        BattleMenu()
        # If pokemon switches, reset stats
        userFaints += 1
        # Check which move has the higher priority
        # Check if return is 0 for same priority, if so, check speed
        # if(CheckPriority(userMove, enemyMove) == 0):
            # # Checks speed for the same priority
            # if(CheckSpeed(userPokemon, enemyPokemon) == 0):
                # Use the user's move
            # else:
                # use enemy's move
    # After battle, reset stats
        


def calculateDamage(userLvl, movePower, userAtk, enemyDef, stab, typeMult):
    # will return the hp to be subtracted from the defending pokemon
    
    # level not defined yet

    # critical hit chance to be defined later
    critical = 1
    
    # userAtk is the attack stat for the pokemon using the move
    # enemyDef is the defense stat for the defending pokemon
    # stab is 1.5 if the move being used matches the user's type, 1 otherwise
    # typeMult is the multiplier returned by the TypeMatchup() function

    # Damage function from Generation 1 Pokemon 
    # Damage = (((((2 * level * critical  /  5 ) + 2) * Power * Attack/Def)  / 50  ) + 2) * stab * typemultiplier * random


    randomNum = random.randint(217, 255)

    step1 = ((2.0 * userLvl * critical) / 5.0) + 2 
    step2 = (step1 * movePower * (float(userAtk) / float(enemyDef)))
    step3 = (step2 / 50) + 2
    step4 = step3 * stab * typeMult * randomNum
    return step4

        

def TypeMatchup(type1, type2, moveType):
    # Will return either: 0, 0.25, 0.5, 1, 2, 4

    multiplier = 1.0

    # Normal Type Move
    if(moveType == "NRM"):
        if(type1 == "RCK" or type2 == "RCK"):
            multiplier *= .5
        if(type1 == "GHT" or type2 == "GHT"):
            multiplier *= 0
        if(type1 == "STL" or type2 == "STL"):
            multiplier *= .5
            
    # Grass Type Move
    if (moveType == "GRS"):
        if(type1 == "FIR" or type2 == "FIR"):
            multiplier *= .5
        if(type1 == "WTR" or type2 == "WTR"):
            multiplier *= 2
        if(type1 == "GRS" or type2 == "GRS"):
            multiplier *= .5
        if(type1 == "PSN" or type2 == "PSN"):
            multiplier *= .5
        if(type1 == "GRD" or type2 == "GRD"):
            multiplier *= 2
        if(type1 == "FLY" or type2 == "FLY"):
            multiplier *= .5
        if(type1 == "BUG" or type2 == "BUG"):
            multiplier *= .5
        if(type1 == "RCK" or type2 == "RCK"):
            multiplier *= 2
        if(type1 == "DRG" or type2 == "DRG"):
            multiplier *= .5
        if(type1 == "STL" or type2 == "STL"):
            multiplier *= .5

    # Fire Type Move
    if (moveType == "FIR"):
        if(type1 == "FIR" or type2 == "FIR"):
            multiplier *= .5
        if(type1 == "WTR" or type2 == "WTR"):
            multiplier *= .5
        if(type1 == "GRS" or type2 == "GRS"):
            multiplier *= 2
        if(type1 == "ICE" or type2 == "ICE"):
            multiplier *= 2
        if(type1 == "BUG" or type2 == "BUG"):
            multiplier *= 2
        if(type1 == "RCK" or type2 == "RCK"):
            multiplier *= .5
        if(type1 == "DRG" or type2 == "DRG"):
            multiplier *= .5
        if(type1 == "STL" or type2 == "STL"):
            multiplier *= 2
            
    # Water Type Move
    if (moveType == "WTR"):
        if(type1 == "FIR" or type2 == "FIR"):
            multiplier *= 2
        if(type1 == "WTR" or type2 == "WTR"):
            multiplier *= .5
        if(type1 == "GRS" or type2 == "GRS"):
            multiplier *= .5
        if(type1 == "GRD" or type2 == "GRD"):
            multiplier *= 2
        if(type1 == "RCK" or type2 == "RCK"):
            multiplier *= 2
        if(type1 == "DRG" or type2 == "DRG"):
            multiplier *= .5

    # Bug Type Move
    if (moveType == "BUG"):
        if(type1 == "FIR" or type2 == "FIR"):
            multiplier *= .5
        if(type1 == "GRS" or type2 == "GRS"):
            multiplier *= 2
        if(type1 == "FGT" or type2 == "FGT"):
            multiplier *= .5
        if(type1 == "PSN" or type2 == "PSN"):
            multiplier *= .5
        if(type1 == "FLY" or type2 == "FLY"):
            multiplier *= .5
        if(type1 == "PSY" or type2 == "PSY"):
            multiplier *= 2
        if(type1 == "GHT" or type2 == "GHT"):
            multiplier *= .5
        if(type1 == "DRK" or type2 == "DRK"):
            multiplier *= 2
        if(type1 == "STL" or type2 == "STL"):
            multiplier *= .5

    # Poison Type Move
    if (moveType == "PSN"):
        if(type1 == "GRS" or type2 == "GRS"):
            multiplier *= 2
        if(type1 == "PSN" or type2 == "PSN"):
            multiplier *= .5
        if(type1 == "GRD" or type2 == "GRD"):
            multiplier *= .5
        if(type1 == "RCK" or type2 == "RCK"):
            multiplier *= .5
        if(type1 == "GHT" or type2 == "GHT"):
            multiplier *= .5
        if(type1 == "STL" or type2 == "STL"):
            multiplier *= 0

    # Electric Type Move
    if (moveType == "ELC"):
        if(type1 == "WTR" or type2 == "WTR"):
            multiplier *= 2
        if(type1 == "ELC" or type2 == "ELC"):
            multiplier *= .5
        if(type1 == "GRS" or type2 == "GRS"):
            multiplier *= .5
        if(type1 == "GRD" or type2 == "GRD"):
            multiplier *= 0
        if(type1 == "FLY" or type2 == "FLY"):
            multiplier *= 2
        if(type1 == "DRG" or type2 == "DRG"):
            multiplier *= .5

    # Ground Type Move
    if (moveType == "GRD"):
        if(type1 == "FIR" or type2 == "FIR"):
            multiplier *= 2
        if(type1 == "ELC" or type2 == "ELC"):
            multiplier *= 2
        if(type1 == "GRS" or type2 == "GRS"):
            multiplier *= .5
        if(type1 == "PSN" or type2 == "PSN"):
            multiplier *= 2
        if(type1 == "FLY" or type2 == "FLY"):
            multiplier *= 0
        if(type1 == "BUG" or type2 == "BUG"):
            multiplier *= .5
        if(type1 == "RCK" or type2 == "RCK"):
            multiplier *= 2
        if(type1 == "STL" or type2 == "STL"):
            multiplier *= 2
        

    # Fighting Type Move
    if (moveType == "FGT"):
        if(type1 == "NRM" or type2 == "NRM"):
            multiplier *= 2
        if(type1 == "ICE" or type2 == "ICE"):
            multiplier *= 2
        if(type1 == "PSN" or type2 == "PSN"):
            multiplier *= .5
        if(type1 == "FLY" or type2 == "FLY"):
            multiplier *= .5
        if(type1 == "PSY" or type2 == "PSY"):
            multiplier *= .5
        if(type1 == "BUG" or type2 == "BUG"):
            multiplier *= .5
        if(type1 == "RCK" or type2 == "RCK"):
            multiplier *= 2
        if(type1 == "GHT" or type2 == "GHT"):
            multiplier *= 0
        if(type1 == "DRK" or type2 == "DRK"):
            multiplier *= 2
        if(type1 == "STL" or type2 == "STL"):
            multiplier *= 2

    # Psychic Type Move
    if (moveType == "PSY"):
        if(type1 == "FGT" or type2 == "FGT"):
            multiplier *= 2
        if(type1 == "PSN" or type2 == "PSN"):
            multiplier *= 2
        if(type1 == "PSY" or type2 == "PSY"):
            multiplier *= .5
        if(type1 == "DRK" or type2 == "DRK"):
            multiplier *= 0
        if(type1 == "STL" or type2 == "STL"):
            multiplier *= .5
        

    # Rock Type Move
    if (moveType == "RCK"):
        if(type1 == "FIR" or type2 == "FIR"):
            multiplier *= 2
        if(type1 == "ICE" or type2 == "ICE"):
            multiplier *= 2
        if(type1 == "FGT" or type2 == "FGT"):
            multiplier *= .5
        if(type1 == "GRD" or type2 == "GRD"):
            multiplier *= .5
        if(type1 == "FLY" or type2 == "FLY"):
            multiplier *= 2
        if(type1 == "BUG" or type2 == "BUG"):
            multiplier *= 2
        if(type1 == "STL" or type2 == "STL"):
            multiplier *= .5

    # Ghost Type Move
    if (moveType == "GHT"):
        if(type1 == "NRM" or type2 == "NRM"):
            multiplier *= 0
        if(type1 == "PSY" or type2 == "PSY"):
            multiplier *= 2
        if(type1 == "GHT" or type2 == "GHT"):
            multiplier *= 2
        if(type1 == "DRK" or type2 == "DRK"):
            multiplier *= .5
        if(type1 == "STL" or type2 == "STL"):
            multiplier *= .5

    # Ice Type Move
    if (moveType == "ICE"):
        if(type1 == "FIR" or type2 == "FIR"):
            multiplier *= .5
        if(type1 == "WTR" or type2 == "WTR"):
            multiplier *= .5
        if(type1 == "GRS" or type2 == "GRS"):
            multiplier *= 2
        if(type1 == "ICE" or type2 == "ICE"):
            multiplier *= .5
        if(type1 == "GRD" or type2 == "GRD"):
            multiplier *= 2
        if(type1 == "FLY" or type2 == "FLY"):
            multiplier *= 2
        if(type1 == "DRG" or type2 == "DRG"):
            multiplier *= 2
        if(type1 == "STL" or type2 == "STL"):
            multiplier *= .5

    # Dragon Type Move
    if (moveType == "DRG"):
        if(type1 == "DRG" or type2 == "DRG"):
            multiplier *= 2
        if(type1 == "STL" or type2 == "STL"):
            multiplier *= .5

    # Dark Type Move
    if (moveType == "DRK"):
        if(type1 == "FGT" or type2 == "FGT"):
            multiplier *= .5
        if(type1 == "PSY" or type2 == "PSY"):
            multiplier *= 2
        if(type1 == "GHT" or type2 == "GHT"):
            multiplier *= 2
        if(type1 == "DRK" or type2 == "DRK"):
            multiplier *= .5
        if(type1 == "STL" or type2 == "STL"):
            multiplier *= .5

    # Steel Type Move
    if (moveType == "STL"):
        if(type1 == "FIR" or type2 == "FIR"):
            multiplier *= .5
        if(type1 == "WTR" or type2 == "WTR"):
            multiplier *= .5
        if(type1 == "ELC" or type2 == "ELC"):
            multiplier *= .5
        if(type1 == "ICE" or type2 == "ICE"):
            multiplier *= 2
        if(type1 == "RCK" or type2 == "RCK"):
            multiplier *= 2
        if(type1 == "STL" or type2 == "STL"):
            multiplier *= .5

    # Flying Type Move
    if (moveType == "FLY"):
        if(type1 == "ELC" or type2 == "ELC"):
            multiplier *= .5
        if(type1 == "GRS" or type2 == "GRS"):
            multiplier *= 2
        if(type1 == "FGT" or type2 == "FGT"):
            multiplier *= 2
        if(type1 == "BUG" or type2 == "BUG"):
            multiplier *= 2
        if(type1 == "RCK" or type2 == "RCK"):
            multiplier *= .5
        if(type1 == "STL" or type2 == "STL"):
            multiplier *= .5


    return multiplier


        




# Hardcoded Parties for testing purposes
userParty = []
enemyParty = []

userParty.append(pokedex.Squirtle)
userParty.append(pokedex.Ivysaur)
userParty.append(pokedex.Charizard)

enemyParty.append(pokedex.Bulbasaur)
enemyParty.append(pokedex.Charmeleon)
enemyParty.append(pokedex.Blastoise)

# Battle(userParty, enemyParty)
print(TypeMatchup("RCK", "STL", "NRM"))





