label v_dialogue:

    play music "music/v_theme.wav"

    if v_score == 0:
        show v_placeholder at center
        "{i}You decide to sit next to the gloomy one.{/i}"
        "HI I'm W.C; what's your name?"
        v "V."
        "..."
        "..."
        "{i}Great Start{/i}"
        "{i}You pull your heavy textbooks form your bag, letting them fall on the table with a resoudning *THUMP*"
        "{i}V looks right at you{/i}"
        v "Was that loud enough for you?"
        "I just wanted to make sure the table knew I meant business."
        
        menu:
            v "Clearly..."
        
            "What's your plan for this session":
                v "Study quietly, by myself"
        
            "Wanna work together?":
                v "No thanks."
        
        "Oh.. ok"
        "{i}V puts on their headphones{/i}"
        "{i}Off to a great start W.C {/i}"
 
        #You proceed to do the math game and if you win her score goes up and you get some dialogue else it goes down and you silently leave
        $ v_score = 1
        menu:
            "You hear heavy metal music through their headphones"

            "Headbang to it":
                v "What are you doing?"
                "Rocking out"
                v "You actually like this music?"
                "Duh, who doesn't?"
                v "..."
                "{i}V looks pleasantly suprised"
                
            "Ignore it":
                "{i}You decide to ignore the music sneaking out of their headphones and continue studying"              
        return

    if v_score == 1:
        show v_placeholder at center
        "{i} You make your way over to V{/i}"
        
        menu:
            v "You again?"
        
            "Of course, why so suprised?":
                v "I just thought that you would run away after the first session."
                "And miss the story? No way!"

            "You say that like I'm a bad penny":
                v "More like an unfortunate detour"
                "Hey! Detours can lead to interesting places."
                v "Or dead ends."
                "True, but at least they can lead to good stories."
            
        v "If only math problems had plot."
        "Sure they do! John has 38 watermelons, Jane takes 4."
        v "I meant good stories."

        menu:
            v "Depends on the story, what did you have in mind?"
            "Knights and Dragons!":
                v "Eh.."
                "Well it's good enough for me"
                v "That says a lot about you"
                "Whatever"             
                        
            "Tragic Romance":
                v "Good taste, I like it"
                        

    #You do the math minigame here and if you win her score goes uop and you get some dialogue else it goes down and nothing happens
       
        $ v_score = 2
        v "You might not be a cog in the machine after all"
        "You really really really mean it?"
        v "Now I'm not so sure"
        return

    if v_score == 2:
        show v_placeholder at center
        "{i}You approach V once again.{/i}"
        "{i}This time they are wearing really cool looking accessories"
        "That looks totally hardcore"
        v "Really? Thanks."
        v "You are interested in this type of stuff?"
        "Definitely"
        v "Wanna see more? I have lots of stuff like this"
        "Would I ever!"
        v "Good, but first we need to pass our tests"

        #You do the math minigame/ the final test and if you succeed you get her ending
        $ v_score = 3
        return

label v_ending:
    show v_placeholder at center
    
    "{i}You walk up to V as you both leave the exam hall{/i}"
    "Hey I passed! What about you?"
    v "Same I passed too"
    v "So, what are you doing after this?"
    "Oh, I was proabably going back to my dorm. What about you?"
    v "Oh nothing, I was just wondering if you wanted to come back to my dorm and chill and listen to heavy metal?"
    "Yeah of course, let's go!"

    scene black

    "Congrats on the ending with V."
    return
