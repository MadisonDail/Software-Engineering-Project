import pokemon
import Items
import pokeball
import pokedex
import moves
import random
import math
import moveList
import pygame
import battleScreen
import copy

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



# Choosing the move for a battle
def BattleMenu(pkmn):
    print(pkmn.move1.name)
    print(pkmn.move2.name)
    print(pkmn.move3.name)
    print(pkmn.move4.name)
    moveChoice = 0
    while(moveChoice < 1 or moveChoice > 4):
        moveChoice = int(input())
        if(moveChoice < 1 or moveChoice > 4):
            print("Invalid")
        else:
            return moveChoice
        
def HealParty(party):
    for pkmn in party:
        pkmn.currentHp = pkmn.hp
        
def SwitchMenu(party, current):
    for i in range(len(party)):
        print(str(i + 1) + ". " + party[i].name)
    choice = 0
    while((choice < 1 or choice > len(party)) or (choice == (current + 1))):
        choice = int(input("Which pokemon would you like to send out "))
        if(choice == current + 1):
            print("That pokemon is already in battle")
        if(choice < 1 or choice > len(party)):
           print("Invalid Choice")
    return choice

# Checks if either team has all fainted pokemon, returns 1 if user party is all fainted, 2 if enemy party is all fainted, 0 if there are alive pokemon on both teams
def CheckAliveParty(partyUser, partyEnemy):
    counter = 0
    for currentPokemon in partyUser:
        if(currentPokemon.currentHp <= 0):
            counter += 1
    if(counter == len(partyUser)):
        return 1
    counter = 0
    for currentPokemon in partyEnemy:
        if(currentPokemon.currentHp <= 0):
            counter += 1
    if(counter == len(partyEnemy)):
        return 2
    else:
        return 0

def CheckAlivePokemon(pkmn):
    # Checks if single pokemon is alive, 1 for fainted, 0 for alive
    if(pkmn.currentHp <= 0):
        return 1
    else:
        return 0
    

def CheckPriority(userMove, enemyMove):
    # Checks if user's move has higher priority
    if(userMove.priority > enemyMove.priority):
        return 1
    # Checks if enemy's move has higher priority
    elif(enemyMove.priority > userMove.priority):
        return -1
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
        
def CheckAccuracy(move):
    if(random.randint(0, 100) > move.accuracy):
        return False
    else:
        return True

def CheckStab(user, moveType):
    if(user.type1 == moveType or user.type2 == moveType):
        return 1.5
    else:
        return 1

def UseMove(move, attacker, defender, attackerStats, defenderStats):
    # Checks if the move is a status, physical, or special move
    # If it is a status move, check effect
    if(move.category == "ST"):
        CheckEffect(move, attacker, defender, attackerStats, defenderStats)
    # If it is a physical or special move, check accuracy, calculate damage and apply secondary effect
    elif(move.category == "SP" or move.category == "PH"):
        if(CheckAccuracy(move)):
            # Uses special defense and special attack if the move is special, regular defense and attack for physical
            if(move.category == "SP"):
                defender.currentHp -= int(calculateDamage(20, move.damage, attacker.specAttack + (10 * attackerStats[2]), defender.specDefense + (10 * defenderStats[3]), CheckStab(attacker, move.type), TypeMatchup(defender.type1, defender.type2, move.type)))
                CheckEffect(move, attacker, defender, attackerStats, defenderStats)
            else:
                defender.currentHp -= int(calculateDamage(20, move.damage, attacker.attack + (10 * attackerStats[0]), defender.defense + (10 * defenderStats[1]), CheckStab(attacker, move.type), TypeMatchup(defender.type1, defender.type2, move.type)))
                CheckEffect(move, attacker, defender, attackerStats, defenderStats)


    pass


