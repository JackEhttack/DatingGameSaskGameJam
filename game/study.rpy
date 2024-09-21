label study:
    play music "music/make_it_count.wav"

    scene study
    menu:
        "Who should I study with?"

        "Study with Desmond":
            call desmond

        "Study with V":
            call v_dialogue

        "Study with Kate":
            call kate

        "Study with Professor Commodore":
            call commadore

    if c_score == -1:
        $ c_score = 1
        jump study

    play music "music/make_it_count.wav"

    return