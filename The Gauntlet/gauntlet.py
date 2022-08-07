# The Gauntlet

import random

# Player Classes

class player:
    class test:
        name = "Dev"
        health = 50000
        attack = 2500
    class test_base:
        name = "Dev"
        health = 50000
        attack = 2500
    class test_buff:
        name = "Dev"
        health = 50000
        attack = 5000
    class paladin_base:
        name = "Paladin"
        health = 1200
        attack = 250
    class paladin:
        name = "Paladin"
        health = 1200
        attack = 250
    class paladin_buff:
        name = "Paladin"
        health = 2500
        attack = 500
    class knight_base:
        name = "Knight"
        health = 1000
        attack = 100
    class knight:
        name = "Knight"
        health = 1000
        attack = 100
    class knight_buff:
        name = "Knight"
        health = 2000
        attack = 250
    class fighter_base:
        name = "Monk"
        health = 800
        attack = 200
    class fighter:
        name = "Monk"
        health = 800
        attack = 200
    class fighter_buff:
        name = "Monk"
        health = 1600
        attack = 400
    class rogue_base:
        name = "Rogue"
        health = 500
        attack = 300
    class rogue:
        name = "Rogue"
        health = 500
        attack = 300
    class rogue_buff:
        name = "Rogue"
        health = 1200
        attack = 600
    class selected:
        name = ""
        health = 0
        attack = 0

# Enemy Classes

class enemy:
    class rat:
        name = "Large Rat"
        health = 200
        attack = 50
    class skeleton:
        name = "Undead"
        health = 300
        attack = 75
    class wolf:
        name = "Wolf"
        health = 400
        attack = 150
    class man_at_arms:
        name = "Man at Arms"
        health = 500
        attack = 200
    class bear:
        name ="Bear"
        health = 750
        attack = 250
    class nurse:
        name = "Sacrificial Priestess"
        health = 1500
        attack = 100
    class squire: 
        name = "Squire"
        health = 1000
        attack = 250
    class knight:
        name = "Knight"
        health = 1200
        attack = 250
    class lion:
        name = "Lion"
        health = 1200
        attack = 500
    class imperial_guard:
        name = "Imperial Guardian"
        health = 1500
        attack = 500
    class emperor:
        name ="The Emperor"
        health = 2000
        attack = 1000

# Game Logic

