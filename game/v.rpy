label v_dialogue:
    "{i}You decide to study with V.{/i}"

    if v_score == 0:
        show v_placeholder at center
        "{i} She seems unintereseted and barely notices you there{/i}"
        "You try to start a conversation but she is cold to you and doesn't respond"
        "You decide to just work alongside her silently until you can leave"
        $ v_score = 1
        return

    if v_score == 1:
        v ""
        $ v_score = 2
        return

    if v_score == 2:
        v ""
        $ v_score = 3
        return

label V_ending:
    v ""
