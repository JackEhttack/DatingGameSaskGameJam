label kate:

    play music "music/kate_theme.wav"

    if k_score == 0:
        show kate_placeholder at center
        "{i}You decide to study with Kate.{/i}"
        
        k "{b}Why can't I just play football instead{/b}"
        "{i}Huh, she sounds like she is struggling.{/i}"
        "{i}Maybe I can help?{/i}"
        "Hey, do you need any help at all"
        k "Really? I would really appreciate it dweeb"
        
        $ k_score = 1
        return

    if k_score == 1:
        k ""
        $ k_score = 2
        return

    if k_score == 2:
        k ""
        $ k_score = 3
        return

label kate_ending:
    k "You absolute IDIOT, did you really think you get to see MY ending????"
    k "Those puny stupid DEVELOPERS forgot to put it in the GAME."
    k "BWAHAHAHAHAHAHA."
    return
