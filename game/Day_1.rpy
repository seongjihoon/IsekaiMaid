 # 0. 기상
label WakeUp_Event:
    scene bg black
    play sound DoorKnock
    $ renpy.pause(1.5, hard = True)
    voice Yunsarang_013
    yun '"주인님..."'

    voice Yunsarang_014
    yun '"아직 주무시고 계시나요?"'

    voice Yunsarang_015
    yun '"... 어쩌지."'

    $ renpy.pause(2, hard = True)
    play sound DoorOpen2
    scene bg Myroom with Dissolve(1.5, alpha = True)

    show Yun_lookout at yun_standsize_ms with Dissolve(1, alpha = True)
    voice Yunsarang_016
    yun '"으음..."'

    hide Yun_lookout with None
    show Yun_stare at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_017
    yun '"주인님을 이대로 깨우기에는 너무 귀여운데..."'

    hide Yun_stare with None
    show Yun_wink at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_018
    yun '"조금은 늦게 내려가도 괜찮겠지?"'

    scene bg black with Dissolve(.5 ,alpha = True)
    $ renpy.pause(2, hard = True)
    voice Yunsarang_019
    yun '"..."'

    '열린 창문 틈으로 들어온 빛이 단잠을 방해했다.'
    '알림이 울리지 않았으니, 아직은 더 자도 괜찮을 텐데.'
    '빛을 피하고자 몸을 뒤척이니 낯선 무게감이 느껴졌다.'
    '침대 위에 무거운 걸 올리고 잤었나?'
    '눈을 뜬 시야에 보인 것은...'

    # 윤사랑 테마곡
    play music Yunsarang_1 fadein 4.0
    show Sarang_CG_1_1 with Dissolve(4, alpha = True)         # 수정사항 4
    $ renpy.pause(1.0, hard = True)
    # hide Sarang_CG_1 with None
    voice Yunsarang_020
    yun '"...아."'

    voice Yunsarang_021
    yun '"일어나셨군요. 주인님!"'

    show Sarang_CG_1_2 with Dissolve(.5, alpha = True)
    hide Sarang_CG_1_1 with None
    '나와 눈이 마주친 윤사랑은 해맑게 웃으며 내게 인사했다.'
    '거리가 너무 가깝지 않아?'
    '그것보다 어제 분명 문을 잠그고 잤는데 어떻게 들어온 거지?'

    show Sarang_CG_1_1 with Dissolve(.5 ,alpha = True)
    hide Sarang_CG_1_2 with None
    # play music "audio/BGM/normal_b.mp3" fadein 1.0
    voice Yunsarang_022
    yun '"나쁜 꿈이라도 꾸신 건가요?"'

    player '"그건 아니야. 어떻게 네가 내 방에 들어왔는지 추측하고 있었어."'
    player '"혹시 창문을 넘어서 들어왔니?"'
    show Sarang_CG_1_2 with Dissolve(.5 , alpha = True)
    hide Sarang_CG_1_1 with None
    '내 말이 뭐가 웃기는지 윤사랑은 웃음을 터트렸다.'
    voice Yunsarang_023
    yun '"주인님도 참, 무슨 말씀을 하시는 거예요."'
    voice Yunsarang_024
    yun '"당연히 문을 열고 들어왔죠."'

    player '"난 분명 어젯밤에 문을 잠그고 잤거든?"'
    show Sarang_CG_1_1 with Dissolve(.5 , alpha = True)
    hide Sarang_CG_1_2 with None
    '그제서야 윤사랑은 이해가 간다는 표정을 지었다.'

    voice Yunsarang_025
    yun '"관리자님이 주인님을 모셔오라고 하면서 방 문 열쇠를 주셨어요."'
    player '"그래?"'
    voice Yunsarang_026
    yun '"네. 문 앞에서 주인님을 깨우려고 했지만 주인님이 안 일어나셔서..."'
    '문을 열고 들어온 부분에 대해서는 어느 정도 해명이 되었지만...'
    '침대에 엎드려서 내 자는 얼굴을 본 이유는 모르겠다.'
    '물어보고 싶은 마음이 굴뚝같았지만, 저 순수한 얼굴을 보니 도저히 물을 수 없었다.'
    player '"일어나게 좀 비켜줄래?"'
    voice Yunsarang_027
    yun '"앗, 네!"'

    play sound standup
    scene bg black with Dissolve(.5 ,alpha = True)
    $ renpy.pause (1, hard = True)
    scene bg Myroom with Dissolve(1 , alpha = True)
    show Yun_Normal at yun_standsize_bs  with Dissolve( 1, alpha = True)
    player '"그러고 보니 관리자가 날 찾는다고 하지 않았어?"'

    hide Yun_Normal with None
    show Yun_Happy at yun_standsize_ms with Dissolve(.5 ,alpha= True)
    voice Yunsarang_028
    yun '"네! 다 같이 밥을 먹어야 하니 주인님을 모셔오라고 했어요!"'

    stop music fadeout 2.0
    player '"그... 다른 애들도 다 나를 기다리고 있는 거야?"'
    '왠지 감이 좋지 않았다.'

    hide Yun_Happy with None
    show Yun_Laughter at yun_standsize_ms  with Dissolve(.5 ,alpha = True)
    voice Yunsarang_029
    yun '"네, 다들 식당에서 주인님을 기다리고 있어요!"'

    play sound ThudReverb
    voice Scarlet_25
    scarlet '"이봐!!! 이 몸을 언제까지 기다리게 할 거냐!"' with hpunch
    '저택 전체에 스칼렛의 사자후가 울려 퍼졌다.'

    hide Yun_Laughter with None
    show Yun_panic at yun_standsize_ms with Dissolve(.5 ,alpha  =True)
    player '"이크..."'
    '잔뜩 화가 난 스칼렛의 표정이 머릿속에 그려졌다.'
    '가뜩이나 나를 마음에 들어 하지 않는데, 더 싫어할 이유를 제공하는 꼴이네.'
    hide Yun_panic with None
    show Yun_anxiety at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    '걱정하는 나를 보며 윤사랑은 안절부절못했다.'
    hide Yun_anxiety with None
    show Yun_tear at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_030
    yun '"죄송해요, 저 때문에..."'
    player '"괜찮아. 애들이 더 화내기 전에 내려가자."'

    hide Yun_tear with None
    show Yun_Sad at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_031
    yun '"네...!"'

    play sound FootStep1
    scene bg black with Dissolve(.5 ,alpha = True)
    stop music fadeout 2
    jump Morning

# 아침
label Morning:
    play music comic_sound fadein 2.0
    scene bg BG_Livingroom with Dissolve(1 ,alpha= True)
    play sound Thud1

    show Scarlet_ppagchim at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_26
    scarlet '"야! 왜 이렇게 늦어!"' with hpunch

    show Elice_Angry at elice_standsize_ms_L with Dissolve(.5,alpha= True)
    voice Elice_15
    elice '"그런 간단한 일 하나 제대로 못하다니..."'

    show Isabel_heung at isabel_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Isabel_020
    isabel '"아침 식사를 제사상으로 받을 뻔했네요."'
    '나랑 윤사랑이 식당에 들어오자마자 불만이 터져 나왔다.'
    player '"미안, 그래도 기다려줘서 고마워."'

    hide Scarlet_ppagchim with None
    show Scarlet_jjajeung at scarlet_standsize_ms with Dissolve(.5,alpha = True)
    voice Scarlet_27
    scarlet'"자발적으로 네놈을 기다렸겠냐?"'

    hide Isabel_heung with None
    show Isabel_pout at isabel_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Isabel_021
    isabel '"관리자님께서 당신이 오기 전까지는 먹지 말라고 한 탓에..."'

    hide Scarlet_jjajeung with None
    show Scarlet_displease at scarlet_standsize_ms with Dissolve(.5, alpha = True)
    voice Scarlet_28
    scarlet '"덕분에 음식 구경만 실컷 했다?"'
    player '"다음부터는 주의할게..."'

    hide Scarlet_displease with None
    show Scarlet_heung at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_29
    scarlet '"크릉... 이번만 특별히 넘어가 주지."'

    hide Scarlet_heung
    hide Isabel_pout
    hide Elice_Angry
    with Dissolve(.5 ,alpha = True)

    show Elice_Committed at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_16
    elice '"명심해 두번째 기회는 없다는 걸."'
    show Elice_Committed at elice_bs_to_bs_L with None
    $renpy.pause(1.0)

    show Isabel_heung at isabel_standsize_bs_R with Dissolve(.5 ,alpha= True)
    voice Isabel_022
    isabel '"다음부터는 조심해 주셨으면 좋겠네요, 어제도 말씀드렸지만 저는 환자라서 말이죠.... 약 먹는 시간을 지켜야 해요."'
    player '"아, 그건 미안... 다음부터는 절대 늦지 않을 테니까!"'

    hide Elice_Committed
    hide Isabel_heung
    with None

    play sound Thud1
    with vpunch
    show Hyeyeon_Angry at admin_standsize_bs with Dissolve(.5 ,alpha = True)
    admin '"싸움은 이제 그만!"'
    admin '"밥이나 먹어!"'

    hide Hyeyeon_Angry with None

    show Food_Defualt at Scene_bs_to_top with Dissolve(.5)
    $renpy.pause(3.0 ,hard = True)
    hide Food_Defualt with Dissolve(1.0)
    show screen Mini_Scene(Food_Defualt_mini, _x = .5, _y = 0.06) with Dissolve(.5)
    player '"...우와, 이게 뭐야?"'
    '휘둥그레진 눈으로 관리자가 차린 아침 식사를 바라봤다.'
    '오븐에서 꺼낸 지 얼마 안 된 듯, 노릇노릇하게 잘 구워진 크루아상.'
    '버터를 발라서 구운 식빵, 그 위에 올려진 노른자가 살아있는 반숙 계란후라이.'
    '금방이라도 육즙이 터져 나올 것 같은 소세지'
    '또 언제 준비한 건지, 우리의 얼굴이 그려진 커피 컵도 있었고'
    '싱싱함이 살아있는 카프레제 샐러드에는 연어와 새우까지 올려져 있었다.'

    hide screen Mini_Scene with Dissolve(.5)
    player '"누가 만든 거야?"'

    show Hyeyeon_Happy at admin_standsize_bs with Dissolve(.5)

    admin '"전부 이 몸이 만들었지!"'
    '나는 깜짝 놀라서 관리자를 바라보았다.'
    '어깨를 으쓱이며 잔뜩 뽐을 내는 관리자가 다르게 보였다.'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(.5)

    admin '"주인님이 왔으니까, 이제 다들 식사합시다~!"'
    play sound Table
    hide Hyeyeon_Laughter with None
    '관리자의 말이 끝나기가 무섭게 스칼렛이 식사를 시작했다.'
    '식사하는 와중 오가는 대화는 없었다.'
    '침묵에 숨이 막힐 것 같다는 생각이 들 즈음, 윤사랑이 내게 말을 걸어왔다.'

    show Yun_Sad at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_032
    yun '"죄송해요. 주인님, 괜히 저 때문에..."'
    player '"아냐, 굳이 원인을 따지자면 늦게 말해준 관리자 탓이지만..."'

    hide Yun_Sad with None
    show Yun_tear at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_033
    yun '"하지만..."'

    show Hyeyeon_Normal at admin_ms_Rout_to_R with None
    # $ renpy.pause(3.0, hard =True)
    admin '"거기, 다 들리거든?!"'
    player '"네에~"'
    show Hyeyeon_Normal at admin_ms_R_to_Rout with None
    $ renpy.pause(1.5, hard = True)
    hide Hyeyeon_Normal
    hide Yun_tear
    with dissolve

    '윤사랑은 여전히 할 말이 남은 표정으로 나를 바라봤지만, 관리자의 주의 때문인지 말없이 식사를 이어갔다.'
    '숨 막힐 듯 조용한 분위기 속에서 진행된 식사지만, 음식 맛은 하나같이 뛰어났기에 체하지 않고 다 먹었다.'
    '음식 맛이 이만큼 뛰어나지 않았다면, 분명 체했을 거야...'
    show screen Mini_Scene(Food_Clean_mini, _x =.5, _y = .06) with Dissolve(2.0)
    '다들 음식이 입에 맞는지, 얼굴에는 흉악한 인상 대신 만족스러운 미소만 남아있다.'
    hide screen Mini_Scene with Dissolve(2.0)

    show Hyeyeon_Happy at admin_standsize_ms with Dissolve(.5 ,alpha= True)
    admin '"다들 맛있게 먹었어? 그 많던 음식이 다 사라졌네~"'

    # 뜨끔 효과음
    show Scarlet_panic at scarlet_standsize_ms_L with Dissolve(.5 ,alpha = True)
    show Scarlet_panic at scarlet_one_jump_Lms with None
    play sound Jump1
    voice Scarlet_30
    scarlet '"크흠..."'

    '유독 스칼렛의 앞에만 그릇이 잔뜩 쌓여있었다.'
    hide Hyeyeon_Happy
    hide Scarlet_panic
    with Dissolve( .5 ,alpha = True)
    show Hyeyeon_Happy at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    admin '"내가 준비한 음식 맛이 어때? 굉장히 맛있지?"'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(.5 ,alpha = True)
    admin '"당연하지! 이날을 위해서 이 몸께서 연습한 음식이니까~"'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve (.5 ,alpha = True)
    admin '"감상평을 남기는 착한 아이에겐 디저트를 하사하도록 하지!"'

    hide Hyeyeon_Normal with None
    show Yun_huc at yun_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Yunsarang_034
    yun '"지금까지 먹어본 아침 중에서 최고였어요~!"'

    show Elice_Pudency at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_17
    elice '"못 먹을 수준은 아니더군."'

    show Scarlet_lookout at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_31
    scarlet '"그..."'

    hide Yun_huc
    hide Elice_Pudency
    hide Scarlet_lookout
    with None

    show Hyeyeon_Happy at admin_standsize_bs with Dissolve(.5)
    admin '"그?"'

    show Hyeyeon_Happy at admin_bs_to_bs_R with None
    $renpy.pause(.2)
    show Scarlet_lookout at scarlet_standsize_bs_L with Dissolve(.5 ,alpha = True)
    voice Scarlet_32
    scarlet '"어떤 맛이었냐면..."'

    hide Scarlet_lookout with None
    show Scarlet_pout at scarlet_standsize_bs_L with Dissolve(.5 ,alpha = True)
    voice Scarlet_33
    scarlet '"..."'
    #
    # hide Hyeyeon_Happy
    # hide Scarlet_pout
    # with None
    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_bs_R with Dissolve(.5 ,alpha = True)
    admin '"스칼렛은 디저트가 별로 먹고 싶지 않나 봐?"'
    # 뜨끔 효과음

    hide Scarlet_pout with None
    show Scarlet_panic at scarlet_standsize_bs_L with Dissolve(.5 ,alpha = True)
    show Scarlet_panic at scarlet_one_jump_Lbs with None
    voice Scarlet_34
    scarlet '"그게 아니라...! 이렇게 맛있는 건 처음이라서..."'
    '스칼렛의 얼굴이 점점 붉게 달아올랐다.'
    '왜 부끄러워하지? 잘 이해가 가지 않았다.'

    hide Hyeyeon_Laughter
    hide Scarlet_panic
    with Dissolve(.5 ,alpha = True)
    # 점점점 사운드?
    show Elice_Coloration at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    '잠시 고민하다가 엘리스랑 눈이 마주쳤다. 아하...'

    hide Elice_Coloration with dissolve
    show Isabel_nodap at isabel_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Isabel_023
    isabel '"저도 말해야 하는 건가요?"'
    show Hyeyeon_Laughter at admin_standsize_ms_R with Dissolve(.5 ,alpha = True)
    admin '"당연하지!"'
    voice Isabel_024
    isabel '"먹기 편해서 좋았어요."'

    hide Isabel_nodap with None
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Happy at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    admin '"자, 그럼 주인님 차례!"'
    player '"에, 나도 말해야 해?"'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Angry at admin_standsize_bs with Dissolve(.5 ,alpha = True)
    admin '"당연한 거 묻지 마!"'
    player '"덕분에 맛있게 잘 먹었어. 고마워."'

    hide Hyeyeon_Angry with None
    show Hyeyeon_Happy at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    admin '"흐흐, 디저트는 저쪽에 준비해두었으니 가져가서 먹어!"'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Normal at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    admin '"지금부터는 자유시간이야. 저택을 돌아보던, 친목을 다지던 너희 하고 싶은 대로 해!"'
    admin '"왜냐면..."'
    player '"왜냐면?"'

    hide Hyeyeon_Normal with None
    show Hyeyeon_Happy at admin_standsize_bs with Dissolve(.5 ,alpha = True)
    admin '"난 지금부터 낮잠 잘 거거든!"'

    play sound Thud2
    player '"뭐?"'with vpunch

    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_bs  with Dissolve(.5 ,alpha = True)
    admin '"일어난 후에 할 일을 줄 테니까 자유를 즐기고 있으라고~"'

    hide Hyeyeon_Laughter with None
    play sound teleport_snap
    '관리자는 순식간에 우리 눈앞에서 사라졌고, 윤사랑을 제외한 다른 사람은 자리를 떠났다.'

    play sound footstep_group
    '쟤네는 저게 익숙한가...?'
    player '"다들 가버렸네, 넌 뭐 할 생각이야?"'

    show Yun_huc at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_035
    yun '"저는 정원 산책을 하고 싶은데..."'
    '윤사랑은 나를 한 번, 정원을 한 번 바라봤다.'
    hide Yun_huc with None
    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_036
    yun '"괜찮다면 같이 가실래요? 관리가 잘 되었는지 구경할 게 많더라고요!"'

    hide Yun_fallinlove with None
    show Yun_panic at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_037
    yun '"그... 먼저 정원에 가 있을 테니까! 같이 산책하실 거라면 정원으로 와주세요!"'

    play sound run
    # hide Yun_panic with None
    show Yun_panic at yun_ms_to_Lout with None# ms에서 오른쪽 화면 밖으로 다급히 이동
    $ renpy.pause (1.5, hard = True)
    hide Yun_panic with None

    '윤사랑은 대답도 듣지 않고 정원으로 뛰쳐나갔다.'
    '굉장히 빠른 속도로 달리는 걸 보니, 쟤는 육상 선수였을지도 몰라...'
    player '"아무튼.. 뭘 하는게 좋을까..."'
    '나에게 정해진 임무를 수행하기 위해서는 일단 메이드들과 친해지는게 좋겠지?'
    '다들 혼자서 시간을 보내는 것 같으니, 여러 명하고 대화하는 건 힘들지도 모르겠네.'
    player '"음..."'

    menu:
        "연회장":
            jump D_1_Hall
        "정원":
            jump D_1_Garden
        "서재":
            jump D_1_Library
        "지하실":
            jump D_1_Underoom


label D_1_Hall:
    '여기서 가장 가까운 곳이 어디더라...'
    player '"분명... 연회장이었지."'
    '어제 메이드들과 다 같이 인사를 나눴던 곳이기도 하다.'
    '누가 있을지 대충 짐작은 가는데...'
    scene bg black with Fade(1.0 ,0.0, 1.0)
    stop music fadeout 2.0
    $ renpy.pause(1.0)
    play music Elicetheme
    scene bg BG_Hall with Dissolve(1.0, alpha = True)
    show Elice_Ignore_2 at elice_standsize_ms with Dissolve(.5 ,alpha = True)
    $ renpy.pause(1.0)
    hide Elice_Ignore_2
    show Elice_Gladness at elice_standsize_ms
    with Dissolve(.5 ,alpha = True)
    $ renpy.pause(1.0)
    hide Elice_Gladness
    show Elice_Difficulty at elice_standsize_ms
    with Dissolve(.5, alpha = True)

    $renpy.pause(2.0)

    player '"역시나..."'
    '연회장 문을 열고 들어가다 엘리스와 눈이 마주쳤다.'
    '엘리스는 붉은 와인이 담긴 잔을 들고 있었다.'
    '낮부터 술이라니... 자라나는 청소년이 보기에는 좋지 않은 광경이다.'
    '작게 한숨을 내쉬고 주변을 둘러보려 했다.'
    hide Elice_Difficulty with None
    show Elice_coldsmiley at elice_standsize_ms with Dissolve(.5 ,alpha = True)
    '엘리스가 내게 손짓하기 전까지는.'
    '가까이 오라는 건가?'
    menu:
        '다가간다.':                    # 호감도 상승
            '부른다고 가는 개는 아니지만...'
            '거부했을 때의 엘리스 반응이 좀 무서울 것 같았다.'
            '엘리스는 왠지... 따를 수밖에 없는 분위기가 있으니까.'
            play sound FootStep1
            '나는 순순히 엘리스 곁으로 다가갔다.'
            '엘리스는 나름 만족한 듯한 미소를 지었다.'

            hide Elice_coldsmiley with None
            show Elice_Gladness at elice_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Elice_18
            elice '"멍청한 녀석인 줄 알았는데, 나름 쓸만하네."'
            player '"나를 어떻게 평가하고 있는 거야...?"'

            hide Elice_Gladness with None
            show Elice_coldsmiley_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Elice_19
            elice '"궁금해?"'
            player '"...아니. 됐어."'

            hide Elice_coldsmiley_2 with None
            show Elice_Strong at elice_standsize_bs with Dissolve(.5 , alpha = True)
            voice Elice_20
            elice '"싱겁기는."'
            '엘리스의 얼굴에 미소가 사라졌다.'
            $ elice_f += 0.5
            pass

        '다가가지 않는다.':
            '부른다고 가다니.. 내가 개도 아니고.'
            '나는 자리에 가만히 있었다.'

            hide Elice_coldsmiley with None
            show Elice_Committed_2 at elice_standsize_bs  with Dissolve(.5 ,alpha = True)
            voice Elice_21
            elice '"내가 오라고 했을 텐데?"'
            player '"어... 응."'
            '나는 개다.'
            '비굴하다고 할지언정, 어쩔 수 없었다.'
            play sound FootStep1
            '엘리스의 저런 얼굴을 직접 본 사람이라면, 누구라도 발을 움직였을 거라고!'
            hide Elice_Committed_2 with None
            show Elice_Contempt at elice_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Elice_22
            elice '"멍청한 녀석..."'
            '엘리스는 중얼거리는 것치고는 큰 목소리로 말했다.'
            player '"다 들리는데..."'

            hide Elice_Contempt with None
            show Elice_Strong at elice_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Elice_23
            elice '"어쩌라고?"'
            '엘리스는 차게 식은 눈으로 나를 바라봤다.'
            pass
        # "몰?루" if Select == 1:
        #     '나는 바보다'
    hide Elice_Strong with None
    show Elice_Committed_2 at elice_standsize_bs with Dissolve(.5 ,alpha= True)
    voice Elice_24
    elice '"너, 이름은?"'
    player '"...어제 자기소개 때 말했는데?"'
    '잊어버렸냐는 질문은 입안으로 꾹 들어갔다.'
    '달리 원하는게 있어서 물어보는 건가.'
    player '"내 이름은... [player_name]."'

    hide Elice_Committed_2 with None
    show Elice_Surprised_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_25
    elice '"그래, 그런 이름이었지."'

    hide Elice_Surprised_2 with None
    show Elice_Surprised at elice_standsize_bs with Dissolve(.5, alpha = True)
    voice Elice_26
    elice '"나이는?"'
    player '"19살."'
    '갑자기 신상 조사 시작인가...?'

    hide Elice_Surprised with None
    show Elice_Coloration at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_27      # 뭐야 성인이였어? 가 여기로 들어가는 것 같음.
    elice '"너 성인이였어?"'
    player '"나를 몇 살 정도로 생각한 거야..."'

    hide Elice_Coloration with None
    show Elice_coldsmiley_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_28
    elice '"글쎄, 네가 말한 것보다 둘, 셋 정도 적게?"'
    player '"그렇게 동안이라고 생각한 적 없는데."'
    '어리다는 말은 너무 아이 같다는 느낌이라서 별로다.'

    hide Elice_coldsmiley_2 with None
    show Elice_Gladness at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_29
    elice '"관리자가 너에게 술을 주면 안 된다고 하도 난리를 피워서, 젖먹이인 줄 알았지."'
    player '"아, 응..."'
    '엘리스는 와인잔을 돌리며 말을 이었다.'

    hide Elice_Gladness with None
    show Elice_Coloration_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_30
    elice '"관리자와는 무슨 사이지?"'
    player '"아무 사이도 아니야. 어제 처음 봤다고?"'

    hide Elice_Coloration_2 with None
    show Elice_Coloration at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    '내 말을 어떤 식으로 해석한 건지, 엘리스는 눈을 가늘게 뜨고 날 샅샅이 수색했다.'
    '다른 수상한 의도를 찾아내겠다는 듯.'
    player '"진짜로, 갑자기 눈을 떠보니 저택의 정원에 있었다니까?"'
    hide Elice_Coloration with None
    show Elice_Difficulty at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_31
    elice '"...그래, 믿어주지."'

    '엘리스는 전혀 믿지 않는다는 눈으로 대답했다.'
    player '"정말 어제 처음 봤어. 관리자가 내 나이를 아는 것도 지금 너한테 들어서 알았고."'

    hide Elice_Difficulty with None
    show Elice_Surprised_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_32
    elice '"흐음... 멍청한 네 얼굴을 보니, 거짓말은 아닌 것 같네."'

    player '"멍청하다니..."'
    '와인을 마시는 엘리스는 굳이 내 말에 대답해 주지 않았다.'
    player '"그런데 오전부터 그렇게 와인을 마셔도 괜찮은 거야?"'
    player '"와인은 도수가 꽤 높은 거로 아는데..."'
    # show Sarang_CG_1 with Dissolve(1.0, alpha = True)

    hide Elice_Surprised_2 with None
    show Elice_CG_1 with Dissolve(1.0, alpha = True)
    voice Elice_33
    elice '"고작 이 정도 술에 내가 취할 거라 생각하는 거야?"'
    voice Elice_34
    elice '"네게 걱정 받을 수준은 아닌데..."'
    '오전의 햇빛이 들어오는 연회장에 서 있는 엘리스에게서 시선을 뗄 수 없었다.'
    '누가 시키지 않아도 엘리스의 앞에 무릎을 꿇고 싶을 정도였다.'
    voice Elice_35
    elice '"생각한 것보다 더 평범하네, 넌."'
    '딱히 답할 말을 찾지 못해서 어깨를 으쓱이는 것으로 답을 대신했다.'

    hide Elice_CG_1 with None
    show Elice_Difficulty at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_36
    elice '"관리자에 대한 정보를 캐내려고 했는데, 아는 것도 없고..."'

    hide Elice_Difficulty with None
    show Elice_Difficulty_2 at elice_standsize_bs with Dissolve(.5, alpha = True)
    voice Elice_37
    elice '"흐음..."'

    '엘리스는 잠시 주변을 둘러봤다.'
    hide Elice_Difficulty_2 with None
    show Elice_Surprised at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_38
    elice '"달리 시종도 없는데, 이렇게 깨끗하다니... 신기하지 않아?"'
    player '"어, 그러게?"'

    hide Elice_Surprised with None
    show Elice_Surprised_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_39
    elice '"고작 4명의 메이드가 청소하기에는 굉장히 넓어."'
    voice Elice_40
    elice '"이 바닥만 해도..."'

    play sound footstep_Elice # 톡톡 사운드
    '엘리스는 구두 앞 굽으로 바닥을 톡톡 쳤다.'
    player '"얼굴이 비칠 정도로 광이 나네."'
    hide Elice_Surprised_2 with None
    show Elice_Difficulty_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_41
    elice '"그래, 이에 대해서 무슨 생각이 안 들어?"'
    player '"음... 더럽게 쓰지 않도록 조심해야겠네?"'

    hide Elice_Difficulty_2 with None
    show Elice_Coloration at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    '엘리스에게는 눈으로 말하는 능력이라도 있는 것 같았다.'
    '너, 그 정도 밖에 생각 못 하는구나...'
    '나한테 뭘 바라는지 정확하게 말해줬으면 좋겠는데.'
    hide Elice_Coloration with None
    show Elice_Difficulty at elice_standsize_bs with Dissolve(.5 ,alpha  = True)
    voice Elice_42
    elice '"네가 어떤 녀석인지 대충 파악했어."'
    player '"그으래... 내가 도움이 되었다니 다행이네."'

    hide Elice_Difficulty with None
    show Elice_Gladness at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_43
    elice '"아, 나는 다른 할 일이 있으니 이것 좀 치워."'
    '엘리스는 다 마신 와인잔을 내게 건네주었다.'

    show img_gradation
    show itemBack
    show get_Item_gif
    play sound Bell
    $ renpy.pause(0.325)
    show Wine:
        xalign 0.505, yalign 0.46
        rotate 00
    show screen item_TextScren
    $ renpy.pause(2.0, hard = True)
    show screen Click_Text
    pause
    hide screen item_TextScren
    hide screen Click_Text
    hide get_Item_gif
    hide itemBack
    hide Wine
    hide img_gradation
    with Dissolve(0.38, alpha = True)
    $ persistent.m_bgetWine = True # 와인잔 추가

    '나를 아랫사람 부리듯 하는군...'
    hide Elice_Gladness with None
    '엘리스는 오늘 내가 봤던 표정 중 가장 밝은 미소를 짓고서는 자리를 떠났다.'
    '엘리스에 대해서 알아내려고 했는데, 나만 잔뜩 파악된 기분이다.'
    scene bg black with Dissolve(.5 ,alpha =True)
    stop music fadeout 2.0
    $renpy.pause(1.0, hard = True)
    jump D_1_Lunch

    # 점심으로 점프

    return

