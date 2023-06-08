### sarang ending

label End_Sarang:
    scene bg black with Dissolve(3.0)
    $ renpy.pause(3.0, hard = True)
    '문을 넘어가려고 했을 때, 윤사랑이 멈췄다.'
    '윤사랑은 나와 잡고 있던 손을 놓고 뒤를 돌았다.'
    '무슨 일인지, 제대로 이해못하고 있던 그 때...'
    # 일러스트 삽입 , Yun_CG_004.png
    show Sarang_CG_4 with None         # 수정사항 4
    with vpunch

    # 샷건 장전 후 발사하는 사운드
    '커다란 총소리가 울려퍼진다.'
    '나는 도무지 윤사랑의 손에 들려있는 총과 방금 울려퍼진 총소리를 매치시키지 못한다.'
    play music horror_a fadein 2.0
    '대체 무슨 일이 일어나고 있는거지?'
    '놀란 눈으로 윤사랑을 바라보면, 평소의 해맑은 표정이 아닌 어둡고, 섬뜩한 미소를 지은 윤사랑이 나를 바라봤다.'
    voice Yunsarang_
    yun '"조금만 물러나 주세요..."'

    #총구 돌리는 사운드
    show Sarang_CG_5 with None
    hide Sarang_CG_4 with None
    '총구가 나를 향해 겨누어 졌을 때, 놀라서 뒷걸음질 쳤다.'
    with vpunch

    # 샷건 장전 후 발사하는 사운드
    '윤사랑은 망설임 없이 내가 있던 자리를 쏘았고, 그곳에는....'
    # 나무 문이 부숴지는 소리
    '아...'
    scene bg black with None
    '윤사랑은 현실 세계로 돌아갈 수 있는 문을 쏴버렸다.'
    '총알이 문을 관통하자, 문은 모래처럼 무너지며 순식간에 사라져 버린다.'
    '모든 일은 순식간에 벌어졌다. '
    '나를 귀찮게 하던 파란머리 관리자는 손을 쓸 새도 없이 시체가 되어버렸다.'
    '관리자의 시체를 수습하겠다는 생각도 들지 않는다.'
    '돌아갈 방법이 사라진 것 보다도, 눈 앞의 윤사랑이 너무 무서웠다.'
    '도망치고 싶어도, 두 다리가 움직이지 않았다.'
    '어제까지만 해도, 사랑을 나누던 상대였는데...'
    '가슴을 문지르던 설레임은, 공포가 된지 오래다.'
    scene bg BG_Underoom with Dissolve(.5)
    show Yun_Sad2 at yun_standsize_ms with Dissolve(.5)
    yun '"도망가지 않으셨군요. 기특해라."'
    play sound FootStep1
    '총을 든 윤사랑이 다가왔다.'
    hide Yun_Sad2 with None
    show Yun_cuty at yun_standsize_bs with Dissolve(.5)
    yun '"왜 그런 표정이신가요? 아, 얼굴에 피가 묻어버렸네요..."'
    hide Yun_cuty with None
    play sound Clothes
    '윤사랑은 옷 소매로, 뺨에 묻은 피를 닦아버린다.'
    show Yun_cuty at yun_standsize_bs with Dissolve(.5)
    player '"어, 어째서..."'
    yun '"네?"'
    player '"어째서 관리자를 죽인거야!"'
    player '"우리가 돌아갈 방법마저도 없애버리다니, 무슨 생각인거야?!"'
    '우리를 강제로 끌고 온 관리자에게 악감정을 품는 건 이해한다.'
    '동의하는 건 아니지만, 영문 모를 곳에 끌고 온 관리자를 죽이고 했을 수도 있지만...'
    '함께 돌아갈 수 있는 길을 없앤 이유는 도무지 알 수가 없었다.'
    '분명 같은 마음을 가지고 있다 장담했는 데, 몇 분동안 일어난 일 때문에 윤사랑은 전혀 모르는 사람이 되어버렸다.'

    hide Yun_cuty with None
    show Yun_anxiety at yun_standsize_bs with Dissolve(.5)
    yun '"저에게 화를 내시는 건가요?"'
    hide Yun_anxiety with None
    show Yun_cuty at yun_standsize_bs with Dissolve(.5)
    yun '"음... 그런 표정을 보는 건 처음이라서 조금 두근거렸어요."'
    player '"진지하게 대답해!"'
    '윤사랑의 눈에 제대로 된 초점이 잡히지 않았다.'
    hide Yun_cuty with None

    show Scarlet_heung at scarlet_standsize_ms with Dissolve(.5)
    scarlet '"어이, 무슨 일이야!"'
    show Elice_Contempt at elice_standsize_ms_L with Dissolve(.5)
    elice '"대체 무슨 소..."'
    show Isabel_contempt at isabel_standsize_ms_R with Dissolve(.5)
    isabel '"하아... 윤사랑씨."'
    '차례대로 메이드들이 등장했다.'
    '그들은 관리자의 시체를 보고 말을 잃거나, 한숨을 내쉴 뿐이었다.'
    hide Scarlet_heung
    hide Elice_Contempt
    hide Isabel_contempt
    with None

    show Elice_Angry_2 at elice_standsize_ms_L with Dissolve(.5)
    elice '"여태까지 참은 게 용한건가."'
    show Yun_cuty at yun_standsize_ms_R with Dissolve(.5)
    '엘리스의 말에 윤사랑은 가만히 웃어보일 뿐이었다.'
    hide Elice_Angry_2
    hide Yun_cuty
    with None
    # with Dissolve(.5)

    show Isabel_contempt at isabel_standsize_ms_L with Dissolve(.5)
    isabel '"[player_name] 씨, 윤사랑 씨한테서 떨어지세요."'
    show Scarlet_Angry at scarlet_standsize_ms_R with Dissolve(.5)
    scarlet '"분홍... 너...!"'
    # 박수치는 소리 추가
    show Yun_cuty at yun_standsize_ms with Dissolve(.5)
    '윤사랑은 분위기를 환기 시키듯 박수를 쳤다.'
    hide Yun_cuty with None
    show Yun_Happy at yun_standsize_ms with Dissolve(.5)
    yun '"네네, 방해꾼들은 이제 원래 세계로 돌아가실 시간이예요."'
    hide Yun_Happy with None
    show Yun_Laughter at yun_standsize_ms with Dissolve(.5)
    yun '"다들 이런 곳에서 빨리 벗어나고 싶어했잖아요. 기쁘죠?"'
    # hide Yun_Laughter with None
    hide Isabel_contempt with None
    show Isabel_fear at isabel_standsize_ms_L with Dissolve(.5)
    isabel '"잠..."'

    play sound teleport_snap
    hide Isabel_fear
    hide Scarlet_Angry
    with None

    $ renpy.pause(.5, hard = True)
    hide Yun_Laughter with None
    show Yun_cuty at yun_standsize_ms with Dissolve(.5)
    '윤사랑이 손가락을 튕기자, 이자벨을 시작으로 모두들 사라지기 시작했다.'
    '허무할 정도로, 그동안 탈출 방법을 찾았던 것이 우스울 정도로 빠르게.'
    player '"...정말 다 돌려보낸 거야?"'
    hide Yun_cuty with None
    show Yun_Normal at yun_standsize_ms with Dissolve(.5)
    yun '"네, 오기 전에 있었던 곳으로 다 돌려보내주었어요."'
    hide Yun_Normal with None
    show Yun_lookout at yun_standsize_ms with Dissolve(.5)
    yun '"원하신다면 확인 시켜드릴 수 있어요."'
    yun '"주인님은 상냥하니까, 계속 신경쓸거잖아요?"'
    hide Yun_lookout with None
    show Yun_pout at yun_standsize_ms with Dissolve(.5)
    yun '"조금 마음에 들지 않더라도, 원래 있었던 곳으로 안전히 보내서 더는 관심 줄 일을 없도록 하면 되겠죠."'
    hide Yun_pout with None
    show Yun_Normal at yun_standsize_ms with Dissolve(.5)
    yun '"너무 미안해하지 마세요, 저는 다른 여자를 걱정한다고 연인에게 뭐라하는 속 좁은 사람이 아니니까."'
    hide Yun_Normal with None
    show Yun_cuty at yun_standsize_ms with Dissolve(.5)
    yun '"물론 질투가 나지 않는 건 아니지만..."'
    hide Yun_cuty with None
    show Yun_Happy at yun_standsize_ms with Dissolve(.5)
    yun '"주인님의 그런 상냥한 모습까지 포함해서 좋아하게 되어버린 제가 배려해드려야죠."'
    '혼자서 자화자찬하고 있는 윤사랑을 보자니 기가 찼다.'
    '연인을 배려할 줄은 알면서, 생명의 소중함은 모르나 보지?'

    hide Yun_Happy with None
    show Yun_lookout at yun_standsize_bs with Dissolve(.5)
    player '"언제부터 그런 힘이 있던거야? 제대로 설명하는 게 좋을거야."'
    player '"관리자를 죽이고, 돌아갈 문을 없앤 시점에서 우리 사이의 신뢰는 깨진 거니까."'
    hide Yun_look with None
    show Yun_lookout at yun_standsize_bs with Dissolve(.5)
    play sound FootStep1

    '단호하게 말을 하면서 뒤로 물러났다.'
    '이제 이 저택에 나를 도와줄 사람은 없다.'
    '관리자가 갑자기 일어나서 장난이었다고 말하면 좋을테지만, 체온을 잃어가는 시체가 그럴 일은 없다.'

    hide Yun_lookout with None
    show Yun_panic at yun_standsize_ms with Dissolve(.5)
    yun '"...설마 제가 주인님을 속였다고 생각하는 건 아니죠?"'
    yun '"연인 사이의 신뢰는 기본이잖아요."'
    hide Yun_panic with None
    show Yun_anxiety at yun_standsize_ms with Dissolve(.5)
    yun '"저랑 주인님, 분명 서로 사랑하는 사이인데..."'
    player '"눈 앞에서 이런 일을 벌인 사람을, 이유도 없이 믿을 수는 없어."'
    '윤사랑의 표정은 어두워졌다. 설마 총으로 나도 쏘려는 건 아니겠지?'
    hide Yun_anxiety with None
    show Yun_pout at yun_standsize_ms with Dissolve(.5)
    yun '"아무리 화가 나도 제 손으로 주인님을 해치는 일은 없을테니 걱정하지 않으셔도 좋아요."'
    player '"그걸 어떻게..."'

    hide Yun_pout with None
    show Yun_lookout at yun_standsize_ms with Dissolve(.5)
    yun '"응? 다들 말해줬잖아요. 주인님은 생각이 얼굴에 드러나는 타입이라고."'

    hide Yun_lookout with None
    show Yun_cuty at yun_standsize_ms with Dissolve(.5)
    yun '"항상 주인님을 지켜봐왔으니까... 더 알기 쉬워요."'
    yun '"저를 무서워하는 표정까지 모두, 귀여워요 주인님."'
    player '"내, 내가 질문한 거에나 대답해!"'
    hide Yun_cuty with None
    show Yun_lookout at yun_standsize_ms with Dissolve(.5)
    yun '"언제부터 이런 힘이 생겼냐는 질문이요?"'
    hide Yun_lookout with None
    show Yun_Laughter at yun_standsize_ms with Dissolve(.5)
    yun '"이 힘은 방금 생겼어요. 주인님이 보는 앞에서."'
    hide Yun_Laughter with None
    show Yun_Normal at yun_standsize_ms with Dissolve(.5)
    yun '"마법소녀처럼 멋진 변신이라도 있었으면 좋았을텐데... 굉장히 수수한지라 눈치 못채셨군요."'
    '그리 말하는 윤사랑의 태도는 평소와 차이점이 없는 것 같았다.'
    player '"무슨 소리를 하는 거야..."'
    hide Yun_Normal with None
    show Yun_wink at yun_standsize_ms with Dissolve(.5)
    yun '"주인님은 멍청해서 귀여워요."'
    hide Yun_wink with None
    show Yun_Happy at yun_standsize_ms with Dissolve(.5)
    yun '"제가 관리자를 죽였기 때문에, 다음 관리자가 된거예요."'
    yun '"덕분에 메이드들을 쫓아낼 수도 있었고..."'
    hide Yun_Happy with None
    show Yun_Normal at yun_standsize_ms with Dissolve(.5)
    yun '"원래 세계로 돌아가는 문쯤이야 얼마든지 다시 만들어드릴 수 있죠."'
    player '"그렇다면...!"'
    hide Yun_Normal with None
    show Yun_cuty at yun_standsize_ms with Dissolve(.5)
    yun '"하지만, 주인님이 원래 세계로 돌아가시는 일은 없을 거예요."'
    yun '"드디어 주인님을 손에 넣었는 데 놓아줄리가 없잖아요."'
    yun '"항상 이러고 싶었어요. 주인님을... 내 것으로... 응..."'
    play sound Clothes
    hide Yun_cuty with None
    show Yun_cuty at yun_standsize_bs with Dissolve(.5)
    yun '"[player_name], 너를... 가지고 싶었어..."'
    scene bg black with Dissolve(2.0)
    '이 상황이 되어서야, 다른 메이드들의 충고가 떠오른다.'
    '첫날부터 윤사랑을 경계하던 엘리스....'
    '왠지 모를 꺼림직함이 느껴진다 말하는 이자벨...'
    '조심하라고 경고해주던 스칼렛까지.'
    '모든 퍼즐 조각이 이제서야 맞춰지는 기분이었다.'
    '어리숙한 스토커 같은 모습도 다 꾸며낸 것이었구나.'
    scene bg BG_Underoom with Dissolve(2.0)
    show Yun_Happy at yun_standsize_bs with Dissolve(.5)
    player '"왜, 이렇게까지 하는 거야?"'
    player '"내가 선택한 건 너였고, 가만히 있었어도 우리는 함께 현실 세상으로 돌아갈 수 있었어!"'
    hide Yun_Happy with None
    show Yun_stare at yun_standsize_bs with Dissolve(.5)
    yun '"그걸로는 부족해요!"'
    hide Yun_stare with None
    show Yun_panic at yun_standsize_bs with Dissolve(.5)
    yun '"주인님은 이해 못해요... 제가 얼마나 주인님을 좋아하는지..."'
    yun '"그동안 얼마나 많이 참아왔는지!"'
    hide Yun_panic with None
    show Yun_anxiety at yun_standsize_bs with Dissolve(.5)
    yun '"주인님의 곁을 스치는 사람, 생명체 모두 죽이고 싶은 걸 참고..."'
    yun '"평생 나만 볼 수 있는 곳에 가두고 싶은 것도 참고..."'
    yun '"가질 수 없다면 죽이고 싶은 마음도 열심히 참아왔는 데."'
    player '"...뭐?"'
    '윤사랑은 그동안 봤던 것중에서 가장 환한 미소를 지으며 내게 말했다.'
    hide Yun_anxiety with None
    show Yun_Happy at yun_standsize_bs with Dissolve(.5)
    yun '"이제 걱정 안하셔도 괜찮아요 주인님."'
    yun '"계속, 이곳에서, 저의 보호를 받으며 계시면 되니까..."'
    hide Yun_Happy with None
    show Yun_cuty at yun_standsize_bs with Dissolve(.5)
    yun '"동화처럼, 영원히 행복하게 살았습니다로 끝나는 이야기예요."'
    player '"난 그런 걸 바란 적 없어...!"'
    yun '"주인님도 언젠가는 저를 이해해주실 거예요."'
    play sound Clothes
    scene bg black with Dissolve(.5)
    '윤사랑의 손이 눈 위로 올라온다.'
    '어두운 시야 속에서, 인위적인 졸음이 몰려온다.'
    '잠에 들면 안된다고 생각해도, 눈꺼풀에 추가 달린 듯 무겁다.'
    player '"윤....사...랑..."'
    yun '"네, 주인님의 윤사랑이에요."'
    yun '"안심하고 편히 주무세요."'
    stop music fadeout 3.0
    $ renpy.pause(6.0, hard = True)
    '끼익. 저택의 문이 열리는 소리가 들렸다.'
    scene bg BG_Hall_dark with Dissolve(3.0)

    UnknownPlayer2 '"여기는 어디야..."'
    UnknownPlayer2 '"저기..."'
    play sound teleport_snap
    show Yun_Normal at yun_standsize_bs with Dissolve(.5)
    UnknownPlayer2 '"으악!"'
    hide Yun_Normal with None
    show Yun_cuty at yun_standsize_bs with Dissolve(.5)
    yun '"놀라게 했다면 죄송해요, 저는 이곳의 관리자 윤사랑이라고해요."'
    # 조명이 꺼지는 소리
    scene bg black with None
    yun '"메이드들의 새 주인이 될 당신의 이름은 무엇인가요?"'
    stop music fadeout 3.0
    $ renpy.pause(3.5, hard = True)

    jump endcredits



    pass
