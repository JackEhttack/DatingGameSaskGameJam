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
                c "Is there something on my monitor?"
                "Oh uh, sorry?"
                c "You were staring at me."
                c "And yes, I am a professor."
                "{i}phew"

        #mathtime
        
        menu:
            "{i}what now?"
            
            "{i}I should flirt with him now":
                menu:
                    "{i}The time is now"

                    "How about some multiplication between you and I?":
                        c "subtract yourself from my presence"

                    "I feel like we could manage some integration later.":
                        c "what kind of integration?"
                        "the type with undefined limits"
                        c "No."

                    "on a scale of 1-10 I'd rate you an 'i' because you're unreal":
                        c "and I wish you were only imaginary"

                    "Are you category theory? because I dont get you at all":
                        c "Neither do I"
                        c "Now do your math"

                "{i}Worth a shot."

            "{i}I should study.":
                c "yes you should."
                "did he just read my mind?"
        
        "time for study i guess."
        
        #mathtime
        
        call screen pong

        $ c_score = 2
        return

    if c_score == 2:
        c "You are very insistant with this arrangement"
        "well.. confidence is key"
        menu:
        c "It would make my life easier if you weren't so confident."
            "I should definitely try my pickup lines again":
                c "."
                c ".."
                c "..."
                menu:
                    C "just get it out of your system."

                    "Do you satisfy all the sentences of some formal theory? Because you look like a model.":
                        c "I appreciate the compliment"
                        c "Not the intent behind it."

                    "Do you contain all of my limits? Because I think you complete me.":
                        c "Get to studying"

                    "Do you absorb multiplication from either side? Because I think you're ideal.":
                        c "Ideally... you would be studying"

                    "are you the non-trivial reduced local homology group of a manifold?":
                        "Because I'd like you to be on top."
                        c "I'm going to forget you said that."
                        c "And there's no way you came up with that."

                "worth a shot"
                c "No."
                c "No it was not."
            
            "Time to study hard":
                c "Good plan"
                #make math here
                #afterwards math is called again >
        #right here. this allows the player to do math after a pickup line
        #and do double math for the other option.

        # funny coffee gag
        $ c_score = 3
        return

    if c_score == 3:
        c "Not implemented."
        $ c_score = 4
        return

label commadore_ending:
    c "Oh joy, it's my ending."
    # coffee