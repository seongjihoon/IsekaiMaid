label start:
    # jump Select_Dinner_Elice
    '어디서 부터 시작할 것인지 선택해주세요.'
    jump std
    menu:
        '0일차':
            pass
        '1일차':
            jump WakeUp_Event
            pass
        '2일차':
            jump D_2_Selected
            pass
        '3일차':
            jump D_3_Morning
            pass
        '엘리스 호러':
            jump End_Elice
            pass


    scene bg black with Dissolve(2.0)
    stop music fadeout 2.0
    $renpy.pause(5.0, hard = True)

    # play music footrain
    # play sound rain_car
    '당신' '"수능 끝난 게 두 달 전인데 아직도 학교에 가다니..."'
    '한숨 같은 말이 튀어나왔다.'
    '수능을 본 것도 벌써 작년 일이다.'
    '수업은 하지 않은 지 오래. 선생님들은 영화를 틀어주고 할 일 하라고 하신다.'
    '고전 영화는 재미없고, 게임은 질리고, 잠은 너무 많이 잤다.'
    '다들 체험학습을 내고 학교를 나오지 않는다.'
    '당신' '“체험학습 좀 아껴서 쓸걸.”'
    '후회는 아무리 빨라도 늦다고 하지.'
    '그나마 옆 반 친구랑 노닥거리던 것이 낙이었는데, 그 친구도 이제 학교에 나오지 않는다고 한다.'
    '아이돌 연습생이었던 그 애는 데뷔 조로 뽑혔다고 한다.'
    '축하해주지 못할망정, 학교에서 보지 못한다고 서운해하는 건 말도 안 되는 일이다.'
    '부모님은 학교에 너무 가기 싫으면 빠져도 된다고 하셨지만, 무단결석은 왠지 양심이 찔리고.'
    '당신' '"빨리 졸업이나 했으면 좋겠다."'
    '올려다본 하늘은 비가 와서 어둑했다.'
    '도로가 미끄러우니, 운전자들은 조심하라는 일기예보가 생각났다.'
    '파란불이 노란불로 바뀌었다.'

    stop music
    '오늘은 학교에서 무엇을 할까, 그런 고민을 하면서 신호등을 바라봤다.'
    '당신' '"응...?"'
    '초록불이 노란불로 바뀌었다.'
    # play car_fast

    '차들이 급하게 넘어가기 위해 속력을 높이는 상황 속에 트럭 하나가 눈에 띄었다.'
    scene bg Reality_Truck
    # 트럭 경적 소리
    '평소에는 보기 힘든 5톤 트럭이 다른 차보다 빠른 속도로 달려왔다.''인도를 들이박는 트럭을 보며, 트럭 기사를 바라보았다.'
    '인도를 들이박는 트럭을 보며, 트럭 기사를 바라보았다.'
    '놀란 눈으로 핸들을 붙잡은 트럭 기사를 보니, 트럭이 고장 났구나... 라는 생각이 들었다.'
    '얼어붙은 다리와 달리 팽팽 움직이는 머리의 대조가 꽤 웃겼다.'
    '멍청한 다리는 움직일 생각을 하지 않고, 달려오는 트럭만 바라볼 뿐이다.'
    # 철벅거리며 달리는 소리
    voice Yunsarang_001
    unknown_yun '"안돼!!!"'
    '누군가가 나를 부르며 달리는 목소리가 들렸지만, 누구의 목소리인지 떠오르지 않았다.'
    scene bg black with Dissolve(2.0)
    # 차에 치이는 소리
    '이렇게 죽는 걸까...'
    scene bg black with Dissolve(.5)
    $renpy.pause(.5, hard = True)
    # GOGO 영상 삽입
    # play sound "audio/BGM/chapter.wav"
    play sound teleport_world
    show bg_Isekai_ogg with Dissolve(2.0)
    $ renpy.pause(4.0, hard = True )
    stop sound
    hide bg_Isekai_ogg with None
    scene bg black with Dissolve(2.0, hard = True)

    # play sound 빠져나가는 소리
    play sound teleport_out
    scene bg white with Dissolve(.3)
    scene bg black with Dissolve(1.0)
    $renpy.pause(2.0)

    # scene bg black with Dissolve(2.0)
    # # call Prolog
    # stop music fadeout 2.0
    # $renpy.pause(3.0, hard = True)
    #
    # scene bg black with Dissolve(2.0)
    # # play music foot_rain
    # # play sound rain_car
    #
    # "수능도 끝나고, 20살도 되었지만, 고등학교 졸업식이 남았다는 이유로 학교를 왔었다."
    # "대충 시간을 때우다 집에 가는 길, 비가 내려서인지 차들이 평소보다 영 불안했다."
    #
    # # 음악이 없?네
    # stop music
    # "신호등을 조심해야지, 생각하던 그 때였다."
    # UnknownPlayer '"응...?"'
    # "초록불이 노란불로 바뀌었다."
    # # play sound 트럭이 달리는 소리
    # play sound car_fast
    # "차들이 급하게 넘어가기 위해 속력을 높이는 상황 속에 트럭 하나가 눈에 띄였다."
    # play sound rain_car_stop
    # # 트럭 경적 소리
    # scene bg BG_Reality_Truck with None
    # "평소에는 보기 힘든 5톤 트럭이 다른 차보다 빠른 속도로 달려왔다."
    # "멍청한 다리는 움직일 생각을 하지 않고, 달려오는 트럭만 바라볼 뿐이다."
    # # play sound 철벅거리며 달리는 소리
    # play sound rain_run
    # unknown '"야!"'
    # "누군가가 나를 부르며 달려오는 소리가 들렸지만, 누구의 목소리인지 떠오르지 않았다."
    # # play sound 차에 치이는 소리
    #
    # play sound Car_attack
    # show BG_light_Red with Dissolve(.2)
    # with vpunch
    # scene bg black with None
    # "난 그렇게 의식을 잃었다."
    # scene bg black with Dissolve(1.0)
    # $renpy.pause(3.0, hard = True)
    # # play sound 이세계로 빨려들어가는소리
    # play sound teleport_word
    #
    # # GOGO 영상 삽입
    # # play sound "audio/BGM/chapter.wav"
    # play sound teleport_world
    # show bg_Isekai_ogg with Dissolve(2.0)
    # $ renpy.pause(4.0, hard = True )
    # stop sound
    # hide bg_Isekai_ogg with None
    # scene bg black with Dissolve(2.0, hard = True)
    #
    # # play sound 빠져나가는 소리
    # play sound teleport_out
    # scene bg white with Dissolve(.3)
    # scene bg black with Dissolve(1.0)
    # $renpy.pause(2.0)

    jump SelectedName

