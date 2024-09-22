label commadore:
    # commadore has four relationship score, it increases by two after the first encounter though so it's mostly the same
    
    if c_score == 0:
        
        "{i}You decide to study with the Professor.{/i}"

        show commodore_placeholder at right
        stop music fadeout 0
        # show jumpscare
        c "No."
        # backup
        c "You have classmates do you not?"
        $ c_score = -1
        return

    "{i}You decide to study with the Professor.{/i}"

    if c_score == 1:
        show commodore_placeholder
        with moveinbottom
        c "If you insist."
        "{i}You take a seat next to the Professor and begin quietly going over class material.{/i}"
        "{i}The library is nearly silent, only occasionally being broken by one of the others calling him over for assistance.{/i}"
        "{i}He remains quiet and focused on his own work. You can't see exactly what he's working on but you can only assume he's grading assignments.{/i}"
        "{i}A thought re-enters the back of your mind.{w} Is he really a professor?{/i}"
        "{i}He looks way too young to have been in school for at least ten years{/i}"
        menu:
            "Ask him?"

            "Sure.":
                "Commadore... are you really a professor?"
                stop music
                c "..."
                "{i} The rest of the room looks over."
                c "..."
                c "No."
                c "..."
                "..."
                "{i}The rather dull silence bittered into an awkward silence.{/i}"
                "{i}He continues.{/i}"
                c "I want to be one some day."
                play music "music/make_it_count.wav"

            "Remain silent.":
                "{i}You continue studying, letting that intrusive thought escape you.{/i}"

        call tutorial
        call screen Minigame("Question", "Answer")

        $ c_score = 2
        return

    if c_score == 2:
        c "Not implemented."

        call screen Minigame("Question", "Answer")

        # funny coffee gag
        $ c_score = 3
        return

    if c_score == 3:
        c "Not implemented."

        call screen Minigame("Question", "Answer")

        $ c_score = 4
        return

label commadore_ending:
    c "Oh joy, it's my ending."
    # coffee