def CheckEffect(move, userPokemon, enemyPokemon, attackerStats, defenderStats):
    splitEffect = move.secondaryEffect.split()
    if(splitEffect[0] == "NONE"):
        
        return
    if(splitEffect[0] == "SELF"):
        # Apply Effect to userPokemon
        ApplyEffect(splitEffect, userPokemon, attackerStats)
        pass
    elif(splitEffect[0] == "ENEMY"):
        # Apply Effect to enemyPokemon
        ApplyEffect(splitEffect, enemyPokemon, defenderStats)
        pass


def ApplyEffect(effect, pkmn, stats):
    # Will apply effect on the pokemon
    if(effect[1] == "PRZ"):
        if(random.randint(1, 100) < int(effect[2])):
            # Apply Paralysis to Pokemon
            pkmn.status = "PRZ"
            pass
    elif(effect[1] == "BRN"):
        if(random.randint(1, 100) < int(effect[2])):
            # Apply Burn to Pokemon
            pkmn.status = "BRN"
            pass
    elif(effect[1] == "PSN"):
        if(random.randint(1, 100) < int(effect[2])):
            # Apply Poison to Pokemon
            pkmn.status = "PSN"
            pass
    elif(effect[1] == "SLP"):
        if(random.randint(1, 100) < int(effect[2])):
            pkmn.status = "SLP"
            # Apply Sleep to Pokemon
            pass
    elif(effect[1] == "ATK"):
        # Will have to adjust multiplier for attack
        # pkmn.attack += int(effect[2])
        stats[0] += int(effect[2])
        if(stats[0] > 6):
            stats[0] = 6
        elif(stats[0] < -6):
            stats[0] = -6
        pass
    elif(effect[1] == "DEF"):
        # pkmn.defense += int(effect[2])
        if(stats[1] > 6):
            stats[1] = 6
        elif(stats[1] < -6):
            stats[1] = -6
        pass
    elif(effect[1] == "SPATK"):
        # pkmn.specAttack += int(effect[2])
        if(stats[2] > 6):
            stats[2] = 6
        elif(stats[2] < -6):
            stats[2] = -6
        pass
    elif(effect[1] == "SPDEF"):
        # pkmn.specDefense += int(effect[2])
        if(stats[3] > 6):
            stats[3] = 6
        elif(stats[3] < -6):
            stats[3] = -6
        pass
    elif(effect[1] == "SPD"):
        # pkmn.speed += int(effect[2])
        if(stats[4] > 6):
            stats[4] = 6
        elif(stats[4] < -6):
            stats[4] = -6
        pass
    elif(effect[1] == "HP"):
        pkmn.currentHp += (pkmn.hp / 8)
        if(pkmn.currentHp > pkmn.hp):
            pkmn.currentHp = pkmn.hp
        pass

def ResetStats(currentPokemon, statStages):
    for i in range(5):
        statStages[i] = 0
    currentPokemon.currentAttack = currentPokemon.attack
    currentPokemon.currentDefense = currentPokemon.defense
    currentPokemon.currentSpecAttack = currentPokemon.specAttack
    currentPokemon.currentSpecDefense = currentPokemon.specDefense
    currentPokemon.currentSpeed = currentPokemon.speed
    

def calculateDamage(userLvl, movePower, userAtk, enemyDef, stab, typeMult):
    # will return the hp to be subtracted from the defending pokemon
    
    # level not defined yet

    # critical hit chance to be defined later
    
    # userAtk is the attack stat for the pokemon using the move
    # enemyDef is the defense stat for the defending pokemon
    # stab is 1.5 if the move being used matches the user's type, 1 otherwise
    # typeMult is the multiplier returned by the TypeMatchup() function

    # Damage function from Generation 1 Pokemon 
    # Damage = (((((2 * level * critical  /  5 ) + 2) * Power * Attack/Def)  / 50  ) + 2) * stab * typemultiplier * random


    randomNum = random.randint(217, 255) / 255.0

    step1 = ((2.0 * userLvl) / 5.0) + 2.0
    step2 = (step1 * movePower * (float(userAtk) / float(enemyDef)))
    step3 = (step2 / 50.0) + 2.0
    step4 = step3 * stab * typeMult * randomNum
    print("DAMAGE " + str(step4))
    return int(step4)