def start_game():

    # Battle Eleven vs Emperor

    def end_game():
        print("Congratulations !!! ")
        ("")
        play_again = input("Would you like to play again? (yes or no) ")
        if play_again == "yes":
            start_game()
        else:
            print("Thank you for playing !!! ")  

    def battle_eleven():

        print("----------------------------------------------------------------")
        print("")
        print("You walk into a new room inside the dungeon.")
        print("")
        print("You are approached by", enemy.emperor.name, " !")

    # Enemy Turn

        def enemy_turn():
            random_number = random.randint(1, 10)
            enemy_action = random_number
            if enemy_action >= 1 and enemy_action <= 6:
                print("")
                print(enemy.emperor.name, "attacks you for", enemy.emperor.attack, "damage !")
                player.selected.health = player.selected.health - enemy.emperor.attack
                player.selected.attack = player.selected.attack * 2
                print("")
                print("You have", player.selected.health, "health left !")
                if player.selected.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()
            elif enemy_action >= 7 and enemy_action <= 9:
                player.selected.attack = player.selected.attack / 2
                print("")
                print(enemy.emperor.name, "guards against your attack !")
                print("")
                print("The battle continues !")
                player_turn()
            else:
                enemy.emperor.health = enemy.emperor.health - (player.selected.attack * 2)
                print("")
                print(enemy.emperor.name, "hesitates ! You attack for", (player.selected.attack * 2), "damage !")
                print("")
                print(enemy.emperor.name, "has", enemy.emperor.health, "health left !")
                if enemy.emperor.health <= 0:
                    print("")
                    print("You have defeated", enemy.emperor.name, " !!")
                    reset_player_after_buff()
                    end_game()
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()

    # Player Turn

        def player_turn():
            print("")
            player_action = input("What will you do? (attack or defend) ")
            if player_action == "attack":
                print("")
                print("You attack the", enemy.emperor.name, "for", player.selected.attack, "damage !")
                print("")
                enemy.emperor.health = enemy.emperor.health - player.selected.attack
                enemy.emperor.attack = enemy.emperor.attack * 2
                print("The", enemy.emperor.name, "has", enemy.emperor.health, "health left !")
                if enemy.emperor.health <= 0:
                    print("")
                    print("You have defeated the", enemy.emperor.name, " !!")
                    reset_player_after_buff()
                    end_game()
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()               
            elif player_action == "defend":
                enemy.emperor.attack = enemy.emperor.attack / 2
                print("")
                print("You guard against the", enemy.emperor.name, " !")
                print("")
                print("The battle continues !")
                enemy_turn()            
            else:
                player.selected.health = player.selected.health - (enemy.emperor.attack * 2)
                print("")
                print("You hesitate ! The", enemy.emperor.name, "attacks for", (enemy.emperor.attack * 2), "damage !")
                print("")
                print("You have", player.selected.health, "health left !")
                if player.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()

        player_turn()

    # Battle Ten vs Imperial Guardian

    def battle_ten():

        print("----------------------------------------------------------------")
        print("")
        print("You walk into a new room inside the dungeon.")
        print("")
        print("You are approached by an", enemy.imperial_guard.name, " !")

    # Enemy Turn

        def enemy_turn():
            random_number = random.randint(1, 10)
            enemy_action = random_number
            if enemy_action >= 1 and enemy_action <= 6:
                print("")
                print("The", enemy.imperial_guard.name, "attacks you for", enemy.imperial_guard.attack, "damage !")
                player.selected.health = player.selected.health - enemy.imperial_guard.attack
                player.selected.attack = player.selected.attack * 2
                print("")
                print("You have", player.selected.health, "health left !")
                if player.selected.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()
            elif enemy_action >= 7 and enemy_action <= 9:
                player.selected.attack = player.selected.attack / 2
                print("")
                print("The", enemy.imperial_guard.name, "guards against your attack !")
                print("")
                print("The battle continues !")
                player_turn()
            else:
                enemy.imperial_guard.health = enemy.imperial_guard.health - (player.selected.attack * 2)
                print("")
                print("The", enemy.imperial_guard.name, "hesitates ! You attack for", (player.selected.attack * 2), "damage !")
                print("")
                print("The", enemy.imperial_guard.name, "has", enemy.imperial_guard.health, "health left !")
                if enemy.imperial_guard.health <= 0:
                    print("")
                    print("You have defeated the", enemy.imperial_guard.name, " !!")
                    reset_player_after_buff()
                    battle_eleven()
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()

    # Player Turn

        def player_turn():
            print("")
            player_action = input("What will you do? (attack or defend) ")
            if player_action == "attack":
                print("")
                print("You attack the", enemy.imperial_guard.name, "for", player.selected.attack, "damage !")
                print("")
                enemy.imperial_guard.health = enemy.imperial_guard.health - player.selected.attack
                enemy.imperial_guard.attack = enemy.imperial_guard.attack * 2
                print("The", enemy.imperial_guard.name, "has", enemy.imperial_guard.health, "health left !")
                if enemy.imperial_guard.health <= 0:
                    print("")
                    print("You have defeated the", enemy.imperial_guard.name, " !!")
                    reset_player_after_buff()
                    battle_eleven()
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()               
            elif player_action == "defend":
                enemy.imperial_guard.attack = enemy.imperial_guard.attack / 2
                print("")
                print("You guard against the", enemy.imperial_guard.name, " !")
                print("")
                print("The battle continues !")
                enemy_turn()            
            else:
                player.selected.health = player.selected.health - (enemy.imperial_guard.attack * 2)
                print("")
                print("You hesitate ! The", enemy.imperial_guard.name, "attacks for", (enemy.imperial_guard.attack * 2), "damage !")
                print("")
                print("You have", player.selected.health, "health left !")
                if player.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()

        player_turn()

    # Battle Nine vs Lion

    def battle_nine():

        print("----------------------------------------------------------------")
        print("")
        print("You walk into a new room inside the dungeon.")
        print("")
        print("You are approached by a", enemy.lion.name, " !")

    # Enemy Turn

        def enemy_turn():
            random_number = random.randint(1, 10)
            enemy_action = random_number
            if enemy_action >= 1 and enemy_action <= 6:
                print("")
                print("The", enemy.lion.name, "attacks you for", enemy.lion.attack, "damage !")
                player.selected.health = player.selected.health - enemy.lion.attack
                player.selected.attack = player.selected.attack * 2
                print("")
                print("You have", player.selected.health, "health left !")
                if player.selected.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()
            elif enemy_action >= 7 and enemy_action <= 9:
                player.selected.attack = player.selected.attack / 2
                print("")
                print("The", enemy.lion.name, "guards against your attack !")
                print("")
                print("The battle continues !")
                player_turn()
            else:
                enemy.lion.health = enemy.lion.health - (player.selected.attack * 2)
                print("")
                print("The", enemy.lion.name, "hesitates ! You attack for", (player.selected.attack * 2), "damage !")
                print("")
                print("The", enemy.lion.name, "has", enemy.lion.health, "health left !")
                if enemy.lion.health <= 0:
                    print("")
                    print("You have defeated the", enemy.lion.name, " !!")
                    reset_player_after_buff()
                    battle_ten()
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()

    # Player Turn

        def player_turn():
            print("")
            player_action = input("What will you do? (attack or defend) ")
            if player_action == "attack":
                print("")
                print("You attack the", enemy.lion.name, "for", player.selected.attack, "damage !")
                print("")
                enemy.lion.health = enemy.lion.health - player.selected.attack
                enemy.lion.attack = enemy.lion.attack * 2
                print("The", enemy.lion.name, "has", enemy.lion.health, "health left !")
                if enemy.lion.health <= 0:
                    print("")
                    print("You have defeated the", enemy.lion.name, " !!")
                    reset_player_after_buff()
                    battle_ten()
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()               
            elif player_action == "defend":
                enemy.lion.attack = enemy.lion.attack / 2
                print("")
                print("You guard against the", enemy.lion.name, " !")
                print("")
                print("The battle continues !")
                enemy_turn()            
            else:
                player.selected.health = player.selected.health - (enemy.lion.attack * 2)
                print("")
                print("You hesitate ! The", enemy.lion.name, "attacks for", (enemy.lion.attack * 2), "damage !")
                print("")
                print("You have", player.selected.health, "health left !")
                if player.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()

        player_turn()

    # Battle Eight vs Knight

    def battle_eight():

        print("----------------------------------------------------------------")
        print("")
        print("You walk into a new room inside the dungeon.")
        print("")
        print("You are approached by a", enemy.knight.name, " !")

    # Enemy Turn

        def enemy_turn():
            random_number = random.randint(1, 10)
            enemy_action = random_number
            if enemy_action >= 1 and enemy_action <= 6:
                print("")
                print("The", enemy.knight.name, "attacks you for", enemy.knight.attack, "damage !")
                player.selected.health = player.selected.health - enemy.knight.attack
                player.selected.attack = player.selected.attack * 2
                print("")
                print("You have", player.selected.health, "health left !")
                if player.selected.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()
            elif enemy_action >= 7 and enemy_action <= 9:
                player.selected.attack = player.selected.attack / 2
                print("")
                print("The", enemy.knight.name, "guards against your attack !")
                print("")
                print("The battle continues !")
                player_turn()
            else:
                enemy.knight.health = enemy.knight.health - (player.selected.attack * 2)
                print("")
                print("The", enemy.knight.name, "hesitates ! You attack for", (player.selected.attack * 2), "damage !")
                print("")
                print("The", enemy.knight.name, "has", enemy.knight.health, "health left !")
                if enemy.knight.health <= 0:
                    print("")
                    print("You have defeated the", enemy.knight.name, " !!")
                    reset_player_after_buff()
                    battle_nine()
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()

    # Player Turn

        def player_turn():
            print("")
            player_action = input("What will you do? (attack or defend) ")
            if player_action == "attack":
                print("")
                print("You attack the", enemy.knight.name, "for", player.selected.attack, "damage !")
                print("")
                enemy.knight.health = enemy.knight.health - player.selected.attack
                enemy.knight.attack = enemy.knight.attack * 2
                print("The", enemy.knight.name, "has", enemy.knight.health, "health left !")
                if enemy.knight.health <= 0:
                    print("")
                    print("You have defeated the", enemy.knight.name, " !!")
                    reset_player_after_buff()
                    battle_nine()
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()               
            elif player_action == "defend":
                enemy.knight.attack = enemy.knight.attack / 2
                print("")
                print("You guard against the", enemy.knight.name, " !")
                print("")
                print("The battle continues !")
                enemy_turn()            
            else:
                player.selected.health = player.selected.health - (enemy.knight.attack * 2)
                print("")
                print("You hesitate ! The", enemy.knight.name, "attacks for", (enemy.knight.attack * 2), "damage !")
                print("")
                print("You have", player.selected.health, "health left !")
                if player.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()

        player_turn()

    # Battle Seven vs Squire

    def battle_seven():

        print("----------------------------------------------------------------")
        print("")
        print("You walk into a new room inside the dungeon.")
        print("")
        print("You are approached by a", enemy.squire.name, " !")

    # Enemy Turn

        def enemy_turn():
            random_number = random.randint(1, 10)
            enemy_action = random_number
            if enemy_action >= 1 and enemy_action <= 6:
                print("")
                print("The", enemy.squire.name, "attacks you for", enemy.squire.attack, "damage !")
                player.selected.health = player.selected.health - enemy.squire.attack
                player.selected.attack = player.selected.attack * 2
                print("")
                print("You have", player.selected.health, "health left !")
                if player.selected.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()
            elif enemy_action >= 7 and enemy_action <= 9:
                player.selected.attack = player.selected.attack / 2
                print("")
                print("The", enemy.squire.name, "guards against your attack !")
                print("")
                print("The battle continues !")
                player_turn()
            else:
                enemy.squire.health = enemy.squire.health - (player.selected.attack * 2)
                print("")
                print("The", enemy.squire.name, "hesitates ! You attack for", (player.selected.attack * 2), "damage !")
                print("")
                print("The", enemy.squire.name, "has", enemy.squire.health, "health left !")
                if enemy.squire.health <= 0:
                    print("")
                    print("You have defeated the", enemy.squire.name, " !!")
                    reset_player_after_buff()
                    battle_eight()
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()

    # Player Turn

        def player_turn():
            print("")
            player_action = input("What will you do? (attack or defend) ")
            if player_action == "attack":
                print("")
                print("You attack the", enemy.squire.name, "for", player.selected.attack, "damage !")
                print("")
                enemy.squire.health = enemy.squire.health - player.selected.attack
                enemy.squire.attack = enemy.squire.attack * 2
                print("The", enemy.squire.name, "has", enemy.squire.health, "health left !")
                if enemy.squire.health <= 0:
                    print("")
                    print("You have defeated the", enemy.squire.name, " !!")
                    reset_player_after_buff()
                    battle_eight()
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()               
            elif player_action == "defend":
                enemy.squire.attack = enemy.squire.attack / 2
                print("")
                print("You guard against the", enemy.squire.name, " !")
                print("")
                print("The battle continues !")
                enemy_turn()            
            else:
                player.selected.health = player.selected.health - (enemy.squire.attack * 2)
                print("")
                print("You hesitate ! The", enemy.squire.name, "attacks for", (enemy.squire.attack * 2), "damage !")
                print("")
                print("You have", player.selected.health, "health left !")
                if player.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()

        player_turn()

    # Battle Six vs Healing Nurse

    def battle_six():

        print("----------------------------------------------------------------")
        print("")
        print("You walk into a new room inside the dungeon.")
        print("")
        print("You are approached by a", enemy.nurse.name, " !")

    # Enemy Turn

        def enemy_turn():
            random_number = random.randint(1, 10)
            enemy_action = random_number
            if enemy_action >= 1 and enemy_action <= 6:
                print("")
                print("The", enemy.nurse.name, "attacks you for", enemy.nurse.attack, "damage !")
                player.selected.health = player.selected.health - enemy.nurse.attack
                player.selected.attack = player.selected.attack * 2
                print("")
                print("You have", player.selected.health, "health left !")
                if player.selected.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()
            elif enemy_action >= 7 and enemy_action <= 9:
                player.selected.attack = player.selected.attack / 2
                print("")
                print("The", enemy.nurse.name, "guards against your attack !")
                print("")
                print("The battle continues !")
                player_turn()
            else:
                enemy.nurse.health = enemy.nurse.health - (player.selected.attack * 2)
                print("")
                print("The", enemy.nurse.name, "hesitates ! You attack for", (player.selected.attack * 2), "damage !")
                print("")
                print("The", enemy.nurse.name, "has", enemy.nurse.health, "health left !")
                if enemy.nurse.health <= 0:
                    print("")
                    print("You have defeated the", enemy.nurse.name, " !!")
                    player_buff()
                    battle_seven()
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()

    # Player Turn

        def player_turn():
            print("")
            player_action = input("What will you do? (attack or defend) ")
            if player_action == "attack":
                print("")
                print("You attack the", enemy.nurse.name, "for", player.selected.attack, "damage !")
                print("")
                enemy.nurse.health = enemy.nurse.health - player.selected.attack
                enemy.nurse.attack = enemy.nurse.attack * 2
                print("The", enemy.nurse.name, "has", enemy.nurse.health, "health left !")
                if enemy.nurse.health <= 0:
                    print("")
                    print("You have defeated the", enemy.nurse.name, " !!")
                    player_buff()
                    battle_seven()
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()               
            elif player_action == "defend":
                enemy.nurse.attack = enemy.nurse.attack / 2
                print("")
                print("You guard against the", enemy.nurse.name, " !")
                print("")
                print("The battle continues !")
                enemy_turn()            
            else:
                player.selected.health = player.selected.health - (enemy.nurse.attack * 2)
                print("")
                print("You hesitate ! The", enemy.nurse.name, "attacks for", (enemy.nurse.attack * 2), "damage !")
                print("")
                print("You have", player.selected.health, "health left !")
                if player.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()

        player_turn()

    # Battle Five vs Bear

    def battle_five():

        print("----------------------------------------------------------------")
        print("")
        print("You walk into a new room inside the dungeon.")
        print("")
        print("You are approached by a", enemy.bear.name, " !")

    # Enemy Turn

        def enemy_turn():
            random_number = random.randint(1, 10)
            enemy_action = random_number
            if enemy_action >= 1 and enemy_action <= 6:
                print("")
                print("The", enemy.bear.name, "attacks you for", enemy.bear.attack, "damage !")
                player.selected.health = player.selected.health - enemy.bear.attack
                player.selected.attack = player.selected.attack * 2
                print("")
                print("You have", player.selected.health, "health left !")
                if player.selected.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()
            elif enemy_action >= 7 and enemy_action <= 9:
                player.selected.attack = player.selected.attack / 2
                print("")
                print("The", enemy.bear.name, "guards against your attack !")
                print("")
                print("The battle continues !")
                player_turn()
            else:
                enemy.bear.health = enemy.bear.health - (player.selected.attack * 2)
                print("")
                print("The", enemy.bear.name, "hesitates ! You attack for", (player.selected.attack * 2), "damage !")
                print("")
                print("The", enemy.bear.name, "has", enemy.bear.health, "health left !")
                if enemy.bear.health <= 0:
                    print("")
                    print("You have defeated the", enemy.bear.name, " !!")
                    reset_player()
                    battle_six()
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()

    # Player Turn

        def player_turn():
            print("")
            player_action = input("What will you do? (attack or defend) ")
            if player_action == "attack":
                print("")
                print("You attack the", enemy.bear.name, "for", player.selected.attack, "damage !")
                print("")
                enemy.bear.health = enemy.bear.health - player.selected.attack
                enemy.bear.attack = enemy.bear.attack * 2
                print("The", enemy.bear.name, "has", enemy.bear.health, "health left !")
                if enemy.bear.health <= 0:
                    print("")
                    print("You have defeated the", enemy.bear.name, " !!")
                    reset_player()
                    battle_six()
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()               
            elif player_action == "defend":
                enemy.bear.attack = enemy.bear.attack / 2
                print("")
                print("You guard against the", enemy.bear.name, " !")
                print("")
                print("The battle continues !")
                enemy_turn()            
            else:
                player.selected.health = player.selected.health - (enemy.bear.attack * 2)
                print("")
                print("You hesitate ! The", enemy.bear.name, "attacks for", (enemy.bear.attack * 2), "damage !")
                print("")
                print("You have", player.selected.health, "health left !")
                if player.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()

        player_turn()

    # Battle Four vs Man at Arms

    def battle_four():

        print("----------------------------------------------------------------")
        print("")
        print("You walk into a new room inside the dungeon.")
        print("")
        print("You are approached by a", enemy.man_at_arms.name, " !")

    # Enemy Turn

        def enemy_turn():
            random_number = random.randint(1, 10)
            enemy_action = random_number
            if enemy_action >= 1 and enemy_action <= 6:
                print("")
                print("The", enemy.man_at_arms.name, "attacks you for", enemy.man_at_arms.attack, "damage !")
                player.selected.health = player.selected.health - enemy.man_at_arms.attack
                player.selected.attack = player.selected.attack * 2
                print("")
                print("You have", player.selected.health, "health left !")
                if player.selected.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()
            elif enemy_action >= 7 and enemy_action <= 9:
                player.selected.attack = player.selected.attack / 2
                print("")
                print("The", enemy.man_at_arms.name, "guards against your attack !")
                print("")
                print("The battle continues !")
                player_turn()
            else:
                enemy.man_at_arms.health = enemy.man_at_arms.health - (player.selected.attack * 2)
                print("")
                print("The", enemy.man_at_arms.name, "hesitates ! You attack for", (player.selected.attack * 2), "damage !")
                print("")
                print("The", enemy.man_at_arms.name, "has", enemy.man_at_arms.health, "health left !")
                if enemy.man_at_arms.health <= 0:
                    print("")
                    print("You have defeated the", enemy.man_at_arms.name, " !!")
                    reset_player()
                    battle_five()
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()

    # Player Turn

        def player_turn():
            print("")
            player_action = input("What will you do? (attack or defend) ")
            if player_action == "attack":
                print("")
                print("You attack the", enemy.man_at_arms.name, "for", player.selected.attack, "damage !")
                print("")
                enemy.man_at_arms.health = enemy.man_at_arms.health - player.selected.attack
                enemy.man_at_arms.attack = enemy.man_at_arms.attack * 2
                print("The", enemy.man_at_arms.name, "has", enemy.man_at_arms.health, "health left !")
                if enemy.man_at_arms.health <= 0:
                    print("")
                    print("You have defeated the", enemy.man_at_arms.name, " !!")
                    reset_player()
                    battle_five()
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()               
            elif player_action == "defend":
                enemy.man_at_arms.attack = enemy.man_at_arms.attack / 2
                print("")
                print("You guard against the", enemy.man_at_arms.name, " !")
                print("")
                print("The battle continues !")
                enemy_turn()            
            else:
                player.selected.health = player.selected.health - (enemy.man_at_arms.attack * 2)
                print("")
                print("You hesitate ! The", enemy.man_at_arms.name, "attacks for", (enemy.man_at_arms.attack * 2), "damage !")
                print("")
                print("You have", player.selected.health, "health left !")
                if player.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()

        player_turn()

    # Battle Three vs Wolf

    def battle_three():

        print("----------------------------------------------------------------")
        print("")
        print("You walk into a new room inside the dungeon.")
        print("")
        print("You are approached by a", enemy.wolf.name, " !")

    # Enemy Turn

        def enemy_turn():
            random_number = random.randint(1, 10)
            enemy_action = random_number
            if enemy_action >= 1 and enemy_action <= 6:
                print("")
                print("The", enemy.wolf.name, "attacks you for", enemy.wolf.attack, "damage !")
                player.selected.health = player.selected.health - enemy.wolf.attack
                player.selected.attack = player.selected.attack * 2
                print("")
                print("You have", player.selected.health, "health left !")
                if player.selected.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()
            elif enemy_action >= 7 and enemy_action <= 9:
                player.selected.attack = player.selected.attack / 2
                print("")
                print("The", enemy.wolf.name, "guards against your attack !")
                print("")
                print("The battle continues !")
                player_turn()
            else:
                enemy.wolf.health = enemy.wolf.health - (player.selected.attack * 2)
                print("")
                print("The", enemy.wolf.name, "hesitates ! You attack for", (player.selected.attack * 2), "damage !")
                print("")
                print("The", enemy.wolf.name, "has", enemy.wolf.health, "health left !")
                if enemy.wolf.health <= 0:
                    print("")
                    print("You have defeated the", enemy.wolf.name, " !!")
                    reset_player()
                    battle_four()
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()

    # Player Turn

        def player_turn():
            print("")
            player_action = input("What will you do? (attack or defend) ")
            if player_action == "attack":
                print("")
                print("You attack the", enemy.wolf.name, "for", player.selected.attack, "damage !")
                print("")
                enemy.wolf.health = enemy.wolf.health - player.selected.attack
                enemy.wolf.attack = enemy.wolf.attack * 2
                print("The", enemy.wolf.name, "has", enemy.wolf.health, "health left !")
                if enemy.wolf.health <= 0:
                    print("")
                    print("You have defeated the", enemy.wolf.name, " !!")
                    reset_player()
                    battle_four()
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()               
            elif player_action == "defend":
                enemy.wolf.attack = enemy.wolf.attack / 2
                print("")
                print("You guard against the", enemy.wolf.name, " !")
                print("")
                print("The battle continues !")
                enemy_turn()            
            else:
                player.selected.health = player.selected.health - (enemy.wolf.attack * 2)
                print("")
                print("You hesitate ! The", enemy.wolf.name, "attacks for", (enemy.wolf.attack * 2), "damage !")
                print("")
                print("You have", player.selected.health, "health left !")
                if player.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()

        player_turn()

    # Battle Two vs Skeleton

    def battle_two():

        print("----------------------------------------------------------------")
        print("")
        print("You walk into a new room inside the dungeon.")
        print("")
        print("You are approached by an", enemy.skeleton.name, " !")

    # Enemy Turn

        def enemy_turn():
            random_number = random.randint(1, 10)
            enemy_action = random_number
            if enemy_action >= 1 and enemy_action <= 6:
                print("")
                print("The", enemy.skeleton.name, "attacks you for", enemy.skeleton.attack, "damage !")
                player.selected.health = player.selected.health - enemy.skeleton.attack
                player.selected.attack = player.selected.attack * 2
                print("")
                print("You have", player.selected.health, "health left !")
                if player.selected.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()
            elif enemy_action >= 7 and enemy_action <= 9:
                player.selected.attack = player.selected.attack / 2
                print("")
                print("The", enemy.skeleton.name, "guards against your attack !")
                print("")
                print("The battle continues !")
                player_turn()
            else:
                enemy.skeleton.health = enemy.skeleton.health - (player.selected.attack * 2)
                print("")
                print("The", enemy.skeleton.name, "hesitates ! You attack for", (player.selected.attack * 2), "damage !")
                print("")
                print("The", enemy.skeleton.name, "has", enemy.skeleton.health, "health left !")
                if enemy.skeleton.health <= 0:
                    print("")
                    print("You have defeated the", enemy.skeleton.name, " !!")
                    reset_player()
                    battle_three()
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()

    # Player Turn

        def player_turn():
            print("")
            player_action = input("What will you do? (attack or defend) ")
            if player_action == "attack":
                print("")
                print("You attack the", enemy.skeleton.name, "for", player.selected.attack, "damage !")
                print("")
                enemy.skeleton.health = enemy.skeleton.health - player.selected.attack
                enemy.skeleton.attack = enemy.skeleton.attack * 2
                print("The", enemy.skeleton.name, "has", enemy.skeleton.health, "health left !")
                if enemy.skeleton.health <= 0:
                    print("")
                    print("You have defeated the", enemy.skeleton.name, " !!")
                    reset_player()
                    battle_three()
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()               
            elif player_action == "defend":
                enemy.skeleton.attack = enemy.skeleton.attack / 2
                print("")
                print("You guard against the", enemy.skeleton.name, " !")
                print("")
                print("The battle continues !")
                enemy_turn()            
            else:
                player.selected.health = player.selected.health - (enemy.skeleton.attack * 2)
                print("")
                print("You hesitate ! The", enemy.skeleton.name, "attacks for", (enemy.skeleton.attack * 2), "damage !")
                print("")
                print("You have", player.selected.health, "health left !")
                if player.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()

        player_turn()

    # Battle One vs Rat

    def battle_one():
        
        print("----------------------------------------------------------------")
        print("")
        print("You walk into a new room inside the dungeon.")
        print("")
        print("You are approached by a", enemy.rat.name, " !")

    # Enemy Turn

        def enemy_turn():
            random_number = random.randint(1, 10)
            enemy_action = random_number
            if enemy_action >= 1 and enemy_action <= 6:
                print("")
                print("The", enemy.rat.name, "attacks you for", enemy.rat.attack, "damage !")
                player.selected.health = player.selected.health - enemy.rat.attack
                player.selected.attack = player.selected.attack * 2
                print("")
                print("You have", player.selected.health, "health left !")
                if player.selected.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues  !")
                    player_turn()
            elif enemy_action >= 7 and enemy_action <= 9:
                player.selected.attack = player.selected.attack / 2
                print("")
                print("The", enemy.rat.name, "guards against your attack  !")
                print("")
                print("The battle continues !")
                player_turn()
            else:
                enemy.rat.health = enemy.rat.health - (player.selected.attack * 2)
                print("")
                print("The", enemy.rat.name, "hesitates ! You attack for", (player.selected.attack * 2), "damage !")
                print("")
                print("The", enemy.rat.name, "has", enemy.rat.health, "health left !")
                if enemy.rat.health <= 0:
                    print("")
                    print("You have defeated the", enemy.rat.name, " !!")
                    reset_player()
                    battle_two()
                else:
                    print("")
                    print("The battle continues !")
                    player_turn()

    # Player Turn

        def player_turn():
            print("")
            player_action = input("What will you do ? (attack or defend) ")
            if player_action == "attack":
                print("")
                print("You attack the", enemy.rat.name, "for", player.selected.attack, "damage !")
                enemy.rat.health = enemy.rat.health - player.selected.attack
                enemy.rat.attack = enemy.rat.attack * 2
                print("")
                print("The", enemy.rat.name, "has", enemy.rat.health, "health left !")
                if enemy.rat.health <= 0:
                    print("")
                    print("You have defeated the", enemy.rat.name, " !!")
                    reset_player()
                    battle_two()
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()               
            elif player_action == "defend":
                enemy.rat.attack = enemy.rat.attack / 2
                print("")
                print("You guard against the", enemy.rat.name, " !")
                print("")
                print("The battle continues !")
                enemy_turn()            
            else:
                player.selected.health = player.selected.health - (enemy.rat.attack * 2)
                print("")
                print("You hesitate ! The", enemy.rat.name, "attacks for", (enemy.rat.attack * 2), "damage !")
                print("")
                print("You have", player.selected.health, "health left  !")
                if player.health <= 0:
                    print("")
                    print("You have died !!!")
                else:
                    print("")
                    print("The battle continues !")
                    enemy_turn()

        player_turn()

    def player_class_select():
        print("")
        print("Select Player Class: ")
        global player_class
        player_class = input("Paladin, Knight, Fighter, or Rogue ? ")
        if player_class == "Paladin":
            player.selected = player.paladin
        elif player_class == "Knight":
            player.selected = player.knight
        elif player_class == "Fighter":
            player.selected = player.fighter
        elif player_class == "Rogue":
            player.selected = player.rogue
        elif player_class == "Dev":
            player.selected = player.test
        else:
            print("Input Error  !")
            print("Make sure the first letter of your selected class is capitalized !")
            player_class_select() 

    player_class_select()

    print("")
    print("You selected: ")
    print(player.selected.name)
    print("")
    print("Your starting health is: ")
    print(player.selected.health)
    print("")
    print("Your starting attack is: ")
    print(player.selected.attack)

    battle_one()

    # Player Status

def reset_player():
    if player_class == "Paladin":
        player.selected.attack = player.paladin_base.attack
    elif player_class == "Knight":
        player.selected.attack = player.knight_base.attack
    elif player_class == "Fighter":
        player.selected.attack = player.fighter_base.attack
    elif player_class == "Rogue":
        player.selected.attack = player.rogue_base.attack
    else:
        player.selected.attack = player.test_base.attack

def player_buff():
    if player_class == "Paladin":
        player.paladin = player.paladin_buff
    elif player_class == "Knight":
        player.knight = player.knight_buff
    elif player_class == "Fighter":
        player.fighter = player.fighter_buff
    elif player_class == "Rogue":
        player.rogue = player.rogue_buff
    else:
        player.selected.attack = player.test_buff.attack

def reset_player_after_buff():
    if player_class == "Paladin":
        player.selected.attack = player.paladin_buff.attack
    elif player_class == "Knight":
        player.selected.attack = player.knight_buff.attack
    elif player_class == "Fighter":
        player.selected.attack = player.fighter_buff.attack
    elif player_class == "Rogue":
        player.selected.attack = player.rogue_buff.attack
    else:
        player.selected.attack = player.test_buff.attack

start_game()