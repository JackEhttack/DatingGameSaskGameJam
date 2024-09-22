# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("V")
define k = Character("Kate")
define d = Character("Desmond")
define c = Character("Professor Commodore")

define v_score = 0
define k_score = 0
define d_score = 0
define c_score = 0

define tutorial = False

image hall = "images/lecture_hall.jpg"
image outside = "images/outside_school.png"
image study = "images/study_room.png"

image failed paper = "images/sprites/failed_paper.png"

image blank final = "images/sprites/blank_final.png"
image failed final = "images/sprites/failed_final.png"
image ok final = "images/sprites/ok_final.png"
image good final = "images/sprites/good_final.png"
image best final = "images/sprites/best_final.png"

image p end = "images/end/p_card.png"
image c end = "images/end/c_card.png"
image v end = "images/end/v_card.png"
image d end = "images/end/d_card.png"
image k end = "images/end/k_card.png"

transform veryleft:
    xanchor 1
    xpos 1

transform middleleft:
    xanchor 1
    xpos 0.25

transform middleright:
    xanchor 1
    xpos 0.5

transform veryright:
    xanchor 1
    xpos 0.75

transform offscreenbottom:
    yalign -2.0

transform flip:
    xzoom -1

# The game starts here.

label start:

    # scene outside_school
    # call screen Minigame("Name it chungy.", "Chungy.")
    call intro

    # put a thank you for playing our game here
