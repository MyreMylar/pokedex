import random
import tkinter
from util.pokeapi import get_pokemon_data, get_pokemon_image

# -----------------------------------------------------------------------------------------
# Using the Tkinter graphical user interface library
# ---------------------------------------------------
#
# Tkinter is a python library for creating graphical user interfaces. A library is just a
# load of code already written by somebody else and made available (usually on the internet)
# for other people to use. Generally libraries that are popular are those focused on a particular
# task, or group of related tasks.
#
# We use GUI as a shorthand for Graphical User Interface. I pronounce it 'gooey'.
#
# You can see in the bit of code above that I have written 'import tkinter', this is so that we can use
# the tkinter library in our code. We also import random and some functions from our pokeapi code file.
#
# -----------------------------------------------------------------------------------------
# Scroll down past challenge 3 to reach challenges 1 & 2 which are at the bottom of the file!
# ------------------------------------------------------------------------------------------

# define fonts
small_font = ["Ariel", 10]
small_bold_font = ["Ariel", 10, "bold"]
medium_font = ["Ariel", 14]
big_font = ["Ariel", 24]


# This function is used to update the UI labels
# based on a pokemon database
def show_pokemon_data():
    # -------------------------------------------------------------
    # Challenge 3
    # -------------
    # Get the number typed into the entry box
    # - Don't forget to assign the number to a variable
    # - Pass the number into the get_pokemon_data() function
    #   you can use pokemon_number as your variable name or a new
    #   variable name you make up.
    # ------------------------------------------------------------

    # use the function above to get the pokemon data and the image
    pokemon_dictionary = get_pokemon_data(pokemon_number)
    pokemon_image = get_pokemon_image(pokemon_number)

    # --------------------------------------------------------------
    # Challenge 3 continued
    # -----------------------
    # Get the data from the dictionary and use it to set the label's
    # text
    # - I have provided commented out examples of the code you need below
    # - You will need to change the label variable names (e.g. 'label_name_value') to your
    #   own label variables.
    # -----------------------------------------------------------
    
    # label_name_value.configure(text = pokemon_dictionary["name"])
    # label_hp_value.configure(text = pokemon_dictionary["hp"])
    # label_attack_value.configure(text = pokemon_dictionary["attack"])
    # label_defence_value.configure(text = pokemon_dictionary["defense"])
    # label_speed_value.configure(text = pokemon_dictionary["speed"])
    
    # add the image and add it to a label
    label_image.configure(image=pokemon_image)
    label_image.image = pokemon_image


# --------------------------------------------------------------------------
# Challenge 1 
# ------------
# I have defined some GUI elements for you already that you can modify.
# - Make the changes described on the worksheet to make the example elements
#   more like a pokedex.
# --------------------------------------------------------------------------

# create the main window
window = tkinter.Tk()
window.config(bg="#e0e0ff")
window.minsize(250, 300)
window.title("Basic GUI")

# label for text entry
label_entry = tkinter.Label(window, text="Text Entry:", font=small_font)
label_entry.config(bg="#e0e0ff", fg="#111111")
label_entry.pack()  # this command determines the layout of the GUI element, pack is the simplest layout.

# text entry widget
text_entry = tkinter.Entry(window, text="", font=small_font)
text_entry.pack()

# button
go_button = tkinter.Button(window, text="Button", font=small_font)
go_button.pack()

# ------------------------------------------------------------
# Challenge 1 & 2
# ------------
# Add new labels below this comment as described on the worksheet.
# - Remember to rename the label's variable name after copy pasting
# ------------------------------------------------------------


# label for an image
label_image = tkinter.Label(window)
label_image.config(bg="#e0e0ff", fg="#111111")
label_image.pack()

window.mainloop()
