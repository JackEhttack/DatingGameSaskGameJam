label intro:

    play sound "sfx/intro_footsteps.wav"

    "{p=4}{cps=*0.2}You walk to the front of the lecture hall to grab your paper...{/cps}"

    scene hall
    with fade

    play sound "sfx/paper_noise.wav"

    show failed paper at top
    with moveinbottom

    "{p=1}..."

    "{i}Oh.{/i}"

    "{cps=*0.2}...{/cps}"

    show failed paper at default
    with move

    "{cps=*0.2}...{/cps}"

    "{i}Okay now that's just bullshit.{/i}"

    scene black
    with fade

    hide failed paper

    pause 1

    play music "music/make_it_count.wav"
    scene outside
    with fade

    "{i}I can't believe it. It was only first year math right?{/i}"
    "{i}I tried to study, I really did.{/i}"
    "{i}But as soon as I glanced at the first variable my eyes felt heavy and shortly after sleep took over my body.{/i}"

    show failed paper at top
    with moveinbottom

    "Stupid paper."

    hide failed paper at offscreenbottom
    with move

    play sound "sfx/paper_ripping.wav"

    show kate_placeholder at offscreenright

    "{p=2}..."

    show kate_placeholder at offscreenleft
    with MoveTransition(2)
    "???" "Yeah! Die stupid paper!!" 

    "{i}Huh...{/i}"
    "{i}Guess I'll head back to the dorms.{/i}"

    show commodore_placeholder at right
    with moveinright 

    "{i}Before you appears a well dressed man with a... monitor for a head.{p=1}He doesn't appear to be much older than you.{/i}" 
    "{i}He peers down at your tattered test. Even though you can't read his face you can still feel a twinge of disappointment.{/i}"
    "???" "Excuse me, are your initials {u}WC{/u}?"
    "Yes?"
    "???" "I have been informed that you did not pass the midterm."
    "Yeah..."
    "???" "Well, you have been {i}invited{/i} to attend our {b}mandatory{/b} study sessions."
    "???" "I host them every Wednesday, 3pm sharp on the first floor of the Amiga Library."
    "Right."
    "???" "I expect to see you there."
    "Uh-huh."
    show commodore_placeholder at offscreenright
    with move
    "{i}Ugh... 'invited' my ass.{/i}"
    show commodore_placeholder at right
    with move
    "???" "Forgot to mention. My name is Commadore, Professor Commadore."
    "{i}There is no way blud is a professor.{/i}"
    "Oh, mine's We-{p=1}{nw}"
    show v_placeholder at left, flip
    with moveinleft
    "{i}He's already wandered off to talk to another student. Presumably voluntelling them to join his study sessions.{/i}"

    scene black
    with fade

    pause 1

    jump day1