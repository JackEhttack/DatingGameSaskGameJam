label kate:
    "{i}You decide to study with Kate.{/i}"

    if k_score == 0:
        show kate_placeholder at center
        k "What do you want dweeb?"
        "Ummm, my name is WC. What's your's?"
        k "Like I'd tell you dweeb"
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
    k ""