label D_1_Garden:
    '자꾸만 창문 너머의 시선이 신경 쓰였다'
    '분홍색이 왔다 갔다 하는 걸 보면, 윤사랑의 시선이겠지?'
    player '"그렇게 궁금하면 나가기 전에 물어보지."'
    '내가 어디로 갈지 궁금해서 기웃거리는 모습이 귀엽다면 귀엽게 볼 수 있었다.'
    '눈앞에서 알짱거리는 분홍 머리를 무시하지 못해, 난 정원으로 향했다.'
    scene bg black with Fade(1.0, 0.0, 1.0)
    stop music fadeout 2.0
    $ renpy.pause(1.0)
    play music Yunsarang_2 fadein 2.0
    scene bg BG_Garden_Morning with Dissolve(.5 ,alpha = True)
    show Yun_fallinlove at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_038
    yun '"와주셨군요, 주인님!"'
    player '"응. 내가 정원을 본 건 밤이라서 낮에는 어떨지 궁금했거든."'
    '너를 그냥 무시하기도 어려웠고...'

    hide Yun_fallinlove with None
    show Yun_Happy at yun_standsize_ms with Dissolve(.5,alpha = True)
    voice Yunsarang_039
    yun '"주인님이랑 같이 정원을 둘러볼 수 있어서 기뻐요."'

    hide Yun_Happy with None
    show Yun_huc at yun_standsize_ms with Dissolve(.5 ,alpha =True)
    voice Yunsarang_040
    yun '"주인님이 처음 눈을 뜬 곳도 이 정원이라고 했죠?'
    player '"어, 응... 이쯤이었을걸?"'
    '사람 한 명이 누워있을 법한 자리를 가리키며 말했다.'
    '딱히 내 소지품이 떨어져 있거나 하지는 않지만... 여기만 풀이 눌려있는걸?'

    hide Yun_huc with None
    show Yun_panic at yun_ms_to_down with None
    $renpy.pause(.6, hard = True)
    play sound Thud1
    voice Yunsarang_041
    yun '"우, 우왓!"'with vpunch
    '종종걸음으로 날 쫓아오던 윤사랑은 갑자기 정원에서 넘어졌다.'
    '그것도 내가 처음 눈을 뜬 곳으로 추정되는 장소에.'

    hide Yun_panic with None
    play music Isabel_2
    show Sarang_CG_2 with Dissolve(2 ,alpha=  True)
    voice Yunsarang_042
    yun '"으아... 넘어져 버렸어요."'
    player '"괜찮아? 조심 좀 하지... 다친 곳은 없어?"'

    voice Yunsarang_043
    yun '"무릎이 조금 아프지만, 괜찮아요!"'
    '자리에서 일어나려는 윤사랑에게 손을 내밀었다.'
    '윤사랑은 살짝 붉어진 얼굴로 내 손을 잡았다.'
    player '"다행이네..."'
    '너무 대놓고 나를 좋아한다는게 티가 나서, 어떻게 반응해야 할지 민망했다.'

    hide Sarang_CG_2 with Dissolve(2.0)
    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_044
    yun '"주인님은 친절하시네요."'
    player '"그래? 그나저나 이 정원에는 파란색 꽃만 피어있는 건가?"'

    hide Yun_fallinlove with None
    show Yun_lookout at yun_standsize_bs with Dissolve(.5 ,alpha= True)
    voice Yunsarang_045
    yun '"그런가 봐요. 다른 색 꽃은 아직 보지 못했어요."'

    hide Yun_lookout with None
    show Yun_pout at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_046
    yun '"분홍색이라던가, 붉은색 꽃도 있으면 좋을 텐데 말이죠..."'
    player '"다른 색이 있으면 확실히 볼거리가 많겠지."'

    hide Yun_pout with None
    show Yun_Normal at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_047
    yun '"주인님은 무슨 색을 가장 좋아하세요?"'

    player '"갑자기?"'
    hide Yun_Normal with None
    show Yun_huc at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_048
    yun '"갑자기 궁금해졌거든요! 대답하기에 곤란한가요?"'
    player '"아니... 그런 건 아니지만..."'
    player '"내가 제일 좋아하는 색은..."'

    menu:
        "붉은색":      # 무증감
            '"난... 붉은색이 좋아. 열정적이잖아?"'
            hide Yun_huc with None
            show Yun_Laughter at yun_standsize_bs with Dissolve (.5 ,alpha = True)
            voice Yunsarang_049
            yun '"주인님도 그렇게 생각하시나요? 저도 붉은색이 가장 좋아요!"'
            player '"그래? 의외네. 분홍색을 좋아할 줄 알았는데."'

            hide Yun_Laughter with None
            show Yun_fallinlove at yun_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Yunsarang_050
            yun '"그건... 제 머리색이 분홍색이라?"'
            player '"아, 응."'

            hide Yun_fallinlove with None
            show Yun_Happy at yun_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Yunsarang_051
            yun '"분홍색도 좋아하지만, 제일은 붉은색이에요."'

            hide Yun_Happy with None
            show Yun_cuty at yun_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Yunsarang_053
            yun '"살아있다고 느끼게 하거든요."'

            hide Yun_cuty with None
            pass
        "파란색":      # 무증감
            player '"나는 파란색. 시원한 느낌이 보기 좋잖아."'
            hide Yun_huc with None
            show Yun_panic at yun_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Yunsarang_054
            yun '"아... 그렇군요."'

            hide Yun_panic with None
            show Yun_pout at yun_standsize_bs with Dissolve(.5 ,alpha= True)
            voice Yunsarang_055
            yun '"파란색... 나쁘진 않죠."'
            player '"별로 좋아하지는 않나 봐?"'

            hide Yun_pout with None
            show Yun_Normal at yun_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Yunsarang_056
            yun '"음... 좋아하지 않을 뿐이에요! 저는 붉은색을 더 좋아하거든요."'

            hide Yun_Normal with None
            show Yun_cuty at yun_standsize_bs with Dissolve(.5 ,alpha =True)
            voice Yunsarang_057
            yun '"살아있다고 느끼게 하거든요."'

            hide Yun_cuty with None
            pass
        "분홍색":      # 증가
            player '"나는 분홍색이 귀여워서 좋더라고."'
            hide Yun_huc with None
            show Yun_lookout at yun_standsize_bs with Dissolve(.5 ,alpha =True)
            voice Yunsarang_058
            yun '"분홍색도 좋지만, 제가 제일 좋아하는 색은 붉은색이에요."'
            player '"응? 의외네..."'
            player '"머리카락이 분홍색이라서, 분홍색을 좋아할 줄 알았어."'

            hide Yun_lookout with None
            show Yun_cuty at yun_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Yunsarang_059
            yun '"그런가요? 붉은색은 살아있다고 느끼게 하잖아요. 분홍색과 다르게."'

            voice Yunsarang_060
            yun '"그래서 붉은색을 더 좋아하는 것 같아요."'

            hide Yun_cuty with None
            $yun_f += .5
            pass
        "보라색":      # 감소
            player '"나는 보라색. 묘하게 신비스럽잖아?"'
            hide Yun_huc with None
            show Yun_anxiety at yun_standsize_bs with Dissolve(.5 ,alpha = True)
            '윤사랑의 얼굴이 순식간에 어두워졌다.'
            '처음 보는 윤사랑의 표정은 무서웠고, 등에 소름이 돋았다.'

            hide Yun_anxiety with None
            show Yun_fallinlove at yun_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Yunsarang_062
            yun '"아..."'
            '눈이 마주치자, 윤사랑의 표정은 평소로 돌아왔다.'

            hide Yun_fallinlove with None
            show Yun_Happy at yun_standsize_bs with Dissolve(.5, alpha = True)
            voice Yunsarang_063
            yun '"주인님은... 보라색을 좋아하는군요. 다른 색은 싫어하시나요?"'

            voice Yunsarang_064
            yun '"붉은색이라던가..."'
            player '"아, 붉은색도 좋아해."'

            hide Yun_Happy with Dissolve(.5 ,alpha = True)
            show Yun_huc at yun_standsize_bs with None
            $ renpy.pause (.5 )
            show Yun_huc at yun_one_jump_bs with None
            play sound jump1
            voice Yunsarang_065
            yun '"저도요! 살아있다는 느낌을 주는게 좋지 않나요?"'

            hide Yun_huc with None
            pass
    show Yun_Laughter at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_066
    yun '"색을 물어본 이유는 다름이 아니라..."'

    show img_gradation
    show itemBack
    show get_Item_gif
    play sound Bell
    $ renpy.pause(0.325)
    show Ribbon:
        xalign 0.505, yalign 0.46
        rotate 25
    show screen item_TextScren
    $ renpy.pause(2.0, hard = True)
    show screen Click_Text
    pause
    hide screen item_TextScren
    hide screen Click_Text
    hide get_Item_gif
    hide itemBack
    hide Ribbon
    hide img_gradation
    with Dissolve(0.38, alpha = True)

    $ persistent.m_bgetRibbon = True# 리본 추가

    hide Yun_Laughter with None
    show Yun_Normal at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_067
    yun '"이걸 드리고 싶었어요."'
    player '"이건..."'
    '윤사랑이 매고 있는 리본이랑 같은 붉은색 리본.'

    hide Yun_Normal with None
    show Yun_Happy at yun_standsize_bs with Dissolve(.5 ,alpha =True)
    '내 시선을 눈치챈 윤사랑은 볼을 붉혔다.'
    player '"그러고 보니, 계속 궁금했던 건데..."'
    player '"전에 우리 만난 적 있나?"'

    hide Yun_Happy with None
    show Yun_lookout at yun_standsize_bs with Dissolve(.5,alpha = True)
    voice Yunsarang_068
    yun '"...네?"'
    '윤사랑은 고개를 갸우뚱 기울이며 되물었다.'

    hide Yun_lookout with None
    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5 ,alpha =True)
    voice Yunsarang_069
    yun '"무슨 뜻인가요?"'
    player '"묘하게 나를 대하는 태도가 익숙해서... 아는 사이인가 했어."'
    player '"혹시라도 내가 착각한 거라면 미안."'

    hide Yun_fallinlove with None
    show Yun_fallinlove at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_070
    yun '"아, 그건..."'

    hide Yun_fallinlove with None
    show Yun_pout at yun_standsize_ms with Dissolve(.5 ,alpha =True)
    voice Yunsarang_071
    yun '"그게 말이죠..."'

    hide Yun_pout with None
    show Yun_tear at yun_standsize_ms with Dissolve(.5 ,alpha =True)
    voice Yunsarang_070
    yun '"제가... 사실은…. 아니..."'
    '완성되지 못한 단어가 튀어나온다.'
    '금방이라도 울 것 같은 표정이 안쓰러웠지만, 이성이 감정을 억누른다.'
    '왜 저런 반응을 보이는 걸까? 내가 심한 말을 한 것도 아닌데.'

    hide Yun_tear with None
    show Yun_fallinlove at yun_standsize_ms with Dissolve(.5 ,alpha =True)
    voice Yunsarang_073
    yun '"...제가 먼저 물어보고 싶어요."'
    voice Yunsarang_074
    yun '"주인님은 저에 대한 기억이 하나도 없으신 건가요?"'
    '윤사랑은 나를 똑바로 바라보며 물었다.'
    player '"응. 난 어제 너를 처음 만났어."'
    hide Yun_fallinlove with None
    show Yun_pout2 at yun_standsize_ms with Dissolve(.5 ,alpha =True)
    voice Yunsarang_075
    yun '"주인님이 그렇게 기억한다면... 저희는 모르는 사이가 맞을 거예요."'

    voice Yunsarang_076
    yun '"저는 저택에 오기 전의 기억이 없거든요. 제 나이도 모르고, 부모님은 어떤 분인지, 형제자매가 있었는지... 아무것도 기억이 안 나서..."'

    voice Yunsarang_077
    yun '"주인님을 만난 적 있냐는 질문에 정확한 답을 해드릴 수 없어요."'
    player '"그, 미안. 괜한 걸 물어봤네..."'

    hide Yun_pout2 with None
    show Yun_Normal at yun_standsize_ms with Dissolve(.5 ,alpha =True)
    voice Yunsarang_078
    yun '"괜찮아요! 주인님은 나쁜 의도가 아니었잖아요? 그렇게 심각한 것도 아니니까..."'

    hide Yun_Normal with None
    show Yun_Laughter at yun_standsize_ms with Dissolve(.5 ,alpha =True)
    voice Yunsarang_079
    yun '"주인님이 그런 의문을 가진 것도 어느 정도 추측할 수 있어요."'
    player '"응?"'

    hide Yun_Laughter with None
    show Yun_huc at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_080
    yun '"처음 주인님을 봤을 때부터 묘하게 친숙한 느낌이 들었던 탓에, 거리감이 없었거든요."'

    hide Yun_huc with None
    show Yun_Normal at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_081
    yun '"제가 너무 가까이 다가간 탓이니까..."'
    '오전부터 분위기가 너무 무거워졌다.'

    hide Yun_Normal with None
    show Yun_wink at yun_standsize_ms with Dissolve(.5 ,alpha =True)
    voice Yunsarang_082
    yun '"그래도 주인님과 함께 있다 보면 이것저것 기억나서 좋아요!"'
    player '"그래?"'

    hide Yun_wink with None
    show Yun_huc at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_083
    yun '"사실 붉은색을 좋아한다는 것도 주인님과 대화하면서 떠올랐어요."'

    hide Yun_huc with None
    show Yun_Happy at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_084
    yun '"앞으로도 계속 주인님과 대화하게 해주세요."'
    player '"아, 응. 여건이 된다면 얼마든지."'

    hide Yun_Happy with None
    show Yun_Normal at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    show Yun_Normal at yun_ms_to_Lout with None
    play sound run
    '윤사랑은 기쁘게 웃더니, 저택 안으로 뛰어 들어갔다.'

    play sound Thud1
    with vpunch
    '그렇게 뛰다가 또 넘어졌다는 건... 모르는 척 해줘야겠지?'

    scene bg black with dissolve
    stop music fadeout 2.0
    $renpy.pause(1.0)
    jump D_1_Lunch

    # 점심으로 점프

    return

label D_1_Library:
    '서재에는 어떤 책이 있을까...'
    '정보를 수집하려면 역시 글이 가장 많은 곳을 가야겠지?'
    '메이드들과 친해지는 것도 중요하지만, 이전 주인의 일기라던가... 쓸모 있는 걸 찾으면 좋을 텐데.'
    scene bg black with Dissolve(2.0 ,alpha =True)
    stop music fadeout 2.0
    $ renpy.pause(1.0, hard = True)
    scene bg BG_Adimroom with Dissolve(1.0 ,alpha = True)
    play music Isabel_1 fadein 2.0
    play sound DoorOpen2
    '서재의 문 여는 소리가 너무 커서 깜짝 놀랐다.'
    voice Isabel_025
    isabel '"누구세요?"'
    '안에서 들려오는 이 차분한 목소리는... 이자벨?'
    player '"어, 나야."'

    show Isabel_CG_1 with Dissolve(2.0 ,alpha =True)
    voice Isabel_026
    isabel '"아... 당신이군요. 그러니까 이름이..."'
    player '"[player_name]"'

    voice Isabel_027
    isabel '"...[player_name] 씨. 다들 당신을 주인님이라 불러서 잘 기억이 나지 않더라고요."'

    voice Isabel_028
    isabel '"주인님이라는 호칭은 너무 오글거려서 부르기도 애매하고..."'
    player '"나도 주인님이라는 호칭보다는, 이름 불리는게 더 좋아."'
    player '"[player_name]씨 보다는 [player_name]라고 불리는 걸 더 좋아하고."'

    voice Isabel_029
    isabel '"친하지도 않은 사람의 이름을 막 부르는 건 좀..."'
    '이자벨은 날 경계하는게 보이지만, 유일한 상식인 같아서 자꾸 다가가고 싶었다.'
    '누가 죄인이고, 누가 무고한지 모르는 상황에서 마음을 여는 건 위험하지만...'

    hide Isabel_CG_1 with None
    show Isabel_nodap at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_030
    isabel '"여기에는 무슨 일인가요?"'
    player '"정보가 필요해서."'

    hide Isabel_nodap with None
    show Isabel_panic at isabel_standsize_ms with Dissolve(.5 ,alpha =True)
    '이자벨은 의외라는 얼굴을 하고 나를 바라봤다.'
    '나는 아직 아무것도 안 했는데, 왜 다들 날 멍청하다고 생각하는 거지?'
    '천재는 아니지만... 바보인 것도 아닌데. 평범한 나로서는 그저 억울할 뿐이다.'
    player '"이곳이 어떤 곳인지도 모르는 상태에서 그냥 시간을 보내기에는 좀 찜찜했거든..."'

    hide Isabel_panic with None
    show Isabel_Normal at isabel_standsize_ms with Dissolve(.5 ,alpha =True)
    voice Isabel_031
    isabel '"관리자가 당신에게 모든 걸 가르쳐준 건 아닌가 보죠?"'
    player '"응. 너희보다 저택의 규칙을 많이 알고 있을 뿐이지... 저택에 관한 자세한 건 아무것도 몰라."'

    hide Isabel_Normal with None
    show Isabel_Laughter at isabel_standsize_ms with Dissolve(.5 ,alpha =True)
    voice Isabel_032
    isabel '"뭐, 당신이 그리 특별한 사람일 거라고는 생각하지 않았어요. 당신은 음... 좀 평범하잖아요? 갑자기 끌려온 우리랑 비교하자면."'
    '독설이 쏟아질 줄 알고 마음의 준비를 하고 있었는데... 생각보다 상냥한 말을 들어서 당황스러웠다. '

    hide Isabel_Laughter with None
    show Isabel_heung at isabel_standsize_ms with Dissolve(.5,alpha = True)
    voice Isabel_033
    isabel '"...뭐예요 그 표정은? 제가 조금 까칠한 성격이긴 하지만, 누구처럼 예의를 모르는 무례한 사람은 아니라고요."'
    player '"아, 미안..."'

    hide Isabel_heung with None
    show Isabel_Happy at isabel_standsize_ms with Dissolve(.5, alpha = True)
    voice Isabel_034
    isabel '"사과를 받아들이죠. 필요한 정보가 있다면 교환하고 싶은데... 당신 생각은 어때요?"'

    menu:
        "좋아. 정보를 교환하자!":
            call D_1_1_Library from _call_D_1_1_Library
            $ isabel_f += 1.5
        "나 혼자서도 충분한데?":
            call D_1_2_Library from _call_D_1_2_Library
    jump D_1_Lunch
    return

