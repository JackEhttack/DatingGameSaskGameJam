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
            call commodore

    if c_score == -1:
        $ c_score = 1
        jump study

    play music "music/make_it_count.wav"

    return

label tutorial:
    if not tutorial:
        "Tutorial" "It's time to study now!"
        "Tutorial" "Unfortunately, you are a narcoleptic and have the tendency get sleepy at very inopportune times."
        "Tutorial" "As you get more tired, the sleep dulls your senses and soon enough you won't even be able to read your own writing (<25\%), let alone the question."
        "Tutorial" "You have to really concentrate on keeping yourself awake by holding down on the sleepy meter."
        "Tutorial" "Additionally, your mind tends to wander and you need to focus on the question to properly read it. And you can't focus all that well while tired. (<75\%)"
        "Tutorial" "You only have so much stamina, and if you take too long you will no longer be able to recover your sleepy fast enough."
        menu:
            "Understood?"

            "Yes.":
                return
            
            "No.":
                jump tutorial
        
        $ tutorial = True