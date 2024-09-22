label desmond:

    play music "music/commodore_theme.wav"
    #play music "sfx/desmond_theme.wav"
    
    "{i}You decide to study with Desmond.{/i}"

    if d_score == 0:
        show desmond_placeholder at center

        "{i}You decide to study with Desmond.{/i}"
        
        d "Heh, come to witness my superior intellect?"
        "Uhh no?"
        "What's your name?"
        d "My name is Desmond, the smartest person in the room."
        "I'm W.C but then why are you here?"
        d "You think I'm here to improve my grade?"
        show desmond happy
        d "HAHAHAHAHA!!"
        show desmond normal
        d "You're all so below me in intelligence." 
        d "You know what just for the hell of it I guess I'll help you."
        d "What do you need help with?"
        
        #You proceed to do the math game with desmond and if you're right his score goes up else it goes down
        call tutorial
        call screen Minigame("Question", "Answer")

        $ d_score = 1
        show desmond disappointed
        d "Heh, not bad kid you did alright."
        d "But still beneath me in intelligence."
        "Umm.. thanks for the compliment."
        "I guess I'll see you tommorrow."
        return

    if d_score == 1:
        show desmond_placeholder at center
        
        "{i}You walk over to Desmond again.{/i}"
        show desmond disappointed
        d "Oh, hey it's you again."
        "{i}He says this and quickly hides something in his binder.{/i}"
        "Hey Desmond what are you doing?"
        d "Nothing don't worry about it"
        "Tell me what's going on"
        show desmond normal
        d "*SIGHS* Okay I'm having trouble with this problem"
        "Oh really, let me see if I can solve it"
        show desmond disappointed
        d "I doubt YOU could solve this problem."
        
        #You do the math minigame again
        call screen Minigame("Question", "Answer")
        
        $ d_score = 2
        show desmond angry
        d "Wait what how did you solve that??"
        "It wasn't super difficult"
        show desmond disappointed
        d "It seems I have underestimated your abilities..."
        return

    if d_score == 2:
        show desmond_placeholder at center
        show desmond normal
        "{i}You sit down next to Desmond again.{/i}"
        "{i}You also notice that most of nalis are painted a bright orange.{/i}"
    
        d "Hey W.C"
        "Hey Desmond, are you ready for the final exam?"
        d "Of COURSE I am."
        "..."
        "What's going on with your nails?"
        "{i}He looks down at his nails then looks away{/i}"
        show desmond disappointed
        d "Umm.. that was my sister... "
        d "she did them."
        d "She wanted to paint my nails last night, so I let her."
        "Thats pretty nice of you."
        show desmond angry
        d "Hey!"
        d "Let's not get off track! we need to study for the final exam."

        #You do the math minigame with him again

        $ d_score = 3
        show desmond happy
        d "I think we're finally ready for the test"
        "You think so?"
        show desmond disappointed
        d "I said it didn't I?"
        "Hey Desmond, tell your sister she did a good job"
        d "Uhh.."
        d "I'll relay the message."
        return

label desmond_ending:
    show desmond_placeholder at center
    "{i}Desmond and you seem to be the last people to leave the exam hall.{/i}"

    "Hey Desmond I passed! What about you."
    show desmond happy
    d "Is that even a question?"

    "{i}He pushes his glasses upwards as they shine from their glint.{/i}"
    "{i}He slams his paper on a table to show a grade better than yours.{/i}"

    "Yeah that's not suprising."
    return