label D_1_Underoom:
    '복도에서 보았던 문 하나가 생각난다. 지하실이었나...?'
    '밖이 밝을 때 가도 무서운 곳이지만, 어두울 때는 더 무서우니 지금 가봐야지.'
    scene bg black with Dissolve(.5 ,alpha = True)
    stop music fadeout 2.0
    play music Scarlet_1 fadein 1.0
    play sound FootStep1
    '지하실로 이어지는 계단은 빛 한 점 없어서 꽤나 공포스러운 분위기를 연출하지만, 이미 누가 들어갔는지 안에서 빛이 보여서 내려갔다.'
    '문을 열고 들어간 지하실의 풍경은....'
    play sound DoorCreak1
    $renpy.pause(1.0)
    play music Scarlet_1 fadein 2.0
    scene bg BG_Underoom_Blood with Dissolve(3.0 ,alpha = True)
    play sound Thud1
    player '"으아아악!!!!"' with vpunch
    '피, 피?! 저거 피지?!!!!'
    play sound Thud1
    show Scarlet_CG_1 with hpunch
    $renpy.pause(1.0, hard = True)
    voice Scarlet_35
    scarlet '"시끄러워 짜샤!"'
    player '"으아악!!"'
    '갑자기 나타난 스칼렛 때문에 놀라서 비명을 질렀다.'
    '스칼렛은 손을 들어, 내 입을 막았고, 나는 눈을 굴려서 스칼렛과 핏자국을 번갈아 봤다.'

    voice Scarlet_36
    scarlet '"다시 비명을 지르면, 그때는 네 목을 비틀어버릴 거야. 알겠어?"'
    '나는 있는 힘을 다해 고개를 끄덕였다.'

    voice Scarlet_37
    scarlet '"좋아..."'

    hide Scarlet_CG_1 with Dissolve(2.0)
    show Scarlet_displease at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    '스칼렛은 손을 내렸고, 나는 침을 꼴깍 삼키고 스칼렛을 바라봤다. 누, 누굴 죽인 거지...?'
    '윤사랑은 아까 나와 있었으니 이자벨 혹은 엘리스인가?'

    hide Scarlet_displease with None
    show Scarlet_jjajeung at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_38
    scarlet'"무슨 상상을 하는지 다 알겠는데, 그런 거 아니거든?"'
    player '"그...그럼 이 자국은..."'

    hide Scarlet_jjajeung with None
    show Scarlet_lookout at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_39
    scarlet '"그 금발이 내려와서 다투다가..."'
    player '"다투다 화나서 죽였어?"'

    hide Scarlet_lookout with None
    show Scarlet_ppagchim at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    play sound Thud1
    show Scarlet_ppagchim at scarlet_one_jump_bs with None
    voice Scarlet_40
    scarlet '"아니야! 이 몸은 고작 그런 이유로 사람을 죽이지 않아!"' with vpunch

    hide Scarlet_ppagchim with None
    show Scarlet_stare at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    show Scarlet_stare at scarlet_one_jump with None
    voice Scarlet_41
    scarlet '"그렇지...? 아니, 왜 멀어지는 거야 너!"'
    player '"그...내가 언제 멀어졌다고?"'

    hide Scarlet_stare with None
    show Scarlet_inflate at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    show Scarlet_inflate at scarlet_one_jump with None
    voice Scarlet_42
    scarlet '"하아... 이건 와인병이 튄 흔적이야. 사람 피 같은 게 아니라."'
    player '"진짜...?"'

    hide Scarlet_inflate with None
    show Scarlet_ppagchim at scarlet_standsize_ms with Dissolve( .5,alpha = True)
    show Scarlet_ppagchim at scarlet_one_jump with None
    voice Scarlet_43
    scarlet '"진짜지! 그럼 가짜겠냐?!"'
    '진심으로 분해하는 스칼렛의 얼굴을 보니, 피가 아니라는 건 진짜 같았다.'
    '어쩐지 이곳에서 진한 와인 향이 나더라니...'

    hide Scarlet_ppagchim with None
    show Scarlet_stare at scarlet_standsize_ms with Dissolve( .5, alpha = True)
    voice Scarlet_44
    scarlet '"네놈은 여기까지 무슨 일이지?"'
    player '"나는 지하실에 뭐가 있는지 궁금했거든. 와인을 보관하는 장소였구나..."'
    '지하실에 가득 찬 와인은 그 수만큼 종류도 다양했다.'
    '술을 즐기는 사람이라면 좋아하겠지만, 미성년자인 나는 마실 수 없겠군...'

    hide Scarlet_stare with None
    show Scarlet_Angry at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_45
    scarlet'"혹시라도 마실 생각은 하지 마라. 파랭이가 너한테 술을 주지 말라고 주의를 줬으니까 말이지."'
    player '"파랭이라면... 관리자 말이지? 왜 나한테 술을 주면 안 되는데."'

    hide Scarlet_Angry with None
    show Scarlet_displease at scarlet_standsize_bs with Dissolve (.5 ,alpha = True)
    voice Scarlet_47
    scarlet '"그야 네놈이 갓 태어난 새끼니까. 아무리 이 몸이 모시는 신께서 무질서와 혼돈을 사랑하신다지만, 어린 짐승을 막 풀어둘 분은 아니다."'
    player '"아직 학생 신분이기는 하지만, 이래 봬도 20살이거든?"'
    '스칼렛은 내게 얼굴을 들이밀고서는 코를 킁킁거렸다.'

    hide Scarlet_displease with None
    show Scarlet_ppagchim at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_49
    scarlet '"아직도 젖비린내가 나는 놈이 무슨."'
    player '"젖비린내 같은 거 안 나거든! 스칼렛은 왜 지하실에 온 거야?"'

    hide Scarlet_ppagchim with None
    show Scarlet_Laughter at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_50
    scarlet '"흐응? 이 몸이야 당연히 신께 받칠 공물을 찾고 있었지. 그분께 제를 올릴만한 곳을 찾으면 더 좋겠다만..."'

    hide Scarlet_Laughter with None
    show Scarlet_Happy at scarlet_one_jump with Dissolve(.5 ,alpha = True)
    voice Scarlet_52
    scarlet '"...그래. 네놈에게 쓸모를 증명할 기회를 주지."'
    player '"응? 갑자기?"'

    hide Scarlet_Happy with None
    show Scarlet_Laughter at scarlet_standsize_ms with Dissolve( .5,alpha = True)
    voice Scarlet_53
    scarlet '"그래. 이 몸이 특별히 하사한 기회니 감사히 여기도록."'
    player '"어... 내가 뭘 해야 하는데?"'

    hide Scarlet_Laughter with None
    show Scarlet_Normal at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_54
    scarlet '"신께 올릴 와인을 찾도록. 최대한 오래되고 귀한 것으로!"'
    player '"직접 찾으면 되잖아...? 연도라던가 이름도 쓰여 있고..."'
    hide Scarlet_Normal with None
    show Scarlet_lookout at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_55
    scarlet '"..."'
    '스칼렛은 아무런 대답도 하지 않고 시선을 피했다.'
    '스칼렛이 대답을 피하는 이유는 뭘까...'
    menu:
        "부끄러워서":
            '아침에 있었던 일을 떠올리니, 대충 짐작이 갔다.'
            '글을 읽을 수 없거나, 와인에 대해 잘 모르거나... 혹은 둘 다일 수도 있겠지.'
            '스스로 좋은 와인을 고르지 못한다는 걸 말하기 부끄러워서 대답을 못 하는 거다. 이럴 때는 모른 척 넘어가 줘야겠지?'
            player '"난 와인에 대해서 잘 모르지만... 스칼렛이 준 기회니까 열심히 해볼게!"'
            hide Scarlet_lookout with None
            show Scarlet_panic at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Scarlet_56
            scarlet '"아, 네놈은 갓 태어났었지..."'
            player '"아니, 그 정도는 아니라니까?"'
            hide Scarlet_panic with Dissolve(1.0, alpha = True)
            $ scarlet_f += 1.0


        "내가 한심해서":
            '자기의 뜻을 헤아리지 못하는게 한심해서 대답해 주지 않는 건가...'
            '내가 궁예나 독심술사도 아니고, 말 한마디에 속뜻을 어떻게 알아차려!'
            player '"스칼렛, 왜 대답을 안 하는 거야?"'
            hide Scarlet_lookout with None
            show Scarlet_jjajeung at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
            voice Scarlet_57
            scarlet '"크흠... 이, 이 몸은 다른 할 일이 있어서 그렇다!"'
            '뭔가 미심쩍은 대답이지만, 일단은 이걸로 넘어가야 하려나?'
            '수상한 스칼렛을 뒤로하고 와인을 고르러 갔다.'
            hide Scarlet_jjajeung with Dissolve(1.0, alpha = True)

    '와인에 대해서 잘 아는게 아닌지라, 제일 오래되고 비싸 보이는 걸로 골랐다.'
    '스칼렛이 마음에 들어 하면 좋을 텐데...'
    '내가 와인을 가져오자 스칼렛은 붉은 꼬리를 흔들며 기쁘게 웃었다.'
    show Scarlet_Happy at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_59
    scarlet '"잘했다! 네 놈도 꽤 쓸모가 있군! 이건 이 몸이 네게 특별히 하사하는 거다!"'

    show img_gradation
    show itemBack
    show get_Item_gif
    play sound Bell
    $ renpy.pause(0.325)
    show Alcohol:
        xalign 0.505, yalign 0.46
        rotate 25
    show screen item_TextScren
    $ renpy.pause(2.0, hard = True)
    show screen Click_Text
    pause
    hide screen item_TextScren
    hide screen Click_Text
    hide get_Item_gif
    hide itemBack
    hide Alcohol
    hide img_gradation
    with Dissolve(0.38, alpha = True)

    $ persistent.m_bgetAlcohol = True # 컬렉션 , 와인 추가

    player '"이건... 와인이잖아?"'

    hide Scarlet_Happy with None
    show Scarlet_Laughter at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_60
    scarlet '"네놈이 시답잖은 걸 골라오면, 그걸 공물로 바치려고 했지만... 꽤나 좋은 걸 가져왔으니 그건 쓸모 없어졌다."'
    player '"나한테 지금 넘기는 거야? 쓰레기 처리?"'

    hide Scarlet_Laughter with None
    show Scarlet_inflate at scarlet_standsize_bs with Dissolve(.5, alpha = True)
    voice Scarlet_62
    scarlet '"이 몸이 특.별.히. 하사한 거라고 했을 텐데?"'
    player '"어, 응. 고마워..."'

    hide Scarlet_inflate with None
    show Scarlet_lookout at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_63
    scarlet '"크릉... 이제 제단을 만들 곳만 찾으면 되는데..."'

    hide Scarlet_lookout with Dissolve(.5 ,alpha = True)
    '스칼렛은 주변을 살펴보더니, 마음에 드는 곳을 찾지 못했는지 지하실 밖으로 나가버렸다.'

    scene bg black with Dissolve(2.0 ,alpha =True)
    stop music fadeout 2.0
    $ renpy.pause(1.0, hard = True)
    jump D_1_Lunch

    pause


    return


label D_1_1_Library:
    player '"좋아. 모르는게 있다면 얼마든지 물어봐. 나도 너에게 물어볼 테니까..."'
    hide Isabel_Happy with None
    show Isabel_lookout at isabel_standsize_ms with Dissolve(.5, alpha =True)
    voice Isabel_035
    isabel '"이자벨."'
    player '"응?"'

    hide Isabel_lookout with None
    show Isabel_pout at isabel_standsize_ms with Dissolve(.5 ,alpha =True)
    voice Isabel_036
    isabel '"이자벨이에요, 제 이름. 어제 자기소개 때 말했을 텐데요?"'
    player '"아... 미안 이자벨."'

    hide Isabel_pout with None
    show Isabel_heung at isabel_standsize_bs with Dissolve(.5,alpha =True)
    voice Isabel_037
    isabel '"흥, [player_name] 씨가 먼저 내게 물어봐요. 알려줄 수 있는 건 적을 테지만 시간 절약은 되겠죠."'
    '힐끔 쳐다보니 이자벨의 등 너머에 쌓여있는 책이 보였다. 우와 그 짧은 시간에 저 책을 다 읽은 거야?'

    hide Isabel_heung with None
    show Isabel_lookout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_038
    isabel '"저는 몸이 아파서 남들보다 일찍 일어나요. 할 게 없어서 미리 서재에 와서 책을 읽고 있었고..."'
    '내 시선을 눈치챈 이자벨이 설명을 붙여주었다.'
    player '"아, 그래서..."'

    hide Isabel_lookout with None
    show Isabel_Laughter at isabel_standsize_bs with Dissolve(.5 ,alpha =True)
    voice Isabel_039
    isabel '"아플 때 책을 워낙 많이 읽어서인지 남들보다 책 읽는 속도가 좀 빠르기도 하고요."'
    player '"대단하네. 난 그렇게 빨리, 많이 못 읽는데..."'

    hide Isabel_Laughter with None
    show Isabel_Happy at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_040
    isabel '"자랑은 이쯤하고... 궁금하신 건 없나요?"'
    player '"아, 이 저택이 언제 만들었는지. 저택에 어떤 사람이 왔다 갔는지... 알 수 있을까?"'

    hide Isabel_Happy with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_041
    isabel '"음... 어려운 질문이네요. 여태껏 이 저택에 왔던 사람들의 기록을 봤지만, 누가 처음으로 왔는지 저택은 언제부터 존재했는지 알 수 없어요."'

    hide Isabel_pout with None
    show Isabel_Normal at isabel_standsize_bs with Dissolve(.5 ,alpha =True)
    voice Isabel_042
    isabel '"공통점이 있다면 이들이 말하는 관리자는 파란 머리카락을 가진 성별을 알 수 없는 아이."'

    hide Isabel_Normal with None
    show Isabel_panic at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_043
    isabel '"기록은 전부 주인의 시점인데, 특이사항이 있다면 그들의 기록은 다 3일 밖에 없다는 점...?"'
    player '"아, 그건..."'
    '3일만 있으면 돌아갈 수 있으니까. 라고 대답하려다 입을 막았다. 이자벨에게 이건 말해줘도 되나...?'

    hide Isabel_panic with None
    show Isabel_soAngry at isabel_standsize_bs with Dissolve(.5 ,alpha =True)
    voice Isabel_044
    isabel '"...제게 숨길 게 있다면, 본인의 의지로 숨기는 것인지 아니면 말할 수 없는 것인지 알려주세요."'

    voice Isabel_045
    isabel '"당신은 얼굴에서 티가 나거든요."'
    player '"응... 말해도 되는지, 안되는지 모르거든... 나중에 관리자에게 확인해 보고 알려줄게."'

    hide Isabel_soAngry with None
    show Isabel_nodap at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_046
    isabel '"...좋아요. 메이드 시점의 기록은 없지만, 주인들의 기록은 잔뜩 남아있어요. 메이드는 네 명... 모두 같은 세계에서 온 건 아닌 것 같더라고요."'
    player '"다른 세계라면..."'
    hide Isabel_nodap with None

    show Isabel_lookout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_047
    isabel '"스칼렛이라는 사람처럼, 수인이 있는 세상이라던가... 마법, 신 이런 게 존재하는 세상이겠죠."'
    player '"신은 보통 세계에서도 존재하지 않나?"'

    hide Isabel_lookout with None
    show Isabel_Sad at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_048
    isabel '"글쎄요... [player_name] 씨가 사는 세계는 어떤지 모르지만. 제가 살던 곳에는 없었어요."'
    player '"그렇구나..."'

    hide Isabel_Sad with None
    show Isabel_nodap at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_049
    isabel '"주인들은 대부분 메이드에 대한 세세한 정보를 기록하던데, 당신도 해야 할 수도 있으니..."'

    show img_gradation
    show itemBack
    show get_Item_gif
    play sound Bell
    $ renpy.pause(0.325)
    show Paper:
        xalign 0.505, yalign 0.46
        rotate 25
    show screen item_TextScren
    $ renpy.pause(2.0, hard = True)
    show screen Click_Text
    pause
    hide screen item_TextScren
    hide screen Click_Text
    hide get_Item_gif
    hide itemBack
    hide Paper
    hide img_gradation
    with Dissolve(0.38, alpha = True)
    $ persistent.m_bgetPaper = True # 찢어진 종이 획득

    player '"이건..."'

    hide Isabel_nodap with None
    show Isabel_Laughter at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_050
    isabel '"바닥에 떨어져 있더라고요. 임시로 여기다 쓰다가, 관리자가 제대로 된 책이나 수첩을 건네주면 기록을 옮기세요."'
    player '"응, 넌 나한테 궁금한 거 있어?"'

    hide Isabel_Laughter with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_051
    isabel'"당신이 알려줄 수 있는 건 한정적인 것 같으니...음."'

    hide Isabel_pout with None
    show Isabel_nodap at isabel_standsize_bs with Dissolve(.5 , alpha = True)
    voice Isabel_052
    isabel '"아, 이 저택은 바다 위에 떠 있는 섬에 지어져 있다고 했죠?"'
    player '"응."'

    hide Isabel_nodap with None
    show Isabel_lookout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_053
    isabel '"혹시 다른 생명체를 본 적 없나요? 벌레나...쥐처럼 작은 거라도 상관없으니 우리 말고 다른 살아있는 생명체요."'
    player '"음... 없었던 것 같아. 벌레 우는소리는 못 들어봤어."'

    hide Isabel_lookout with None
    show Isabel_Happy at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_054
    isabel '"그렇군요. 궁금한 게 생기면 따로 물어볼게요."'

    scene bg black with dissolve
    stop music fadeout 2.0
    $renpy.pause(1.0, hard = True)

    return
    # 점심으로 이동

label D_1_2_Library:
    player '"나 혼자서 알아봐도 충분한데..."'
    hide Isabel_Happy with None
    show Isabel_soAngry at isabel_standsize_bs with Dissolve (.5 ,alpha = True)
    voice Isabel_055
    isabel '"..."'
    voice Isabel_056
    isabel '"그게 당신의 뜻이라면... 두 번 권할 이유는 없죠. 혼자 쓰는 공간이 아니니 너무 큰 소리를 내는 건 자제해 주세요."'
    player '"어, 응..."'
    hide Isabel_soAngry with Dissolve(.5 ,alpha = True)
    '침묵만이 감도는 서재에서 나는 여러 가지 책을 살펴봤다.'
    '딱히 참고될만한 책은 못 읽어본 것 같다.'
    '관리자가 요리하는데 참고했던 책은 본 것 같지만... 내가 궁금했던 건 이게 아니라고!'

    scene bg black with dissolve
    stop music fadeout 2.0
    $ renpy.pause(1.0, hard = True)
    return


