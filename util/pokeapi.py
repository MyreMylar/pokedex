import json
import tkinter


# function to get the data for a pokemon
def get_pokemon_data(num):
    data = open("data/" + str(num) + ".json", 'rb').read()
    pokemon_dict = json.loads(data.decode("UTF-8"))
    return pokemon_dict


# function to get the image for a pokemon
def get_pokemon_image(num):
    file_name = "data/img/" + str(num) + ".gif"
    tk_image = tkinter.PhotoImage(file=file_name)
    return tk_image
