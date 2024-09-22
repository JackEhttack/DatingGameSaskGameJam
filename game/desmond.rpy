label desmond:

    play music "music/commodore_theme.wav"
    #play music "sfx/desmond_theme.wav"
    
    "{i}You decide to study with Desmond.{/i}"

    if d_score == 0:
        show desmond normal at center
        d "Heh, come to witness my superior intellect?"
        "Uhh no?"
        "What's your name?"
        d "My name is Desmond, the smartest person you'll ever meet"
        "Then why are you here?"
        d "You think I'm here to improve my grade?"
        d "HAHAHAHAHA!!" #He is laughing/smiling during this
        d "You're all just simple barbarians and morons compared to me" 
        d "You know what just for the hell of it I guess I'll help you."
        d "What do you need help with"
        
        #You proceed to do the math game with desmond and if you're right his score goes up else it goes down
        call tutorial
        call screen Minigame("Question", "Answer")

        $ d_score = 1
        d "You're not that dumb kid, although that was a pretty simple question" #Just a neutral face
        return

    
        #This is if you fail the minigame
        $ d_score = 0
        return

    if d_score == 1:
        d "Oh, its you again you need help again."
        d "Sure I guess, here's a vector problem"
        
        #You do the math minigame again
        call screen Minigame("Question", "Answer")
        
        $ d_score = 2
        return

    if d_score == 2:
        d "Not implemented."

        call screen Minigame("Question", "Answer")

        $ d_score = 3
        return

label desmond_ending:
    d "Umm actually, it's my ending."
    # classroom
    