label SelectedName:

    call screen nameInput   #당신의 이름을 입력 해 주세요.

    $ player_name = _return # 이름 입력 완료
    if player_name == "":
        $ player_name = default_name # default name
    call screen Succese
    $ nameCheck = _return
    if nameCheck == False:
        jump SelectedName

    "확인 했습니다. 저택에 오신 것을 환영합니다. [player_name]"
    window hide
    hide screen quick_menu
    # $ persistent.m_bgetBear = True
    # $ persistent.m_bgetSarangRing = True

    # $ persistent.m_bgetFlower = True
    # $ persistent.m_bgetRibbon = True
    # $ persistent.m_bgetAlcohol = True
    # $ persistent.m_bgetWine = True
    # $ persistent.m_bgetPaper = True
    # $ persistent.m_bgetBear = True
    # $ persistent.m_bgetSarangRing = True
    # $ persistent.m_bgetpendant = True
    # $ persistent.m_bgetIsabelRing = True
    # $ persistent.m_bgethairpin = True
    # $ persistent.m_bgetpen = True
    # $ persistent.m_bgetDreamcatcher = True
    # $ persistent.m_bgetFlowerpot = True

    jump intro
    pass

label testScene:


    voice Glass
    scarlet '안녕'

    voice Glass
    yun ' 안녕'
