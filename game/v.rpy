label v_dialogue:

    play music "music/v_theme.wav"

    "{i}You decide to study with V.{/i}"

    if v_score == 0:
        show v_placeholder at center
        "{i} She seems uninterested and barely notices you there.{/i}"
        "{i}You decide to just work alongside her silently until you can leave{/i}"
        "{i}As you're working you start to hear heavy metal music playing.{/i}"
        "{i}You realize it's coming from her earbuds and you decide to ask her{/i}"
        "So , which heavy metal band is you're favourite?"
        "{i}She finally looks up at you{/i}"
        v "You listen to heavy metal too?" #She has a suprised expression on her while asking
        "I dabble in heavy metal such as: Slipknot and Iron Maiden"
        v "Sweet, hey I need help with this equation can you help me?"
        
        call tutorial
        call screen Minigame("Question", "Answer")

        #You proceed to do the math game with v and if you win her score goes up else it goes down
        $ v_score = 1
        return

    if v_score == 1:
        v ""

        call screen Minigame("Question", "Answer")

        $ v_score = 2
        return

    if v_score == 2:
        v ""

        call screen Minigame("Question", "Answer")

        $ v_score = 3
        return

label v_ending:
    v "You got my ending... or something."
