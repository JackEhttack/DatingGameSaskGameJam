label ending:
    "{i}It's the day of the final.{/i}"
    if v_score + c_score + d_score + k_score <= 0:
        "{i}I feel like I know even less than I did on the first day.{/i}"
    elif v_score + c_score + d_score + k_score == 1:
        "{i}I'm not as ready as I could be, but there's nothing else I can do.{/i}"
    elif v_score + c_score + d_score + k_score == 2:
        "{i}I think I can take this, I'm pretty sure it won't be a perfect score but it'll certainly be a passing grade.{/i}"
    elif v_score + c_score + d_score + k_score == 3:
        "{i}This will be a breeze! I'll even tackle the bonus questions and hopefully make up for the abyssmal performance on the midterm.{/i}"
    
    pause 1

    scene hall
    with fade

    play sound "sfx/paper_noise.wav"
    show blank final
    with moveinbottom

    if v_score + c_score + d_score + k_score <= 0:
        "{i}I can hardly spell my own name on the page, let alone attempt any of the questions.{/i}"
        "{i}I'll just put down C for every answer. That'll work.{/i}"
    elif v_score + c_score + d_score + k_score == 1:
        "{i}This is tough. I'm making slow progress but I don't think I'll finish before the end.{/i}"
        "{i}I'll just put down C for the remaining answers. That'll work.{/i}"
    elif v_score + c_score + d_score + k_score == 2:
        "{i}This isn't nearly as bad as I thought it would be.{/i}"
        "{i}There's a two questions I can't quite answer and the bonus questions are too far out of my comfort zone to attempt.{/i}"
        "{i}I'll just put down C for those.{/i}"
    elif v_score + c_score + d_score + k_score == 3:
        "{i}Already twenty minutes in and I'm finished. Bonus questions and all.{/i}"
        "{i}I'm confident in all of my answers.{/i}"
        "{i}Surprisingly enough {b}none{/b} of the answers to any of the questions is C.{/i}"
        "{i}That's statistically suspect but it doesn't matter anyways."

    scene black
    with fade
    pause 1

    scene hall
    with fade

    "{i}Moment of truth...{/i}"
    play sound "sfx/paper_noise.wav"

    if v_score + c_score + d_score + k_score <= 0:
        show failed_final
        with moveinbottom
        "{i}In hindsight this is the expected outcome.{/i}"
        jump worst_end
    elif v_score + c_score + d_score + k_score == 1:
        show ok_final
        with moveinbottom
        "{i}This is a mercy pass if anything.{/i}"
        "{i}What sort of maniac gives one thousandth of a percent credit anyways?{/i}"
    elif v_score + c_score + d_score + k_score == 2:
        show good_final
        with moveinbottom
        "{i}I feel alright with this score.{/i}"
    elif v_score + c_score + d_score + k_score >= 3:
        show best_final
        with moveinbottom
        "{i}Easy peasy.{/i}"

    "{i}The rest of the students in the exam hall file out through the exits.{/i}"

    if v_score + c_score + d_score + k_score <= 0:
        "{i}You scantly recognize any faces.{/i}"

    scene black
    with fade
    pause 1.0
    scene outside
    with fade

    jump ending_decider

label ending_decider:
    if d_score == 1 and v_score == 1 and k_score == 1:
        jump best_end

    if c_score == 4:
        jump commadore_ending

    if v_score == 3:
        jump v_ending

    if k_score == 3:
        jump kate_ending

    if d_score == 3:
        jump desmond_ending

    # Congrats, you managed to hit the failsafe ending.
    jump worst_end

label worst_end:

    if v_score + c_score + d_score + k_score <= 0:
        "{i}With your head held low you stumble back towards your dorm room.{/i}"
    else:
        "{i}Lonely, but not defeated you walk back towards your dorm room.{/i}"
    "{i}Not even bothering to look both ways before crossing the-{/i}{nw}"
    scene black
    play sound "sfx/ouchie.wav"
    "..."
    "You did not make it count.\n{p}Join us in the next game where our protagonist, Wet Cardboard, is reincarnated into a fantasy world void of their only weakness: math."
    "Remember to look both ways before crossing the street kids!"
    return

label best_end:
    "Not implemented, but congrats on getting the best ending!"
    return