label D_1_Lunch:
    play music Normal_a fadein 2.0
    scene bg BG_Livingroom with Dissolve(2.0,alpha = True)
    '메이드와 함께 시간을 보낸 후, 관리자가 불러 아까의 식당에 다시 모이게 되었다.'
    '만나지 않았던 메이드는 어디서 시간을 보냈는지 궁금하네~'
    show Hyeyeon_Normal at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    admin '"다들 충분히 쉬었어? 충분히 못 쉬었어도 일은 줄 거지만!"'

    show Elice_Strong at elice_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Elice_44
    elice '"해야 할 일은 뭐지?"'

    show Scarlet_Angry at scarlet_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Scarlet_64
    scarlet '"크릉... 이 몸을 부려 먹으려고 하다니..."'

    hide Hyeyeon_Normal
    hide Elice_Strong
    hide Scarlet_Angry
    with Dissolve(.5 ,alpha = True)

    show Hyeyeon_Angry at admin_standsize_bs with Dissolve(.5 ,alpha =True)
    admin '"지방 방송 금지! 너희가 해야 할 일은, 이 식당을 청소하는 거야!"' with hpunch

    hide Hyeyeon_Angry with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(.5 ,alpha = True)
    admin '"청소는 메이드의 본분 아니겠어?"'

    hide Hyeyeon_Laughter with None
    show Isabel_nodap at isabel_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Isabel_057
    isabel '"보통의 메이드 역할이라면... 이쪽이 맞긴 하죠."'

    show Yun_huc at yun_standsize_ms_R with Dissolve(.5 ,alpha =True)
    voice Yunsarang_085
    yun '"저 청소는 나름 잘해요!"'

    show Scarlet_displease at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_65
    scarlet '"이 몸에게 시키는게 고작 청소...?"'

    hide Yun_huc
    hide Scarlet_displease
    hide Isabel_nodap
    with Dissolve(.5)

    show Hyeyeon_Happy at admin_standsize_bs with Dissolve(.5 ,alpha = True)
    admin '"일하지 않는 자 먹지도 말라!"'

    hide Yun_huc
    hide Isabel_nodap
    hide Scarlet_displease
    hide Hyeyeon_Happy
    with Dissolve(.5, alpha = True)

    show Elice_Difficulty_2 at elice_standsize_ms_L with Dissolve(.5 ,alpha =True)
    voice Elice_45
    elice '"...일리가 있는 말이군."'

    show Scarlet_lookout at scarlet_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Scarlet_66
    scarlet '"납득했다."'
    player '"뭐야 이 흐름?"'

    hide Elice_Difficulty_2
    hide Scarlet_lookout
    with Dissolve(.5 ,alpha = True)
    show Hyeyeon_Laughter at admin_standsize_bs_R with Dissolve(.5 , alpha = True)
    admin '"뭐, 이 관리자님이 뛰어난 말솜씨로 모두를 설득한 거지!"'
    admin '"주인님은 메이드가 아니니까 청소하지 않아도 된다만... 같이 하고 싶다면 줄까?"'
    player '"뭐를?"'

    show Isabel_nodap at isabel_standsize_bs_L with Dissolve(.5 , alpha =True)
    voice Isabel_058
    isabel '"메이드 복이겠죠."'

    hide Hyeyeon_Laughter
    hide Isabel_nodap
    with Dissolve(.5 ,alpha = True)
    show Yun_huc at yun_standsize_ms with Dissolve(.5, alpha = True)
    voice Yunsarang_086
    yun '"와, 같이 입어요. 주인님!"'
    player '"싫어! 난 그런 옷 안 입는다고!"'

    show Elice_Normal_2 at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_46
    elice '"왜 잘 어울릴 것 같은데."'

    show Scarlet_pout at scarlet_standsize_ms_L with Dissolve(.5 ,alpha =True)
    voice Scarlet_67
    scarlet '"한 번쯤은 괜찮잖아?"'
    player '"싫다고!"'
    '질색하는 나를 보며 메이드들은 저들끼리 웃기 시작했다.'
    extend '그렇게 투닥거리더니, 왜 나를 놀릴 때가 되니까 사이가 좋은 거야?!'
    hide Yun_huc
    hide Elice_Normal_2
    hide Scarlet_pout
    with Dissolve(.5 ,alpha = True)

    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5 ,alpha =True)
    admin '"자자, 좀만 더 놀리면 주인님 울겠다~"'

    show Scarlet_panic at scarlet_standsize_ms_L with Dissolve(.5 ,alpha =True)
    voice Scarlet_68
    scarlet '"하긴... 저놈은 갓 태어났으니 너무 심하게 놀리면 울지도 모르지."'

    show Isabel_Happy at isabel_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Isabel_059
    isabel '"아... 저희가 심했나요? 미안해요."'
    player '"그 정도로 안 울어!"'

    hide Hyeyeon_Laughter
    hide Scarlet_panic
    hide Isabel_Happy
    with Dissolve(.5, alpha = True)

    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(.5 ,alpha =True)
    admin '"하하, 어디를 누가 청소할지는 너희가 알아서 정하는 거지만..."'
    admin '"나중에 검사했을 때 더러운 곳이 있다면 오늘 저녁은 없는 거야!"'

    hide Hyeyeon_Normal with Dissolve(.5 ,alpha = True)
    show Yun_fallinlove at yun_standsize_ms_R with Dissolve(.5 ,alpha =True)
    voice Yunsarang_087
    yun '"네에?!"'

    show Isabel_heung at isabel_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Isabel_060
    isabel '"먹을 거로 협박하는 건 좀 치사한데요..."'

    show Scarlet_lookout at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_69
    scarlet '"읏..."'

    hide Yun_fallinlove
    hide Isabel_heung
    hide Scarlet_lookout
    with Dissolve(1.0 ,alpha = True)

    show Hyeyeon_Happy at admin_standsize_bs with Dissolve(.5 ,alpha = True)
    admin '"다들 열심히들 하라고~!"'
    hide Hyeyeon_Happy with Dissolve(.5 ,alpha = True)
    play sound teleport_snap
    '관리자는 아까처럼 눈앞에서 퐁 하고 사라졌다.'
    '이후, 다들 이야기를 나눠 구역 1개씩을 맡아 청소한 뒤 다시 모이기로 했다.'
    '그리고 떨이처럼 혼자 남게 된 난.. 누굴 도와주러 가볼까..? '
    # 청소게임 진입 선택지
    menu:
        "엘리스에게 간다":
            $ e_D_1_Lunch = True
            $ GetOut_YvE = Elice
            scene bg black with Dissolve(2.0, alpha = True)
            stop music fadeout 2.0
            $ renpy.pause (1.0)
            play music Elicetheme fadein 2.0
            scene bg BG_Hall with Dissolve( 1.0, alpha = True)
            show Elice_Angry_2 at elice_standsize_bs with Dissolve(1.0 , alpha =True)
            voice Elice_47
            elice '"..."'

            hide Elice_Angry_2 with None
            show Elice_Angry_2 at elice_standsize_bs with Dissolve(.5    ,alpha = True)
            voice Elice_48
            elice '"네까짓 게 날 돕겠다고?"'
            voice Elice_49
            elice '"...방해되면 엉덩이를 걷어차 버릴 거야."'
            scene bg black with Dissolve(1.0)
            stop music fadeout 1.0
            # play music MiniGame fadein 2.5

            call Trash_Game_Elice from _call_Trash_Game_Elice

            scene bg black with Dissolve(2.0 ,alpha = True)
            stop music fadeout 2.0
            $ renpy.pause(1.0)
            play music Elicetheme fadein 2.0
            scene bg BG_Hall    with Dissolve(1.0 ,alpha =True)
            if CleaningPoint >= 23:
                show Elice_Surprised at elice_standsize_bs with Dissolve(1.0 ,alpha = True)
                voice Elice_50
                elice '"흐음..."'
                hide Elice_Surprised with None
                show Elice_Ignore at elice_standsize_bs with Dissolve(.5 ,alpha = True)
                voice Elice_51
                elice '"생각만큼 나쁘지 않군."'
                # 청소 게임 성공 아이템 컬랙션 획득
                hide Elice_Ignore with None
                show Elice_Gladness_2  at elice_standsize_bs with Dissolve(.5)
                voice Elice_52
                elice '"자, 이건 내가 주는 상이야."'
                # 아이템 획득

                show img_gradation
                show itemBack
                show get_Item_gif
                play sound Bell
                $ renpy.pause(0.325)
                show Elice_Hairpin:
                    xalign 0.505, yalign 0.46
                    rotate 00
                show screen item_TextScren
                $ renpy.pause(2.0, hard = True)
                show screen Click_Text
                pause
                hide screen item_TextScren
                hide screen Click_Text
                hide get_Item_gif
                hide itemBack
                hide Elice_Hairpin
                hide img_gradation
                with Dissolve(0.38, alpha = True)
                $ persistent.m_bgethairpin = True # 머리핀 추가

                hide Elice_Gladness_2 with None
                show Elice_Happy at elice_standsize_bs with Dissolve(.5 ,alpha = True)
                voice Elice_53
                elice '"식당 쪽에 일이 남았으니, 그쪽으로 가도록 하지."'

                play sound FootStep1
                $elice_f += 1.0

            else :
                show Elice_Strong at elice_standsize_bs with Dissolve(.5 ,alpha = True)
                voice Elice_54
                elice '"너 따위에게 기대를 한 내가 한심해지는군..."'

                # 청소 게임 성공 아이템 컬랙션 획득
                hide Elice_Strong with None
                show Elice_Coloration at elice_standsize_bs with Dissolve(.5 ,alpha = True)
                voice Elice_55
                elice '"잘했다면 상을 주었을 텐데 말이야."'

                # 성공 아이템 획득
                hide Elice_Coloration with None
                show Elice_Committed at elice_standsize_bs with Dissolve(.5)
                voice Elice_56
                elice '"뭘 봐? 때리기 전에 식당으로 돌아가지?"'

            scene bg black with Dissolve(2.0, alpha = True)
            stop music fadeout 2.0
            $ renpy.pause (1.0)

        "윤사랑에게 간다.":
            $ GetOut_YvE = Sarang
            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0
            $ renpy.pause(1.0)
            play music Yunsarang_1 fadein 2.0
            scene bg BG_Livingroom with Dissolve(1.0)
            show Yun_fallinlove at yun_standsize_bs with Dissolve(1.0)
            voice Yunsarang_088
            yun '"아... 저를 도와주시려구요..?"'

            hide Yun_fallinlove with None
            show Yun_pout at yun_standsize_bs with Dissolve(.5)
            voice Yunsarang_089
            yun '"제가 못 미더워서 오신 거겠지만..."'

            hide Yun_pout with None
            show Yun_wink at yun_standsize_bs with Dissolve(.5)
            voice Yunsarang_090
            yun '"주인님이 도와주신다고 하니 기쁘네요!"'

            scene bg black with Dissolve(1.0)
            stop music fadeout 1.0

            call Trash_Game_Sarang from _call_Trash_Game_Sarang

            # call screen End_Window with Dissolve(.5 ,alpha = True)
            scene bg black with Dissolve(1.0)
            stop music fadeout 2.0
            $renpy.pause(1.0)
            play music Yunsarang_1 fadein 2.0
            scene bg BG_Livingroom with Dissolve(1.0)

            if CleaningPoint >= 23:
                show Yun_wink at yun_standsize_bs with Dissolve(1.0)
                voice Yunsarang_091
                yun '"주인님께서 도와주시니 금방 끝낼 수 있었네요!"'

                hide Yun_wink with None
                show Yun_Happy at yun_standsize_bs with Dissolve(.5)
                voice Yunsarang_092
                yun '"도와주셔서 정말 고맙습니다!"'

                hide Yun_Happy with None
                show Yun_pout2 at yun_standsize_bs with Dissolve(.5)
                voice Yunsarang_093
                yun '"이건... 약소하지만 저의 보답이에요."'

                show img_gradation
                show itemBack
                show get_Item_gif
                play sound Bell
                $ renpy.pause(0.325)
                show Bear:
                    xalign 0.505, yalign 0.46
                    rotate 00
                show screen item_TextScren
                $ renpy.pause(2.0, hard = True)
                show screen Click_Text
                pause
                hide screen item_TextScren
                hide screen Click_Text
                hide get_Item_gif
                hide itemBack
                hide Bear
                hide img_gradation
                with Dissolve(0.38, alpha = True)
                $ persistent.m_bgetBear = True # 곰인형 추가
                # 아이템 획득

                hide Yun_pout2 with None
                show Yun_fallinlove at  yun_standsize_bs with Dissolve(.5)
                voice Yunsarang_094
                yun '"이, 이제 식당으로 가요! 다들 기다리고 있을 거예요!"'
                $yun_f += 1.0

            else:
                show Yun_Sad at yun_standsize_bs with Dissolve(1.0)
                voice Yunsarang_095
                yun '"아..."'

                hide Yun_Sad with None
                show Yun_pout at yun_standsize_bs with Dissolve(.5)
                voice Yunsarang_096
                yun '"너, 너무 침울해하지 말아요, 주인님!"'

                hide Yun_pout with None
                show Yun_pout2 at yun_standsize_bs with Dissolve(.5)
                voice Yunsarang_097
                yun '"다음번에 잘하면 되니까..."'

                hide Yun_pout2 with None
                show Yun_Normal at yun_standsize_bs with Dissolve(.5)
                voice Yunsarang_098
                yun '"식당으로 돌아갈까요?"'

            play sound FootStep1
            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0
            $ renpy.pause(1.0)

            pass
        "이자벨에게 간다.":
            $ GetOut_YvE = Isabel
            $ i_D_2_Lunch = True

            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0
            $renpy.pause(1.0)
            play music Isabel_1 fadein 2.0
            scene bg BG_Adimroom with Dissolve(1.0)
            show Isabel_nodap at isabel_standsize_bs with Dissolve(1.0)
            voice Isabel_061
            isabel '"아, 저를 도와주러 오신 건가요?"'
            hide Isabel_nodap with None
            show Isabel_Normal at isabel_standsize_bs with Dissolve(.5)
            voice Isabel_062
            isabel '"의외네요. 다른 사람을 도와주러 가실 줄 알았거든요."'
            hide Isabel_Normal with None
            show Isabel_lookout at isabel_standsize_bs with Dissolve(.5)
            voice Isabel_063
            isabel '"뭐... 싫단 건 아니지만요."'
            scene bg black with Dissolve(1.0)
            stop music fadeout 1.0
            # play music MiniGame fadein 2.5

            call Trash_Game_Isabel from _call_Trash_Game_Isabel

            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0
            $renpy.pause(1.0)
            play music Isabel_1 fadein 2.0
            scene bg BG_Adimroom with Dissolve(1.0)

            if CleaningPoint >= 23:
                show Isabel_Laughter at isabel_standsize_bs with Dissolve(1.0)
                voice Isabel_064
                isabel '"덕분에 청소를 빨리 끝낼 수 있었어요. 고맙습니다."'

                hide Isabel_Laughter with None
                show Isabel_Happy at isabel_standsize_bs with Dissolve(.5)
                voice Isabel_224_1
                isabel '"이건 감사 인사니까 받아주세요."'
                # 아이템 획득

                show img_gradation
                show itemBack
                show get_Item_gif
                play sound Bell
                $ renpy.pause(0.325)
                show Fountain_Pen:
                    xalign 0.505, yalign 0.46
                    rotate 00
                show screen item_TextScren
                $ renpy.pause(2.0, hard = True)
                show screen Click_Text
                pause
                hide screen item_TextScren
                hide screen Click_Text
                hide get_Item_gif
                hide itemBack
                hide Fountain_Pen
                hide img_gradation
                with Dissolve(0.38, alpha = True)
                $ persistent.m_bgetpen = True # 만년필 획득



                hide Isabel_Happy with None
                show Isabel_Laughter at isabel_standsize_bs with Dissolve(.5)
                voice Isabel_225_1
                isabel '"식당 쪽에 일이 남은 걸로 기억하는데, 이제 그쪽으로 가죠."'
                $isabel_f += 1.0

            else:
                show Isabel_nodap at isabel_standsize_bs with Dissolve(1.0)
                voice Isabel_226_1
                isabel '"..."'

                hide Isabel_pout with None
                show Isabel_Normal at isabel_standsize_bs with Dissolve(.5)
                voice Isabel_227_1
                isabel '"식당 쪽 일이 남았으니 그쪽으로 가죠."'

            play sound FootStep1
            scene bg black with Dissolve(2.0 ,alpha = True)
            stop music fadeout 2.0
            $renpy.pause(1.0)

            pass
        "스칼렛에게 간다.":
            $ s_D_1_Lunch = True
            $ GetOut_YvE = Scarlet

            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0
            $renpy.pause (1.0)
            play music Scarlet_1 fadein 2.0
            scene bg BG_Underoom with Dissolve(1.0)

            show Scarlet_heung at scarlet_standsize_bs with Dissolve(1.0)
            voice Scarlet_70
            scarlet '"...뭐야?"'

            hide Scarlet_heung with None
            show Scarlet_jjajeung at scarlet_standsize_bs with Dissolve(.5)
            voice Scarlet_71
            scarlet '"이 몸을 돕겠다고? 네놈이?"'

            hide Scarlet_jjajeung with None
            show Scarlet_Happy at scarlet_standsize_bs with Dissolve(.5)
            voice Scarlet_72
            scarlet '"그 마음만은 갸륵히 여겨주마."'
            scene bg black with Dissolve(1.0)
            stop music fadeout 1.0
            # play sound MiniGame fadein 2.5

            call Trash_Game_Scarlet from _call_Trash_Game_Scarlet

            scene bg black with Dissolve(2.0 ,alpha = True)
            stop music fadeout 2.0
            $renpy.pause (1.0)
            play music Scarlet_1 fadein 2.0
            scene bg BG_Underoom with Dissolve(1.0)

            if CleaningPoint >= 23:
                show Scarlet_panic at scarlet_standsize_bs with Dissolve(1.0)
                voice Scarlet_73
                scarlet '"크릉, 꽤 하잖아?"'

                hide Scarlet_panic with None
                show Scarlet_Happy at scarlet_standsize_bs with Dissolve(.5)
                voice Scarlet_74
                scarlet '"앞으로도 이렇게만 하거라."'

                hide Scarlet_Happy with None
                show Scarlet_Normal at scarlet_standsize_bs with Dissolve(.5)
                voice Scarlet_75
                scarlet '"이건... 이 몸이 주는 공치사다."'
                # 스칼렛 아이템 획득

                show img_gradation
                show itemBack
                show get_Item_gif
                play sound Bell
                $ renpy.pause(0.325)
                show Flowerpot:
                    xalign 0.505, yalign 0.46
                    rotate 00
                show screen item_TextScren
                $ renpy.pause(2.0, hard = True)
                show screen Click_Text
                pause
                hide screen item_TextScren
                hide screen Click_Text
                hide get_Item_gif
                hide itemBack
                hide Flowerpot
                hide img_gradation
                with Dissolve(0.38, alpha = True)
                $ persistent.m_bgetFlowerpot = True # 문어화분 획득
                voice Scarlet_76
                scarlet '"그 파랑이가 식당으로 오라고 하지 않았나?"'

                $scarlet_f += 1.0
            else:
                show Scarlet_displease at scarlet_standsize_bs with Dissolve(1.0)
                voice Scarlet_77
                scarlet '"크릉.... 한심하군."'

                hide Scarlet_displease with None
                show Scarlet_jjajeung at scarlet_standsize_bs with Dissolve(.5)
                show Scarlet_jjajeung at scarlet_one_jump_bs with None
                voice Scarlet_78
                scarlet '"당분간 이 몸 앞에 나타날 생각도 하지 말거라!"'

            play sound FootStep1
            scene bg black with Dissolve(1.0)
            stop music fadeout 2.0
            $ renpy.pause (1.0)

    scene bg BG_Livingroom with Dissolve(2.0 ,alpha = True)
    play music Normal_b fadein 2.0

    '배정된 구역의 청소를 마친 우리는 관리자가 사전에 공지했던 대로 식당에 모였다.'
    player '"여기만 청소하면 일은 끝인 거지?"'
    show Yun_huc at yun_standsize_ms with Dissolve(.5)
    show Yun_huc at yun_one_jump with None
    # play sound jump1
    voice Yunsarang_099
    yun '"네! 금방 끝날 테니, 주인님은 쉬고 계시는게 어떤가요?"'
    show Elice_Strong at elice_standsize_ms_L with Dissolve(.5)
    show Scarlet_Angry at scarlet_standsize_ms_R with Dissolve(.5)
    '말로는 설명 못할 살벌한 시선이 뒤에서 느껴졌다...'
    '윤사랑은 좋은 의도로 한 말이었겠지만... 나만 빠진다고 하면 저 둘이 나를 가만 안 둘 것 같은데?'
    player '"조금 밖에 안 남았으니 다 같이 해야지. 다들 고생했잖아?"'
    hide Elice_Strong
    hide Scarlet_Angry
    hide Yun_huc
    with Dissolve(1.0)
    show Elice_Normal_2 at elice_standsize_ms_L with Dissolve(.5)
    voice Elice_57
    elice '"나쁘지 않은 판단이야."'

    show Scarlet_displease at scarlet_standsize_ms_R with Dissolve(.5)
    voice Scarlet_79
    scarlet '"크릉... 쉰다면 네가 아닌 저 환자가 쉬어야지."'

    hide Scarlet_displease
    hide Elice_Normal_2
    with Dissolve(.5)
    show Isabel_pout at isabel_standsize_ms with Dissolve(.5)
    '스칼렛이 이자벨을 가리키자, 분위기가 숙연해졌다.'
    player '"...앉아서 조금 쉴래, 이자벨?"'

    '내 말에 이자벨은 고개를 저었다.'
    '혼자만 빠질 수 없다는 뜻이겠지.'

    hide Isabel_pout with None
    show Isabel_Laughter at isabel_standsize_ms with Dissolve(.5)
    isabel '"아뇨. 다들 열심히 하시는데 저만 빠질 수는 없죠. 신경 쓰지 않으셔도 괜찮아요."'
    player '"...도중에 힘들면 말해."'

    hide Isabel_Laughter with None
    show Isabel_Normal at isabel_standsize_ms with Dissolve(.5)
    isabel '"네."'
    hide Isabel_Normal with None
    '조금은 어색한 분위기 속에서 우리는 식당 청소를 시작했다.'
    play music Elicetheme fadein 1.0
    show Elice_Surprised at elice_standsize_bs with Dissolve(.5 ,alpha= True)
    voice Elice_58
    elice '"이봐."'
    player '"응?"'

    voice Elice_59
    elice '"너는 이 식탁을 치우도록 해. 청소하는데 방해되니까."'
    player '"어...응."'

    voice Elice_60
    elice '"분홍 머리."'
    hide Elice_Surprised with None
    show Elice_Surprised at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Yunsarang_100
    yun '"아, 네!"'

    show Yun_huc at yun_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Elice_61
    elice '"너는 청소 도구를 가져와."'

    voice Elice_62
    elice '"짐승은 물을 떠 오고, 환자는 걸레나 가져와서 닦아."'

    hide Yun_huc with None
    show Scarlet_heung at scarlet_standsize_ms_L with Dissolve(.5 ,alpha=  True)
    voice Scarlet_80
    scarlet '"크릉... 이 몸을 짐승이라 부르지 마라!"'

    hide Elice_Surprised with None
    show Elice_Difficulty at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_63
    elice '"그런 울음소리를 내면서 사람 취급을 받으려는 거야?"'

    hide Scarlet_heung with None
    show Scarlet_contempt at scarlet_standsize_ms_L with Dissolve(.5 ,alpha =True)
    voice Scarlet_81
    scarlet '"아무것도 모르는 주제에..."'

    show Isabel_heung at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_065
    isabel '"저런 사람은 상대하지 않는게 편해요, 스칼렛. 저랑 같이 가시죠."'

    voice Isabel_066
    isabel '"그리고 엘리스... 불필요한 싸움은 줄이는게 신상에 이로울 거예요. 관리자는 우리끼리 싸우는 걸 좋아하진 않거든요."'

    hide Isabel_heung
    hide Scarlet_contempt
    hide Elice_Difficulty
    with Dissolve(.5 ,alpha= True)

    show Elice_Contempt at elice_standsize_ms with Dissolve(.5 ,alpha =True)
    voice Elice_64
    elice '"흥."'

    '엘리스의 명령 덕분에 해야 할 일은 나누어졌지만... 분위기는 좋지 않다.'
    '아까까지의 훈훈한 분위기는 어디 간 거야? 내가 좀 곤란해도 괜찮으니까 차라리 날 놀리며 화목했으면 좋겠다...'
    '식탁을 구석으로 밀려는데 엘리스가 다가왔다.'
    hide Elice_Contempt with None
    show Elice_Coloration at elice_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Elice_65
    elice '"너 설마 식탁을 그냥 밀어버리려는 건 아니지?"'
    player '"어? 그러려고 했는데. 무슨 문제 있어?"'

    voice Elice_66
    elice '"하아... 그러면 바닥에 자국이 남잖아. 들어서 옮겨야지."'
    player '"보통 사람은 식탁을 혼자서 못 들어... 누가 도와주지 않는 이상."'
    '엘리스를 빤히 바라보니, 엘리스는 혀를 차면서도 곁으로 다가왔다.'

    hide Elice_Coloration with None
    show Elice_Coloration_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_67
    elice '"내가 왜 이런 일을 해야 하는지..."'
    '불평하는 와중에도 엘리스는 착실히 식탁을 옮겼다.'
    '식탁만 옮기고 끝일 줄 알았는데, 의자도 같이 옮겨줘서... 되게 놀랐다.'
    '솔직히 시키기만 하고 자긴 놀 것 같았는데...'

    hide Elice_Coloration_2 with None
    show Elice_Strong at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_68
    elice '"또 무례한 생각."'
    player '"내가 무슨 생각을 하는지 네가 어떻게 알아."'

    voice Elice_69
    elice '"흥, 네 생각 따위야 훤히 보이지."'

    hide Elice_Strong with Dissolve(.5 ,alpha = True)
    show Elice_Surprised at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    show Yun_Happy at yun_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Yunsarang_101
    yun '"저희 왔어요!"'
    '엘리스와의 대화는 다른 메이드들이 오면서 중단되었다.'

    hide Elice_Surprised with None
    show Elice_Contempt at elice_standsize_ms_R with Dissolve(.5, alpha = True)
    voice Elice_70
    elice '"난 저 짐... 붉은 머리한테 물을 길어오라고 했을 텐데?"'

    hide Yun_Happy with None
    show Yun_Laughter at yun_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Yunsarang_102
    yun '"그게 말이죠... 스칼렛이 들기에는 너무 무거워서 제가 들고 왔어요!"'
    player '"생각보다 약하네, 스칼렛?"'

    hide Yun_Laughter
    hide Elice_Contempt
    with None
    show Scarlet_inflate at scarlet_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Scarlet_82
    scarlet '"읏, 이 몸은 약하지 않다! 그저... 그분과의 연결이 끊긴 부작용일 뿐! 이 몸은 고작 저런 물동이 하나 못 들 만큼 약하지 않다!"' with hpunch

    show Isabel_pout at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_067
    isabel '"스칼렛, 귀가 아파요."'

    hide Scarlet_inflate with None
    show Scarlet_Sad at scarlet_standsize_ms_L with Dissolve(.5 ,alpha  = True)
    voice Scarlet_84
    scarlet '"미, 미안..."'
    '청소 도구를 가지러 가는 사이에 무슨 일이 있던 걸까?'
    '이자벨과 스칼렛, 그리고 윤사랑의 사이가 눈에 띄게 가까워졌다.'
    '제일 무거워 보이던 물동이는 윤사랑이, 청소 도구는 이자벨과 스칼렛이 나눠 들고 왔지만... 스칼렛이 더 적게 든 것 같다.'
    '최강자라고 생각했던 스칼렛이 최약자라니...'

    show Elice_Difficulty at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_71
    elice '"이제야 청소할 준비가 됐네. 다만... 저 붉은 머리가 이렇게 약할 줄은 몰랐는데."'

    hide Scarlet_Sad with None
    show Scarlet_inflate at scarlet_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Scarlet_85
    scarlet '"이게 다 그분과의 연결이 끊어져서...!"'

    hide Elice_Difficulty with None
    show Elice_Contempt_2 at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_72
    elice '"시끄러워. 지금 당장은 약한 게 맞잖아? 하아... 넌 저기서 환자랑 같이 걸레 들고 창틀과 식기를 닦아."'

    hide Scarlet_inflate with None
    show Scarlet_lookout at scarlet_standsize_ms_L with Dissolve(.5 ,alpha =True)
    voice Scarlet_86
    scarlet '"크윽..."'

    hide Isabel_pout with None
    show Isabel_pout at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_068
    isabel '"배려해 주시는 건가요? 감사합니다."'

    hide Scarlet_lookout with None
    show Scarlet_lookout at scarlet_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Scarlet_87
    scarlet '"이 몸은 감사 인사 따위 하지 않는다!"'

    hide Elice_Contempt_2 with None
    show Elice_Angry at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_73
    elice '"너 같은 이의 감사 인사는 듣고 싶지도 않아. 딱히 감사를 들으려고 한 일도 아니고."'

    hide Elice_Angry with None
    show Elice_Angry_2 at elice_standsize_ms_R with Dissolve(.5, alpha =True)
    voice Elice_74
    elice '"너랑 나는 걸레로 바닥을 닦고, 분홍 머리 너는 쓰레기를 버려."'

    hide Scarlet_lookout with None
    show Yun_panic at yun_standsize_ms_L with Dissolve(.5 , alpha = True)
    voice Yunsarang_103
    yun '"저 쓰레기는 너무 무거워 보이는데..."'

    hide Elice_Angry_2 with None
    show Elice_Strong at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_75
    elice '"네가 들고 온 물보다는 가벼울 텐데?"'

    hide Yun_panic with None
    show Yun_pout at yun_standsize_ms_L with Dissolve(.5 ,alpha = True)
    show Yun_pout at yun_Lms_to_Lout_walk with None
    play sound FootStep1
    $ renpy.pause (3.6)
    hide Yun_pout with None
    '윤사랑은 불만이 있는지 입술을 삐쭉 내밀고서는 순순히 쓰레기를 버리러 나갔다.'
    '엘리스는 사람을 참 잘 쓰네. 스칼렛은 걸레로 창문을 닦고 있었고, 이자벨은 식기를 꼼꼼히 닦고 있었다.'

    hide Elice_Strong
    hide Isabel_pout
    with None
    show Isabel_Normal at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_069
    isabel '"스칼렛, 창문에 물기가 너무 많아요."'

    hide Isabel_Normal with None
    show Isabel_pout at isabel_standsize_ms with Dissolve(.5 ,alhpa = True)
    voice Isabel_070
    isabel '"걸레가 제대로 안 짜여서 그런 것 같은데... 당신?"'
    player '"어,  나 불렀어?"'

    hide Isabel_pout with None
    show Isabel_nodap at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_071
    isabel '"네. 이 걸레 좀 대신 짜주시겠어요? 물이 제대로 안 짜여서..."'
    player '"그 정도야 쉽지."'

    show yun_huc at yun_Lout_to_Lms_Fast with Dissolve(.5 ,alpha = True)
    play sound run
    voice Yunsarang_104
    yun '"제가 도와드릴게요!"'
    '쓰레기를 버리고 온 윤사랑이 호다닥 뛰어와서 이자벨과 스칼렛의 걸레를 가로챘다.'
    player '"되게 빠르네..."'

    hide Isabel_nodap with None
    show Isabel_panic at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_072
    isabel '"조금만 더 힘을 줬으면 걸레가 찢어졌겠어요."'

    show Scarlet_panic at scarlet_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Scarlet_88
    scarlet '"분홍 머리... 힘 되게 세네."'

    hide Scarlet_panic
    hide yun_huc
    hide Isabel_panic
    with Dissolve(.5 ,alpha = True)

    show Yun_wink at yun_standsize_bs with Dissolve(.5, alpha = True)
    voice Yunsarang_105
    yun '"이 정도야 쉽죠! 제가 더 도울 일은 없을까요?"'
    '이곳에 오기 전 윤사랑이 어떤 일을 했을지 굉장히 궁금해지기 시작했다. 그냥 운동선수가 아니라 국가대표 같은 걸 하지 않았을까?'
    '다들 열심히 자기 할 일을 하고, 시작할 때 나빴던 분위기는 나름 괜찮아졌다.'
    '이렇게 무탈하게 청소가 끝나나 싶었을 때... 우려하던 일이 일어났다.'

    hide Yun_wink with None
    show Isabel_Normal at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_073
    isabel '"물이 더러워졌네요... 윤사랑 씨?"'
    show Yun_huc at yun_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Yunsarang_106
    yun '"네~ 도와드릴 일이 있나요?"'
    hide Isabel_Normal with None
    show Isabel_Happy at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_074
    isabel '"물을 갈아야 하는데, 여기서 가장 믿음직스러운 게 사랑 씨라서."'

    hide Yun_huc with None
    show Yun_Laughter at yun_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Yunsarang_107
    yun '"제가 금방 갈아올게요!"'
    player '"아, 무거울 테니까 내가 같이 갈게."'

    show Elice_Coloration at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_76
    elice '"이봐, 너는 나랑 같이 바닥을 닦아야지."'
    player '"응? 거의 다 닦지 않았어? 걸레가 이렇게 더러우면 더는 못 닦을 것 같으니까 같이 가서 겸사겸사 빨고 올게."'

    hide Elice_Coloration with None
    show Elice_Committed at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_77
    elice '"분홍 머리를 돕겠다는 핑계로 너는 쉬겠다는 거야?"'
    player '"핑계가 아니라...!"'

    hide Yun_Laughter with None
    show Yun_panic at yun_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Yunsarang_108
    yun '"싸우지 마세요! 저는 혼자 가도 괜찮으니까... 주인님은 엘리스랑 같이 청소하고 계세요! 금방 물을 떠 올게요."'

    show Yun_panic at yun_Lms_to_Lout_Fast with None
    play sound run

    $renpy.pause(1.0)

    hide Yun_panic with None
    '윤사랑은 급하게 더러워진 물을 들고 뛰어나갔다.'
    '바닥에 흘린 더러운 물을 보며 엘리스는 한숨을 푸욱 내쉬었다.'

    hide Elice_Committed with None
    show Elice_Contempt at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_78
    elice '"돕는다더니, 일을 늘리기나 하고!"'
    player '"이게 다 너 때문이잖아, 엘리스."'

    hide Elice_Contempt with None
    show Elice_Strong_2 at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_79
    elice '"뭐?"'
    player '"네가 그런 말을 하니까..."'

    hide Elice_Strong_2 with None
    show Elice_Contempt at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_80
    elice '"하, 네가 쓸데없는 짓을 하니까 한 말이잖아. 저 분홍 머리 혼자서도 할 수 있는 일을 돕겠다고 나서니까...!"'

    player '"..."'
    show Scarlet_contempt at scarlet_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Scarlet_89
    scarlet '"야 금..."'

    hide Isabel_Happy with None
    show Isabel_Normal at isabel_standsize_ms with Dissolve(.5 ,alpha= True)
    voice Isabel_075
    isabel '"쉿, 스칼렛. 우리가 끼어들 문제가 아니에요."'

    voice Elice_81
    elice '"하아... 이놈이고 저놈이고 짜증 나는 일만 가득하네."'

    '싸해진 분위기 속에서 스칼렛만 어리둥절한 표정을 짓고 있었다.'
    '저 사람... 여러모로 모자란 것 같지?'

    hide Isabel_Normal
    hide Scarlet_contempt
    hide Elice_Contempt
    with Dissolve(.5 ,alpha = True)
    show Yun_Happy at yun_standsize_ms_L with Dissolve(.5 ,alpha = True)
    show Elice_Surprised at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Yunsarang_109
    yun '"오래 기다리셨죠! 물 길어 왔어요~!"'


    hide Yun_Happy
    show Yun_panic at yun_standsize_ms_L
    with Dissolve(.5 ,alpha = True)
    voice Yunsarang_110
    yun '"어... 어라... 자, 잠시만! 으아악!!"'

    show Yun_panic at yun_ms_L_to_ms with None
    $renpy.pause(.5)
    show Yun_panic at yun_ms_to_down with None
    $renpy.pause(.5)
    hide Yun_panic
    hide Elice_Surprised
    with Dissolve(.5, alpha = True)

    show screen Mini_Scene(pail) with Dissolve(.5)
    play sound Water1
    with vpunch

    '물통을 들고 급하게 걸어오던 윤사랑은 발이 꼬여서 넘어졌다.'

    play music horror_a fadein 2.0

    '불행하게도 물통은 하늘을 날았고, 윤사랑과 제일 가까운 곳에 있던 엘리스는 그 물을 정통으로 뒤집어썼다.'
    hide screen Mini_Scene with Dissolve(.5)
    show Yun_Sad at yun_standsize_ms_L with Dissolve(.5 ,alpha =True)
    voice Yunsarang_111
    yun '"아..."'

    show Scarlet_panic at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_90
    scarlet '"그...."'

    show Isabel_Sad at isabel_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Isabel_076
    isabel '"일 났네요."'
    hide Isabel_Sad
    hide Scarlet_panic
    hide Yun_Sad
    with Dissolve(.5 ,alpha = True)

    show Elice_Strong_2 at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_82
    elice '"하아... 너... 이게 무슨 짓이지?"'

    show Yun_Sad at yun_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Yunsarang_112
    yun '"으, 으아.... 죄, 죄송해요!"'
    voice Yunsarang_113
    yun '"얼른 닦아드릴게요! 수, 수건이 어딨더라!"'
    '윤사랑은 급하게 수건을 찾았지만, 식당 어디서도 수건을 찾을 수 없었다.'
    '당황한 윤사랑보다 더 걱정되는 건 엘리스다. 표정을 보니 엄청나게 화난 것 같은데...'

    hide Elice_Strong_2 with None
    show Elice_Strong at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_83
    elice '"필요 없어. 그보다 너, 방금 일부러 그런 거지?"'
    voice Yunsarang_114
    yun '"아, 아니에요! 일부로라뇨! 하늘에 맹세코 절대 아니에요!"'

    hide Elice_Strong with None
    show Elice_Angry at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_84
    elice '"뻔뻔하기도 하지. 내가 그런 거짓말에 속을 것 같아?"'
    voice Yunsarang_115
    yun '"거, 거짓말이 아니에요! 제가 마음이 급해서... 그리고 전 원래 덜렁거리는 성격이라..."'

    voice Elice_85
    elice '"넌 상대를 잘못 골랐어. 훌륭한 연기지만... 내가 속아 넘어갈 것 같아?"'

    hide Yun_Sad with None
    show Isabel_Sad at isabel_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Isabel_077
    isabel '"윤사랑 씨가 넘어진 건 아무리 봐도 실수였어요."'

    hide Scarlet_panic with None
    show Scarlet_Sad at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_91
    scarlet '"금발, 네가 오해하는 거 아니야?"'

    hide Elice_Angry with None
    show Elice_Angry_2 at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_86
    elice '"이 녀석들 때문에 거짓말을 계속하는 거구나?"'

    hide Isabel_Sad with None
    show Yun_Sad at yun_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Yunsarang_116
    yun '"죄, 죄송해요... 정말 죄송해요..."'

    hide Scarlet_Sad with None
    show Scarlet_Sad at scarlet_standsize_ms with Dissolve(.5,alpha = True)
    voice Scarlet_92
    scarlet '"어, 우...울지마 분홍..."'

    hide Yun_Sad
    show Isabel_Sad at isabel_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Isabel_078
    isabel '"엘리스 씨, 당신이 성격이 안 좋은 건 알지만... 이번은 좀 심한 것 같아요."'

    hide Elice_Angry_2 with None
    show Elice_Angry at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_87
    elice '"쓸모없는 것들..."'

    hide Scarlet_Sad with None
    show Scarlet_Angry at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_93
    scarlet '"야, 금발!"'
    player '"하아..."'

    '한숨밖에 나오지 않는 상황이다.'
    '끝까지 윤사랑이 거짓말을 한다고 주장하는 엘리스와 울기 시작한 윤사랑...'
    '어떡하지?'

    menu:
        "엘리스를 데리고 나간다.":
            $ elice_f += .5
            jump GetOut_with_elice

            pass

        "윤사랑을 데리고 나간다.":
            $ yun_f += .5
            jump GetOut_with_sarang
            pass
    # hide

    pause

