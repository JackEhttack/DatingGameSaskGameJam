label kate:

    play music "music/kate_theme.wav"

    if k_score == 0:
        show kate_placeholder at center
        "{i}You sit down near a very outgoing athlete.{/i}"
        
        k "{b}Why can't I just play football instead uhh{/b}"
        "{i}Huh, she sounds like she is struggling.{/i}"
        "{i}Maybe I can help?{/i}"
        "Hey, do you need any help at all"
        k "I guess I could use some help"
        k "My name is Kate"
        "Call me W.C"
        
        #You do the math minigame with kate and if you succeed her score goes up and you have some dialogue else her score goes down

        $ k_score = 1
        k "Thanks for the help pointdexter!"
        "Yeah, no worries."
        k "Man I do not like math but I can't wait for the big game after the final exam"
        "Oh really what sport do you do?"
        k "I'm the quaterback of the football team" #She should be happy during this
        "Oh cool, I love football it's definitely my favourite sport"
        k "Same, football's definitely the best sport!"
        k "Well thanks for the help, see ya later" 
        return

    if k_score == 1:
        show kate_placeholder at center
        
        "{i}You walk over to Kate again{/i}"
        k "Oh hi it's you again!"
        "Hey, you need any help again?"
        k "Yes please!"
        k "If I don't pass the final exam I won't be able to participate in the big game afterwards."
        "No worries, let's get to it!"

#You do the math minigame again and if you succeed her socre goes up and you get some dialogue else her score goes down

        $ k_score = 2
        k "Thanks so much, pointdexter"
        k "I'm starting to finally get it a little bit"
        "Well that's good see ya later"
        return

    if k_score == 2:
        show kate_placeholder at center
        
        "{i}You go sit next to Kate again{/i}"
        k "Hey pointdexter, this stuff is actually starting to make sense"
        "Well that's good"
        k "Hey If we pass this test I challenge you to a 1v1 football game"
        "Well, I accpet."
        "But first let's make sure we're ready for it."

        #You do the last math mingame with her and if you succeed her score goes up and you get some dialogue else her score goes down

        $ k_score = 3
        k "We're going to slam this test"
        "Hopefully we do"
        k "Hey remeber if we pass, we got our 1v1"
        return

label kate_ending:
    show kate_placeholder at center

    "{i}You catch up to Kate outside of the class{/i}"
    "Hey Kate, I passed! Did you?"
    k "I did, you know what that means?"
    "Yes I definitely do"
    k "Then I'll see you later on the field W.C"
    return
