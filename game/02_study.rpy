label day1:

    scene hall
    with fade

    "{i}Wowie, that was exceptionally boring lecture.{w=1} Even more so than normal."
    "{i}Think we were talking about trigonometry today?"
    "{i}Guess it's time to go to my mandatory study group."

    scene study
    with fade

    show commodore_placeholder at default, veryright
    with moveinright

    show desmond_placeholder at default, middleright
    with moveinright

    show kate_placeholder at default, middleleft
    with moveinleft

    show v_placeholder at default, flip, veryleft
    with moveinleft

    "{i}You arrive at the study room a few minutes later than you'd like, but it'll have to do.{/i}"

    # round table dialogue

    call study
    
    scene black
    with fade

    pause 1

    jump day2