label GetOut_with_elice:

    '일단 엘리스를 데리고 자리를 피해야겠다.'
    '다들 윤사랑 편을 들고 있으니까, 울고 있는 윤사랑을 데리고 나가도 상황은 나아지지 않는다.'
    '괜히 자기들끼리 싸움 나는 걸 보는 것보다 이게 낫겠지.'
    player '"엘리스, 나가서 이야기 하자."'
    hide Elice_Angry with None
    show Elice_Strong at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_89
    elice '"...그래."'
    '엘리스는 답지 않게 작은 목소리로 대답하며 나를 쫓아 나왔다.'
    # 조건부 추가 대사

    hide Elice_Strong
    hide Scarlet_Angry
    hide Isabel_Sad
    with Dissolve(.5 ,alpha = True)
    call WhoisSelected_e from _call_WhoisSelected_e

    scene bg black with Dissolve(.5 ,alpha = True)
    stop music fadeout 2.0
    play sound Footstep_flower
    # play sound FootStep1
    $ renpy.pause(2.0)
    scene bg BG_Garden_Morning with Dissolve(.5 ,alpha = True)
    play music Elicetheme fadein 2.0
    show Elice_Difficulty at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    '나는 엘리스와 같이 정원으로 나왔다.'
    '윤사랑이 엎은 물 때문에 물에 빠진 생쥐 꼴이 된 엘리스지만, 특유의 기품은 사라지지 않는다.'
    '물 한 번 엎었다고 사람이 저 정도 될 정도면, 양동이에 물이 얼마나 있던 거야?'
    '정원으로 나오는 길 중간에 챙긴 수건을 엘리스에게 건네주었다.'
    player '"오래 있으면 추울 테니까 짧게 이야기하고 들어가자."'
    voice Elice_91
    elice '"..."'
    player '"넌 정말 윤사랑이 일부로 물을 엎었다고 생각해?"'
    hide Elice_Difficulty with None
    show Elice_Strong at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_92
    elice '"그래. 다른 사람들 눈은 속여도 내 눈은 못 속여."'
    player '"그때의 상황은 누가 봐도 실수였어."'
    player '"어제 처음 만난 윤사랑이 너에게 원한을 가질 일도 없고."'
    player '"그런데도, 고의라고 확신하는 이유가 뭐야?"'
    hide Elice_Strong with None
    show Elice_Angry at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_93
    elice '"네 질문에 대답하기 전에 내가 먼저 묻지."'
    player '"아, 응. 무엇이든지."'
    hide Elice_Angry with None
    show Elice_Surprised at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_94
    elice '"너도 아까의 그 둘처럼 내가 억지를 부린다고 생각해?"'

    '무덤덤하게 말하는 엘리스를 보며 아까의 상황을 떠올렸다.'
    '윤사랑은 울고, 이자벨과 스칼렛은 엘리스를 몰아갔다.'
    '평범한 사람이었다면 상처받았겠지만... 엘리스는 글쎄?'
    '윤사랑의 수에 당한 것에 분해하며, 자신을 몰아간 둘을 한심하게 여기는 듯했다.'
    '여기서 대답을 잘못하면 나도 바보 취급받을 것 같은데...?'
    menu:
        '정말로 네가 착각한 거 아닐까?':
            player '"억지 부리는 거라고는 생각하지 않아."'
            player '"그렇지만, 다들 윤사랑이 실수라고 생각하는데..."'
            player '"네가 착각했을 확률도 있지 않을까?"'
            '말을 하면 할수록 엘리스의 표정이 굳는게 느껴졌다.'
            '틀린 답을 골랐다는 자각은 있지만... 다른 답이 떠오르지 않았다.'
            hide Elice_Surprised with None
            show Elice_Strong_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Elice_95
            elice '"하... 그나마 나은 녀석인가 했더니."'
            hide Elice_Strong_2 with None
            show Elice_Angry at elice_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Elice_96
            elice '"그런 식으로 나온다면 내가 할 말은 없어."'

            '엘리스는 내가 준 수건을 내려놓고 저택 안으로 돌아갔다.'
            '엘리스가 있던 자리에는 물에 젖은 장미 가지가 있었다.'
            jump D_1_Dinner
            pass
        '윤사랑의 수작은 너무 티났어.':
            player '"솔직히, 윤사랑의 수작은 너무 티가 났어."'
            player '"다들 왜 눈치 못 채고 너를 몰아가는 걸까 의문이 들 정도로."'
            '내 대답을 들은 엘리스의 표정은 미묘해졌다.'
            hide Elice_Surprised with None
            show Elice_Coloration  at elice_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Elice_98


            elice '"...네가 그걸 알아봤을 리가 없는데."'
            player '"응?"'
            hide Elice_Coloration with None
            show Elice_Surprised_2 at elice_standsize_bs with Dissolve(.5, alpha = True)
            voice Elice_99
            elice '"아니야. 그 검은 속내를 알아봤다니 다행이네."'
            # 선택지 탈출
            pass
        '네가 그렇게 말하는데 이유가 있겠지.':
            player '"억지 부린다고 생각하지 않아."'
            player '"네가 그렇게 말하는데 이유가 있겠지."'
            player '"너를 오랫동안 안 건 아니지만... 떼를 부리는 성격은 아니잖아?"'

            hide Elice_Surprised with None
            show Elice_Strong_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Elice_100
            elice '"...하아. 네놈은 어떻게 아직도 살아있는 거지?"'
            player '"응?"'

            hide Elice_Strong_2 with None
            show Elice_Difficulty at elice_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Elice_101
            elice '"조언을 해주자면, 아무 사람이나 그리 쉽게 믿는게 아니야."'

            hide Elice_Difficulty with None
            show Elice_Difficulty_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Elice_102
            elice '"네 말대로 우린 만난 지 얼마 지나지도 않았고, 네가 나에 대해 아는 정보는 내 외관과 이름밖에 없잖아?"'

            hide Elice_Difficulty_2 with None
            show Elice_Coloration at elice_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Elice_103
            elice '"그런데 어떻게 그리 쉽게 믿는다고 말하는지..."'
            player '"직접적으로 믿는다고 말한 적은 없지만... 아무 사람이 아니잖아?"'

            hide Elice_Coloration with None
            show Elice_Contempt_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Elice_104
            elice '"그만. 네 이야기를 듣다 보면 나까지 바보가 되는 기분이야."'
            # 선택지 탈출로 점
            pass

    stop music fadeout 2.0
    hide Elice_Contempt_2 with Dissolve(.5)
    show Elice_Surprised at elice_standsize_bs with Dissolve(1.0)
    $ renpy.pause(1.0)
    play music emotional fadein 2.0
    show Elice_Surprised_2 at elice_standsize_bs with Dissolve(.5)
    hide Elice_Surprised with None
    voice Elice_105
    elice '"분명 네 말대로 나는 윤사랑과 어제 처음 만났지만, 원한이 생기기엔 충분한 시간이야."'

    hide Elice_Surprised_2 with None
    show Elice_Surprised at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_106
    elice '"그런 일을 저지를 동기가 없다는 건 추측이지."'
    player '"그렇구나."'

    hide Elice_Surprised with None
    show Elice_Surprised at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_107
    elice '"그리고, 동기쯤은 쉽게 추측할 수 있어."'
    player '"어?"'

    hide Elice_Surprised with None
    show Elice_Strong at elice_standsize_bs with Dissolve(.5,alpha = True)
    voice Elice_108
    elice '"걘 나를 싫어하거든. 정확하게 말하자면... 저택에 있는 모두를 싫어하겠지만."'
    player '"...전혀 몰랐어."'

    hide Elice_Strong with None
    show Elice_Coloration at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_109
    elice '"대놓고 티를 내는 멍청이가 어디 있겠어?"'
    player '"왜 싫어하는지 알 수 있다면 좋을 텐데..."'

    hide Elice_Coloration with None
    show Elice_Coloration_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    '엘리스는 내 말에 기가 막힌다는 듯한 표정을 지었다.'
    '한숨을 푸욱 내쉰 엘리스가 말했다.'

    hide Elice_Coloration_2 with None
    show Elice_Difficulty_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_110
    elice '"지금까지 살아있을 수 있었던 건... 운인가?"'
    player '"무슨 말인지 모르겠어."'

    hide Elice_Difficulty_2 with None
    show Elice_Strong at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_111
    elice '"저 바보 둘이 윤사랑의 편을 드는 동안은, 저 가증스러운 연기를 계속 봐야겠지..."'
    player '"스칼렛이랑 이자벨은 윤사랑이 실수했다고 굳게 믿으니까."'

    '한동안 우리 사이에 말은 없었다.'
    '엘리스는 혼자서 잠시 생각하다, 이내 화를 내고, 다시 차분히 생각하고...'
    '도저히 따라갈 수 없는 분위기에 은근 슬쩍 뒤로 물러나버렸다.'
    player '"엘리스, 내 생각에는 네가 먼저 사과하는게 좋을 것 같아."'

    hide Elice_Strong with None
    show Elice_Committed_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    '엘리스의 표정은 엄청나게 무서워졌다.'
    player '"네 말을 믿지 않는게 아니야."'
    player '"다들 너를 믿지 않으니까... 일단은 물러나서 윤사랑을 지켜보는게 좋겠다는 뜻이지."'
    player '"말하자면... 이보 전진을 위한 일보 후퇴?"'

    hide Elice_Committed_2 with None
    show Elice_Surprised at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_112
    elice '"흐음. 일리는 있군."'
    player '"윤사랑은 몰라도 다른 둘과 사이가 나쁜 건 곤란하지 않겠어?"'

    hide Elice_Surprised with None
    show Elice_Difficulty at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_113
    elice '"...곤란하네."'
    player '"왜?"'

    hide Elice_Difficulty with None
    show Elice_Difficulty_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_114
    elice '"남한테 사과 같은 건 해본 적 없어서 말이지."'
    player '"...얼마나 귀하게 자랐으면 사과 한 번 해본 적 없는 거야? 공주님?"'
    hide Elice_Difficulty_2 with None
    show Elice_coldsmiley_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_115
    elice '"고작 공주? 그보다 훨씬 높지."'
    '엘리스는 자신만만한 표정을 짓고 나를 바라봤다.'
    # voice Elice_116
    player '"공주님이 아니라면...여왕폐하?"'

    hide Elice_coldsmiley_2 with None
    show Elice_Angry at elice_standsize_bs with Dissolve(.5 ,alpha = True)

    voice Elice_116
    elice '"그보다 더 높지."'
    voice Elice_117
    elice '"내가 다스린 나라는 왕국 따위가 아니라 제국이야."'
    player '"그 대단하신 황제 폐하가 지금은 메이드가 된 거구나."'

    hide Elice_Angry with None
    show Elice_Angry_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_118
    elice '"...쳇."'
    player '"너희 나라에서나 황제 폐하지, 여기서는 메이드니까 남들의 시선을 의식할 필요가 있어."'

    hide Elice_Angry_2 with None
    show Elice_Coloration_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_119
    elice '"... 너 같은 녀석에게 충고를 받을 줄이야."'
    player '"칭찬이라 생각할게."'
    player '"감기 걸릴지도 모르니까 안으로 들어가자."'

    hide Elice_Coloration_2 with None
    show Elice_Surprised_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_120
    elice '"그래... 그 분홍과는 알아서 대화할 테니 넌 여기서 좀 기다리다 와."'
    player '"응? 같이 사과하러 가지 않아도 괜찮아?"'

    hide Elice_Surprised_2 with None
    show Elice_Contempt at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_121
    elice '"너의 도움 따위 필요 없어."'
    player '"아... 추울 테니까 이거 두르고 가."'
    '나는 엘리스에게 내 겉옷을 주었다.'

    hide Elice_Contempt with None
    show Elice_Pudency at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_122
    elice '"흠... 고마워."'

    play sound Footstep_flower_2
    hide Elice_Pudency with Dissolve(1.0)

    '엘리스는 감사 인사만 남긴 후, 빠르게 자리를 떠났다.'
    '고마워...라니. 그 엘리스가 나에게 감사 인사를 할 줄이야.'
    '괜히 얼굴이 붉어지는 기분이다. 무언가... 인정받았다는 기분.'
    '엘리스가 있던 자리에는 물에 젖은 장미 가지가 있었다.'
    player '"엘리스랑 닮았네..."'

    show img_gradation
    show itemBack
    show get_Item_gif
    play sound Bell
    $ renpy.pause(0.325)
    show Flower:
        xalign 0.505, yalign 0.46
        rotate 0
    show screen item_TextScren
    $ renpy.pause(2.0, hard = True)
    show screen Click_Text
    pause
    hide screen item_TextScren
    hide screen Click_Text
    hide get_Item_gif
    hide itemBack
    hide Flower
    hide img_gradation
    with Dissolve(0.38, alpha = True)
    $ persistent.m_bgetFlower = True
    # 컬렉션 , 젖은 장미가지 추가.


    jump D_1_Dinner
    return

