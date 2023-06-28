

from requests_html import HTMLSession
import pickle

url_base="https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="


def get_pokemon(pokemon_number):
    url="{}{}".format(url_base,pokemon_number)
    session=HTMLSession()
    pokemon_page=session.get(url)

    pokemon_base={"name":"",
              "base_health":100,
              "health":100,
              "type":"",
              "attacks":"",
                        }

    pokemon_base["name"]=pokemon_page.html.find('.mini', first=True).text.split("\n")[0]
    pokemon_base["type"]=[]
    pokemon_base["attacks"]=[]

    for img in pokemon_page.html.find(".pkmain", first=True).find(".bordeambos",first=True).find("img"):
        pokemon_base["type"].append(img.attrs["alt"])


    for attack_item in pokemon_page.html.find(".pkmain")[-1].find("tr .check3"):    
        attack={
          "name":attack_item.find("td",first=True).find("a", first=True).text,
          "type":attack_item.find("td")[1].find("img",first=True).attrs["alt"],
          "min_level":attack_item.find("th",first=True).text,
          "damage": int(attack_item.find("td")[3].text.replace("--","0")), 
          }
        
        pokemon_base["attacks"].append(attack)
        

    return pokemon_base



def get_all_pokemons():
    
    all_pokemons=[]
    try:
        with open ("pokefile.pkl","rb") as pokefile:
            all_pokemons=pickle.load(pokefile)
            print("The File is Ready!!..")

    except FileNotFoundError:
        print("We can Find the File, We will start to Downloaded!! \n Downloaded for internet...")
        for index in range(151):
            all_pokemons.append(get_pokemon(index+1))
            print("*",end="") 
        
        with open("pokefile.pkl", 'wb') as pokefile:
            pickle.dump(all_pokemons, pokefile)
        
        print("\n All the Pokemons are ready! ")
    
    return all_pokemons

get_all_pokemons()
