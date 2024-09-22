label commodore:
    # commodore has four relationship score, it increases by two after the first encounter though so it's mostly the same
    
    if c_score == 0:
        
        "{i}You decide to study with the Professor.{/i}"

        show commodore normal at right
        stop music fadeout 0
        # show jumpscare
        show commodore angry
        c "No."
        # backup
        c "You have classmates do you not?"
        $ c_score = -1
        return

    "{i}You decide to study with the Professor.{/i}"

    if c_score == 1:
        show commodore normal
        with moveinbottom
        show commodore disappointed
        c "If you insist."
        "{i}You take a seat next to the Professor and begin quietly going over class material.{/i}"
        "{i}The library is nearly silent, only occasionally being broken by one of the others calling him over for assistance.{/i}"
        "{i}He remains quiet and focused on his own work. You can't see exactly what he's working on but you can only assume he's grading assignments.{/i}"
        "{i}A thought re-enters the back of your mind.{w} Is he really a professor?{/i}"
        "{i}He looks way too young to have been in school for at least ten years{/i}"
        menu:
            "Ask him?"

            "Sure.":
                "commodore... are you really a professor?"
                show commodore normal
                stop music
                c "..."
                "{i} The rest of the room looks over."
                c "..."
                show commodore disappointed
                c "No."
                c "..."
                "..."
                "{i}The rather dull silence bittered into an awkward silence.{/i}"
                "{i}He continues.{/i}"
                show commodore normal
                c "I want to be one some day."
                play music "music/make_it_count.wav"

            "Remain silent.":
                "{i}You continue studying, letting that intrusive thought escape you.{/i}"
                show commodore disappointed
                c "Is there something on my monitor?"
                "Oh uh, sorry?"
                c "You were staring at me."
                c "And yes, I am a professor."
                "{i}phew"

        #mathtime
        show commodore normal
        menu:
            "{i}what now?"
            
            "{i}I should flirt with him now":
                menu:
                    "{i}The time is now"

                    "How about some multiplication between you and I?":
                        show commodore disappointed
                        c "subtract yourself from my presence"

                    "I feel like we could manage some integration later.":
                        show commodore disappointed
                        c "what kind of integration?"
                        "the type with undefined limits"
                        show commodore angry
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
        show commodore_placeholder
        with moveinbottom
        c "You are very insistant with this arrangement"
        "well.. confidence is key"
        menu:
            c "It would make my life easier if you weren't so confident."
            "I should definitely try my pickup lines again":
                c "."
                c ".."
                c "..."
                show commodore disappointed
                menu:
                    c "just get it out of your system."

                    "Do you satisfy all the sentences of some formal theory? Because you look like a model.":
                        show commodore normal
                        c "I appreciate the compliment"
                        show commodore disappointed
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
                show commodore normal
                c "Good plan"
                #make math here
                #afterwards math is called again >
        #right here. this allows the player to do math after a pickup line
        #and do double math for the other option.

        # funny coffee gag
        $ c_score = 3
        return

    if c_score == 3:
        show commodore_placeholder
        show commodore normal
        with moveinbottom
        c "Once more before the exam I see?"
        
        "You know it"
        
        c "I do indeed."
        
        "{i}lets get to work!"
        #mathtime here

        "..."

        "do you find me annoying?"
        show commodore question
        c "what makes you say that?"

        "your entire character"
        show commodore disappointed
        c "well you are hard to ignore"

        "{i}A real compliment?!"

        c "That was not a compliment"

        "shoot"
        show commodore normal 
        menu:
            "{i}what now?"  

            "You already know!":
                menu:
                    c "I can tell whats coming..."
                    
                    "Every prime number 1 mod 4 is a sum of two squares. uhhh... wanna go out for dinner?":
                        show commodore disappointed
                        c "ran out of good ones?"
                        "erm.."
                        c "If you get to buy me a coffee will you finally leave me alone?"
                        "I don't know about thaaat.."
                        c "I'll take free coffee none the less. so long as you pass the exam."

                    "I can't come up with any!":
                        show commodore disappointed
                        c "Finally ran out?"
                        "Sort of."
                        c "Well im sure you will come up with new ones"
                        c "And i'm getting tired of this"
                        c "Will you stop bothering me if you get what you want?"
                        "Probably!."
                        c "well if you pass the exam you can buy me coffee. and you will stop."
                        "OKAY!"

                "Score!"
            
            "Home stretch!":
                show commodore question
                c "ready for the exam?"
                "yes sir!"
                show commodore normal
                c "good. I can be done with this assignment."
                "do you want to get coffee after?"
                c "free coffee? so long as you pass. thats reward enough."
                "{i}score!"

        c "Good luck"
        "{i}W.C. turns and leaves"
        c "finally"
        c "the pain is over"

        $ c_score = 4
        return

label commodore_ending:
    show commodore happy coffee
    c "Oh joy, a free fresh cup of coffee..."
    "enjoying it?"
    show commodore angry coffee
    c "oh right..."
    c "you're still here"
    show commodore disappointed coffee
    c "I was under the impression you would be silent"
    "Yeah but I lied"
    show commodore normal coffee
    c "I cant escape..."
    show commodore happy coffee
    c "In any case, I thank you for the coffee."


    # coffee