label GetOut_with_sarang:
    '일단 윤사랑을 데리고 나가야겠다.'
    '윤사랑이 계속 이곳에서 울고 있으면, 다들 엘리스를 몰아갈 테니까...'
    '남들이 싸우고 있으면 윤사랑도 진정하기 어려울 거다.'
    player '"나랑 나가서 바람 좀 쐬고 오자."'
    hide Scarlet_Angry with None
    # show Yun_Sad at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    # voice Yunsarang_121
    # yun '"...네."'
    # '윤사랑은 내 옷자락을 잡고 고개를 끄덕였다.'
    # hide Elice_Strong
    # hide Yun_Sad
    # hide Isabel_Sad
    # with Dissolve(.5 ,alpha = True)
    call WhoisSelected_y from _call_WhoisSelected_y

    stop music fadeout 2.0
    scene bg black with Dissolve(2.0 ,alpha = True)
    $ renpy.pause(2.0 ,hard = True)
    play music emotional fadein 1.0
    scene bg Myroom with Dissolve(1.5, alpha = True)
    show Yun_Sad at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    '윤사랑을 데리고 내 방으로 데리고 왔다.'
    '윤사랑이 진정되면 다시 식당으로 돌아가서 차분히 대화해 봐야지.'
    '오해가 있다면 푸는게 우선이다.'
    '방에 있던 손수건을 윤사랑에게 건네주었다.'
    '친한 친구라면 직접 눈물을 닦아주겠지만... 아직 그런 사이는 아니니까?'
    '윤사랑은 손수건을 멀뚱히 쳐다보다 옷소매로 눈물을 닦았다.'
    player '"손수건으로 닦지, 눈가 다 짓무를 텐데."'

    hide Yun_Sad with None
    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_121
    yun '"아..."'
    '뒤늦게 깨달은 듯, 윤사랑의 얼굴은 붉어졌다.'

    hide Yun_fallinlove with None
    show Yun_panic at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    show Yun_panic at yun_one_jump_bs with None
    voice Yunsarang_122
    yun '"죄, 죄송해요..."'
    player '"죄송할게 뭐 있어. 다음에 제대로 쓰면 되는 거지."'

    hide Yun_panic with None
    show Yun_Sad at yun_standsize_bs with Dissolve(.5 ,alpha  = True)
    '윤사랑은 고개를 푹 숙였다. 분위기가 점점 이상해지네'
    player '"아까는 엘리스가 심했어. 단지 실수인데 그렇게까지 따지다니."'
    player '"네가 일부로 그럴 일도 없을 텐데 말이야?"'
    '윤사랑은 열심히 고개를 끄덕이며 동의를 표했다.'

    hide Yun_Sad with None
    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    show Yun_fallinlove at yun_one_jump_bs with None
    voice Yunsarang_123
    yun '"저, 정말로 발이 꼬였을 뿐이에요."'

    hide Yun_fallinlove with None
    show Yun_Sad at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_124
    yun '"엘리스 씨가 의심하는 것도 이상한 일은 아니에요..."'

    hide Yun_Sad with None
    show Yun_tear at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_125
    yun '"바닥이 그렇게까지 미끄러웠던 것도 아니고, 무언가 놓여있던 것도 아니니까."'
    '겨우 울음을 그친 게 무색하게, 윤사랑은 다시 눈물을 흘리고 있었다.'
    voice Yunsarang_126
    yun '"제가 바보 같은 탓에 이런 일이..."'
    player '"바보 같지 않아! 나도 종종 이유 없이 넘어지니까?"'

    hide Yun_tear with None
    show Yun_pout at yun_standsize_bs with Dissolve(.5 ,alhpa = True)
    voice Yunsarang_127
    yun '"그렇지만... 하필이면 들고 있던 물도 엘리스 씨에게 끼얹어버려서..."'
    player '"운이 나빴을 뿐이야."'
    '하나하나 맞받아치지 않으면, 윤사랑은 금방이라도 굴을 파고 들어갈 것 같았다.'
    player '"너는 분명 실수에 대한 사과를 했어. 그걸 받아주지 않고 몰아간 엘리스 쪽이 나빠."'

    hide Yun_pout with None
    show Yun_panic at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_128
    yun '"에, 엘리스 씨는 나쁘지 않아요..."'
    player '"윤사랑, 이 상황에서 너는 피해자야. 엘리스를 원망해도 된다고?"'

    hide Yun_panic with None
    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    show Yun_fallinlove at yun_one_jump_bs with None
    voice Yunsarang_129
    yun '"그렇게 단정 지어서는 안돼요, 주인님... 혹시라도 엘리스 씨 말대로 제가 일부로 그런 거면 어쩌려고요?"'
    '윤사랑의 발언은 여러모로 이해가 어려웠다.'
    '자책을 하는 건 그렇다 쳐도, 왜 엘리스를 감싸는 듯한 언행을 하는 거지?'
    '가지를 뻗어나가던 의문은 하나의 생각에 도달한다.'
    '엘리스에게 협박이라도 받고 있나?'
    '모두의 예쁜 외형에 속아 깜빡한 것이 있다.'
    '여기는 단 한 명을 제외한 모두가 죄인이라는 것.'
    '엘리스가 비교적 착해 보이는 윤사랑을 협박하는 것도 무리는 아니다.'
    player '"혹시... 엘리스가 너한테 뭐라도 했어?"'

    hide Yun_fallinlove with None
    show Yun_Sad at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    show Yun_Sad at yun_one_jump_bs with None
    voice Yunsarang_130
    yun '"네? 아, 아무것도 하지 않으셨어요! 저는 엘리스 씨의 화가 정당하다고 생각해서..."'
    voice Yunsarang_131
    yun '"엘리스 씨가 오해하도록 행동한 제가 나빠요."'
    player '"아니, 넌 잘못한 게 없다니까?"'

    hide Yun_Sad with None
    show Yun_tear at yun_standsize_bs with  Dissolve(.5 ,alpha = True)
    show Yun_tear at yun_one_jump_bs with None
    voice Yunsarang_132
    yun '"하... 하지만..."'
    '나는 입을 꾹 다물고, 윤사랑이 횡설수설 늘여놓는 이야기를 들었다.'
    '어디선가 들어본 적 있는 패턴인데...'
    player '"아."'
    '윤사랑의 말에서 느껴지던 이상함을 깨달았다.'
    '어떻게든 자기 탓을 하며, 상황을 무마시키려 하는 것...'
    '단순히 착한 아이 흉내를 내는 걸 수도 있지만, 전문가도 아니라서 확신할 수 없다.'
    '알 수 있는 건 윤사랑의 의견은 객관성이 없다는 것 정도?'

    hide Yun_tear with None
    show Yun_lookout at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_133
    yun '"저, 주인님..."'
    player '"응?"'

    hide Yun_lookout with None
    show Yun_Normal at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_134
    yun '"이, 이제 가서 정리해요..."'
    # voice Yunsarang_134
    # yun '"다 같이 청소하고 있었잖아요? 손이 비면 다들 곤란할 거예요."'

    hide Yun_Normal with None
    show Yun_pout at yun_standsize_ms with Dissolve(.5 ,alpha= True)
    voice Yunsarang_135
    yun '"무거운 걸 옮길 수 있는 건 엘리스 씨 밖에 없고..."'
    '이자벨과 스칼렛을 떠올렸다.'
    '누가 봐도 연약해 보이는 이자벨, 강해 보이는 외관과 달리 가장 약했던 스칼렛.'
    '평범해 보이는 엘리스가 셋 중 가장 강하다니... 혼자서 청소도구를 옮길 걸 생각하면 탄식이 절로 나왔다.'
    player '"꼭 가야 할까?"'

    hide Yun_pout with None
    show Yun_Laughter at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_136
    yun '"아... 쉬고 싶으신 거라면 제가 다른 메이드들에게 말해둘게요."'
    '윤사랑은 금방이라도 문을 열고 나가려 했다.'
    player '"그런 게 아니야."'
    player '"조금만 더 농땡이 피우다 가도 괜찮을걸?"'

    hide Yun_Laughter with None
    show Yun_pout at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_137
    yun '"그치만..."'
    '윤사랑은 무척이나 걱정스럽다는 표정을 지었다.'
    '혼자서 뒷정리를 할 엘리스를 떠올리는 걸까?'
    '언젠가 들었던 착한 아이 콤플렉스에 대해서 떠올린다.'
    '조금 정도는 화를 내도 괜찮을 텐데.'
    player '"아예 안 가겠다는 건 아니야. 조금만 늦게 가자는 거지."'

    hide Yun_pout with None
    show Yun_lookout at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_138
    yun '"으음..."'
    player '"너무 일찍 내려가면 스칼렛과 이자벨도 걱정할걸?"'

    hide Yun_lookout with None
    show Yun_lookout at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_139
    yun '"그렇다면..."'

    hide Yun_lookout with None
    show Yun_lookout at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    '윤사랑은 다시 내 침대 위에 앉았다.'

    hide Yun_lookout with None
    show Yun_Normal at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_140
    yun '"있죠, 주인님."'
    player '"응?"'

    hide Yun_Normal with None
    show Yun_pout at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_141
    yun '"아까도 그렇지만, 저는 실수가 많아요."'

    hide Yun_pout with None
    show Yun_Sad at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_142
    yun '"이번에는 이자벨 씨와 스칼렛 씨가 제 편을 들어줬지만, 같은 실수를 하면 두 분도 저를 의심할 거예요."'

    hide Yun_Sad with None
    show Yun_pout2 at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_143
    yun '"그때도 제 편을 들어주실 수 있으신가요?"'
    '윤사랑은 반짝이는 눈으로 나를 바라봤다.'

    menu :
        "당연하지":
            player '"물론이지. 너는 절대로 일부로 남에게 피해를 주는게 아니니까."'
            player '"같이 사과해 줄 테니까 너무 걱정하지 마."'
            pass
        "글쎄...":
            player '"미안, 당장 확신은 못할 것 같아."'

            hide Yun_pout2 with None
            show Yun_lookout at yun_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Yunsarang_144
            yun '"아..."'
            player '"그때의 상황에서 나름대로 합리적인 추론을 한 다음에."'
            player '"네가 무고하다면 네 편을 들어줄게."'

            hide Yun_lookout with None
            show Yun_huc at yun_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Yunsarang_145
            yun '"저, 저는 그걸로도 충분해요."'

            pass
    '적당히 휴식을 취했다는 생각이 들었다.'
    '붉어졌던 윤사랑의 눈도 어느 정도 안정이 된 것 같으니까, 슬슬 돌아가 볼까?'
    player '"이제 슬슬 내려갈까?"'

    hide Yun_huc
    hide Yun_pout2
    with None

    show Yun_Laughter at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_146
    yun '"저 혼자서 갈 테니까, 주인님은 좀 더 쉬세요!"'
    player '"어? 내가?"'

    hide Yun_Laughter with None
    show Yun_Normal at yun_standsize_bs with Dissolve(.5, alpha = True)
    voice Yunsarang_147
    yun '"청소는 원래 메이드의 일이잖아요."'

    hide Yun_Normal with None
    show Yun_Happy at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_148
    yun '"주인님은 많이 도와주셨으니까... 나머지는 저희끼리 알아서 할게요."'
    '윤사랑은 믿어달라는 듯, 웃으며 나를 바라봤다.'
    player '"괜찮겠어? 엘리스라던가..."'

    hide Yun_Happy with None
    show Yun_wink at yun_standsize_bs with Dissolve(.5, alpha = True)
    voice Yunsarang_149
    yun '"주인님에게 잔뜩 위로받았으니까 괜찮아요."'

    voice Yunsarang_150
    yun '"차분히 대화하면, 엘리스 씨도 오해를 풀어주실 테니까..."'
    '음... 솔직히 말하자면 많이 걱정되지만, 저렇게까지 말하는 걸 무시할 수는 없겠지?'
    player '"알겠어. 힘든 일 있으면 부르러 와?"'

    hide Yun_wink with None
    show Yun_huc at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_151
    yun '"네! 걱정 마세요!"'
    '활짝 웃는 얼굴은 내 안에 있던 어둠마저도 사라지게 하는 것 같았다.'
    '여전히 말로 표현 못 할 찜찜함이 남아있지만...'

    scene bg black with Dissolve(2.0 ,alpha = True)
    stop music fadeout 2.0
    $ renpy.pause(1.0, hard = True)

    jump D_1_Dinner

    pause

label D_1_Dinner:
    scene bg Myroom with Dissolve(1.5, alpha = True)
    play music comic_sound fadein 1.5
    show Hyeyeon_Laughter at admin_ms_Lout_to_L with Dissolve(.5 ,alpha = True)
    $ renpy.pause(1.1, hard = True)
    admin '"곤란한 일이 있었나 봐 주인님?"'
    player '"으악!!"' with hpunch
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(.5 ,alpha = True)
    admin '"하핫, 놀랐어?"'
    player '"다, 당연한 건 아니야?"'
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Normal at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    admin '"다 지켜보고 있었어. 벌써부터 싸우다니, 정말 곤란하다니까~"'
    admin '"그래도 주인님이 잘 중재해 줘서 다행이야."'
    hide Hyeyeon_Normal with None
    show Hyeyeon_Happy at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    admin '"서로 죽이기라도 하면 일이 귀찮아지거든."'
    player '"뭐라고?"'
    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    admin '"방금 건 농담~"'
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Normal at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    admin '"메이드끼리 싸울 일이 생기면, 방금처럼 잘 중재해 줘."'
    hide Hyeyeon_Normal with None
    show Hyeyeon_Absurd at admin_standsize_ms with Dissolve(.5 ,alpha=  True)
    admin '"어제 말했던 것처럼, 네 명 중 셋은 끔찍한 범죄자라서 상대를 죽이려 들지도 모르거든!"'
    player '"그, 말리려다가 내가 죽으면...?"'
    hide Hyeyeon_Absurd with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5 ,alpha= True)
    admin '"저택의 규칙상 메이드는 주인님을 해치지 못하니까 괜찮아!"'
    player '"그런 건 미리 말해주면 안 돼?"'
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Happy at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    admin '"하하, 싫어. 바보 같은 주인님 표정 보는게 재밌는걸!"'
    admin '"식당 청소는 다 끝났으니까 이제 내려와."'
    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    show Hyeyeon_Laughter at admin_one_jump with None
    admin '"밥 먹을 시간이야!"'

    hide Hyeyeon_Laughter with Dissolve(.5 ,alpha= True)
    play sound teleport_snap
    # play sound 순간이동
    '관리자는 눈 깜짝할 사이에 눈앞에서 사라졌다.'
    '나타났다, 사라졌다... 다 순식간이라 어이가 없을 지경이다.'
    '보고 있었으면 진작에 좀 말려주던가!'
    scene bg black with Dissolve(2.0, alpha = True)
    stop music fadeout 2.0
    $ renpy.pause(1.0, hard = True)
    play music Elicetheme fadein 1.0
    play sound FootStep2
    scene bg BG_Livingroom with Dissolve(1.0 ,alpha = True)
    show Elice_Surprised at elice_standsize_ms_L with Dissolve(.5 ,alpha = True)
    show Yun_lookout at yun_standsize_ms_R with Dissolve(.5 ,alpha = True)
    '식당에 가니, 아침보다 더 어색한 공기가 맴돌고 있었다.'
    '윤사랑이랑 엘리스 둘 다 식사 자리에 참여한 건 관리자의 압력 때문일까, 아니면 둘의 사이가 어느 정도 풀어져서일까...?'
    play sound Table
    '최대한 후자이길 바라며 식사를 시작했다.'
    '아침은 그래도 그럭저럭 견딜만했는데, 저녁 식사는 진짜 지옥이었다.'
    '분위기가 너무 우울해서 음식 맛도 제대로 느껴지지 않았다.'
    # play sound 의자에서 일어나는 사운드
    '식사를 끝마친 메이드는 그릇을 치우고 자리를 떠난다.'
    '가만히 있으면 다들 자기 방으로 갈 것 같은데...?'

    hide Elice_Surprised
    hide Yun_lookout
    with Dissolve(.5 ,alpha= True)
    # 마지막은 모두 밤으로 이동
    menu :
        "이자벨을 부른다.":
            jump Call_By_Isabel
            pass
        "스칼렛을 부른다.":
            $ s_D_1_Dinner = True
            jump Call_By_Scarlet
            pass
        "윤사랑을 부른다.":
            jump Call_By_Sarang
            pass
        "엘리스를 부른다.":
            $ e_D_1_Dinner = True
            jump Call_By_Elice
            pass

    pause

label Call_By_Isabel:
    show isabel_nodap at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    player '"저기, 이자벨!"'
    hide isabel_nodap with None
    show Elice_Angry at elice_standsize_ms_L with Dissolve(.5 ,alpha = True)
    show Scarlet_jjajeung at scarlet_standsize_ms_R with Dissolve(.5 ,alpha = True)
    show Yun_anxiety at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    '큰 목소리로 이자벨을 부르자 모두 나를 쳐다본다.'
    '윤사랑은 무언가 배신당한 것 같은 눈빛을 보내지만, 객관적인 상황 설명은 이자벨이 더 잘할 것 같았다.'
    '윤사랑과 엘리스가 잘 화해했나 궁금하기도 하고, 이자벨에 대해서 궁금하기도 하니까...'

    hide Elice_Angry
    hide Scarlet_jjajeung
    hide Yun_anxiety
    with Dissolve(.5 ,alpha = True)
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_080
    isabel '"무슨 일이시죠?"'
    player '"잠시 이야기할 수 있을까?"'
    '이자벨은 의아한 표정을 짓다 곧 고개를 끄덕였다.'

    hide Isabel_pout with None
    show Isabel_nodap at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_081
    isabel '"좋아요."'
    player '"어디서 대화할까, 내 방?"'

    hide Isabel_nodap with None
    show Isabel_lookout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_082
    isabel '"음..."'

    hide Isabel_lookout with None
    show Isabel_nodap at  isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_083
    isabel '"제 방에서 하도록 하죠. 이동을 최소화하고 싶거든요."'
    player '"좋아. 넌 몸이 약하다고 했으니..."'
    '대화를 다 나눈 후에 방에서 휴식을 취할 생각이구나.'
    '납득을 하며, 이자벨과 같이 이자벨의 방으로 갔다.'

    hide Isabel_nodap with Dissolve(.5 ,alpha = True)
    scene bg black with Dissolve(2.0 ,alpha = True)
    stop music fadeout 2.0
    $ renpy.pause(1.0, hard = True)
    play music Isabel_2 fadein 2.0
    play sound FootStep2
    scene bg BG_Maidroom with Dissolve(1.5 ,alpha = True) # c추후 메이드의 방으로 수정
    show isabel_nodap at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_084
    isabel '"조금 어질러 있지만, 적당히 이해하세요."'
    player '"어? 응..."'
    '이자벨의 방은 묘하게 병원 냄새가 났다.'
    '알콜 냄새 속에 섞여있는 꽃향기는 창문 너머로 들어온 것 같았다.'
    player '"내 방이랑 크게 다른 건 없네."'

    hide isabel_nodap with None
    show Isabel_pout at isabel_standsize_ms with Dissolve(.5 ,alpha= True)
    voice Isabel_085
    isabel '"그래요? 당신은 주인이니 더 큰 방을 쓰거나 하지 않나요?"'
    player '"...그러게. 왜 내 방은 작은 걸까."'

    hide Isabel_pout with None
    show Isabel_nodap at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_086
    isabel '"말뿐인 주인 취급이라는 거겠죠."'

    hide Isabel_nodap with None
    show isabel_normal at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_087
    isabel '"당신도 알고 있잖아요? 관리자는 당신에게 주인님이라고 부를 뿐, 그 어느 권한도 주지 않았다는걸."'

    hide isabel_normal with None
    show Isabel_lookout at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_088
    isabel '"메이드들과 다른 점은... 노동하지 않을 자유일까요?"'
    player '"아, 그건 확실히 특별 대우일려나."'
    '3일이 지나면 나갈 수 있다는 사실을 아는 나와 달리, 정보가 없는 이자벨은 나름대로 여러 가지 추론을 세운 것 같았다.'
    '대화에 응한 것도 나에게서 정보를 얻기 위한 거겠지?'

    hide Isabel_lookout with None
    show Isabel_Laughter at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_089
    isabel '"당신과 대화할 생각이 있었는데, 먼저 제안해 주셔서 다행이에요."'

    hide Isabel_Laughter with None
    show Isabel_lookout at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_090
    isabel '"엘리스 씨나, 윤사랑 씨에게 먼저 말을 걸 거라 생각했는데..."'
    '이자벨이 나에게 뭔가를 원하는 것처럼, 나도 이자벨에게 원하는게 있다.'
    player '"그 둘에 관해서 물어보고 싶은 게 있어."'

    hide Isabel_lookout with None
    show Isabel_nodap at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_091
    isabel '"음...제게요?"'
    player '"응. 당사자들 이야기도 중요하지만, 제3자의 시선이 더 궁금했거든."'

    hide Isabel_nodap with None
    show Isabel_Normal at isabel_standsize_ms with Dissolve(.5,alpha = True)
    voice Isabel_092
    isabel '"제가 대답해 드릴 수 있는 거라면 뭐든 해드릴게요."'
    player '"윤사랑이랑 엘리스는 잘 화해했어? 저녁 식사 때의 분위기가 묘하게 이상해서..."'
    '이자벨은 작게 한숨을 내쉬었다.'

    hide Isabel_Normal with None
    show Isabel_soAngry at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_093
    isabel '"화해 같은 건 하지 않았지만, 다시 싸우는 일은 없을 거예요."'
    player '"어째서?"'

    hide Isabel_soAngry with None
    show Isabel_pout at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_094
    isabel '"둘은 싸웠던 걸 없는 일 취급하기로 결정한 듯, 식당에 돌아와서는 아무 말 없이 해야 할 일을 끝냈어요."'

    voice Isabel_095
    isabel '"거기서 저랑 스칼렛이 더 중재할 것도 없었고..."'

    hide Isabel_pout with None
    show Isabel_lookout at isabel_standsize_ms with Dissolve(.5 , alpha = True)
    player '"곧 저녁 시간이 되어서 나와 관리자가 왔다?"'

    hide Isabel_lookout with None
    show Isabel_nodap at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_096
    isabel '"네. 그게 전부예요."'
    player '"아하... 알려줘서  고마워."'

    hide Isabel_nodap with None
    show Isabel_Laughter at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_097
    isabel '"별말씀을요."'
    '나는 잠시 이자벨의 눈치를 봤다.'
    player '"나한테 묻고 싶은 게 있지 않아?"'

    hide Isabel_Laughter with None
    show Isabel_nodap at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_098
    isabel '"네, 저는 [player_name] 씨가 저와 같은 곳 출신이라고 생각하고 있어요."'
    player '"응?"'

    hide Isabel_nodap with None
    show Isabel_pout at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_099
    isabel '"스칼렛 씨는 누가 봐도 다른 세계의 존재지만, 메이드들끼리는 구분이 어렵단 말이죠."'
    voice Isabel_100
    isabel '"기억을 전부 잃어버렸다는 윤사랑 씨라던가, 귀족처럼 행세하는 엘리스 씨라던가..."'

    hide Isabel_pout with None
    show Isabel_Sad at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_101
    isabel '"다들 용모도 화려하고, 머리색은 더 특이해서 국적이나 시대를 유추하는게 어려웠어요."'

    hide Isabel_Sad with None
    show Isabel_nodap at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_102
    isabel '"하지만 [player_name] 씨는 다른 두 분보다 알기 쉬워서 유추 정도는 할 수 있거든요."'
    voice Isabel_103
    isabel '"이건 제 추측이 맞는지 확인하는 질문이니까 평범하게 대답해 주세요."'
    player '"어...알겠어."'
    '골든벨이라도 나가는 것 같은 긴장감.'

    hide Isabel_nodap with None
    show Isabel_nodap at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_104
    isabel '"살고 계시는 지역이 어디인가요?"'
    player '"대한민국 서울."'

    hide Isabel_nodap with None
    show Isabel_Normal at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_105
    isabel'"한글을 만든 사람은?"'
    player '"세종대왕."'

    hide Isabel_Normal with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5 ,alpha= True)
    voice Isabel_106
    isabel '"나의 죽음을..."'                # 스탠딩 이상
    player '"적들에게 알리지 마라!"'

    hide Isabel_pout with None
    show Isabel_stare at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_107
    isabel '"Fe는 뭘까요?"'
    player '"철!"'

    hide Isabel_stare with None
    show Isabel_Laughter at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_108
    isabel '"잘 대답하고 계세요."'

    hide Isabel_Laughter with None
    show Isabel_nodap at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_109
    isabel '"경찰서 번호는?"'
    player '"112"'

    hide Isabel_nodap with None
    show Isabel_lookout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_110
    isabel '"마지막으로 좋아하는 김치는?"'      # 스탠딩 이상
    player '"난 평범하게 배추김치."'

    hide Isabel_lookout with None
    show Isabel_Happy at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_111
    isabel '"저는 파김치요. 병원 식단으로 나오는 일이 좀처럼 없거든요."'
    '이세계 물에서 흥얼거리는 노래로 동향 사람을 알아보는 건 자주 봤지만...'
    '김치로 알아보는 건 또 처음이다.'
    player '"이자벨도 한국 사람이었구나."'

    hide Isabel_Happy with None
    show Isabel_lookout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_112
    isabel '"네, 이름 때문에 아니라고 생각하셨나 보군요."'
    player '"아, 응. 윤사랑은 한국 사람일 수 있다고 생각했지만 너는 아닐 거라고 생각했어."'

    hide Isabel_lookout with None
    show Isabel_stare at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_113
    isabel '"..."'
    player '"그... 미안?"'

    hide Isabel_stare with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_114
    isabel '"됐어요. 당신도 한국 사람이라면 말이 좀 통하겠네요."'
    player '"응. 어쩐지 이자벨이랑 대화하는게 좀 편하더라니..."'

    hide Isabel_pout with None
    show Isabel_nodap at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_115
    isabel '"여기에 끌려온 사람이 어떤 사람들인지 제대로 파악해야, 어떻게 나갈 수 있는지도 알 수 있을 거예요."'

    hide Isabel_nodap with None
    show Isabel_lookout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_116
    isabel '"같은 한국인인 [player_name] 씨가 도와주셨으면 하는데... 어떠신가요?"'

    menu:
        "나는 좋아":
            player '"좋아. 얼마든지 부탁하라고."'
            hide Isabel_lookout with None
            show Isabel_Happy at isabel_standsize_bs with Dissolve(.5 ,alpha = True)    # 스탠딩 이상
            '이자벨은 미소로 답했다.'
            # 선택지 탈출!
            pass
        "당장 결정하기에는 좀...":
            player '"음... 지금 당장 결정하기에는 좀 섣부른 것 같아."'
            hide Isabel_lookout with None
            show Isabel_heung at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Isabel_117
            isabel '"네... 알겠어요."'
            '이자벨은 더 이상 대화를 잇지 않고 방 문을 열었다.'
            player '"응?"'

            hide Isabel_heung with None
            show Isabel_stare at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Isabel_118
            isabel '"대화가 끝났으니 나가시라는 거예요."'
            player '"이렇게 갑자기?"'

            hide Isabel_stare with None
            show Isabel_soAngry at isabel_standsize_bs with Dissolve(.5 ,alpha = True) # 스탠딩 이상
            voice Isabel_119
            isabel '"네. 저는 피곤하니까 이제 그만 쉬려고요. 늦은 밤 수고하셨어요."'
            '방에서 쫓겨나듯 나온 나는 내 방으로 돌아갔다.'
            # 밤으로 이동
            jump D_1_Night
            pass
    hide Isabel_Happy with None
    hide Isabel_soAngry with None
    show Isabel_nodap at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_120
    isabel'"윤사랑 씨가 저희와 같은 곳 출신이 아닐지 추측하고 있어요."'
    hide Isabel_nodap with None
    show Isabel_lookout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_121
    isabel '"마냥 상냥해 보이셔도, 경계가 심하신 분이니 [player_name] 씨가 물어봐 주셨으면 좋겠어요."'
    '내가 아는 윤사랑과 메이드들이 아는 윤사랑은 좀 다른 것 같았다.'
    '사람이 항상 모두에게 같은 태도를 보이는 건 아니지만...'
    player '"알겠어. 기회를 봐서 윤사랑에게 물어볼게."'

    hide Isabel_lookout with None
    show Isabel_Laughter at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_122
    isabel '"네.... 이제 슬슬 돌아가 주실 수 있나요?"'
    '그리 부탁하는 이자벨의 얼굴에는 피곤이 가득했다.'
    player '"나는 내 방으로 돌아갈 테니까, 편히 쉬어."'

    hide Isabel_Laughter with None
    show Isabel_Happy at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_123
    isabel '"고마워요. 내일 아침에 봐요."'
    player '"응, 내일 식당에서 보자."'
    '이자벨의 배웅을 받으며 방 밖으로 나왔다.'
    '시간이 늦었으니 방으로 돌아가야지.'
    # 밤으로 이동
    jump D_1_Night

    pause
    return

