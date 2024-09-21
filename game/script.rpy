# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("V")
define k = Character("Kate")
define d = Character("Desmond")
define c = Character("Professor Commadore")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    play sound "sfx/intro_footsteps.wav"

    "{p=4}{cps=*0.2}You walk to the front of the lecture hall to grab your paper...{/cps}"

    play sound "sfx/"

    show sprites failed_paper

    "{p=2}Shit..."

    # e "You've created a new Ren'Py game."

    # "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
