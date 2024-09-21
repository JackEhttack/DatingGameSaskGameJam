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

    scene hall
    with fade

    play sound "sfx/paper_noise.wav"

    if v_score + c_score + d_score + k_score <= 0:
        "{i}I can hardly spell my own name on the page, let alone attempt any of the questions.{/i}"
        "{i}I'll just put down c for every answer. That'll work.{/i}"
    elif v_score + c_score + d_score + k_score == 1:
        "{i}This is tough.{/i}"
    elif v_score + c_score + d_score + k_score == 2:
        "{i}{/i}"
    elif v_score + c_score + d_score + k_score == 3:
        "{i}{/i}"

    return