def CheckSkipStatus(pkmn):
    # Checks statuses that cause a skipped turn (Paralysis and Sleep)
    if(pkmn.status == "PRZ"):
        # 1/4 chance of losing turn due to paralysis, true if turn continues, false if turn is skipped
        randNum = random.randint(1, 4)
        if(randNum == 1):
            return False
        else:
            return True
    # 1/2 chance of waking up, true if turn continues, false if turn is skipped
    elif(pkmn.status == "SLP"):
        randNum = random.randint(1, 2)
        if(randNum == 1):
            return False
        else:
            pkmn.status == "NONE"
            return True
    return True

def CheckDamageStatus(pkmn):
    # Checks statuses that cause pokemon to take damage each turn, burn or poison
    if(pkmn.status == "BRN" or pkmn.status == "PSN"):
        pkmn.currentHp -= int(pkmn.hp / 16)

def CatchPokemon():
    chance = random.randint(0, 100)
    if(chance < 35):
        return True
    else:
        return False

        
# Battle function that will be looped until either party reaches 0
def Battle(userP, enemyP, battleType):
    
    userPokemonIndex = 0         # Index of pokemon that is sent out for the user
    enemyPokemonIndex = 0         # Index of pokemon that is sent out for the user

    userStatStages = [0, 0, 0, 0, 0]    # Stat Stages go from -6 to 6, ordered as Attack, Defense, Special Attack, Special Defense, Speed
    enemyStatStages = [0, 0, 0, 0, 0]
    
    

    userMove = moveList.NOMOVE
    enemyMove = moveList.NOMOVE
    
    while(True):
        # move=battleScreen.BattleScreen(userP, enemyP, userPokemonIndex, enemyPokemonIndex)
        # print(battleScreen.BattleScreen(userP, enemyP, userPokemonIndex, enemyPokemonIndex))
        choice = battleScreen.BattleScreen(userP, enemyP, userPokemonIndex, enemyPokemonIndex, False).split()

        if(CheckAliveParty(userP, enemyP) == 1):
            print("Enemy wins!")
            break
        elif(CheckAliveParty(userP, enemyP) == 2):
            print("User wins!")
            break

        print(choice)
        if(choice[0] == "MOVE"):
            # use move
            if(choice[1] == userP[userPokemonIndex].move1.name):
                userMove = userP[userPokemonIndex].move1
            elif(choice[1] == userP[userPokemonIndex].move2.name):
                userMove = userP[userPokemonIndex].move2
            elif(choice[1] == userP[userPokemonIndex].move3.name):
                userMove = userP[userPokemonIndex].move3
            elif(choice[1] == userP[userPokemonIndex].move4.name):
                userMove = userP[userPokemonIndex].move4
        elif(choice[0] == "POKEMON"):
            # switch pokemon
            
            while(CheckAliveParty(userP, enemyP) != 1 and userP[userPokemonIndex].currentHp > 0):
                ind = 0
                for pokeName in userP:
                    if(choice[1] == pokeName.name):
                        userPokemonIndex = ind
                        userMove = moveList.NOMOVE
                    ind += 1
        elif(choice[0] == "CATCH"):
            if(battleType == "WILD"):
                if(CatchPokemon()):
                    if(len(userP) < 6):
                        userP.append(enemyP[enemyPokemonIndex])
                        print("CAUGHT")
                        break
                    else:
                        userMove = userP[userPokemonIndex].move1
        elif(choice[0] == "RUN"):
            if(battleType == "WILD"):
                break
            else:
                userMove = userP[userPokemonIndex].move1

        # Check if the battle should continue
        
       
        
        eMoveIndex = random.randint(1, 4)
        if(eMoveIndex == 1):
            enemyMove = enemyP[enemyPokemonIndex].move1
        elif(eMoveIndex == 2):
            enemyMove = enemyP[enemyPokemonIndex].move2
        elif(eMoveIndex == 3):
            enemyMove = enemyP[enemyPokemonIndex].move3
        elif(eMoveIndex == 4):
            enemyMove = enemyP[enemyPokemonIndex].move4
        
        # If pokemon switches, reset stats
        # Check which move has the higher priority
        # Check if return is 0 for same priority, if so, check speed
        if(CheckPriority(userMove, enemyMove) == 0):
            # # Checks speed for the same priority
            if(CheckSpeed(userP[userPokemonIndex], enemyP[enemyPokemonIndex]) == 0):
                # Use the user's move first
                # Check Paralysis or sleep
                if(CheckSkipStatus(userP[userPokemonIndex])):
                    UseMove(userMove, userP[userPokemonIndex], enemyP[enemyPokemonIndex], userStatStages, enemyStatStages)
                    print("CHECK1")
                    if(CheckAlivePokemon(enemyP[enemyPokemonIndex]) == 1):
                        print("CHECK1")
                        enemyPokemonIndex += 1
                        enemyMove = moveList.NOMOVE
                        print("SWITCH ENEMY")
                    # if enemy is alive, use enemy move
                    if(CheckAliveParty(userP, enemyP) == 2):
                        print("User wins!")
                        break
                UseMove(enemyMove, enemyP[enemyPokemonIndex], userP[userPokemonIndex], enemyStatStages, userStatStages)
            else:
                # use enemy's move first
                if(CheckSkipStatus(enemyP[enemyPokemonIndex])):
                    UseMove(enemyMove, enemyP[enemyPokemonIndex], userP[userPokemonIndex], enemyStatStages, userStatStages)
                    if(CheckAlivePokemon(userP[userPokemonIndex]) == 1): #if dead
                        print("SWITCH USER")
                        switchFlag = True
                        while(CheckAliveParty(userP, enemyP) != 1 and userP[userPokemonIndex].currentHp > 0):
                            switch = battleScreen.BattleScreen(userP, enemyP, userPokemonIndex, enemyPokemonIndex, switchFlag).split()
                            print("SWITCH")
                            print(switch)
                            print(choice)
                            ind = 0
                            for pkmn in userP:
                                if(switch[1] == pkmn.name):
                                    userPokemonIndex = ind
                                    print("SWITCH INTO " + userP[ind].name)
                                    break
                                ind += 1
                            break
                        switchFlag = False
                        ResetStats(userP[userPokemonIndex], userStatStages)     # Reset stats of the pokemon switched out
                        # userPokemonIndex = SwitchMenu(userP, userPokemonIndex) - 1      # Switch the index of the current pokemon to the new one
                        userMove = moveList.NOMOVE
                    # if user is alive, use user move
                    if(CheckAliveParty(userP, enemyP) == 1):
                        print("Enemy wins!")
                        break
                UseMove(userMove, userP[userPokemonIndex], enemyP[enemyPokemonIndex], userStatStages, enemyStatStages)
        else:
            print("HIGHER PRIORITY")
            if(CheckPriority(userMove, enemyMove) > 0):
                # Use the user's move first
                # Check Paralysis or sleep
                if(CheckSkipStatus(userP[userPokemonIndex])):
                    print(enemyP[enemyPokemonIndex].name)
                    print(enemyP[enemyPokemonIndex].currentHp)
                    UseMove(userMove, userP[userPokemonIndex], enemyP[enemyPokemonIndex], userStatStages, enemyStatStages)
                    print(enemyP[enemyPokemonIndex].currentHp)
                    print("CHECK2")
                    if(CheckAlivePokemon(enemyP[enemyPokemonIndex]) == 1):
                        print("CHECK2")
                        enemyPokemonIndex += 1
                        enemyMove = moveList.NOMOVE
                        print("SWITCH ENEMY")
                    # if enemy is alive, use enemy move
                    if(CheckAliveParty(userP, enemyP) == 2):
                        print("User wins!")
                        break
                UseMove(enemyMove, enemyP[enemyPokemonIndex], userP[userPokemonIndex], enemyStatStages, userStatStages)
            else:
                # use enemy's move first
                if(CheckSkipStatus(enemyP[enemyPokemonIndex])):
                    UseMove(enemyMove, enemyP[enemyPokemonIndex], userP[userPokemonIndex], enemyStatStages, userStatStages)
                    if(CheckAlivePokemon(userP[userPokemonIndex]) == 1):
                        print("SWITCH USER !!!")
                        ResetStats(userP[userPokemonIndex], userStatStages)     # Reset stats of the pokemon switched out
                        switchFlag = True
                        while(CheckAliveParty(userP, enemyP) != 1 and userP[userPokemonIndex].currentHp <= 0):
                            switch = battleScreen.BattleScreen(userP, enemyP, userPokemonIndex, enemyPokemonIndex, switchFlag).split()
                            print("SWITCH")
                            print(switch)
                            print(choice)
                            ind = 0
                            for pkmn in userP:
                                if(switch[1] == pkmn.name):
                                    userPokemonIndex = ind
                                    print("SWITCH INTO " + userP[ind].name)
                                ind += 1
                            break
                        switchFlag = False
                        # userPokemonIndex = SwitchMenu(userP, userPokemonIndex) - 1      # Switch the index of the current pokemon to the new one
                        userMove = moveList.NOMOVE
                    # if user is alive, use user move
                    if(CheckAliveParty(userP, enemyP) == 1):
                        print("Enemy wins!")
                        break
                UseMove(userMove, userP[userPokemonIndex], enemyP[enemyPokemonIndex], userStatStages, enemyStatStages)
            # Check and apply burn or poison
            CheckDamageStatus(userP[userPokemonIndex])
            CheckDamageStatus(enemyP[enemyPokemonIndex])
            print("CHECK3")
            if(CheckAlivePokemon(userP[userPokemonIndex]) == 1):
                print("SWITCH USER")
                ResetStats(userP[userPokemonIndex], userStatStages)     # Reset stats of the pokemon switched out
                # userPokemonIndex = SwitchMenu(userP, userPokemonIndex) - 1      # Switch the index of the current pokemon to the new one
                userMove = moveList.NOMOVE
            elif(CheckAlivePokemon(enemyP[enemyPokemonIndex]) == 1):
                print("CHECK3")
                enemyPokemonIndex += 1
                enemyMove = moveList.NOMOVE
                print("SWITCH ENEMY")
            if(CheckAliveParty(userP, enemyP) == 1):
                        print("Enemy wins!")
                        break
            if(CheckAliveParty(userP, enemyP) == 2):
                        print("User wins!")
                        break

        print("USER HP " + str(userP[userPokemonIndex].currentHp))


    for pkmn in userP:
        ResetStats(pkmn, userStatStages)
    for pkmn in enemyP:
        ResetStats(pkmn, enemyStatStages)
                
    # After battle, reset stats except hp

# Hardcoded Parties for testing purposes
userParty = []
enemyParty = []

temp = copy.copy(pokedex.Bulbasaur)

# userParty.append(temp)
# userParty.append(pokedex.Squirtle)
# userParty.append(pokedex.Ivysaur)
userParty.append(pokedex.Charizard)
# userParty.append(pokedex.Venusaur)
userParty.append(pokedex.Charmeleon)



enemyParty.append(pokedex.Kakuna)
enemyParty.append(pokedex.Metapod)
# enemyParty.append(pokedex.Charizard)
#enemyParty.append(pokedex.Charmeleon)
#enemyParty.append(pokedex.Blastoise)

# Battle(userParty, enemyParty)

Battle(userParty, enemyParty, "WILD")







