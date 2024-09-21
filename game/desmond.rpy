label desmond:
    play music "sfx/desmond_theme.wav"
    "{i}You decide to study with Desmond.{/i}"

    if d_score == 0:
        show desmond_placeholder at center
        d "Heh, come to witness my superior intellect?"
        "Uhh no?"
        "What's your name?"
        d "My name is Desmond, the smartest person you'll ever meet"
        "Then why are you here?"
        d "You think I'm here to improve my grade?"
        d "HAHAHAHAHA!!"
        

        $ d_score = 1
        return

    if d_score == 1:
        d "Not implemented."
        $ d_score = 2
        return

    if d_score == 2:
        d "Not implemented."
        $ d_score = 3
        return

label desmond_ending:
    d "Umm actually, it's my ending."
    # classroom