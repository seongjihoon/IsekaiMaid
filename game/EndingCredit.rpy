
# label tes:
label endcredits:
    # "크레딧 시작"
    $ credits_speed = 25 #scrolling speed in seconds
    scene bg BG_Corridor_credit
    show cred at Move((0.5, 4.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Dissolve(2.0)
    # with Pause(credits_speed)
    $renpy.pause(credits_speed, hard = True)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return
