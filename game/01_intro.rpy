label intro:

    play sound "sfx/intro_footsteps.wav"

    "{p=4}{cps=*0.2}You walk to the front of the lecture hall to grab your paper...{/cps}"

    scene hall
    with fade

    play sound "sfx/paper_noise.wav"

    show failed paper at default
    with moveinbottom

    "{p=1}..."

    "Oh."

    "{cps=*0.2}...{/cps}"

    show failed paper at center

    "Okay now that's just bullshit."

    ""
    scene None
    with fade

    jump day1