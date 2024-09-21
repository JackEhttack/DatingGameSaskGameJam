label desmond:
    "{i}You decide to study with Desmond.{/i}"

    if d_score == 0:
        show desmond_placeholder at center
        d "Heh, come to witness my superior intellect?"
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