from GamePokemon import get_all_pokemons
import random
from pprint import pprint 
import os

def clearscreen():
    os.system("cls")

def get_player_profile(pokemon_list):
    return {
        "Player_name": input("What is your name? "),
        "pokemon_inventory":[random.choice(pokemon_list) for a in range(3)],
        "Combats":0,
        "Pokeballs":0,
        "Health_potions":0

    }

def check_life_pokemons(player_profile,pokemon_choose):
    health_values=[pokemon["health"] for pokemon in player_profile["pokemon_inventory"]]
    if all (health==0 for health in health_values):
        return 0
    else:
        return health_values


def choose_pokemon_started(player_profile, enemy_pokemon):
    pokemon_info=[(pokemon["name"],pokemon["type"]) for pokemon in player_profile["pokemon_inventory"]]
    print('\nHi {}! This pokemons are for you'.format(player_profile["Player_name"]))
    c=0
    for names,type in pokemon_info:
        c+=1
        types_str='/'.join(type).capitalize()
        print("{}.{} ({})\t\t".format(c,names, types_str), end="\t\t")
    name_enemy=enemy_pokemon["name"]
    type_enemy='/'.join(enemy_pokemon["type"]).capitalize()
    print('\n')
    list_enemy=["{} ({})".format(name_enemy,''.join(type_enemy))]
    print("\nThe Pokemon Enemy is going to be: {}".format(list_enemy[0]))
    loop_finish=True
    while loop_finish: 
        try:
            pokemon=int(input("\nPress The Number of the Pokemon you want "))
            if pokemon==1:
                pokemon_choose=pokemon_info[0]
                print("\nLets go! {}".format(pokemon_choose[0]))
                loop_finish=False
            elif pokemon==2:
                pokemon_choose=pokemon_info[1]
                print("\nLets go! {}".format(pokemon_choose[0]))
                loop_finish=False
            elif pokemon==3:
                pokemon_choose=pokemon_info[2]
                print("\nLets go! {}".format(pokemon_choose[0]))
                loop_finish=False

            return pokemon
        except ValueError:
            print("You need to choose a correct number of pokemon. (1, 2, 3)\n\t\t\tTry it again")