label Call_By_Scarlet:
    show Scarlet_nonSad at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    player '"이봐, 스칼렛!"'
    hide Scarlet_nonSad with Dissolve(.5 ,alpha = True)
    show Elice_Angry at elice_standsize_ms_L with Dissolve(.5 ,alpha = True)
    show Isabel_nodap at isabel_standsize_ms_R with Dissolve(.5 ,alpha = True)
    show Yun_anxiety at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    '큰 목소리로 스칼렛을 부르자 모두 나를 쳐다본다.'
    '윤사랑은 무언가 배신당한 것 같은 눈빛을 보내지만, 둘이 알아서 잘 해결 했을 거라고 믿는다.'
    '스칼렛은 여러모로 특이한 사람이니까, 좀 더 궁금하기도 하고.'
    hide Elice_Angry
    hide Isabel_nodap
    hide Yun_anxiety
    with Dissolve(.5 ,alpha = True)

    show Scarlet_heung at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_96
    scarlet '"무슨 일이지?"'
    player '"잠시 이야기하고 싶어서. 괜찮을까?"'
    '스칼렛은 잠시 고민을 하더니 순순히 고개를 끄덕였다.'

    hide Scarlet_heung with None
    show Scarlet_Happy at scarlet_standsize_bs with Dissolve(.5)
    show Scarlet_Happy at scarlet_one_jump_bs with None
    play sound jump1
    voice Scarlet_97
    scarlet '"영광으로 알거라! 이 스칼렛 아나스타샤님께서 기꺼이 네게 시간을 내어주는 거니까!"'
    player '"황송해 죽겠네요."'
    player '"어디서 이야기할까, 내 방?"'

    hide Scarlet_Happy with None
    show Scarlet_lookout at scarlet_standsize_bs with Dissolve(.5,alpha = True)
    voice Scarlet_99
    scarlet '"...아니, 정원으로 나가지. 그쪽에 볼일이 있는 참이니까."'
    player '"알겠어."'
    '스칼렛과 같이 정원으로 나갔다.'

    hide Scarlet_lookout with Dissolve(.5 ,alpha = True)
    scene bg black with Dissolve(2.0 , alpha = True)
    stop music fadeout 2.0
    $ renpy.pause(1.0, hard = True)
    play music emotional_2 fadein 2.0
    play sound Footstep_flower
    scene bg BG_Garden_Night with Dissolve(1.0 ,alpha =True)
    show Scarlet_jjajeung at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    '스칼렛은 정원으로 나올 때까지 아무런 말이 없었다.'
    '얘기할 때 늘 우렁차게 외쳐서, 평소에도 시끄러운 줄 알았는데 조용한 모습은 뭔가 색달랐다.'
    '뭐... 이런 이야기를 할 만큼 친한 사이는 아니지만.'
    '도착한 장소는 정원의 벤치였다.'
    '먼저 앉은 스칼렛은 나에게도 앉으라고 눈짓했다.'

    # play sound 자리에 앉는 소리 추가
    player '"으쌰."'
    '어색함에 입으로 효과음을 낸 나는 자리에 앉았다.'

    hide Scarlet_jjajeung with None
    show Scarlet_lookout at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_100
    scarlet '"그래서, 무슨 용건으로 이 몸을 부른 거지?"'
    player '"으응... 그게."'
    player '"그냥 대화를 해보고 싶어서."'

    hide Scarlet_lookout with None
    show Scarlet_panic at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_101
    scarlet '"하아?"'
    player '"다른 애들이랑은 어느 정도 대화를 해본 것 같은데, 너는 여전히 잘 모르겠어서..."'
    player '"위대한 그분이라든지, 여기에서 뭘 했는지, 무엇이라도 좋으니 들어보고 싶어."'

    hide Scarlet_panic with None
    show Scarlet_pout at scarlet_standsize_bs with Dissolve(.5)

    '다소 어이가 없다는 표정을 짓던 스칼렛은 곰곰이 생각하다 대답했다.'
    hide Scarlet_pout with None
    show Scarlet_stare at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_102
    scarlet '"이 몸을 탐문하겠다?"'
    player '"그런 게 아니야!"'

    hide Scarlet_stare with None
    show Scarlet_nonSad at scarlet_standsize_bs with Dissolve(.5, alpha = True)
    voice Scarlet_103
    scarlet '"농담이다. 네 녀석이 그런 걸 할 정도로 똑똑해 보이진 않으니..."'
    player '"왜 다들 나를 바보 취급 하는 거야..."'
    '조금 억울해진다.'

    hide Scarlet_nonSad with None
    show Scarlet_lookout at scarlet_standsize_bs with Dissolve(.5, alpha = True)
    voice Scarlet_104
    scarlet '"그렇게까지 표정에 모든 게 드러나는데, 어쩔 수 없잖아?"'
    player '"응? 그런 걸로 치면 나보다 스칼렛이 더..."'

    hide Scarlet_lookout with None
    show Scarlet_Angry at scarlet_standsize_bs with Dissolve(.5 , alpha = True)
    voice Scarlet_105
    scarlet '"...무슨 소리지?"'
    player '"아, 아무 것도 아니야! 그보다 이야기해 줄 거야?"'
    '아침에 부끄러워하던 스칼렛이 떠올랐지만, 이건 본인에게 말하면 안 된다는 생각이 들었다.'

    hide Scarlet_Angry with None
    show Scarlet_lookout at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_106
    scarlet '"크흠, 못해줄 것도 없지. 네놈은 그분의 신도가 될 자격도 있으니까 말이야."'
    player '"에, 진짜?"'
    '무슨 뜻인지는 모르겠지만... 스칼렛 시점에서는 칭찬이 아닐까?'

    hide Scarlet_lookout with None
    show Scarlet_nonSad at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_107
    scarlet '"그래. 아직은 부족하지만, 갈고닦으면 훌륭해지겠지."'
    player '"그거 참 좋은 소식이네."'

    stop music fadeout 2.0
    hide Scarlet_nonSad with Dissolve(2.0)
    play music emotional fadein 3.0
    '밤하늘 아래, 주변에 파란 장미가 가득한 정원에서 스칼렛은 이야기를 시작했다.'
    # $renpy.pause(1.0)
    '온통 푸르른 이곳에서 혼자 붉은 스칼렛은 무척이나 눈에 띄었다.'

    show Scarlet_pout at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_108
    scarlet '"나 스칼렛 아나스타샤는 그분의 가장 충실한 신도로써, 다른 신도들을 이끄는 역할을 맡고 있었지."'
    player '"이른 바 \'교주\'라는 거구나?"'

    hide Scarlet_pout with None
    show Scarlet_lookout at scarlet_standsize_bs with Dissolve( .5 ,alpha = True)
    voice Scarlet_109
    scarlet'"그래, 그분의 뜻을 따르며 다른 이들에게도 전파하는 것이 이 몸의 역할이지만..."'

    hide Scarlet_lookout with None
    show Scarlet_Sad at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_110
    scarlet '"다른 이들을 중재하는 것 역시 나의 역할. 교단의 대소사를 결정하는 것 역시 나의 역할인데, 이런 곳에 있으면 안 되는데..."'
    '드물게 보는 스칼렛의 약한 모습에 조금 놀랐다.'
    '무슨 일이 있어도, \'이 몸은 이 정도에 굴하지 않아!\'라고 이겨낼 줄 알았는데.'
    '책임져야 할 사람이 있어서 그런가, 스칼렛은 조금 초조해 보였다.'
    player '"걱정되는 거야?"'

    hide Scarlet_Sad with None
    show Scarlet_stare at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_112
    scarlet '"뭐가."'
    player '"그... 재단 사람들이라던가, 연락이 안 되는 신?"'

    hide Scarlet_stare with None
    show Scarlet_nonSad at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_113
    scarlet '"아, 네 말대로다. 내가 그들을 제대로 이끌어야 하는데..."'

    hide Scarlet_nonSad with None
    show Scarlet_Sad at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_114
    scarlet '"위대하신 그분의 뜻을 제대로 이행하고 있을지 걱정되어서 밥이 목구멍으로 넘어가지 않을 지경이야."'
    player '"그런 것치고는 잘 먹었는데?"'
    hide Scarlet_Sad with None
    show Scarlet_contempt at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_115
    scarlet '"..."'

    voice Scarlet_116
    scarlet '"뭐라고 말했지?"'

    player '"그, 아무것도 아니야."'
    '스칼렛은 다리를 의자 위로 올려서 끌어안았다.'
    hide Scarlet_contempt with None
    show Scarlet_Sad at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_117
    scarlet '"네 녀석은 하나도 걱정되지 않냐?"'
    player '"응?"'

    voice Scarlet_118
    scarlet '"이곳에 오기 전, 놓고 온 것이 있을 것 아닌가."'
    voice Scarlet_119
    scarlet '"가족이나, 동료... 뭐 그런 것."'
    hide Scarlet_Sad with None
    '그리 말하는 스칼렛은 밤하늘 위를 올려다보았다.'
    show BG_Garden_Night_Sky at Scene_bs_to_top with Dissolve(1.0)
    $renpy.pause(3.0, hard= True)
    '별이 가득한 밤하늘은 무척이나 낯설었다.\n'
    hide BG_Garden_Night_Sky with Dissolve(1.0)
    extend'스칼렛이 보는 건 밤하늘이 아닌 것 같았지만.'
    player '"부모님이 좀 보고 싶기는 해."'
    player '"집에서 좀 사랑받는 자식인지라... 갑자기 사라져서 많이 놀라셨을 텐데."'
    '나의 고민과 걱정은 스칼렛과 비교하면 가벼워질 수밖에 없다.'
    '나는 3일 후면 원래 세계로 돌아갈 수 있다는 말을 들었기 때문에, 이제는 슬슬 여행 왔다 생각하고 있지만...'
    '스칼렛은 언제 돌아갈지, 돌아갈 수 있는 방법이 있기는 한 것인지 의문인 상황'
    '방법을 알고 있음에도 말하지 않고 위로를 하는 건 기만이 아닐까 생각한다.'
    show Scarlet_displease at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_120
    scarlet '"전혀 모르는 것이 가득한 곳에 온 것은 오랜만인데..."'
    player '"응? 무슨 뜻이야?"'
    hide Scarlet_displease with None
    show Scarlet_inflate at scarlet_standsize_bs with Dissolve(.5 ,alpha= True)
    voice Scarlet_121
    scarlet '"...인간에게 굳이 알려줄 필요 없지."'
    menu:
        "부디 알려주세요. 위대한 스칼렛 님!":
            player '"제발, 부디 자비를 베풀어 알려주시지 않겠습니까, 스칼렛님?"'
            player '"말을 하다가 관두는 건 사형감이라고!"'
            hide Scarlet_inflate with None
            show Scarlet_lookout at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Scarlet_122
            scarlet '"음... 네 녀석 나라의 법인가, 그건?"'
            player '"응!"'

            voice Scarlet_123
            scarlet '"이 몸이 방황했던 시기의 이야기다. 재미없는, 시시하기만 할 뿐인 이야기지."'

            hide Scarlet_lookout with None
            show Scarlet_nonSad at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Scarlet_124
            scarlet '"이 몸은 자유를 사랑하는 몸으로 이곳저곳 떠돌다가 위대한 그분의 뜻을 전파하기 위해 한곳에 정착했다."'

            hide Scarlet_nonSad with None
            show Scarlet_pout at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Scarlet_125
            scarlet '"설명은 이 정도면 충분하겠지?"'
            '전혀 충분하지 않았지만 나는 그냥 고개를 끄덕였다.'

            hide Scarlet_pout with Dissolve(.5 ,alpha = True)
            # 선택지 탈출
            pass
        "제발 알려줘라!":
            player '"제발 알려줘라! 궁금하단 말이야."'
            hide Scarlet_inflate with None
            show Scarlet_pout at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Scarlet_126
            scarlet '"음... 별 재미없는 이야기다."'

            hide Scarlet_pout with None
            show Scarlet_lookout at scarlet_standsize_bs with Dissolve(.5 ,alpha =True)
            voice Scarlet_127
            scarlet '"이 몸은 과거에 이곳저곳 떠돌아다녔다."'

            voice Scarlet_128
            scarlet '"그게 이야기의 전부지."'
            player '"으응... 그랬구나."'

            hide Scarlet_lookout with Dissolve(1.0)
            #선택지 탈출
            pass

    '분명 밤인데도, 그리 춥지 않다고 느껴졌다.'
    '이 섬의 계절은 어떻게 된 걸까? 봄치고는 따뜻하고, 여름치고는 살짝 춥고...'
    '놀기에는 딱 좋았지만, 달리 친구가 있는 것도 아니기 때문에 아쉬웠다.'
    '어두워져도 저택으로 돌아가는데 문제는 없지만, 슬슬 돌아가는게 좋을 것 같았다.'
    '밤하늘을 올려다보며 상념에 젖어있는 스칼렛에게 손을 내밀었다.'
    show Scarlet_nonSad at scarlet_standsize_bs with Dissolve(.5,alpha = True)
    voice Scarlet_129
    scarlet '"뭐지?"'

    '스칼렛은 내 손 위에 자신의 손을 겹친 후 물었다.'
    '일으켜 세워주겠다는 뜻이었는데... 졸지에 강아지 훈련한 기분이 되었다.'
    player '"이제 슬슬 저택으로 돌아가자고."'
    '손안의 온기는 무척이나 부드러웠다. 제대로 정신을 잡지 않으면 스칼렛의 머리를 잔뜩 쓰다듬을지도....'

    hide Scarlet_nonSad with None
    show Scarlet_lookout at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_130
    scarlet '"꽤나 재밌는 짓을 하는군."'

    # play sound 일어나는 소리 추가
    '자리에서 일어난 스칼렛은 그대로 손을 잡고 저택을 향해 걸었다.'

    play sound Footstep_flower
    '키가 큰 만큼 보폭도 크고, 성격 나쁜 만큼 걷는 속도도 빨라 겨우겨우 스칼렛을 쫓아간다.'

    scene bg black with Dissolve(2.0, alpha = True)
    stop music fadeout 2.0
    '별장에 들어오자 스칼렛은 언제 무슨 일이 있었냐는 표정으로 손을 놓고, 자기 방으로 향했다.'
    '나는 그런 스칼렛을 허망한 표정으로 바라보며 놓아주었다.'
    '최악이었던 첫인상과 달리, 어른스러운 느낌이 있는 것 같았다.'

    # 선택지 밤으로 이동
    jump D_1_Night

    pause

    return

label Call_By_Sarang:
    # 현재 작업 중인 부분
    play music Yunsarang_1 fadein 1.5
    player '"유, 윤사랑!"'
    '나도 모르게 더듬으며 그 이름을 외쳤다.'

    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    '모든 메이드의 시선이 나에게 모이지만, 이름을 불린 윤사랑은 유독 반짝이는 눈으로 나를 바라본다.'
    '분명 자기를 불러주길 기다리고 있었겠지.'

    hide Yun_fallinlove with None
    show Yun_Laughter at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_151
    yun '"네, 주인님!"'
    '윤사랑은 밝게 웃으며 나한테 뛰어왔다.'
    '이번에는 넘어지지 않을까 걱정했는데, 그 먼 거리에서 금방 나에게로 뛰어왔다.'

    hide Yun_Laughter with None
    show Yun_Normal at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_152
    yun '"무슨 일이신가요?"'
    player '"잠시 대화할 수 있나 싶어서."'

    hide Yun_Normal with None
    show Yun_huc at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_153
    yun '"좋아요! 주인님 방에 가있으면 될까요?"'
    '굳이 내방에서 대화를 나누나? 싶었지만 딱히 나쁜 것은 아니었기에 금방 수긍했다.'
    player '"응. 같이 가자."'

    hide Yun_huc with None
    scene bg black with Dissolve(.5 ,alpha= True)
    play sound footstep_couple
    scene bg BG_Corridor with Dissolve(1.5)
    '내 방으로 향하는 윤사랑의 표정에는 내내 미소가 가득했다.'
    '누가 보면 복권에 당첨이라도 된 사람처럼 헤벌쭉 한 미소를 이해하기는 어렵지만...'
    '존중하는 건 매우 쉬운 일이니, 그냥 언급하지 않고 걸었다.'

    play music Yunsarang_1
    scene bg Myroom with Dissolve(1.5 ,alpha = True)
    show Yun_Normal at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    player '"너 침대에 앉아, 나는 의자에 앉을 테니까."'
    '윤사랑이 뭐라 하기 전에 먼저 딱딱한 의자에 앉았다.'
    '요즘 사람들이 책상 앞에 앉아있는 시간이 늘어난 만큼 발전된 의자와 비교하면 정말 최악이다.'
    '하다못해 방석이라도 있으면 좋겠지만, 이 방에 의자는 이것 하나뿐이고, 방석을 본 기억은 없었다.'
    '나름 손님으로 윤사랑을 초대한지라 그나마 좋은 침대 자리는 윤사랑에게 양보했다.'

    hide Yun_Normal with None
    show Yun_huc at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_154
    yun '"저, 저를 부르신 이유가 뭔가요?"'
    player '"그냥 궁금한 게 있어서."'
    '윤사랑은 자신만만한 미소를 지으며 말했다.'

    hide Yun_huc with None
    show Yun_Laughter at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_155
    yun '"뭐든 제가 답해드릴 수 있는 것이라면, 말씀드릴게요!"'
    player '"음, 혹시 기억이 얼마나 있는지 물어볼 수 있을까?"'

    hide Yun_Laughter with None
    show Yun_lookout at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_156
    yun '"네?"'
    player '"나도 너에 대한 기억을 떠올려보고 싶어서 말이야. 뭐라도 이야기를 들으면 떠올릴 수 있지 않을까 싶어서 말이야..."'

    hide Yun_lookout with None
    show Yun_pout at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_157
    yun '"그건... 저를 위한 주인님의 배려일까요?"'
    player '"응. 혹시 부담스러워?"'

    hide Yun_pout with None
    show Yun_huc at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_158
    yun '"아뇨! 너무 기뻐요. 기억난 걸 전부 말해드리면 될까요?"'
    player '"나에 대한 것만 말해준다는 거지?"'

    hide Yun_huc with None
    show Yun_pout at yun_standsize_bs with Dissolve(.5 ,alpha  = True)
    voice Yunsarang_159
    yun '"아...네! 모든 걸 말하면 주인님이 제대로 못 주무실 것 같으니까요."'
    player '"짧은 시간 동안 많은 걸 떠올린 모양이네."'
    '윤사랑은 조금 붉어진 얼굴로 고개를 끄덕였다.'
    '나이가 어떻게 되는지 모르겠지만, 왠지 동생처럼 여린 느낌이 무척 귀여웠다.'

    hide Yun_pout with None
    show Yun_lookout at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_160
    yun '"우선 저의 기본적인 인적 사항 중... 말씀드리지 않았던 게 있죠?"'
    player '"아, 이름을 제외하면 아무것도 못 들었지?"'

    hide Yun_lookout with None
    show Yun_Normal at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_161
    yun '"네. 제 나이는 19살로 주인님과 동갑이에요!"'
    '역시 동갑이었구나...'
    hide Yun_Normal with None
    show Yun_Laughter at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_162
    yun '"고등학교에 재학 중이었고, 반에서 제일 운동을 잘하는 학생이었어요."'

    hide Yun_Laughter with None
    show Yun_Normal at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_163
    yun '"오늘처럼 무거운 물건을 옮길 일이 있거나, 병뚜껑 여는 일은 전부 저한테 맡겼죠."'
    player '"오... 대단한데?"'

    hide Yun_Normal with None
    show Yun_huc at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_164
    yun '"그, 고등학교에서 주인님을 봤었던 것 같거든요...?"'
    player '"응? 진짜? 나는 왜 모르겠지."'

    hide Yun_huc with None
    show Yun_panic at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_165
    yun '"그, 그건 저도 잘 모르겠어요."'

    hide Yun_panic with None
    show Yun_pout at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_166
    yun '"같은 반이 아니라서 그런 거 아닐까요? 주인님도 저처럼 기억이 온전치 않으신 것 같으니까..."'
    player '"아, 확실히. 나도 모든 걸 제대로 기억하고 있다고 확신할 수 없으니까."'

    hide Yun_pout with None
    show Yun_lookout at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_167
    yun '"모든 기억을 잃어버린 저와 다르게 주인님은 일부분만 없어지신 거니까..."'
    voice Yunsarang_168
    yun '"눈치채기 더 어려울 거라고 생각해요..."'
    player '"확실히... 네 말이 맞아."'
    player '"더 떠오르는 건 없어?"'

    stop music fadeout 5.0
    play music Yunsarang_2 fadein 5.0
    hide Yun_lookout with None
    show Yun_pout at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_169
    yun '"아, 저기... 이게 정확하지 않은 건데요..."'

    hide Yun_pout with None
    show Yun_huc at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_170
    yun '"같은 고등학교를 다니기 전부터, 조금 더 어린 시절부터 주인님을 알고 있었다는 느낌이..."'
    player '"응?"'

    hide Yun_huc with None
    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5 ,alpha= True)
    voice Yunsarang_171
    yun '"부, 부정확한 거라 말씀드릴지 말지 고민했던 거라 말하기가 부끄럽네요."'

    hide Yun_fallinlove with None
    show Yun_huc at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_172
    yun '"어떤 고등학교를 다녔고, 평소에는 뭘 하고 지냈는지 기억났어요!"'

    hide Yun_huc with None
    show Yun_lookout at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_173
    yun '"3년 동안 주인님과 같은 반을 한 적이 없는데, 가끔 인사를 하거나 했던 지라..."'

    hide Yun_lookout with None
    show Yun_huc at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_174
    yun '"혹시 그전부터 알았던 사이가 아닐까? 라고 생각해서...!"'
    player '"음..."'

    hide Yun_huc with Dissolve(.5 ,alpha = True)
    '잠시 동안 내 학교생활을 떠올려봤다.'
    '등굣길에 친구들과 만나서 대화를 하면서 가고, 수업에 참여하고, 쉬는 시간에 애들이랑 놀고...'
    '점심시간에는 최대한 빨리 급식을 입에 쑤셔 넣고, 친구들이랑 놀고...'
    '복도에서 아는 사람이랑 마주치면 인사를 주고받고...'
    '좁은 공간에서 만나는 사람이 너무 많아서, 그중에 윤사랑이 있었다고 해도 이상할 게 없을 것 같다.'
    '같은 중학교를 나와서 얼굴을 아는 사이지만, 이름을 까먹은 친구도 많으니...'
    '윤사랑도 그중 하나였던 것일까?'

    show Yun_Normal at yun_standsize_ms with  Dissolve(.5 ,alpha = True)
    '곰곰이 생각하며 윤사랑을 바라보았다.'
    '역시 내 기억 중 일부가 소실된 게 확실한 것 같았다.'
    '저렇게 귀여운 여자아이를 잊어버릴리 없잖아.'
    player '"확실히 일리는 있어. 오기 전의 일과 너에 대한 것 모두 잊어버린 걸까..."'

    hide Yun_Normal with None
    show Yun_Sad at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_175
    yun '"그건 조금 슬픈 이야기네요..."'
    voice Yunsarang_176
    yun '"저도 주인님을 제대로 기억하지 못하고 있지만... 완전히 잊혔다는게..."'
    player '"기, 기억할 수 있도록 노력할 테니까!"'
    '시무룩해하는 윤사랑을 달래기 위해서 나도 모르게 말이 튀어나왔다.'
    '누군가에게 잊히는 두려움 따위 모르지만...'
    '윤사랑이 순간적으로 지었던 표정은 무척이나 슬퍼 보였다.'
    '내가 사람이라면, 위로의 말은 꼭 뱉어야 한다는 생각이 들 정도로.'

    hide Yun_Sad with None
    show Yun_fallinlove at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_177
    yun '"말뿐이라도 감사해요 주인님."'
    player '"정말로 노력할 테니까...."'
    '반짝이는 시선이 부담스러워 눈을 돌리니, 시계가 보였다.'
    '벌써 시간이 이렇게 되었나? '
    '슬슬 자야 할 시간이니... 윤사랑을 돌려보내는게 좋을 것 같다.'
    player '"밤이 어두워졌으니까 슬슬 돌아가는게 좋지 않겠어?"'

    hide Yun_fallinlove with None
    show Yun_huc at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_178
    yun '"아, 시간이 벌써 이렇게 되었네요."'

    hide Yun_huc with None
    show Yun_Normal at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_179
    yun '"주인님과 함께 있으면 시간이 너무 빨리 흐르는 것 같아요."'
    '윤사랑은 방긋 웃으면서 자리에서 일어났다.'

    hide Yun_Normal with None
    show Yun_Laughter at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_180
    yun '"다른 메이드들이 아니라 저를 불러주셔서 감사해요 주인님."'

    hide Yun_Laughter with None
    show Yun_Happy at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_181
    yun '"무엇을 해야 할지 고민하고 있었거든요..."'
    player '"아, 그러고 보니까..."'

    hide Yun_Happy with None
    show Yun_lookout at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_182
    yun '"네?"'
    player '"엘리스랑은 잘 대화했어?"'
    player '"그... 걱정돼서 묻는 거야. 곤란하면 말 안 해도 괜찮아."'

    hide Yun_lookout with None
    show Yun_Normal at yun_standsize_ms with Dissolve(.5 ,alpha =True)
    voice Yunsarang_183
    yun '"아... 주인님이 걱정하실 만한 일은 없어요."'
    voice Yunsarang_184
    yun '"엘리스씨와 잘 대화했으니까."'
    player '"응, 잘 해결했다니 다행이다."'
    player '"걱정했으니까..."'

    hide Yun_Normal with None
    show Yun_cuty at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_185
    yun '"제 생각을 많이 하셨나 봐요 주인님."'
    hide Yun_cuty with None
    show Yun_huc at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_186
    yun '"저는 이만 자러 갈 테니 주인님도 편히 쉬세요!"'
    play sound DoorOpen2

    '그리 말한 윤사랑은 방 밖으로 나갔다.'
    '아는게 없는 사람에게 죄를 찾는 것도 우스운데...'
    # 선택지 밤으로 이동
    jump D_1_Night






    pause
    return

