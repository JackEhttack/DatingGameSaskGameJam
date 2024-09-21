# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("V")
define k = Character("Kate")
define d = Character("Desmond")
define c = Character("Professor Commadore")

image hall = "images/lecture_hall.jpg"
image outside = "images/outside_school.jpg"
image study = "images/study_room.jpg"

image failed paper = "images/sprites/failed_paper.png"

transform offscreenbottom:
    yalign -2.0

define walk_by = MoveTransition(2)

# The game starts here.

label start:

    # c "hello!"
    # scene bg room
    # show eileen happy
    # with transition

    jump intro
