# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v_score = 0
define k_score = 0
define d_score = 0
define c_score = 0

define v = Character("V")
define k = Character("Kate")
define d = Character("Desmond")
define c = Character("Professor Commadore")

image hall = "images/lecture_hall.jpg"
image outside = "images/outside_school.jpg"
image study = "images/study_room.jpg"

image failed paper = "images/sprites/failed_paper.png"

image blank final = "images/sprites/blank_final.png"
image failed final = "images/sprites/failed_final.png"
image ok final = "images/sprites/ok_final.png"
image good final = "images/sprites/good_final.png"
image best final = "images/sprites/best_final.png"

transform offscreenbottom:
    yalign -2.0

transform flip:
    xzoom -1

# The game starts here.

label start:

    # c "hello!"
    # scene bg room
    # show eileen happy
    # with transition
    # jump ending
    call intro
