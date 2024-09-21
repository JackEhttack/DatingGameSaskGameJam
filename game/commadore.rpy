label commadore:
    # commadore has four relationship score, you need it increases by
    "{i}You decide to study with the Professor.{/i}"
    if c_score == 0:
        show commodore_placeholder at right
        # show jumpscare
        c "No."
        # backup
        c "You have classmates do you not?"
        $ c_score = -1
        return

    if c_score == 1:
        c "If you insist."
        $ c_score = 2
        return

    if c_score == 2:
        c "Not implemented."
        $ c_score = 3
        return

    if c_score == 3:
        c "Not implemented."
        $ c_score = 4
        return

label commadore_ending:
    c "Oh joy, it's my ending."
    # coffee