label Call_By_Elice:
    show Elice_Surprised at elice_standsize_ms with Dissolve(.5 ,alpha  = True)
    '엘리스를 부르려고 했지만, 금방 주방 안으로 들어갔다.'

    hide Elice_Surprised with Dissolve(.5 ,alpha = True)
    play sound FootStep1
    '계속 식당에 머물 것 같으니까, 모두가 보는 앞에서 부르지 않아도 괜찮으려나?'

    show Scarlet_heung at elice_standsize_ms_L with Dissolve(.5 ,alpha = True)
    show Isabel_nodap at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    show Yun_lookout at elice_standsize_ms with Dissolve(.5 ,alpha = True)
    '이자벨과 스칼렛은 식사가 끝나자마자 자리를 떠났다.'

    hide Scarlet_heung
    hide Isabel_nodap
    hide Yun_lookout
    with Dissolve(.5 ,alpha = True)

    play sound footstep_couple
    show Yun_Angry at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    '윤사랑은 잠시 나를 바라보다가 식당 밖으로 나왔다.'

    hide Yun_Angry with Dissolve(.5 ,alpha = True)
    '자리에 계속 앉아서 엘리스가 나오기를 기다렸다.'

    show Elice_Ignore at elice_standsize_ms with Dissolve(.5 ,alpha = True)
    play sound Bowl
    '엘리스는 쟁반에 두 개의 찻주전자와 찻잔을  가지고 나왔다.'
    player '"왜 찻잔이 두 개야?"'
    hide Elice_Ignore with None
    show Elice_Ignore_2 at elice_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Elice_123
    elice '"여러 가지 이유가 있지."'
    # play sound 쟁반 내려놓는 소리 이후 차를 따르는 소리
    $ renpy.pause(1.0)
    '쟁반을 내려놓은 엘리스는 찻잔에 차를 따른 후 나에게 건네주었다.'
    hide Elice_Ignore_2 with None
    show Elice_Gladness at elice_standsize_bs with Dissolve(.5, alpha = True)
    voice Elice_124
    elice '"남아있을 주인님을 위한 차 대접이라던가..."'
    '엘리스는 눈짓으로 차를 마셔보라 권했다.'
    '혀로 살짝 차의 온도를 가늠해 보니 마시기에 적당한 것 같았다.'
    # play sound 찻 소리 추가
    '들이마신 차는 꽤나 썼다. 원래 이런 맛인가?'
    '엘리스의 성의를 무시할 수는 없어서, 눈을 딱 감고 전부 마셔버렸다.'

    hide Elice_Gladness with None
    show Elice_Happy_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    '차를 다 마신 후 엘리스를 바라보니, 엘리스는 재밌다는 듯 미소를 짓고 있었다.'

    hide Elice_Happy_2 with None
    show Elice_Happy at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_125
    elice '"버리는 첫물을 담아두는 용도라던가."'

    hide Elice_Happy with None
    show Elice_Laughter at elice_standsize_bs with Dissolve(.5 ,alpha  = True)
    voice Elice_126
    elice '"첫물은 원래 쓴 법이지."'

    hide Elice_Laughter with None
    show Elice_Gladness at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_127
    elice '"마셔봐, 아까와는 다를 거야."'

    player '"아, 정말이네."'
    '첫 번째는 향도 맛도 너무 써서 먹기 힘들었다.'
    '두 번째 잔은 그리 쓰지도 않고, 향이 굉장히 강하지 않아서 마시기 좋았다.'
    '엘리스도 자리에 앉아 차를 마시기 시작했다.'
    '같은 찻잔으로, 같은 차를 마시는데도 분위기가 나랑은 무척 달랐다.'
    '기품 있는 모습이 꼭 영화 속에서 보는 공주님 같다고나 할까.'
    '엘리스가 어떤 환경에서 자랐는지 은연중 느껴지는 부분이다.'
    player '"엘리스는 차 마시는 모습이 꼭 공주님 같네."'

    hide Elice_Gladness with None
    show Elice_Coloration at elice_standsize_bs with Dissolve(.5, alpha = True)
    voice Elice_128
    elice '"하... 그놈의 공주."'

    hide Elice_Coloration with None
    show Elice_Coloration_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_129
    elice '"난 공주가 아니라 황제야. 나를 공주라 부르는 건 죽은 내 오라비의 편을 들었던 자들 뿐이지."'

    hide Elice_Coloration_2 with None
    show Elice_Angry at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_130
    elice '"내 기분을 거스르려고 하는게 아니라면 조심하는게 좋을 거야."'
    player '"아... 미안. 나는 그냥 칭찬으로 했던 말인데."'

    hide Elice_Angry with None
    show Elice_Angry_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_131
    elice '"네가 나에 대해서 알고 한 게 아니란 걸 아니까... 경고로 끝난 거야."'
    player '"응응, 고마워."'
    '엘리스가 사는 세상은 내가 있던 곳과 무척이나 다른 것 같다. '
    '황제라던가, 죽은 오라비라던가....'
    '영화나 소설 속에서만 보던 왕위 다툼 이야기겠지...?'
    '권력이 높은 사람은 죄를 짓기 쉬워지니까... 엘리스는 죄인이 맞을지도 모르겠다.'
    '차를 마시면서 엘리스의 눈치를 봤다. 기분이 그리 나쁘지는 않아 보이는데...'

    hide Elice_Angry_2 with None
    show Elice_Normal at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_132
    elice '"이제 슬슬 말하지그래?"'
    player '"으응?! 뭘?"'

    hide Elice_Normal with None
    show Elice_Normal_2 at elice_standsize_bs with Dissolve(.5 ,alhpa = True)
    voice Elice_133
    elice '"나한테 차를 얻어마시자고, 여기에 남아있던 건 아닐 거 아니야?"'

    hide Elice_Normal_2 with None
    show Elice_Gladness at elice_standsize_bs with Dissolve(.5 ,alhpa = True)
    voice Elice_134
    elice '"나한테 궁금한 게 있는거지?"'
    player '"아, 으응... 몇 가지 있는데, 알려줄 수 있어?"'

    hide Elice_Gladness with None
    show Elice_coldsmiley at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_135
    elice '"어떤 질문이냐에 따라 다르지."'

    hide Elice_coldsmiley with None
    show Elice_coldsmiley_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_136
    elice '"먼저 말해봐."'
    player '"혹시 여기 오기 전에 무슨 일이 있었는지 기억나?"'

    hide Elice_coldsmiley_2 with None
    show Elice_Strong at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_137
    elice '"...."'
    '엘리스의 표정은 갑자기 어두워졌다.'

    hide Elice_Strong with None
    show Elice_Contempt at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_138
    elice '"후..."'
    player '"그, 대답하기 곤란하다면 안 해도 괜찮아."'

    hide Elice_Contempt with None
    show Elice_Contempt_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_139
    elice '"말해줄 테니 기다려."'
    player '"넵."'
    hide Elice_Contempt_2 with None
    show Elice_Difficulty at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_140
    elice '"나는 제국을 다스리는 황제였지만, 그렇게까지 왕권이 강한 건 아니었어."'

    hide Elice_Difficulty with None
    show Elice_Difficulty_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_141
    elice '"오라비를 죽이고 그 자리를 얻었지만... 결국 반역자들 손에 끌어내려질 위기에 처했지."'
    player '"아..."'

    hide Elice_Difficulty_2 with None
    show Elice_Strong at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_142
    elice '"그들의 손을 피해서 죽기 살기로 도망쳤고, 정신을 차려보니 이곳에 와있더군."'

    hide Elice_Strong with None
    show Elice_Strong_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_143
    elice '"중간에 기억이 흐릿해서 내 발로 뛰어온 것이 맞는지 확신할 수 없지만..."'

    hide Elice_Strong_2 with None
    show Elice_Angry_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_144
    elice '"나를 찾으러 올 사람이 없다는 건 확실해."'
    player '"어, 어째서?"'

    hide Elice_Angry_2 with None
    show Elice_Angry at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_145
    elice '"나와 같이 오라비를 끌어내리는데 앞장섰던 이들이 다 돌아섰거든."'

    hide Elice_Angry with None
    show Elice_Difficulty_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_146
    elice '"그것도 내 동생의 편으로 말이지..."'
    player '"와..."'

    hide Elice_Difficulty_2 with None
    show Elice_Strong_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_147
    elice '"답지 않게 정에 휩쓸려 동생을 살려두는게 아니었는데 말이야."'

    hide Elice_Strong_2 with None
    show Elice_Angry_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_148
    elice '"인간이라는 생물이 쉽게 배신하고, 변한다는 걸 잊은 내 잘못이지..."'
    '그리 말하는 엘리스의 표정은 무척이나 지쳐 보였다.'
    '항상 당당하고 자신감으로 가득하던 엘리스라 생각했는데...'

    hide Elice_Angry_2 with None
    show Elice_Coloration at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    # voice Elice_149
    '엘리스는 얼굴을 감싸고 한숨을 내쉬었다.'

    hide Elice_Coloration with None
    show Elice_Coloration_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_149
    elice '"나도 많이 약해진 모양이야."'

    hide Elice_Coloration_2 with None
    show Elice_Difficulty at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_150
    elice '"너 같은 거한테 이런 이야기를 하다니..."'

    hide Elice_Difficulty with None
    show Elice_Difficulty_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_151
    elice '"너는 모르는 세계의 이야기일 텐데."'
    player '"응?"'

    hide Elice_Difficulty_2 with None
    show Elice_Surprised_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_152
    elice '"나처럼 권력과 가까이서 산 사람은, 쉽게 상대방을 파악할 수 있어."'

    hide Elice_Surprised_2 with None
    show Elice_coldsmiley at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_153
    elice '"네가 싸움과는 먼 곳에서, 사랑받으며 자랐다는 것 정도는 아주 쉽게 눈치챘지."'

    hide Elice_coldsmiley with None
    show Elice_coldsmiley_2 at elice_standsize_bs with Dissolve(.5 , alpha = True)
    voice Elice_154
    elice '"권력이니, 반역이니 하는 것 따위 다 처음 들어보는 이야기지?"'
    player '"들어는 봤지만..."'

    hide Elice_coldsmiley_2 with None
    show Elice_Normal_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_155
    elice '"누군가 겪은 이야기를 전해 들은 게 전부겠지."'

    $ renpy.pause(2.0)
    player '"응...."'

    hide Elice_Normal_2 with None
    show Elice_Surprised at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_156
    elice '"대화할 마음이 사라졌어."'

    # hide Elice_Surprised with None
    show Elice_Surprised at elice_standsize_ms with Dissolve(.5, alpha = True)
    play sound standup
    '엘리스는 가지고 왔었던 쟁반을 들고 자리에서 일어났다.'
    player '"저, 저기 엘리스!"'

    hide Elice_Surprised with None
    show Elice_Difficulty at elice_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Elice_157
    elice '"무슨 일이지?"'
    player '"윤사랑이랑 대화는 잘 했나 궁금해서..."'

    hide Elice_Difficulty with None
    show Elice_Surprised_2 at elice_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Elice_158
    elice '"아..."'

    hide Elice_Surprised_2 with None
    show Elice_Surprised at elice_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Elice_159
    elice '"뭐, 그쪽도 나와 생각하는게 비슷하더군."'

    show Elice_Surprised at elice_standsize_ms with Dissolve(.5 ,alhpa = True)
    voice Elice_160
    elice '"네가 걱정하는 일은 없을 테니 신경 꺼도 좋아."'
    player '"어, 응..."'
    hide Elice_Surprised with None
    '엘리스는 미련 없이 뒤돌아서서 주방 안으로 들어갔다.'
    '찻잔을 다 치우고 나온다 해도 나랑 대화하지는 않을 것 같았다.'
    player '"나도 돌아가야지..."'
    # 밤으로 이동
    jump D_1_Night
    pause
    return

label D_1_Night:
    scene bg black with Dissolve(2.0 , alpha = True)
    $renpy.pause(1.0)
    stop music fadeout 1.0
    play music Normal_a
    scene bg Myroom with Dissolve(1.5 ,alpha = True)
    '오늘 하루도 무척이나 힘들었던 것 같다.'
    '열심히 살았구나, 나...!'
    '누가 무고한 사람인지 정확히 알아내지는 않았지만 얼추 윤곽이 잡혀가는 느낌이 들었다.'
    '윤사랑과 엘리스가 싸우지만 않았어도 대화할 시간이 더 많았을 것 같은데...'
    '내일은 최대한 다들 싸우지 않고 지나갔으면 좋겠다.'
    '잘못하면 무서운 관경을 볼 수도 있으니까...'
    play sound DoorKnock
    $renpy.pause(1.5)
    '눈을 감고 잠들려던 그때, 누군가 방 문을 두드렸다.'
    player '"누구세요?"'
    stop music fadeout 2.0
    $renpy.pause(1.0)
    show Hyeyeon_Happy at admin_standsize_ms with Dissolve(1.0 ,alpha = True)
    play music comic
    admin '"다행이다, 아직 안 자고 있었구나 주인님!"'
    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    admin '"어떻게 깨울지 고민하고 있었는데~"'
    player '"깨우지 않는다는 선택지는 없는 거야?"'
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(.5 ,alpha = True)
    show Hyeyeon_Laughter at admin_one_jump_bs with None
    admin '"응! 오늘 안에 이 일기장을 전해줘야 했거든."'
    hide Hyeyeon_Laughter with Dissolve(1.5)
    show screen Mini_Scene(Book) with Dissolve(.5)
    # 일?기장
    player '"이건..."'
    # hide Hyeyeon_Laughter with None
    # show Hyeyeon_Normal at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    admin '"저택에 온 주인님들이 꼭 써야 하는 일기장이야."'
    # hide Hyeyeon_Normal with None
    # show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5 ,alpha  =True)
    admin '"오늘 있었던 일이나, 메이드들을 관찰하면서 겪었던 일에 관한 일을 편히 쓰면 된다고?"'
    # hide Hyeyeon_Laughter with None
    # show Hyeyeon_Happy at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    admin '"메이드들은 그 안의 글씨를 못 보니까, 뭐든지 솔직하게 적어도 괜찮아!"'
    hide screen Mini_Scene with Dissolve(.5)
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    admin '"예를 들면 주인님이 좋아하게 된 여자애라던가~"'
    player '"아직 없거든?"'
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Happy at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    show Hyeyeon_Happy at admin_two_jump with None
    admin '"아직이라는 건 곧 생긴다는 거구나~ 꺄~"'
    player '"소란 떨지 마..."'
    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5 ,alpha = True)
    admin '"후후, 나는 이만 가볼 테니까 일기 열심히 써야해?"'

    hide Hyeyeon_Laughter with None
    play sound teleport_snap
    '잘 가라는 인사를 하기도 전에 관리자는 눈앞에서 뿅하고 사라졌다.'
    '해야 할 일이 하나 생겼군...'
    '의자에 앉아 차분히 펜을 들고 일기를 쓴 후, 잠자리에 누웠다.'
    '하루를 충실히 보낸 탓인지, 금방 잠이 몰려왔다.'
    scene bg black with Dissolve(.5 ,alpha  = True)
    $ renpy.pause(1.0)
    stop music fadeout 2.0

    # 2일차 0.기상으로 이동
    jump D_2_WakeUp
    return

label Trash_Game_Scarlet:
    $ quick_menu = False
    # Trash_Game 진행 시 Scarlet의 방에 생성 됨.
    $ SetBoxPos(0, 150, 750, 950, 0, 650, 875, 950, 600, 650, 750, 950, 1320, 1650, 750, 950)
    $ SetSpacialObject(Scarlet_Special, Scarlet_Special_On, (840, 852), 1)
    $ SetTrash(Scarlet_Trash1, Scarlet_Trash2, Scarlet_Trash3)
    $ SetStanding(Scarlet_SD_Default, Scarlet_SD_Fail, Scarlet_SD_Success)
    if first_Game == False:
        $ InitGame(Scarlet_TrashGame_BG, 5.0)
    else:
        $ InitGame(Scarlet_TrashGame_BG, 10.0)
    scene bg CleaningRoom_Scarlet with Dissolve(2.0 ,alpha = True)
    show screen Cleaning_game_Tutorial with Dissolve(.5 ,alpha = True)
    # "이제 청소를 해 주세요"
    # play music MiniGame fadein 2.5

    $ res = StartGame()

    $ GameAsBG()
    with dissolve

    # call screen End_Window with Dissolve(.5 ,alpha = True)


    $ quick_menu = True
    return

label Trash_Game_Elice:
    $ quick_menu = False
    # Trash_Game 진행 시 Elice의 방에 생성 됨.
    $ SetBoxPos(0, 150, 810, 900, 0, 650, 810, 900, 600, 1650, 810, 900)
    $ SetSpacialObject(Elice_Special_1, Elice_Special_1_on, (1560, 130), 1, Elice_Special_2,Elice_Special_2_on, (1180, 550), 1
                    , Elice_Special_3, Elice_Special_3_on, (450, 600), 1, Elice_Special_4, Elice_Special_4_on, (1350, 270), 1
                    , Elice_Special_5, Elice_Special_5_on, (1450, 720), 1, Elice_Trash1, "", (400, 900), 1
                    , Elice_Trash1, "", (800, 920), 1, Elice_Trash1, "", (1650, 950), 1)


    $ SetTrash(Elice_Trash2, Elice_Trash3)
    $ SetStanding(Elice_SD_Default, Elice_SD_Fail, Elice_SD_Success)

    if first_Game == False:
        $ InitGame(Elice_TrashGame_BG, 5.0)
    else:
        $ InitGame(Elice_TrashGame_BG, 10.0)

    scene bg CleaningRoom_Elice with Dissolve(2.0 ,alpha = True)

    # $ GameAsBG()
    # with Dissolve(2. ,alpha = True)

    # $ InitGame("")
    show screen Cleaning_game_Tutorial with Dissolve(.5 ,alpha = True)

    # "이제 청소를 해 주세요"
    # play music MiniGame fadein 2.5

    $ res = StartGame()

    # scene bg CleaningRoom_Scarlet with Dissolve(2.0 ,alpha = True)

    $ GameAsBG()
    with dissolve

    # call screen End_Window with Dissolve(.5 ,alpha = True)
    # pause
    # 엘리스 청소 게임 시작
    $ quick_menu = True
    return

label Trash_Game_Isabel:
    $ quick_menu = False

    # Trash_Game 진행 시 Scarlet의 방에 생성 됨.
    $ SetBoxPos(0, 150, 750, 950,
    0, 650, 875, 950,
    600, 650, 750, 950,
    1320, 1650, 750, 950)
    $ SetSpacialObject()
    $ SetTrash(Isabel_Trash1, Isabel_Trash2, Isabel_Trash3, Isabel_Trash4, Isabel_Trash5 )
    $ SetStanding(Isabel_SD_Default, Isabel_SD_Fail, Isabel_SD_Success)

    if first_Game == False:
        $ InitGame(Isabel_TrashGame_BG, 5.0)
    else:
        $ InitGame(Isabel_TrashGame_BG, 10.0)

    scene bg CleaningRoom_Isabel with Dissolve(2.0 ,alpha = True)

    # $ InitGame("")
    show screen Cleaning_game_Tutorial with Dissolve(.5 ,alpha = True)

    # "이제 청소를 해 주세요"

    $ res = StartGame()

    $ GameAsBG()
    with dissolve

    # call screen End_Window with Dissolve(.5 ,alpha = True)
    $ quick_menu = True
    return

label Trash_Game_Sarang:
    $ quick_menu = False
    # Trash_Game 진행 시 Scarlet의 방에 생성 됨.
    $ SetBoxPos(0, 150, 800, 920,
    420, 420, 800, 920,
    # 0, 1350, 920, 920,
    1350, 1350, 800, 920)
    $ SetSpacialObject(
    Yun_Special_3_on, Yun_Special_3_on, (720, 490), 0,
    Yun_Special_3_on, Yun_Special_3_on, (1000, 490), 0,
    Yun_Table, Yun_Table, (560, 650), 0,
    Yun_Special_1, Yun_Special_1_on, (610, 425), 1,
    Yun_Special_1, Yun_Special_1_on, (930, 425), 1,
    Yun_Special_2_on, Yun_Special_2_on, (750, 600), 0,
    Yun_Special_2, Yun_Special_2_on, (1060, 600), 1
    )
    # Yun_Special_2, Yun_Special_2_on,
    $ SetTrash(Yun_Trash1, Yun_Trash2)
    $ SetStanding(Sarang_SD_Default, Sarang_SD_Fail, Sarang_SD_Success)

    if first_Game == False:
        $ InitGame(Sarang_TrashGame_BG, 5.0)
    else:
        $ InitGame(Sarang_TrashGame_BG, 10.0)

    scene bg CleaningRoom_Yun with Dissolve(2.0 ,alpha = True)

    # $ InitGame("")
    show screen Cleaning_game_Tutorial with Dissolve(.5 ,alpha = True)

    # "이제 청소를 해 주세요"

    $ res = StartGame()

    $ GameAsBG()
    with dissolve
    $ quick_menu = True
    return


label WhoisSelected_e:

    if GetOut_YvE == Elice:
        show Elice_Difficulty at elice_standsize_ms with Dissolve(.5)
        voice Elice_90
        elice '"...고마워."'
        '자칫 모르고 지나칠 수 있는 작은 목소리였지만, 다행히도 내 귀는 그 목소리를 들었다.'
        '그 엘리스에게서 듣는 감사 인사라니. 뭔가 간지러운 기분이다.'
        hide Elice_Difficulty with None
        pass

    elif GetOut_YvE == Sarang:
        show Yun_Sad at yun_standsize_ms with Dissolve(.5)
        voice Yunsarang_117
        yun '"...가지마세요."'
        '나를 붙잡는 윤사랑의 목소리가 들렸지만, 윤사랑을 생각한다면 엘리스를 데리고 나가는 게 우선이다.'
        hide Yun_Sad with None
        pass

    elif GetOut_YvE == Isabel:
        show Isabel_nodap at Isabel_standsize_ms with Dissolve(.5)
        voice Isabel_079
        isabel '"여긴 저한테 맡겨두세요."'
        '믿음직스러운 이자벨의 목소리가 들렸다.'
        '이자벨이라면 분명 돌아올 때까지 상황 정리를 끝내겠지.'
        hide Isabel_nodap
        pass

    elif GetOut_YvE == Scarlet:
        show Scarlet_ppagchim at scarlet_standsize_ms with Dissolve(.5)
        voice Scarlet_94
        scarlet '"야! 그... 아니다. 분홍은 내가 달랠테니까!"'
        '스칼렛의 우렁찬 목소리가 귀에 맴돈다.'
        '딱히 믿음은 가지 않지만... 기대해볼까?'
        hide Scarlet_ppangchim
        pass

label WhoisSelected_y:

    if GetOut_YvE == Elice:
        show Elice_Angry at elice_standsize_bs with Dissolve(.5)
        voice Elice_88
        elice '"...너!"'
        '엘리스는 뭔가 말하려고 했지만, 다시 입을 다물었다. '
        '하고 싶은 말이 있는지 궁금했지만 지금 듣는 건 어려울 것 같았다.'
        hide Elice_Angry with None
        pass

    elif GetOut_YvE == Sarang:
        show Yun_fallinlove at yun_standsize_bs with Dissolve(.5)
        voice Yunsarang_118
        yun '"주, 주인님..."'
        '윤사랑은 쭈뼛거리며 말을 걸어왔다.'

        hide Yun_fallinlove with None
        show Yun_tear at yun_standsize_bs with Dissolve(.5)
        voice Yunsarang_119
        yun '"믿어주셔서 감사해요."'
        player '"아, 그... 별거 아니야."'

        hide Yun_tear with None
        pass

    elif GetOut_YvE == Isabel:
        show Isabel_nodap at isabel_standsize_bs with Dissolve(.5)
        voice Isabel_079
        isabel '"여긴 저한테 맡겨두세요."'
        '믿음직스러운 이자벨의 목소리가 들렸다.'
        '이자벨이라면 분명 돌아올 때까지 상황 정리를 끝내겠지.'
        hide Isabel_nodap with None
        pass

    elif GetOut_YvE == Scarlet:
        show Scarlet_panic at scarlet_standsize_bs with Dissolve(.5)
        voice Scarlet_95
        scarlet '"분홍 잘 달래줘라!"'
        '스칼렛의 우렁찬 목소리가 귀에 맴돈다.'
        '생각보다 다정한 사람일지도...?'
        hide Scarlet_panic with None
        pass