def fight(player_profile,enemy_pokemon,pokemon_choose):
    clearscreen()
    print ("The Trainer {} started the Batlle!!!".format(player_profile["Player_name"]))
    print("The only way to get out of this battle is wining the Combat Pokemon! \n \t\t Good Luck! \t\t")
    input("\n Press Enter to start the battle")
    clearscreen()
    
    pokemonn_list=player_profile["pokemon_inventory"]

    pokemon_choose_final=pokemonn_list[pokemon_choose-1]

    life_pokemon_mine=pokemon_choose_final['health']
    
    life_pokemon_enemy=enemy_pokemon['health']

    barras=20

    barra_vida_p=int((barras*life_pokemon_mine)/pokemon_choose_final["base_health"])
    barra_vida_e=int((barras*life_pokemon_enemy)/enemy_pokemon["base_health"])

    print("{}:  [{}{}]  ({}/{})".format(pokemon_choose_final["name"],'*'*barra_vida_p,""*(barras-barra_vida_p),life_pokemon_mine,pokemon_choose_final["base_health"]))
    print("{}:  [{}{}]  ({}/{})".format(enemy_pokemon["name"],'*'*barra_vida_e,""*(barras-barra_vida_e),life_pokemon_enemy,enemy_pokemon["base_health"]))
    print("\n")
    # attacks
    attack_player=pokemon_choose_final["attacks"]
    attack_enemy=enemy_pokemon["attacks"]

    while life_pokemon_mine>0 and life_pokemon_enemy>0:
        clearscreen()
        print("Turno de {} ".format(enemy_pokemon["name"]))
        ataque_enemy=random.randint(0,3)
        if ataque_enemy==0:
            attack=attack_enemy[0]
            print('{} used {}! \n'.format(enemy_pokemon["name"],attack["name"]))
            life_pokemon_mine-=attack["damage"]
        elif ataque_enemy==1:
            attack=attack_enemy[1]
            print('{} used {}! \n'.format(enemy_pokemon["name"],attack["name"]))
            life_pokemon_mine-=attack["damage"]
        elif ataque_enemy==2:
            attack=attack_enemy[2]
            print('{} used {}! \n'.format(enemy_pokemon["name"],attack["name"]))
            life_pokemon_mine-=attack["damage"]
        elif ataque_enemy==3:
            attack=attack_enemy[3]
            print('{} used {}! \n'.format(enemy_pokemon["name"],attack["name"]))
            life_pokemon_mine-=attack["damage"]
        
        if life_pokemon_enemy<0:
            life_pokemon_enemy=0
            print("{}:  [{}{}]  ({}/{})".format(pokemon_choose_final["name"],'*'*barra_vida_p,""*(barras-barra_vida_p),life_pokemon_mine,pokemon_choose_final["base_health"]))
            print("{}:  [{}{}]  ({}/{})".format(enemy_pokemon["name"],'*'*barra_vida_e,""*(barras-barra_vida_e),life_pokemon_enemy,enemy_pokemon["base_health"]))
            break
        elif life_pokemon_mine<0:
            life_pokemon_mine=0
            print("{}:  [{}{}]  ({}/{})".format(pokemon_choose_final["name"],'*'*barra_vida_p,""*(barras-barra_vida_p),life_pokemon_mine,pokemon_choose_final["base_health"]))
            print("{}:  [{}{}]  ({}/{})".format(enemy_pokemon["name"],'*'*barra_vida_e,""*(barras-barra_vida_e),life_pokemon_enemy,enemy_pokemon["base_health"]))
            break
        else:
            print("{}:  [{}{}]  ({}/{})".format(pokemon_choose_final["name"],'*'*barra_vida_p,""*(barras-barra_vida_p),life_pokemon_mine,pokemon_choose_final["base_health"]))
            print("{}:  [{}{}]  ({}/{})".format(enemy_pokemon["name"],'*'*barra_vida_e,""*(barras-barra_vida_e),life_pokemon_enemy,enemy_pokemon["base_health"]))

        if life_pokemon_mine>0:
            input('Press enter to continue.... \n \n')
            clearscreen()

            print("Turn of {} ".format(pokemon_choose_final["name"]))
            ataque_player=None

            attack_number_1=attack_player[0]
            attack_number_2=attack_player[1]
            attack_number_3=attack_player[2]
            attack_number_4=attack_player[3]

            print("Choose one of the Following attacks!\n \t\t1.{} ({})\t\t 2.{} ({}) \t\t 3.{} ({})\t\t 4.{} ({})\t\t "
                .format(attack_number_1["name"],attack_number_1["type"],
                        attack_number_2["name"], attack_number_2["type"],
                        attack_number_3["name"], attack_number_3["type"],
                        attack_number_4["name"],attack_number_4["type"]))
        
            while ataque_player!=1 and ataque_player!=2 and ataque_player!=3 and ataque_player!=4:
                ataque_player=int(input("\n ------>  "))
                if ataque_player==1:
                    print('{} used {}! \n'.format(pokemon_choose_final["name"],attack_number_1["name"]))
                    life_pokemon_enemy-=attack_number_1["damage"]
                elif ataque_player==2:
                    print('{} used {}! \n'.format(pokemon_choose_final["name"],attack_number_2["name"]))
                    life_pokemon_enemy-=attack_number_2["damage"]
                elif ataque_player==3:
                    print('{} used {}! \n'.format(pokemon_choose_final["name"],attack_number_3["name"]))
                    life_pokemon_enemy-=attack_number_3["damage"]
                elif ataque_player==4:
                    print('{} used {}! \n'.format(pokemon_choose_final["name"],attack_number_4["name"]))
                    life_pokemon_enemy-=attack_number_4["damage"]
        
            print('\n')

        clearscreen()

        barra_vida_p=int((barras*life_pokemon_mine)/pokemon_choose_final["base_health"])
        barra_vida_e=int((barras*life_pokemon_enemy)/enemy_pokemon["base_health"])

        if life_pokemon_mine<0:
            life_pokemon_mine=0
        elif life_pokemon_enemy<0:
            life_pokemon_enemy=0

        print("{}:  [{}{}]  ({}/{})".format(pokemon_choose_final["name"],'*'*barra_vida_p,""*(barras-barra_vida_p),life_pokemon_mine,pokemon_choose_final["base_health"]))
        print("{}:  [{}{}]  ({}/{})".format(enemy_pokemon["name"],'*'*barra_vida_e,""*(barras-barra_vida_e),life_pokemon_enemy,enemy_pokemon["base_health"]))
        
    clearscreen()

    if life_pokemon_mine> life_pokemon_enemy:
        print ("{} Won the battle!!".format(pokemon_choose_final["name"]))
        combats_win=player_profile["Combats"]
        combats_win+=1
        combat="win"
        player_profile["Combats"]=combats_win
        print ("Win Combats: {}".format(combats_win))
        input("Press Enter to continue...")
        pokemonn_list=player_profile["pokemon_inventory"]
        pokemon_choose_final['health']=life_pokemon_mine
        clearscreen()
        return player_profile,combat
    else:
        combat="lose"
        print("{} Won!!".format(enemy_pokemon["name"]))
        print("If you have more pokemons available, lets use them!!")
        pokemonn_list=player_profile["pokemon_inventory"]
        pokemon_choose_final['health']=life_pokemon_mine
        return player_profile,combat
def main ():
    pokemon_list=get_all_pokemons()
    player_profile=get_player_profile(pokemon_list)   
    enemy_pokemon=random.choice(pokemon_list)
    pokemon_choose=choose_pokemon_started(player_profile,enemy_pokemon)
    game_on=True
    fight_rest,estate_combat=fight(player_profile,enemy_pokemon,pokemon_choose)
    player_profile=fight_rest
    while game_on:
        health_all_pokemons=check_life_pokemons(player_profile,pokemon_choose)
        if health_all_pokemons==0 and estate_combat=="lose":
            game_on=False
            print("The combat ends...")
            break
        elif estate_combat=="lose":    
            pokemon_choose=choose_pokemon_started(player_profile,enemy_pokemon)
            player_profile,estate_combat=fight(player_profile,enemy_pokemon,pokemon_choose)
        else:
            same_pokemon=input("Do you want continue with the same pokemon? Y/N ")
            if same_pokemon=="Y":
                enemy_pokemon=random.choice(pokemon_list)
                pokemon_choose_final=pokemon_choose
                player_profile,estate_combat=fight(player_profile,enemy_pokemon,pokemon_choose_final)

            elif same_pokemon=="N":
                enemy_pokemon=random.choice(pokemon_list)
                pokemon_choose=choose_pokemon_started(player_profile,enemy_pokemon)
                player_profile,estate_combat=fight(player_profile,enemy_pokemon,pokemon_choose)
                
        

if __name__=="__main__":
    main()