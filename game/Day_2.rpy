# Day 2 Morning
label D_2_WakeUp:

    play sound "audio/BGM/chapter.wav"
    ######
    ######
    show bg_chapter2_avi
    $ renpy.pause(7.0, hard = True )
    stop sound
    hide bg_chapter2_avi with Dissolve(1.0, alpha = True)
    scene bg black with Dissolve(2.0, hard = True)

    if elice_f > scarlet_f and elice_f > isabel_f and elice_f > yun_f:
        call Morning_Elice from _call_Morning_Elice
        pass
    elif  scarlet_f > elice_f and scarlet_f > isabel_f and scarlet_f >yun_f:
        call Morning_Scarlet from _call_Morning_Scarlet
        pass
    elif yun_f > elice_f and yun_f > isabel_f and yun_f > scarlet_f:
        call Morning_Sarang from _call_Morning_Sarang
        pass
    elif isabel_f > elice_f and isabel_f> yun_f and isabel_f > scarlet_f:
        call Morning_Isabel from _call_Morning_Isabel
        pass

    scene bg black with Dissolve(2.0)
    $ renpy.pause(1.0, hard = True)
    jump D_2_Morning

    return

label D_2_Morning:
    play music Normal_a fadein 2.0
    scene bg BG_Livingroom with Dissolve(1.0 ,alpha = True)
    # show Eyes at eyesSize
    # hide Eyes with None
    '찌뿌둥한 몸을 풀기 위해서 기지개를 켰다.'
    play sound FootStep1
    '식당에 내려오니, 어제와 달리 메이드들은 이미 식사를 하고 있었다.'
    '나 하나 기다리는 것보다는 다들 이렇게 먹고 있는게 낫지.'
    '다들 이야기도 한마디 나누지 않고 식사만 하고 있었다.'
    '싸우는 것보다는 낫지만... 너무 삭막하지 않아?'
    player '"그러고 보니까, 식사가 끝나면 뭘 할 거야?"'

    show Yun_huc at yun_standsize_ms_L with Dissolve(.5 ,alpha = True)
    show Yun_huc at yun_one_jump_L with None
    voice Yunsarang_199
    yun '"저는 식당에 있으려고요!"'

    show Scarlet_lookout at scarlet_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Scarlet_141
    scarlet'"지하실에 재밌는게 있더군."'

    hide Yun_huc
    hide Scarlet_lookout
    with Dissolve(.5 ,alpha = True)
    show Isabel_pout at isabel_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Isabel_135
    isabel '"저는 저택 밖이요."'

    show Elice_Surprised at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_37
    elice '"..."'

    hide Isabel_pout
    hide Elice_Surprised
    with Dissolve(.5 ,alpha = True)
    '아무도 겹치는 장소가 없었다.'
    '어찌 보면 한결같고, 달리 보면 단합이 안 되고...'
    '굳이 다 같이 있으라고 말할 이유를 찾지 못해서, 그냥 밥이나 먹었다.'
    '슬슬 식사가 끝나갈 때 즈음, 관리자가 나타났다.'

    play sound teleport_snap
    show Hyeyeon_Laughter at admin_standsize_bs with None
    admin '"다들 식사는 맛있게 하고 있어?"'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(.5 ,alpha = True)
    admin '"누가 만들어준 건데, 당연히 잘하고 있어야지!"'

    hide Hyeyeon_Normal with None
    show Hyeyeon_Happy at admin_standsize_bs with Dissolve(.5 ,alpha = True)
    admin '"오늘도 아침은 자유시간, 점심을 먹은 후에는 청소야!"'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(.5 ,alpha = True)
    admin '"난 꽃 구경 해야 하니까, 점심시간이 되기 전에는 찾지 마~"'

    play sound teleport_snap
    hide Hyeyeon_Laughter with None
    '우다다다 자기 할 말만 내뱉은 관리자는 나타날 때와 마찬가지로, 예고도 없이 사라졌다.'
    player '"쟤가 할 일은 우리 청소시키기랑 밥 차려주기 밖에 없어?"'

    show Scarlet_nonSad at scarlet_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Scarlet_142
    scarlet '"제일 중요한 일을 담당하고 있군."'

    show Isabel_nodap at isabel_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Isabel_136
    isabel '"밥 차려주는 거 말이에요?"'

    hide Scarlet_nonSad with None
    show Elice_Normal_2 at elice_standsize_ms_R with Dissolve(.5 ,alpha = True)
    voice Elice_169
    elice '"나름 일리가 있어."'

    hide Isabel_nodap with None
    show Yun_lookout at yun_standsize_ms_L with Dissolve(.5 ,alpha = True)
    voice Yunsarang_201
    yun '"식사는 중요하죠."'
    '오가는 대화를 들으며, 오늘은 누구와 이야기를 할지 고민했다.'

    hide Elice_Normal_2
    hide Yun_lookout
    with Dissolve(.5 ,alpha = True)

    menu:
        "스칼렛":
            $ s_D_2_Morning = True
            jump Say_To_Scarlet
        "이자벨":
            $ i_D_2_Morning = True
            jump Say_To_Isabel
        "엘리스":
            $ e_D_2_Morning = True
            jump Say_To_Elice
        "윤사랑":
            jump Say_To_Sarang

label Morning_Elice:
    play music comic fadein 2.0
    play sound DoorOpen2
    scene bg Myroom with Dissolve(1.0 ,alpha = True)
    $ renpy.pause(1.0)
    show Elice_Angry_2 at elice_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Elice_161
    elice '"어이... 일어나."'
    player '"으음..."'

    hide Elice_Angry_2 with None
    show Elice_Angry at elice_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Elice_162
    elice '"일어나라고 했을 텐데?"'
    player '"조금만 더 자게 해줘..."'

    hide Elice_Angry with None
    show Elice_Coloration at elice_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Elice_163
    elice '"하아..."'

    hide Elice_Coloration with None
    show Elice_Coloration_2 at elice_standsize_ms with Dissolve(.5,alpha = True)
    voice Elice_164
    elice '"말로는 안되는 자로군."'

    hide Elice_Coloration_2 with None
    play sound DoorOpen2
    '엘리스가 문밖으로 나가는 소리가 들렸다.'
    '포기하고 먼저 식사하러 간 걸까?'
    player '"나는 더 잘래..."'
    '자고 싶은 사람은 자고, 밥 먹고 싶은 사람은 먹는게 맞지.'

    play sound DoorOpen2
    '조금의 시간이 흐른 후, 다시 방 안으로 누군가 들어왔다.'
    player '"으응...누구?"'

    show Elice_Committed_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_165
    elice '"지금이라도 일어나면 자비를 베풀어주도록 하지."'
    player '"무리야... 조금만 더 잘래."'
    '어제 하루 종일 저택을 돌아다니느라 얼마나 힘들었는데...'
    '무거운 눈꺼풀을 들어 올릴 힘 따위 나약한 내게는 없다.'

    hide Elice_Committed_2 with None
    show Elice_Committed at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_166
    elice '"난 분명 기회를 줬어."'

    hide Elice_Committed with Dissolve(1.0)
    show screen Mini_Scene(pail) with Dissolve(.5)
    play sound Water1
    with vpunch
    player '"으악!"'
    '엄청나게 차가운 물이 얼굴에 닿자마자 눈이 번떡 뜨였다.'
    player '"엘리스!"'

    hide screen Mini_Scene with Dissolve(.5)
    hide Elice_Committed with None
    show Elice_Ignore at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    '자리에서 일어나 엘리스를 바라봤다.'
    '한없이 오만해 보이는 엘리스는, 내가 아는 그 엘리스다.'

    hide Elice_Ignore with Dissolve(.5)
    show Elice_CG_2
    show Elice_Mini at elice_bs_to_top
    with Dissolve(.5)

    $renpy.pause(2.5, hard = True)
    # show screen Elice_MiniScene with Dissolve(1.0)
    '손에 뭔가 잡히는데... 이건 얼음?'
    player '"너... 얼음 물을 가지러 주방까지 다녀온 거야?"'
    # hide Elice_Ignore with None
    # show Elice_Gladness at elice_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Elice_167
    elice '"말로 할 때 일어났으면 이런 일은 없잖아?"'
    '아까까지만 해도 짜증이 역력했던 목소리는 금세 즐거움으로 가득 찼다.'
    '날 놀리는게 즐겁나 얘는...?'
    # hide Elice_Gladness with None
    # show Elice_Gladness_2 at elice_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Elice_168
    elice '"빨리 나오는게 좋을 거야. 난 기다리는 건 싫어하거든."'

    hide Elice_CG_2
    hide Elice_Mini
    with Dissolve(1.0)
    play sound DoorOpen2

    '엘리스는 자기가 들고 왔던 바가지를 들고 방 밖으로 나갔다.'
    '야무지기도 하지... 청소하기 싫다고 싸울 때는 언제고,\n'
    extend '나를 골탕 먹이겠다고 직접 물까지 떠오다니...'
    '메이드 복을 입는다고 메이드가 아니잖아, 관리자!'
    # 아침으로 점프
    return

label Morning_Sarang:
    play music Yunsarang_2 fadein 1.5
    play sound DoorOpen2
    scene bg Myroom with Dissolve(1.0 ,alpha = True)
    show Yun_lookout at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_187
    yun '"오늘도 주무시고 계시나요?"'
    '문이 열리는 소리와 함께 누군가 방 안으로 들어왔다.'
    '작게 들리는 목소리가 잠을 방해하고 싶지 않다는 것이 느껴진다.'

    hide Yun_lookout with None
    show Yun_Normal at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_188
    yun '"더 주무셔도 괜찮아요. 주인님의 잠자리는 제가 지킬 테니까..."'
    '들려오는 말소리에 눈을 뜨면, 어제와 같은 모양새로 윤사랑이 나를 보고 있다.'

    hide Yun_Normal with None
    show Yun_Happy at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Yunsarang_189
    yun '"좋은 아침이에요, 주인님."'
    player '"아, 좋은 아침."'
    '잠을 깨우러 온 사람치고는 깨울 생각이 없는 것 같았지만...'
    '그래도 굳이 깨우러 와줬다는게 고맙네.'
    player '"깨워줘서 고마워, 내일도 오늘처럼 깨워줄 거야?"'

    hide Yun_Happy with None
    show Yun_huc at yun_standsize_ms with Dissolve(.5 ,alpha = True)
    show Yun_huc at yun_one_jump with None
    voice Yunsarang_190
    yun '"주, 주인님이 원하신다면요...!"'
    '두 손을 움켜쥐고 말하는 윤사랑을 보며 웃음을 터트렸다.'

    show Yun_huc at yun_one_jump with None
    voice Yunsarang_191
    yun '"내일뿐만이 아니라, 그 다음날도, 다음날의 다음날도, 평생도 가능해요!"'
    player '"농담이었어. 아침에 나 깨우러 오는 거 귀찮지 않아?"'
    player '"내일은 꼭 혼자서 일어나 볼게."'

    hide Yun_huc with None
    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    show Yun_fallinlove at yun_one_jump_bs with None
    voice Yunsarang_192
    yun '"귀찮지 않아요!"'
    '윤사랑은 크게 소리치면서 말했다.'

    hide Yun_fallinlove with None
    show Yun_huc at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_193
    yun '"제가 좋아서 하는 일이니까, 부담스러워하지 않으셔도 괜찮아요!"'

    hide Yun_huc with None
    show Yun_pout at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_194
    yun '"그... 그러니까..."'
    '윤사랑은 얼굴을 붉히면서 내 눈치를 봤다.'
    '말해도 괜찮다는 뜻으로 고개를 끄덕이는 걸 본 후에야 말했다.'

    hide Yun_pout with None
    show Yun_Laughter at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_195
    yun '"내일도 제가 주인님을 깨우러 올 수 있게 해주세요."'
    '귀찮은 일을 떠맡는 걸 좋아하는 걸까?'
    '수줍어하는 윤사랑을 보면, 자꾸만 나를 좋아하는 건 아닌가? 하는 착각을 해버린다.'
    '괜히 아는 척했다가 망신 당하면 쪽팔리니 말하지 말아야지.'
    player '"그래도 깨우러 와줘서 고마워."'
    player '"다른 애들이 또 뭐라 하기 전에 식사하러 가자."'

    hide Yun_Laughter with None
    show Yun_Normal at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_196
    yun '"네! 오늘 아침은 죽이래요."'
    player '"죽? 가볍게 먹긴 좋겠네."'

    play sound DoorOpen2
    '내가 문을 열고 나서는 동안 윤사랑은 그 자리에 멈춰 서있었다.'

    hide Yun_Normal with None
    show Yun_lookout at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_197
    yun '"주인님, 주인님을 깨우러 오는게 좋아요."'

    hide Yun_lookout with None
    show Yun_cuty at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_198
    yun '"정말... 좋아서 하는 일인 걸요?"'
    # 아침으로 점프



    return

label Morning_Isabel:

    play music Isabel_2 fadein 1.5
    scene bg Myroom with Dissolve(1.5 ,alpha = True)
    show Isabel_nodap at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_124
    isabel '"...저기요."'
    '귓가에서 누군가 속삭이는 목소리가 들렸다.'
    '착각이라고 생각할 수 있을 만큼 작은 목소리라서 무시하고 그냥 잤다.'

    hide Isabel_nodap with None
    show Isabel_pout at isabel_standsize_ms with Dissolve(.5 ,alpha =True)
    voice Isabel_125
    isabel '"일어나세요..."'

    hide Isabel_pout with None
    show Isabel_heung at isabel_one_jump_ms with Dissolve(.5)
    voice Isabel_126
    isabel '"언제까지 주무실 생각이죠?"'
    '부르는 소리에 점점 화가 실리는 것 같았다.'
    '눈을 뜨지 않으면 무슨 일이 벌어지는 건 아닐까? 라는 불안감이 몸을 감싼다.'
    '하지만 오늘따라 몸이 무거웠기 때문에 정말로 조금만 더 자고 싶었다.'
    '조금만 더 자게 해줘...!'

    hide Isabel_pout with None
    show Isabel_Laughter at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_127
    isabel '"...일어나세요, 주인님."'
    player '"응?"'
    '나도 모르게 눈을 번쩍 떴다.'
    '주인님이라고?'
    '다른 누구도 아니고 이자벨이 부르는 소리다.'
    '놀란 눈으로 이자벨을 바라보니, 이자벨은 수줍다는 듯 웃고 있었다.'

    hide Isabel_Laughter with None
    show Isabel_soAngry at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_128
    isabel '"이런 거에 깨시다니, 조금 재밌네요."'
    player '"뭐? 그, 그런 거 아니야!"'

    hide Isabel_soAngry with None
    show Isabel_Normal at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_129
    isabel '"아니긴 뭘요. 제가 열심히 깨울 때는 꿈쩍도 안 하시다가 한 번에 눈 뜨셨잖아요?"'
    player '"그러니까, 이건...!"'
    player '"너무 놀라서 그런 거지. 이자벨은 나를 주인님이라고 잘 부르지 않잖아?"'

    hide Isabel_Normal with None
    show Isabel_pout at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_130
    isabel '"누구처럼 자주 부르는 건 아니지만, 아예 안 부른 건 아니었다고요?"'

    hide Isabel_pout with None
    show Isabel_nodap at isabel_standsize_ms with Dissolve(.5)
    voice Isabel_131
    isabel '"그 정도로 놀라다니, 너무 순진하시네요."'
    player '"그, 그런 게 아니잖아!"'
    '얼굴이 붉게 달아오르는 것만 같았다.'
    player '"네, 네가 오해하게 만드니까..."'

    hide Isabel_nodap with None
    show Isabel_Happy at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_132
    isabel '"오해라뇨? 무슨 오해를 하셨는데요?"'
    '놀릴 거리를 발견했다는 듯 웃으며 묻는 이자벨의 모습에 나만 억울했다.'
    player '"말할 수 있을 리가 없잖아!"'

    hide Isabel_Happy with None
    show Isabel_Laughter at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_133
    isabel '"말해보세요, 들어드릴 테니까."'
    player '"됐어, 아침이나 먹으러 가자!"'
    '그 나이 대에 맞게 웃는 이자벨의 표정은 무척이나 귀엽지만, 민망한 마음에 큰 소리로 문을 닫고 나왔다.'

    hide Isabel_Laughter with None
    show Isabel_lookout at isabel_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Isabel_134
    isabel '"...제가 원래 이런 말 하는 사람이 아닌데, 왜 그랬는지 모르겠네요..."'
    # 아침으로 최종 점프

    return

label Morning_Scarlet:
    play music comic fadein 1.5
    scene bg Myroom with Dissolve(1.5 ,alpha = True)
    show Scarlet_jjajeung at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_131
    scarlet '"아침이다! 일어나라, 네놈!"'
    player '"으응... 더 자게 해줘."'

    hide Scarlet_jjajeung with None
    show Scarlet_heung at scarlet_standsize_ms with Dissolve(.5 ,alhpa = True)
    voice Scarlet_132
    scarlet '"이 몸이 일어나라고 했을 텐데? 이봐! 이 몸이 말하는데 자지 마라!"'
    '몸을 한껏 웅크린 상태로 이불 속에 파고든다.'
    '아무리 크게 소리쳐도 듣지 않으면 그만!'

    hide Scarlet_heung with None
    show Scarlet_contempt at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_133
    scarlet '"감히 이 몸의 말을 무시했겠다!"'
    play sound standup

    '스칼렛은 내가 덮고 있던 이불을 빼앗아 갔다.'
    '아앗, 나의 소중한 이불 2호가...!'
    '허망한 표정으로 스칼렛을 쳐다보는데, 스칼렛은 무척이나 근엄한 표정으로 나를 내려다보고 있었다.'
    '대체 언제 침대 위로 올라온 건지 모르겠지만.'
    hide Scarlet_contempt with None
    show Scarlet_inflate at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_134
    scarlet '"네 녀석은 사람이길 포기하려는 건가? 언제까지 잘 생각인 거지?"'
    player '"조금만 더 잔다고 사람이길 포기하는 건 아니야..."'
    '하품을 하면서 기지개를 폈다.'

    hide Scarlet_inflate with None
    show Scarlet_panic at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_135
    scarlet '"너... 팔이!"'
    player '"응? 무슨 일... 우왓!"'
    '스칼렛이 기겁을 한 표정으로 내 팔을 가리켰다.'
    '무슨 일인가 싶어서 바라보니, 팔에 작은 상처가 생겨있었다.'
    '날카로운 것에 긁힌 자국과 스칼렛의 손을 보니 대충 예상이 갔다.'
    player '"이런 건 침 한 번 바르면 나아."'

    hide Scarlet_panic with None
    show Scarlet_ppagchim at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_136
    scarlet '"멍청한 소리 하지 마! 상처를 우습게 보면 큰일난다."'
    '심각한 표정을 지은 스칼렛은 구급상자를 들고 왔다.'

    hide Scarlet_ppagchim with None
    show Scarlet_Sad at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_137
    scarlet '"젠장... 다치게 할 생각은 없었는데."'
    '세상 진지한 표정으로 붕대를 감는 스칼렛을 보니 기분이 이상했다.'
    '그렇게 심각하게 다친 것도 아닌데 저런 반응이라니.'
    player '"그, 일부로 그런 것도 아니잖아? 난 괜찮으니까..."'

    hide Scarlet_Sad with None
    show Scarlet_displease at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_138
    scarlet '"...그런 말 하다 죽은 녀석을 여럿 알지."'
    player '"응? 무슨 소리야 그게."'

    hide Scarlet_displease with None
    show Scarlet_Angry at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_139
    scarlet '"네 녀석이 들어봤자 이해 못 할 이야기다."'

    hide Scarlet_Angry with None
    show Scarlet_inflate at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_140
    scarlet '"쯧... 이리 연약한 신체라니, 너도 고생이 많겠군."'

    hide Scarlet_inflate with None
    play sound DoorOpen2
    '붕대를 다 감은 스칼렛은 그 말을 끝으로 방 밖으로 나갔다.'
    '아니, 나랑 같이 가야 하는 거 아니었어?'
    player '"스칼렛, 같이 가!"'
    # 아침으로 최종 이동
    return

label Say_To_Scarlet:
    stop music fadeout 1.0
    scene bg black with Dissolve(1.0 ,alpha = True)
    '스칼렛이 말한 재밌는 것이 궁금했다.'
    '저택에서 제일 재밌게 생긴 녀석이 말하는 재밌는 것은 얼마나 재미있을까?'

    scene bg BG_Underoom with Dissolve(1.0 ,alpha = True)
    play music Scarlet_1 fadein 2.0
    play sound FootStep1
    '식사를 끝낸 후, 지하실로 향했다.'
    '이렇게 어두운 지하실을 제 집 마냥 들락날락하는 스칼렛이 신기할 지경이었다.'

    play sound DoorOpen2
    show Scarlet_jjajeung at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    show Scarlet_jjajeung at scarlet_one_jump with None
    voice Scarlet_143
    scarlet'"아, 네 녀석도 왔는가?"'
    player '"응... 재밌는 걸 발견했다면서?"'

    hide Scarlet_jjajeung with None
    show Scarlet_pout at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    show Scarlet_pout at scarlet_one_jump with None
    voice Scarlet_144
    scarlet'"그래, 정확히 말하면 신기해 보이는 것이지."'
    '여태껏 봤던 것 중에서 제일 밝은 표정을 한 스칼렛이 손가락으로 무언가를 가리켰다.'
    player '"이건..."'

    hide Scarlet_pout with None
    show Scarlet_Laughter at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    show Scarlet_Laughter at scarlet_one_jump_bs with None
    voice Scarlet_145
    scarlet '"마법이 담긴 구슬인 것 같다!"'

    hide Scarlet_Laughter with None
    show Scarlet_Happy at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    show Scarlet_Happy at scarlet_one_jump_bs with None
    voice Scarlet_146
    scarlet '"대체 무슨 마법이 담겨있는지 벌써 궁금해지는군!"'
    '21세기의 대한민국에서 살던 나는, 스칼렛이 말하는 마법 같은 건 잘 모른다.'
    '아무리 마법에 무지한 나라도, 스칼렛이 가리키는 구슬을 건드리면 안 된다는 것만큼은 잘 알 것 같았다.'
    '구슬의 받침대는 메마른 사람의 손 같았고, 불길한 보라색이 일렁거리는 구슬은...'
    '대놓고 \'나를 건드리지 마시오.\'하는 아우라를 풍기고 있었다.'
    '재미고 나발이고, 저런 물건은 건드리지 않는게 상책이다.'
    player '"스칼렛, 저거 왠지 위험해 보이지 않아?"'

    hide Scarlet_Happy with None
    show Scarlet_Normal at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_147
    scarlet '"호오, 네 녀석도 나름대로 위험을 감지할 줄 아는군?"'
    player '"무슨 뜻이야 그거."'
    '피식 웃은 스칼렛은 내 머리를 쓰다듬었다.'

    hide Scarlet_Normal with None
    show Scarlet_Happy at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    show Scarlet_Happy at scarlet_one_jump_bs with None
    voice Scarlet_148
    scarlet '"아직 세상 위험한 줄 모르는 어린 녀석인 줄만 알았지."'
    player '"저기요!"'

    hide Scarlet_Happy with None
    show Scarlet_nonSad at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_149
    scarlet '"저 물건이 위험해 보인다는 건 다른 누구보다도 내가 잘 알고 있다."'
    '스칼렛은 나름대로 진지한 표정을 짓고서는 구슬을 바라보았다.'
    '스칼렛이 바라보면 볼수록 구슬의 위험한 아우라는 더욱 강해졌다.'
    '저 구슬, 스칼렛한테 반응하는 건가...?'

    hide Scarlet_nonSad with None
    show Scarlet_pout at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_150
    scarlet'"이 저택에 있는 물건들 중, 그분을 만족시킬 만한 건 없었지."'

    hide Scarlet_pout with None
    show Scarlet_stare at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_151
    scarlet '"저 마법 구슬이라면 그분을 충분히 만족시킬 거다."'
    player '"...굳이 위험한 일을 자처하는 이유가?"'
    '스칼렛은 꼬리를 탁탁거리며 내게 말했다.'

    hide Scarlet_stare with None
    show Scarlet_Sad at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_152
    scarlet'"그분과의 연결이 끊긴 건 이번이 처음이다."'
    voice Scarlet_153
    scarlet '"제대로 다시 이어내려면 합당한 공물이 있어야겠지."'

    hide Scarlet_Sad with None
    show Scarlet_displease at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_154
    scarlet'"이곳의 메이드나, 너로서는 턱없이 부족하지만..."'
    player '"나를 제물로 바칠 생각을 했던 거야?"'

    hide Scarlet_displease with None
    show Scarlet_stare at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    '스칼렛은 아무런 말도 하지 않고 나를 바라보았다.'
    '... .... .'
    player '"진짜로?!"'

    hide Scarlet_stare with None
    show Scarlet_lookout at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    show Scarlet_lookout at scarlet_one_jump_bs with None
    voice Scarlet_155
    scarlet '"큼, 지금은 없으니까 안심해라!"'
    player '"나중에는 생긴다는 이야기잖아?!"'

    hide Scarlet_lookout with None
    show Scarlet_nonSad at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    '당황한 내가 소리를 지르는 와중에, 스칼렛은 구슬에 손을 대었다.'
    '아니, 내가 위험할 것 같다고 그렇게 말했는데!'
    '스칼렛의 손이 닿자마자 구슬은 점점 붉게 변해갔고, 지하실 안을 채우는 건 붉은색 불빛이다.'
    player '"스칼렛, 괜찮아?"'

    hide Scarlet_nonSad with None
    show Scarlet_Angry at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    '스칼렛은 구슬에서 손을 떼지 않은 상태로 계속 들여다보고 있었다.'
    '눈앞에서 손을 흔들어봤지만, 스칼렛은 전혀 반응하지 않고 구슬만 바라보고 있었다.'
    player '"스칼렛?"'

    hide Scarlet_Angry with None
    show Scarlet_contempt at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    '스칼렛을 자세히 들여다보니, 눈에 초점이 없었다.'
    '이대로 스칼렛을 가만 내버려 두면, 계속 구슬만 바라보고 있을 것 같았다.'
    player '"하아..."'
    '한숨을 내쉰 나는 스칼렛의 옷자락을 붙잡고, 구슬과 떨어뜨리려고 했다.'
    '힘을 어떻게 쥔 것인지, 스칼렛의 손은 구슬에서 잘 떨어지지 않았다.'

    hide Scarlet_contempt with Dissolve(.5 ,alpha = True)
    '대략 10분 동안 별의별 짓을 한끝에, 나는 스칼렛과 구슬을 분리할 수 있었다.'
    '여전히 붉은색을 띠는 구슬 쪽은 조금도 쳐다보기 싫었다.'
    '아직 무슨 일이 일어난 건 아니지만...'
    '아니, 무슨 일은 일어났지. 스칼렛이 정신을 잃었잖아?'
    '저 구슬을 어쩌지 고민하다가 구석에 있던 천을 가져와 덮어버렸다.'
    '불길한 붉은빛이 사라져서 그나마 마음이 안정되었다.'
    player '"스칼렛."'
    player '"정신 좀 차려봐 스칼렛."'
    '나는 스칼렛을 붙잡고 흔들었지만, 사라진 초점은 도무지 돌아올 생각을 하지 않았다.'
    # hide Scarlet_contempt with None
    show Scarlet_socontempt at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_156
    scarlet '"...마."'
    player '"응?"'

    hide Scarlet_socontempt with None
    show Scarlet_sojiajeung at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_157
    scarlet '"...하지 마."'
    player '"어, 응. 그만 흔들게."'
    '작은 목소리로 중얼거리는 스칼렛의 말에 나는 어깨를 흔들던 손을 놓았다.'

    hide Scarlet_sojiajeung with None
    show Scarlet_sotear at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_158
    scarlet '"...나를 괴롭히지 마."'
    player '"엑, 내가 언제!?"'

    hide Scarlet_sotear with None
    show Scarlet_soppagchim at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_159
    scarlet '"왜 나를 괴롭히는 거야. 내가 대체 뭘 잘못했다고!"'

    play sound Thud1
    show Scarlet_soppagchim at scarlet_one_jump with None
    voice Scarlet_160
    scarlet '"나라고 이런 식으로 태어나고 싶어서 태어난 줄 알아?"'

    hide Scarlet_soppagchim with None
    show Scarlet_sojiajeung at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_161
    scarlet '"고를 수만 있었다면... 나도 너희처럼 평범하게 태어나고 싶었어."'

    voice Scarlet_162
    scarlet '"꼬리도 귀도 없는 평범한 인간으로 말이야!"'
    '울분을 토하는 스칼렛의 목소리에는 한이 실려있었다.'

    hide Scarlet_sojiajeung with None
    show Scarlet_socontempt at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_163
    scarlet '"내가 어떤 고통 속에서 사는지 알지도 못하는 주제에..."'
    voice Scarlet_164
    scarlet '"내가 가장 싫어하는 것들로 나를 놀리고, 괴롭히고..."'

    hide Scarlet_socontempt with None
    show Scarlet_sojiajeung at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_165
    scarlet '"꼭, 내가 꼭 너희를 저주할 거야..."'

    hide Scarlet_sojiajeung with None
    show Scarlet_soppagchim at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    show Scarlet_soppagchim at scarlet_one_jump_bs with None
    voice Scarlet_166
    scarlet '"그때 가서 용서를 빌어도 소용없어. 나를 괴롭힌 만큼, 너희를 괴롭게 할 거야."'

    '그리 말하는 스칼렛은 도무지 제정신이라고 볼 수 없었다.'
    '아까 구슬 때문인가?'
    '계속해서 과거의 일을 토해내는 스칼렛이 안쓰럽고, 걱정됐다.'
    '아직은 자기 한탄에 빠져있지만 나를 다른 사람으로 착각하고 덤벼들면 어떡하지?'

    hide Scarlet_soppagchim with Dissolve(.5, alpha = True)
    '주위를 두리번거리던 도중, 내가 천으로 덮어놓은 마법 구슬이 보였다.'
    '아무리 봐도 이 녀석이 모든 사건의 원인이다.'

    play sound Thud2
    '구슬이 깨지자마자 스칼렛은 바닥에 주저앉았다.'

    play sound Glass
    with vpunch
    '바닥에 떨어진 구슬은 쨍그랑! 하는 소리와 함께 깨졌다.'

    show Scarlet_socontempt at scarlet_standsize_ms with Dissolve(.5)
    $renpy.pause(.5,hard = True)
    show Scarlet_socontempt at scarlet_ms_to_down with None
    play sound Thud2
    hide Scarlet_socontempt with Dissolve(0.8)
    voice Scarlet_167
    scarlet '"크흑..."' with vpunch
    player '"스칼렛!"'

    play sound Thud1

    '구슬이 깨지자마자 스칼렛은 바닥에 주저 앉았다.'
    show Scarlet_tear at scarlet_standsize_ms with Dissolve(.5 ,alpha = True) # 효과 추가 - 넘어짐
    play sound standup
    voice Scarlet_168
    scarlet '"나는... 아직... 무너지지 않아..."'
    '초점이 돌아온 눈으로 그리 중얼거린 스칼렛은 금방 눈을 감았다.'
    player '"...죽었나?"'
    '스칼렛의 코밑에 손가락을 가져다 대니, 다행히 숨결이 느껴졌다.'
    '...무슨 말이 하고 싶은 거지?"'
    '잠시 기절한 것 같지? 이대로 스칼렛을 두고 갈 수도 없는 마당이다.'
    '우선.. 편히 눕게 한 뒤 자리를 지켰다.'

    scene bg black with Dissolve(1.0 ,alpha = True)
    $ renpy.pause(2.0)
    '대략 한 시간이 지난 후에야 스칼렛은 잠에서 깼다.'

    scene bg BG_Underoom with Dissolve( 1.0,alpha = True)
    show Scarlet_jjajeung at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_169
    scarlet '"크흑... 무슨 일이 있었던 거지?"'
    player '"아, 일어났어 스칼렛?"'

    hide Scarlet_jjajeung with None
    show Scarlet_lookout at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_170
    scarlet '"...네 녀석 얼굴을 보고 반가워할 일이 생길 줄이야."'
    player '"응?"'

    hide Scarlet_lookout with None
    show Scarlet_Sad at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
    voice Scarlet_171
    scarlet '"과거의 망령을 봤거든. 지독한 악몽이었지."'
    '씁쓸하게 웃는 스칼렛을 보니, 하고 싶은 말이 있었다.'
    menu:
        "사실 네 이야기를 들었어.":
            # 호감도 하락
            player '"스칼렛, 사실 네 이야기를 들었어."'
            hide Scarlet_Sad with None
            show Scarlet_Sad at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
            voice Scarlet_174
            scarlet '"..."'
            player '"괴롭히지마. 라던가 하는 이야기들 말이야."'
            player '"혹시 이야기해줄 수 있어?"'

            hide Scarlet_Sad with None
            show Scarlet_displease at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
            voice Scarlet_175
            scarlet '"크릉... 너같은 어린 녀석에게 함부로 할 이야기는 아니지만..."'
            voice Scarlet_176
            scarlet'"신세를 졌으니 그 정도는 말해줄 수 있겠지."'
            '스칼렛은 깨진 마법 구슬을 한 번 흘긴 후 입을 열었다.'

            hide Scarlet_displease with None
            show Scarlet_stare at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Scarlet_177
            scarlet'"내가 태어난 곳에는 나와 같은 외모를 가진 사람이 별로 없었다."'
            voice Scarlet_178
            scarlet '"귀와 꼬리는 불완전함의 상징이었고, 그런 나를 핍박하는 이들이 많았지."'
            '모든 것을 덤덤히 이야기하는 스칼렛의 눈이 신경쓰였다.'
            '안대로 가리고 있는 눈... 바보같은 설정을 위한 것이라고 생각했지만, 설마...?'
            '나는 직접적으로 말하지 못하고 스칼렛의 눈만 보고 있었다.'

            hide Scarlet_stare with None
            show Scarlet_nonSad at scarlet_standsize_bs with Dissolve(.5)
            voice Scarlet_179
            scarlet '"...이몸의 눈에 대해서 묻고 싶은가?"'
            player '"솔직히 궁금하지."'

            hide Scarlet_nonSad with None
            show Scarlet_displease at scarlet_standsize_bs with Dissolve(.5)
            voice Scarlet_180
            scarlet '"날 핍박하던 이들은 내가 자신들을 바라보는 것 마저 허용치 않더군."'

            voice Scarlet_181
            scarlet '"지나가던 이들을 쳐다봤다는 이유로... 내 눈을 멀게 했지."'
            player '"그게 말이 돼?!"'
            '너무 놀란 난 자리에서 일어났다.'
            '그런 나를 보며 스칼렛은 어쩔 수 없다는 미소를 지으며, 덤덤히 말했다.'

            hide Scarlet_displease with None
            show Scarlet_Sad at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Scarlet_182 # 183 과 합성
            scarlet '"뭐, 이제는 과거의 일이니까 상관없다. 자신들과 다른 존재를 받아들이지 못하는 그들의 속 좁음에 익숙해지기도 했고."."'
            player '"...그런 건 익숙해지면 안 되는 일이야."'
            '덤덤하게 받아들이는 듯한 스칼렛의 태도에 속이 상했다.'

            hide Scarlet_Sad with None
            show Scarlet_panic at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
            player '"다르게 생겼다는 이유 하나만으로 네가 배척받으면 안 돼."'
            player '"너도... 익숙해져서는 안되고."'

            hide Scarlet_panic with None
            show Scarlet_Happy at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Scarlet_184
            scarlet '"... 위로치고는 서툰 말이군."'
            player '"그게..."'

            hide Scarlet_Happy with None
            show Scarlet_lookout at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Scarlet_185
            scarlet '"뭐, 서툰 위로에도 기분이 나아졌다면 내가 이상한 거려나."'

            hide Scarlet_lookout with None
            show Scarlet_pout at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
            voice Scarlet_186
            scarlet'"슬슬 돌아갈까, 다른 녀석들도 기다리고 있을 것 같고..."
            '
            voice Scarlet_187
            scarlet '"배도 고프니까 말이지."'
            '내 위로가 서툴다고 한 것 치고는 스칼렛의 말 돌리는 솜씨가 서툴었다.'
            '자꾸 웃음이 나오는 나도 이상한 것 같았다.'
            hide Scarlet_pout with Dissolve(1.0)
            # 점심으로 점프
            pass
        "나쁜 꿈은 이제 끝이니까":
            # 호감도 상승
            player '"나쁜 꿈은 이제 끝이야. 그 꿈에는 내가 없었잖아?"'
            hide Scarlet_Sad with None
            show Scarlet_inflate at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
            voice Scarlet_172
            scarlet '"...무슨 말이 하고 싶은 거지?"'
            player '"나는 그냥, 너가 힘들어할 때 최대한 도와줄 수 있는 사람이라고..."'

            hide Scarlet_inflate with None
            show Scarlet_lookout at scarlet_standsize_ms with Dissolve(.5 ,alpha = True)
            voice Scarlet_173
            scarlet '"흥, 가소롭군. 뭐... 귀엽긴 하다만."'
            '피식 웃는 스칼렛의 얼굴에는 옅은 홍조가 떠올랐다.'

            pass
    jump D_2_Lunch
    return

label Say_To_Isabel:
    stop music fadeout 1.0
    scene bg black with Dissolve(1.0 ,alpha = True)
    '이자벨은 저택 밖으로 나간다고 했었지?'
    '...조금 걱정되네.'
    '이자벨은 몸도 약하고, 밖에 나가본 적 없을 테니까.'

    '이자벨을 쫓아가기로 마음먹고 저택 밖으로 나섰다.'
    '출발한 지 얼마 되지 않았는지 정원에 있는 이자벨과 마주쳤다.'
    play sound Footstep_flower_2
    scene bg BG_Garden_Morning with Dissolve(1.0,alpha = True)
    play music Isabel_2 fadein 2.0
    player '"저기, 이자벨!"'
    show Isabel_nodap at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_137
    isabel '"무슨 일이신가요, [player_name] 씨."'
    player '"그게... 나도 같이 갈 수 있을까?"'
    player '"걱정돼서 말이야."'

    hide Isabel_nodap with None
    show Isabel_lookout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_138
    isabel '"..."'

    hide Isabel_lookout with None
    show Isabel_Laughter at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_139
    isabel '"좋아요. 함께 가죠."'
    voice Isabel_140
    isabel '"혼자서 가는 건 조금 불안했거든요."'
    player '"응, 왜?"'

    hide Isabel_Laughter with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_141
    isabel'"...[player_name] 씨도 아시다시피, 저는 몸이 안 좋잖아요?"'
    voice Isabel_142
    isabel'"병원 침대에만 누워있었던 탓에 체력이 무척 안 좋아요."'

    hide Isabel_pout with None
    show Isabel_lookout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_143
    isabel '"여러 가지 실험해 보고 싶어서 짐을 챙겼는데..."'

    # 가방 출력
    hide Isabel_lookout with None
    show screen Mini_Scene(bag) with Dissolve(1.0)
    '이자벨은 자연스럽게 등에 매고 있던 가방을 내게 주었다.'

    play sound standup
    player '"우왓"'
    '생각보다 무거운 가방의 무게에 놀랐다.'
    player '"혼자서 이걸 지고 가려고 했던 거야?"'

    hide screen Mini_Scene with Dissolve(1.0)
    # 가방 하이드
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_144
    isabel '"네, 다른 분들의 도움을 기대하긴 힘들 것 같았거든요."'
    player '"... 내가 들 테니까 어서 가자."'

    hide Isabel_pout with None
    show Isabel_Happy at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_145
    isabel '"감사해요. [player_name] 씨가 있어서 다행이네요."'
    play sound Footstep_flower_2

    '밝게 미소 지은 이자벨은 씩씩한 걸음으로 앞장섰다.'
    '뭔가 이용당했다는 느낌이 들지만... 툭 밀면 쓰러질 것 같은 애한테 짐을 돌려줄 수도 없고.'
    play sound Footstep_flower_2

    '가방을 메고서는 이자벨을 쫓아갔다.'
    scene bg BG_Hill with Dissolve(1.0 ,alpha = True)
    play sound sea_waves_3
    show Isabel_panic at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_146
    isabel '"정말로... 당신 말대로네요."'

    hide Isabel_panic with None
    show Isabel_Normal at isabel_standsize_bs with Dissolve(.5 )
    voice Isabel_147
    isabel '"바다 위에 떠 있는 섬이라... 이런 걸 제 두 눈으로 보게 될 줄은 몰랐어요."'
    player '"너무 몸을 앞으로 빼지마, 그러다 빠질라."'
    '내 걱정에 이자벨은 웃으며 물었다.'

    hide Isabel_Normal with None
    show Isabel_Laughter at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_148
    isabel '"걱정해 주시는 거예요?"'
    player '"응? 당연하지."'
    hide Isabel_Laughter with None
    show Isabel_nodap at isabel_standsize_bs with Dissolve(.5 )
    $renpy.pause(1.5)
    hide Isabel_nodap
    show Isabel_lookout at isabel_standsize_bs
    with Dissolve(1.0 ,alpha = True)
    $renpy.pause(1.0)
    '이자벨은 알기 어려운 표정으로 나를 바라보다, 다시 바다를 바라봤다.'

    hide Isabel_lookout with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_149
    isabel '"서재에서 이런 책을 찾았어요."'

    hide Isabel_pout with Dissolve(.5)
    show screen Mini_Scene(Book) with Dissolve(.5)
    '이자벨이 내게 얇은 책 한 권을 건네주었다.'
    player '"이 책은..."'

    hide screen Mini_Scene with Dissolve(.5)
    hide Isabel_pout with None
    show Isabel_nodap at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_150
    isabel '"이곳에 왔던 다른 메이드, 혹은 주인의 기록이죠."'
    voice Isabel_151
    isabel '"이 사람은 섬을 빠져나갈 방법을 찾았던 것 같아요..."'

    play sound book_flipping # 문제 있음
    '이자벨의 이야기를 들으며 책장을 넘겼다.'

    '\'나는 바다에 뛰어들었으나, 눈을 떴을 때는 원래의 자리로 돌아와있었다.\''
    '\'카론에게 뱃삯을 주지 않은 탓일까? 동전을 혀 밑에 넣고 다시 한번 뛰어들었다.\''
    '\'결과는 실패. 혀 밑의 동전만 사라져 있었다.\''
    '뒷장에도 비슷한 내용이 반복되었다.'
    player '"계속 시도했던 것치고는 전부 실패했네..."'

    hide Isabel_nodap with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5, alpha = True)
    voice Isabel_152
    isabel '"그렇죠. 무의미하다 볼 수도 있지만... 그래도 저는 이 사람이 이렇게 기록을 남겨줘서 정말 고마워요."'

    voice Isabel_153
    isabel '"하나하나 시도해 보면 여기서 나갈 방법을 찾을 수 있을지도 몰라요."'
    player '"굳이 실패했던 일을 다시 시도해 보는 이유가 있어?"'
    '내 말을 들은 이자벨은 책의 마지막 장을 가리켰다.'

    hide Isabel_pout with None
    show Isabel_Normal at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_154
    isabel '여길 보세요. \'돌아갈 방법을 찾은 것 같다.\' 라고 쓰여 있죠?'
    voice Isabel_155
    isabel '"이 문장을 끝으로 책에는 아무것도 기록되어 있지 않아요."'
    '이자벨을 한 번, 책을 한 번 들여다보았다.'
    player '"이 많은 방법을 시도하던 도중, 방법을 찾은 것 같다고 생각하는 거야?"'

    hide Isabel_Normal with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_156
    isabel '"네. 다른 어떤 기록도 없으니... 분명히 모든 방법을 시도해 보는게 맞는다고 생각해요 저는."'
    '생각보다 우직한 이자벨의 태도에 무슨 말을 해야 할지 모르겠다.'
    '조금은 미련해 보일 수 있지만, 그 모든 시도가 의미 없는 건 아니다.'
    player '"좋아, 몸을 써야 하는 일은 전부 내가 할 테니까... 너는 옆에서 기록하고 있어줄래?"'

    hide Isabel_pout with None
    show Isabel_Normal at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_157
    isabel '"위험한 일은 제가 할게요."'
    player '"응?"'

    hide Isabel_Normal with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_158
    isabel '"아무리 죄인의 신분으로 왔다지만, 저도 양심이 있는 사람이에요."'

    hide Isabel_pout with None
    show Isabel_nodap at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_159
    isabel '"도와준다는 사람에게 위험한 일을 어떻게 시켜요?"'
    '책에는 바다에 몸을 던지는 등, 위험한 행동이 몇 가지 있었다.'
    '이자벨이 저런 반응을 보이는 건 무리도 아니지만...'
    player '"기록대로라면 크게 위험하진 않을 것 같으니까 내가 할게."'

    hide Isabel_nodap with None
    show Isabel_heung at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_160
    isabel '"... 아뇨, 제가 할게요."'
    player '"걱정하지 않아도 괜찮아. 나 이래 봬도 다이빙도 배워서 높은 곳에서 떨어지는 건 무섭지 않아."'
    player '"고소공포증 같은 것도 없고 말이지!"'

    hide Isabel_heung with None
    show Isabel_Normal at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_161
    isabel '"...그렇게 말씀하신다면, 염치없지만 부탁할게요."'

    hide Isabel_Normal with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_162
    isabel '"뛰어내릴 때 링거를 어떻게 해야 할지 정하지 못했거든요."'
    '이자벨의 실없는 농담에 작은 웃음이 터져 나왔다.'
    player '"그래, 한 번 해보자고."'

    hide Isabel_pout with None
    '이자벨이 건네준 동전을 있는 힘껏 바다를 향해 던졌다.'
    '바다와 절벽 사이의 거리가 커서, 동전이 제대로 빠졌는지 확인할 수 없었다.'
    player '"음... 아무런 변화도 없어."'

    show Isabel_nodap at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_163
    isabel '"그러면... 다음에는 이거예요."'

    show screen Mini_Scene(GlassBottle , _x = 0.5, _y = 0.5) with Dissolve(.5)
    '이자벨은 편지가 든 유리병을 내게 건네주었다.'
    '동전과 마찬가지로 큰 변화는 없었다.'
    '나와 이자벨은 여러 가지 시도를 했지만 의미 있는 결과는 없었다.'

    hide screen Mini_Scene with Dissolve(.5)

    hide Isabel_nodap with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_164
    isabel '"모두 책에 나왔던 대로네요..."'
    voice Isabel_165
    isabel '"당신이 바다에 뛰어들었을 때의 반응도 책과 똑같고..."'
    player '"이상한 경험이었어. 눈을 떠보니 뛰어들기 전과 같은 자리에 있고..."'
    hide Isabel_pout with None
    show Isabel_nodap at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_166
    isabel '"이제 책에 나온 방법은 모두 시도해 봤어요."'
    player '"그래?"'
    play sound standup
    '이자벨의 말을 들은 나는 자리에 주저앉았다.'
    '너무 많은 일을 하다 보니 조금은 지쳤다.'
    player '"이대로 누워서 낮잠이라도 자고 싶은데~"'
    hide Isabel_nodap with None
    show Isabel_Normal at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_167
    isabel '"관리자 씨한테 혼나면 어쩌려고요?"'
    player '"나는 주인님이니까 청소에서는 열외야."'

    hide Isabel_Normal with None
    show Isabel_heung at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_168
    isabel '"그런 식으로 권력을 써먹으려는 거예요?"'
    player '"평소에는 못 쓰는 거, 지금이라도 써야지."'

    hide Isabel_heung with None
    show Isabel_Laughter at isabel_standsize_bs with Dissolve(.5 )
    '씨익 웃은 나를 본 이자벨도 마주 웃었다.'

    hide Isabel_Laughter with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5 )
    voice Isabel_169
    isabel '"이 책의 주인은 대체 어디서 나갈 방법을 깨달은 걸까요..."'
    voice Isabel_170
    isabel '"당신은 눈치 채셨나요?"'
    player '"응? 아니... 왜?"'
    hide Isabel_pout with None
    show Isabel_nodap at isabel_standsize_bs with Dissolve(.5 )
    voice Isabel_171
    isabel'"저는 지켜보기만 했으니까, 직접 움직인 사람의 의견은 다를 수도 있잖아요."'
    player '"나는 잘 모르겠는데? 숙제를 하는 마음으로 해서 그랬던 걸까."'
    hide Isabel_nodap with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5 )
    voice Isabel_172
    isabel '"으음..."'
    voice Isabel_173
    isabel '"답을 찾으려면 제가 직접 했어야 할까요?"'
    voice Isabel_174
    isabel '"제게 절실함이 부족해서 생긴 일이네요."'
    voice Isabel_175
    isabel '"절실함이 부족하다..."'

    hide Isabel_pout with None
    show Isabel_Happy at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_176
    isabel '"푸흣..."'
    '혼자 중얼거리던 이자벨은 갑자기 웃음을 터트렸다.'
    player '"뭐가 웃긴 거야?"'

    hide Isabel_Happy with None
    show Isabel_Laughter at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_176
    isabel '"그냥 이 상황 자체가 웃겨요."'
    player '"응?"'
    '이자벨은 내 옆에 앉으며 바다를 바라봤다.'

    hide Isabel_Laughter with None
    show Isabel_Normal at isabel_standsize_bs with Dissolve(.5 )
    voice Isabel_177
    isabel '"제가 아무런 이유도 없이 저택에 왔다고 생각하지 않아요."'

    voice Isabel_178
    isabel '"다른 사람의 사정은 모르지만... 죄를 지었기 때문에 이런 곳에 왔다고 생각해요."'
    player '"그게 무슨..."'

    voice Isabel_179
    isabel '"저는 제가 언제 죽어도 상관없다고 생각하고 있었어요."'

    hide Isabel_Normal with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_180
    isabel '"이런 몸이니까 차라리 죽는게 주변 사람들에게 나을 거라고 생각했고..."'

    hide Isabel_pout with None
    show Isabel_lookout at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_181
    isabel'"원하던 대로 죽을 때가 되니까 살기 위해 발버둥 치고 있네요?"'

    hide Isabel_lookout with None
    show Isabel_Happy at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_182
    isabel '"제 행동이 너무 모순적이라서... 웃겨요."'
    '갑자기 치고 들어오는 진지한 이야기에 어떤 표정을 지어할지 모르겠다.'

    hide Isabel_Happy with None
    '정말 어지간한 부자가 아닌 이상 환자를 돌보는 건 힘들다고 들었던 기억이 있다.'
    player '"나는 네 상황이 어떤지 잘 모르지만... 나는 도저히 웃을 수 없어."'
    player '"주위 사람들을 소중하게 여겨서 네가 죽는게 낫다는 결론을 내린 거잖아?"'
    player '"살고 싶어지는 건 당연한 행동이고, 가족들에게 아직 아무런 인사도 못했잖아."'
    player '"네가 돌아가기 위해 노력하는 게 난 당연하다 생각해."'

    hide Isabel_pout with None
    show Isabel_Normal at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_183
    isabel '"위로는 고맙지만, 많이 들어봤던 이야기네요."'
    player '"그... 그래? 아직 이런 일에는 미숙해서."'

    hide Isabel_Normal with None
    show Isabel_Laughter at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_184
    isabel '"그래도 충분히 위로가 되었어요. 고마워요."'

    voice Isabel_186
    isabel '"슬슬 돌아갈까요? 관리자 씨가 말한 시간에 늦을지도 몰라요."'
    player '"아, 응."'
    hide Isabel_Laughter with None

    play sound standup
    '먼저 자리에서 일어나 이자벨을 향해 손을 뻗었다.'
    play sound Footstep_flower_2
    '손을 잡고 일어난 이자벨은 뒤도 돌아보지 않고 저택을 향해 걸어갔다.'
    '저리 차갑게 행동할 때면 별로 친해질 생각이 없는 것인가 싶다가도...'
    '태도라던가 이것저것 신경 쓰는 걸 보면 다정해서, 어느 쪽이 맞는 건지 헷갈렸다.'

    player '"생을 포기한 죄..."'
    '이야기를 들어보니 이자벨은 딱히 자살을 했던 것도 아닌 것 같다.'
    '삶의 의지를 잃어버렸단 이유로 죄인 취급을 받을 수 있는 걸까?'
    '주변 사람에게 민폐 끼치기 싫다는 상냥한 마음이 바탕이 된 건데...'

    play sound Footstep_flower_2
    '곰곰이 생각하면서 저택으로 발을 옮겼다.'
    scene bg black with Dissolve(1.0)
    # 점심으로 점프

    jump D_2_Lunch


    # hide
    return

label Say_To_Elice:
    stop music fadeout 1.0
    scene bg black with Dissolve(1.0 )
    '그러고 보니 엘리스는 서재에 간다고 했었지?'
    '서재는 이자벨이라는 공식이 성립되어 있다고 생각 했는데...'
    '엘리스는 서재에서 무엇을 할까? 궁금했기 때문에 서재로 갔다.'
    '문을 열자마자 보이는 건, 집중해서 책을 읽고 있는 엘리스다.'

    stop music fadeout 1.0
    play music Elicetheme fadein 1.0
    play sound DoorOpen2
    scene bg BG_Adimroom with Dissolve(1.0)
    show Elice_Surprised at elice_standsize_bs with Dissolve    (1.5 ,alpha = True)
    voice Elice_170
    elice '"...무슨 일이지?"'
    player '"응?"'

    voice Elice_171
    elice '"내게 용건이 있어서 찾아온 게 아닌가?"'

    hide Elice_Surprised with None
    show Elice_Normal at elice_standsize_bs with Dissolve(.5)
    voice Elice_172
    elice '"책을 읽고 싶어서 서재에 올 사람으로는 안 보이는데 말이지."'
    player '"윽, 딱히 틀린 말은 아니지만..."'
    '내가 서재에 들어가자 엘리스는 읽고 있던 책을 덮었다.'
    player '"책 같은 건 안 볼 줄 알았는데..."'

    hide Elice_Normal with None
    show Elice_Contempt at elice_standsize_bs with Dissolve(.5)
    voice Elice_173
    elice '"뭐?"'
    player '"멍청하다는 뜻이 아니라, 원래 왕이라는 건 지식인들에게 명령하는 위치에 있잖아?"'
    player '"직접 알아보지 않고 다른 사람에게 알아보게 한 다음 결과를 듣는게 왕의 역할이 아닌지..."'
    '의견에 자신이 없었기 때문에 말소리가 점점 줄어들었다.'

    hide Elice_Contempt with None
    show Elice_Coloration at elice_standsize_bs with Dissolve(.5)
    '엘리스는 세상 멍청한 것을 보는 눈으로 나를 봤다.'

    hide Elice_Coloration at elice_standsize_bs with None
    show Elice_Coloration_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_174
    elice '"내 스스로가 아는게 없으면, 아무리 요약된 정보를 들어도 이해하지 못해."'
    voice Elice_175
    elice '"지식을 쌓는 건 왕족의 기본 소양. 두 번 다시 그리 멍청한 소리는 하지마."'
    player '"아...응."'

    '엘리스의 태도는 무척이나 재수가 없었지만, 옆에 쌓여있는 책의 양은 절대로 무시할 것이 못 되었다.'
    '재수가 없는 건 없는 거고, 대단한 건 대단한 거지.'
    '고작 태도 하나 때문에 상대방의 진가를 깎아내리고 싶지 않았다.'
    '엘리스가 어떤 책을 읽었는지 살펴보던 도중, 눈에 익은 책이 보였다.'
    player '"이건... 내 책인데."'

    '고등학교 세계사 교과서를 이렇게 뜬금없는 곳에서 보게 될 줄은 몰랐다.'
    '책등에 적어놓은 이름이나, 페이지 중간중간에 있는 낙서는 이 교과서의 주인이 나라는 걸 강력하게 주장하고 있었다.'

    hide Elice_Coloration_2 with None
    show Elice_coldsmiley at elice_standsize_bs with Dissolve(.5)
    voice Elice_176
    elice '"...책에 글을 쓰는 멍청이가 누군가 했더니."'
    '엘리스는 내가 정성 들여 쓴 필기를 흘겨보며 말했다.'
    player '"이건 교육용 책이라고! 원래 이런 식으로 글을 쓰는게 맞아!"'

    hide Elice_coldsmiley with None
    show Elice_Strong at elice_standsize_bs with Dissolve(.5 )
    voice Elice_177
    elice '"흐음...."'
    '엘리스는 의심스러운 눈빛으로 나를 바라봤지만, 나는 당당하다.'
    '혹시라도 이상한 낙서를 해두었나, 책을 촤르르 펼쳐보던 도중 한 페이지가 접혀 있는 걸 봤다.'
    '접힌 페이지에는 프랑스 혁명에 관한 내용이 쓰여 있었다.'
    '권력이 왕족에게서 자본가에게 넘어간 사건이었지...'
    '이후 유럽에 전체적으로 혁명의 바람이 분 것은 누구나 아는 사실.'
    '별생각없이 읽어내리다가 엘리스를 바라봤다.'
    '엘리스가 사는 세계에서는 아직 낯선 이야기려나.'

    hide Elice_Strong with None
    show Elice_Difficulty at elice_standsize_bs with Dissolve(.5)
    voice Elice_178
    elice '"네가 살던 세계에서는 이런 일이 흔한가?"'
    player '"어떤 일을 말하는 거야?"'

    hide Elice_Difficulty with None
    show Elice_Strong_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_179
    elice '"시민들이 왕을 끌어내려 죽이는 일."'
    player '"으음, 지금은 별로 흔하지 않아."'
    player '"전에는 흔했지만... 이제는 왕족에게 그런 일을 할 가치가 없거든."'

    hide Elice_Strong_2 with None
    show Elice_Surprised at elice_standsize_bs with Dissolve(.5)

    '내 말을 들은 엘리스는 흥미롭다는 듯 눈을 반짝였다.'
    voice Elice_180
    elice '"무슨 뜻이지?"'
    player '"나라를 운영하는 건 왕족이 아니라 다른 사람의 역할이거든."'
    player '"나라가 제대로 굴러가지 않았을 때 책임지는 건 그 사람의 역할이야."'

    hide Elice_Surprised with None
    show Elice_Coloration at elice_standsize_bs with Dissolve(.5)
    voice Elice_181
    elice '"왕족은 무엇을 하고?"'
    player '"그들은 상징으로 존재하지."'
    player '"왕이 아니라면, 왕족을 그만둘 수도 있고 말이야."'
    '내 이야기를 들은 엘리스는 놀랍다는 표정을 지었다.'

    hide Elice_Coloration with None
    show Elice_Difficulty at elice_standsize_bs with Dissolve(.5)
    voice Elice_182
    elice '"신기한 이야기네..."'
    player '"어떤 부분이 신기한 거야?"'

    hide Elice_Difficulty with None
    show Elice_Difficulty_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_183
    elice '"네가 사는 곳에는 왕족이 없다는 것부터."'
    '나는 어깨를 으쓱였다. 한국에 왕이 있는게 더 이상한걸.'
    player '"언젠가 시간이 흐르면 네가 살고 있는 곳도 이런 식으로 변할걸?"'

    hide Elice_Difficulty_2 with None
    show Elice_Strong_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_184
    elice '"왕족이 사라진다..."'
    '엘리스는 책에서 시선을 떼고 창밖을 바라보았다.'

    hide Elice_Strong_2 with None
    show Elice_Laughter at elice_standsize_bs with Dissolve(.5)
    voice Elice_185
    elice '"그때가 오면 어디로 가야 할지 모르겠지만... 나쁘지 않네."'
    '푸른 하늘을 보는 엘리스는 미소를 짓고 있었다.'
    player '"싫지 않아?"'

    hide Elice_Laughter with None
    show Elice_Normal at elice_standsize_bs with Dissolve(.5)
    voice Elice_186
    elice '"글쎄. 아쉽지만 홀가분하다는 느낌도 있어."'
    voice Elice_187
    elice '"왕족이라는 자리가 주는 부담감은 꽤나 무겁거든."'

    hide Elice_Normal with None
    show Elice_coldsmiley at elice_standsize_bs with Dissolve(.5)
    voice Elice_188
    elice '"원해서 왕족이 된 것은 아니지만, 죽지 않기 위해서는 열심히 해야 했지."'
    voice Elice_189
    elice '"왕족으로서의 쓸모를 다하지 않으면 부모에게 버림받고, 너무 잘하면 형제들에게 목숨을 위협받고..."'
    player '"복잡하네."'

    hide Elice_coldsmiley with None
    show Elice_coldsmiley_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_190
    elice '"복잡하지? 그런 게 당연한 세상에서 살다가 왕이 없는 세계의 이야기를 들었는데... 어떻게 신기하지 않겠어."'
    '한참 동안 창밖을 바라보던 엘리스는 손에 들고 있던 책을 덮었다.'

    hide Elice_coldsmiley_2 with None
    show Elice_Ignore_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_191
    elice '"왕이 된 걸 후회하지 않아."'

    hide Elice_Ignore_2 with None
    show Elice_Gladness at elice_standsize_bs with Dissolve(.5)
    voice Elice_192
    elice '"다른 인생을 사는 날 상상해 보지 못한 것이 아쉬울 뿐이지."'

    hide Elice_Gladness with None
    show Elice_Gladness_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_193
    elice '"왕이 없는 건 어디까지나 네 세상의 이야기..."'
    player '"어, 응..."'
    voice Elice_194
    elice '"내가 사는 세상이 너의 세상처럼 변하려면 시간이 꽤나 걸릴 거야."'

    hide Elice_Gladness_2 with None
    show Elice_Normal at elice_standsize_bs with Dissolve(.5)
    voice Elice_195
    elice '"언제가 될지 모르는 미래를 가정하는 건 바보 같은 일이라는 짓이지."'

    hide Elice_Normal with None
    show Elice_Pudency_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_196
    elice '"하지만... 그리 나쁘지 않았어. 흥미롭기도 했고."'
    '자리에서 일어나는 엘리스를 붙잡고 나는 물었다.'
    player '"더 궁금한 게 있다면 언제든 물어봐도 괜찮아."'
    player '"내가 아는 것 안에서 무엇이든지 대답해줄테니까."'

    hide Elice_Pudency_2 with None
    show Elice_Gladness at elice_standsize_bs with Dissolve(.5)
    voice Elice_197
    elice '"그래?"'
    '엘리스는 나를 빤히 바라보았다.'

    hide Elice_Gladness with None
    show Elice_Committed at elice_standsize_bs with Dissolve(.5)
    voice Elice_198
    elice '"그럼 여기서 어떻게 나갈 수 있는지도 말해줄 수 있어?"'
    player '"윽, 그건..."'

    hide Elice_Committed with None
    show Elice_Committed_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_199
    elice '"...."'
    player '"말할 수 없어."'

    hide Elice_Committed_2 with None
    show Elice_Strong at elice_standsize_bs with Dissolve(.5)
    voice Elice_200
    elice '"알고는 있단 뜻이군."'
    player '"윽!"'

    hide Elice_Strong with None
    show Elice_Laughter at elice_standsize_bs with Dissolve(.5)
    voice Elice_201
    elice '"내 세계로 돌아가면 너를 광대로 채용하도록 하지."'

    hide Elice_Laughter with None
    show Elice_Laughter_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_202
    elice '"지켜보는 재미가 있어."'
    player '"사람을 광대 취급하지 마!"' with vpunch

    play sound FootStep1
    hide Elice_Laughter_2 with Dissolve(1.0)

    '엘리스는 소리 내서 웃으며 다른 책을 찾으러 갔다.'
    '사람을 놀리기나 하고!'
    '사색에 잠긴 얼굴보다는, 웃는 얼굴이 훨씬 보기 좋았지만...'
    '미묘한 기분을 어찌 해결해야 할지 모르겠다.'
    scene bg black with Dissolve(1.0)
    jump D_2_Lunch


    return

label Say_To_Sarang:
    stop music fadeout 1.0
    scene bg black with Dissolve(1.0)
    '윤사랑이 여전히 마음에 걸렸다.'
    '무언가 기억날 듯하면서도, 기억나지 않는 것이...'
    '그냥 내버려 두기에는 찜찜했다.'
    '다른 메이드들이 자리를 뜨는 동안, 나는 계속 내 자리에 앉아있었다.'
    '한참 동안 나를 바라보던 윤사랑이 물었다.'

    scene bg BG_Livingroom with Dissolve(1.0)
    play music Yunsarang_1 fadein 1.0
    show Yun_Normal at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_202
    yun '"주인님은 다른 곳에 가지 않으시나요?"'
    player '"응. 너랑 이야기를 나누고 싶어서."'

    hide Yun_Normal with None
    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_203
    yun '"그으... 가, 감사합니다."'

    play sound standup
    '얼굴을 붉힌 윤사랑은 자리에서 일어나 식기를 치우기 시작했다.'
    player '"아, 나도 도와줄게."'

    hide Yun_fallinlove with None
    show Yun_panic at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_204
    yun '"괘, 괜찮아요...! 으악!"'
    '윤사랑이 들고 있던 식기를 받기 위해 손을 내밀었을 때의 일이었다.'

    play sound Glass
    '윤사랑의 손에서 미끄러진 식기 하나가 바닥에 떨어지고, 쨍그랑하는 소리와 함께 깨졌다.'

    hide Yun_panic with None
    show Yun_tear at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_205
    yun '"으아아... 또 실수했어요..."'
    '윤사랑은 금방이라도 울 것 같은 표정을 하고서는 허겁지겁 유리 조각을 주웠다.'

    hide Yun_tear with None
    show Yun_panic at yun_standsize_bs with Dissolve(.5)
    show Yun_panic at yun_one_jump_bs with None
    voice Yunsarang_206
    yun '"아야!"'
    player '"베인 거야?"'

    hide Yun_panic with None
    show Yun_Sad at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_207
    yun '"네에... 죄, 죄송해요..."'
    player '"일어나 봐. 치우는 건 내가 할 테니까."'
    # play sound 'audio/EffectSound/빗자루 소리'
    '유리 조각을 치우던 윤사랑을 뒤로 물리고, 빗자루를 찾아와 바닥에 남은 조각들을 쓸어냈다.'
    player '"맨손으로 하니까 위험하지. 다음부터는 조심해."'

    hide Yun_Sad with None
    show Yun_tear at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_208
    yun '"네, 네에...."'
    player '"깊게 베였어? 한 번 보여줘 봐."'
    '윤사랑의 손을 가져와서 자세히 들여다보았다.'
    '다행히 살짝 스친 정도이지만, 묘하게 거스릴 만한 위치였다.'
    player '"구급상자 가져올 테니까, 여기서 기다리고 있어."'

    hide Yun_tear with None
    show Yun_panic at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_209
    yun '"제, 제가 가져올게요!"'
    player '"그러다 또 다치려고?"'

    hide Yun_panic with None
    show Yun_Sad at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_210
    yun '"그으... 그렇지는 않... 죄, 죄송해요!"'
    player '"장난이니까 너무 미안해하지 마."'
    '선반에 있던 구급상자를 가져와 윤사랑의 손가락에 반창고를 붙여주었다.'
    '얘는 멀쩡해 보이는 애가 정말 뜬금없이 넘어지고, 다치고 하는지 모르겠다.'
    '식당에 마가 낀 건가?'
    player '"여기서는 병원도 못 가니까 조심해."'

    hide Yun_Sad with None
    show Yun_Happy at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_211
    yun '"네... 그래도 주인님이 계셔서 다행이에요."'

    hide Yun_Happy with None
    show Yun_pout at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_212
    yun '"저 혼자 치웠으면 하나로 끝나지 않았을걸요?"'
    player '"그건 나도 동감해."'
    '썼던 약과 반창고를 정리하며 실없는 대화를 나누던 도중이었다.'

    hide Yun_pout with None
    show Yun_Happy at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_213
    yun '"그런 주인님을 좋아해요."'
    player '"응?"'

    hide Yun_Happy with None
    show Yun_Normal at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_214
    yun '"...제가 무슨 말 했나요?"'
    player '"방금, 나를 좋아한다고..."'

    hide Yun_Normal with None
    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5)
    '윤사랑의 얼굴이 금방이라도 터질 것 같은 토마토가 되었다.'
    hide Yun_fallinlove with None
    show Yun_panic at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_215
    yun '"아니, 저는, 그게, 이건...."'
    voice Yunsarang_216
    yun '"저는.... 그, 그런 뜻으로 한 말이 아니었어요!"'
    '당황한 윤사랑이 소리를 빽 질렀다.'
    player '"그런 뜻...?"'

    hide Yun_panic with None
    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_217
    yun '"주인님을 좋아하지만, 연애의 감정이 아니라... 그냥 친구 같은 감정이에요!"'
    player '"아... 그, 그런 거야?"'

    hide Yun_fallinlove with None
    show Yun_pout at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_219
    yun '"네... 주인님이 참 좋은 사람이라서 좋아한다고 말한 거예요."'

    hide Yun_pout with None
    show Yun_panic at yun_standsize_bs with Dissolve(.5)
    show Yun_panic at yun_one_jump_bs with None
    voice Yunsarang_220
    yun '"절대로 주인님이 저랑 사귀어 준다거나, 하나밖에 없는 연인이 된다거나."'

    show Yun_panic at yun_one_jump_bs with None
    voice Yunsarang_221
    yun '"저랑 결혼해서 부부가 되어서 평생을 함께할 동반자가 되길 바란 적..."'

    show Yun_panic at yun_one_jump_bs with None
    voice Yunsarang_222
    yun '"절대로 없으니까!"'
    '벌써 부부가 되는 상상까지 했었구나.'
    '필사적으로 아닌 척하려는 모습이 귀여워서, 한 번쯤 찔러보고 싶다는 생각이 든다.'
    '놀리면 울 것 같은데...'
    '불쌍하니까 그만해야지.'
    player '"그래, 그런 식이라면 나도 좋아해."'

    hide Yun_panic with None
    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_223
    yun '"네?"'
    player '"조금 덜렁거리지만, 열심히 하는 너를 좋아해. 친구로서 말이지."'
    hide Yun_fallinlove with None
    show Yun_Sad at yun_standsize_bs with Dissolve(.5)
    show Yun_Sad at yun_one_jump_bs with None
    voice Yunsarang_224
    yun '"그...네, 가, 감사합니다..."'
    '윤사랑은 무언가 아쉽다는 표정으로 나를 바라봤지만, 원하는 말을 해줄 생각은 조금도 없었다.'
    '언젠가 좋아한다고 제대로 고백해 주면, 그때는 윤사랑이 원하는 답을 해줄 수도 있지 않을까?'
    hide Yun_Sad with None
    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_225
    yun '"그... 저는 잠시 바람 좀 쐬고 올게요."'
    '붉어진 얼굴의 윤사랑은 복도로 나가고, 식당에 남은 건 나 혼자뿐이었다.'
    scene bg black with Dissolve(1.0)
    $ renpy.pause(1.0, hard = True)
    # 점심으로 점프
    jump D_2_Lunch

    return

label D_2_Lunch:
    stop music fadeout 1.0
    scene bg black with Dissolve(2.0)
    play music Normal_a fadein 5.0
    scene bg BG_Livingroom with Dissolve(2.0)
    '점심이라고 해서 딱히 다른 것은 없었다.'
    '관리자는 밥상만 차리고 사라졌고, 다들 아무 말 없이 자리에 앉았다.'
    '학교의 급식실은 지나치게 시끄러웠지만, 이런 부담감은 없었는데...'
    '침묵만 가득한 식당이 껄끄러워, 다른 사람들을 살펴보았다.'

    show screen Mini_Scene(prayer, _x = 0.5, _y = 0.06) with Dissolve(.5)
    # show screen Scarlet_prayer with Dissolve(1.0)
    '스칼렛이 손을 모으고서는 기도하는 모습이 눈에 띄었다.'
    '계속 말하는 \'위대하신 그 분\'을 위한 기도인걸까?'
    hide screen Mini_Scene with Dissolve(1.0)
    player '"저기, 스칼렛."'

    show Scarlet_pout at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_188
    scarlet '"...뭐지?"'
    '기도를 끝낸 듯, 손을 내린 스칼렛이 나를 보며 물었다.'
    player '"방금한 건 뭐야? 식전 기도?"'
    hide Scarlet_pout with None
    show Scarlet_nonSad  at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_189
    scarlet '"아아... 그래. 그 분께 식사를 할 수 있는 몸을 주어서 감사하다는 뜻을 전하고 있었지."'
    voice Scarlet_190
    scarlet '"제대로 전달되었는지는 모르겠다만..."'

    hide Scarlet_nonSad with None
    show Scarlet_Normal at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_191
    scarlet '"내 혀가 제대로 맛을 느낄 수 있는 것도 다 그 분 덕 아니겠어?"'
    '스칼렛은 의기양양한 표정으로 기도에 대해서 주저리 주저리 떠들었다.'
    '어색했던 분위기가 순식간에 사라지는 것 같았다.'
    '역시 스칼렛에게 말을 걸기 잘했어!'

    show Elice_Ignore at elice_standsize_ms_L with Dissolve(.5 )
    show Yun_Happy at yun_standsize_ms_R with Dissolve(.5)
    '엘리스는 이쪽에 시선 한 번 주지 않았고, 윤사랑도 곤란한 듯 웃으며 눈으로는 \'또 시작이네...\' 라고 말하지만.'
    '이렇게 시끌벅적한 게 원래 식사자리 아니겠어?'

    hide Scarlet_Normal
    hide Yun_Happy
    hide Elice_Ignore
    with Dissolve(.5)
    show Scarlet_Laughter at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_192
    scarlet '"그래서 말이지, 네 녀석도 해보지 않겠나?"'
    player '"으응? 나도?"'
    hide Scarlet_Laughter with None
    show Scarlet_Normal at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_193
    scarlet '"그래. 네가 멀쩡히 잘 살아있는 것도 다 그 분의 은총 덕분이지."'
    voice Scarlet_194
    scarlet '"그러니 너도 그 분께 감사 인사를 드리는게 좋을거다!"'
    player '"글쎄...? 제대로 된 신도도 아닌 내가 기도하는 건 그 분도 싫어하지 않을까?"'

    play sound Thud1
    with vpunch
    '내 말을 들은 스칼렛은 책상을 쾅 내리쳤다.'

    hide Scarlet_Normal with None
    show Scarlet_ppagchim at scarlet_standsize_ms with Dissolve(.5)
    show Scarlet_ppagchim at scarlet_one_jump with None
    voice Scarlet_195
    scarlet '"지금 내 앞에서 그 분을 욕보이는 것이냐!"'
    player '"무, 무슨 소리야!"'

    hide Scarlet_ppagchim with None
    show Scarlet_ppagchim at scarlet_standsize_bs with Dissolve(.5)
    show Scarlet_ppagchim at scarlet_one_jump_bs with None
    voice Scarlet_196
    scarlet '"네가 방금 그 분을 모욕했잖느냐! 내가 모시는 위대한 그 분은 결코 그리 속 좁은 분이 아니다!"'
    '갑자기 화를 내는 스칼렛 때문에 식당의 분위기는 아까의 침묵보다 더 처참해졌다.'
    '괜히 스칼렛에게 말을 걸어서...!'
    player '"나는 그런 뜻으로 한 말이 아니었어, 스칼렛."'
    player '"혹시라도 기분 상하게 했다면 미안해."'

    hide Scarlet_ppagchim with None
    show Scarlet_jjajeung at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_198
    scarlet '"사과를 받아야 하는 건 이 몸이 아니라 그 분이다."'
    voice Scarlet_199
    scarlet '"진실된 기도로 그분께 용서를 구하라!"'
    player '"음.... 그게 말이지."'
    '미리 말하지만 나는 철저한 무교다.'
    '신이 있다면 그렇구나. 라고 넘어갈 만큼 무관심한 사람이라고!'
    '스칼렛을 화나게 하지 않을 대답을 고르고 있을 때였다.'

    stop music fadeout 1.0
    voice Isabel_186
    isabel '"적당히 좀 하시는게 어때요?"'

    hide Scarlet_jjajeung with Dissolve(1.0)
    show Isabel_heung at isabel_standsize_ms with Dissolve(.5)
    play music horror_A_Done fadein 1.0
    '포크를 내려놓은 이자벨이 스칼렛에게 쏘아붙였다.'

    hide Isabel_heung with None
    show Isabel_stare at isabel_standsize_ms with Dissolve(.5)
    voice Isabel_187
    isabel '"주인님이 곤란해하잖아요?"'

    voice Isabel_188
    isabel '"스칼렛 씨가 어떤 신을 믿건 자유지만... 남들에게 강요하면 그건 병이거든요."'

    hide Isabel_stare
    hide Scarlet_jjajeun
    hide Yun_Happy
    hide Elice_Ignore
    with Dissolve(.5)

    show Scarlet_ppagchim at scarlet_standsize_ms_L with Dissolve(.5)
    show Isabel_stare at isabel_standsize_ms_R with Dissolve(.5)
    show Scarlet_ppagchim at scarlet_one_jump_Lms with None
    voice Scarlet_200
    scarlet '"뭐?"'

    hide Isabel_stare with None
    show Isabel_soAngry at isabel_standsize_ms_R with Dissolve(.5)
    voice Isabel_189
    isabel '"제가 못 할 말이라도 했나요?"'

    hide Scarlet_ppagchim with None
    show Scarlet_Angry at scarlet_standsize_ms_L with Dissolve(.5)
    voice Scarlet_201
    scarlet '"이봐 환자. 이 몸은 약한 녀석에게는 너그럽지만, 그렇다고 그분이 모욕 당하는 걸 참고 넘어가지는 않는다."'

    hide Isabel_soAngry with None
    show Isabel_fear at isabel_standsize_ms_R with Dissolve(.5)
    voice Isabel_190
    isabel '"제가 욕하는 건 당신의 신이 아니라, 당신이에요."'

    voice Isabel_191
    isabel '"남들에게 신과 믿음을 강요하고, 말도 안 되는 억지를 부리는 사람 말이죠."'

    show Elice_Gladness at elice_standsize_ms with Dissolve(.5)
    voice Elice_203
    elice '"호오."'

    play sound Bowl
    '계속 밥을 먹고 있던 엘리스는 식기를 내려놓았다.'
    '재밌다는 듯 이자벨과 스칼렛의 싸움에 집중하는 엘리스...'
    '윤사랑은 두 사람의 눈치만 보고 있는다.'

    hide Elice_Gladness with Dissolve(.5)
    hide Isabel_fear with None
    show Isabel_soAngry at isabel_standsize_ms_R with Dissolve(.5)
    voice Isabel_192
    isabel '"신이 모든 걸 해결해 준다는 듯한 말투도 무척이나 짜증 나요."'
    voice Isabel_193
    isabel '"결국 다 당신이 한 거잖아요? 주변 사람의 노력까지 다 신의 뜻이라니..."'

    hide Isabel_soAngry with None
    show Isabel_contempt at isabel_standsize_ms_R with Dissolve(.5)
    voice Isabel_194
    isabel '"그 입은 멍청한 신을 찬송하는 것 말고는 할 줄 몰라요?"'
    player '"이자벨, 말이 심하잖아!"'
    '점점 더 감정이 격해지는 이자벨을 붙잡았다.'
    '평소와는 다른 이자벨의 모습에 어디가 아픈 건 아닌지 걱정될 정도였지만... 이자벨에게만 신경 쓸 상황이 아니었다.'

    hide Scarlet_Angry with None
    show Scarlet_contempt at scarlet_standsize_ms_L with Dissolve(.5)
    voice Scarlet_202
    scarlet '"하, 다 죽어가는 시체 주제에 말은 술술 잘 내뱉는군."'
    player '"스칼렛!"'
    voice Scarlet_203
    scarlet '"비록 이 몸이 지금은 그 분과는 소통할 수 없지만..."'

    hide Scarlet_contempt with None
    show Scarlet_nonSad at scarlet_standsize_ms_L with Dissolve(.5)
    voice Scarlet_204
    scarlet '"내 짧은 식견으로 보아도, 네 녀석이 신에게 버림받았다는 건 쉽게 알 수 있다."'

    hide Isabel_contempt with None
    show Isabel_fear at isabel_standsize_ms_R with Dissolve(.5)
    voice Isabel_195
    isabel '"내가... 신에게 버림받았다고요?"'
    '이자벨은 주먹을 움켜쥐었다.'

    hide Scarlet_nonSad with None
    show Scarlet_contempt at scarlet_standsize_ms_L with Dissolve(.5)
    voice Scarlet_205
    scarlet '"아무리 신에게 버림받은 것이 슬퍼도, 이 몸에게 화풀이를 하면 안 되지."'
    voice Scarlet_206
    scarlet '"네가 하는 것은 고작해야 질투, 혹은 투정 밖에 안된다."'

    hide Isabel_fear
    hide Scarlet_contempt
    with None
    show Isabel_fear at isabel_standsize_bs_R
    show Scarlet_nonSad at scarlet_standsize_bs_L
    with Dissolve(.5)

    play sound Thud1
    with vpunch
    voice Isabel_196
    isabel '"너!"'
    '이자벨이 스칼렛의 멱살을 잡았다.'
    voice Isabel_197
    isabel '"그 입 다시는 나불거리지 못하게 하는 수가 있어!"'
    hide Scarlet_nonSad with None
    show Scarlet_jjajeung at scarlet_standsize_bs_L with Dissolve(.5)
    voice Scarlet_207
    scarlet '"곧 죽어가는 네놈이, 날?"'
    play sound Thud1
    with vpunch
    stop music
    player '"둘 다 그만해!"'

    hide Scarlet_jjajeung
    hide Isabel_fear
    with Dissolve(.5)

    show Yun_panic at yun_standsize_ms_L with Dissolve(.5)
    voice Yunsarang_226
    yun '"그, 그만하세요. 싸움은 좋지 않아요!"'
    show Elice_Coloration at elice_standsize_ms_R with Dissolve(.5)
    voice Elice_204
    elice '"... 곧 있으면 관리자가 올지도 모르고?"'

    hide Elice_Coloration
    hide Yun_panic
    with Dissolve(.5)

    '금방이라도 싸울 것 같은 스칼렛과 이자벨의 사이를 갈라놓았다.'
    '여기서 제일 몸이 약한 사람을 뽑으라면 1순위는 스칼렛이요, 그다음이 이자벨이다.'
    '안 그래도 좋지 않은 몸으로 무슨 싸움까지 하겠다는 건지!'
    '관리자가 온다는 엘리스의 말을 신경 쓰기라도 한 것인지 둘 다 한 발자국씩 뒤로 물러났다.'

    show Isabel_soAngry at isabel_standsize_ms_R with Dissolve(.5)
    play sound standup
    '이자벨은 한숨을 푸욱 내쉰 후 자리에 앉았다.'

    show Scarlet_stare at scarlet_standsize_ms_L with Dissolve(.5)
    $renpy.pause(1.0)
    hide Scarlet_stare with Dissolve(.5)
    play sound FootStep1
    '가만히 이자벨을 노려보던 스칼렛은 아무 말 없이 접시를 들고 자리를 떠났다.'

    hide Isabel_soAngry with None
    show Isabel_Sad at scarlet_standsize_ms with Dissolve(.5)
    voice Isabel_198
    isabel '"...분위기를 흐려서 죄송해요."'

    voice Isabel_199
    isabel '"저도 이만 가볼게요."'

    hide Isabel_Sad with Dissolve(.5)
    play sound FootStep1
    '자리에서 일어난 이자벨의 식사는 절반이 넘게 남아 있었다.'
    '저렇게 적게 먹어도 괜찮은 걸까...'

    show Yun_Sad at yun_standsize_ms_L with Dissolve(.5)
    show Elice_Surprised at elice_standsize_ms_R with Dissolve(.5)
    '윤사랑은 안절부절해 하면서도, 본인 식사를 하고 있었다.'
    '엘리스는 뭐... 걱정은커녕 무슨 일이 있기라도 했냐는 듯 자기 식사를 하고 있었다.'

    show Yun_Sad at yun_one_jump_L with None
    voice Yunsarang_227
    yun '"그, 주인님도 식사는 제대로 하시는게 좋을 것 같아요."'
    player '"응?"'

    voice Yunsarang_228
    yun '"오늘도 어제처럼 청소할 수도 있으니까..."'
    player '"아, 응."'
    '체할 것 같은 기분을 무시한 상태로 꾸역꾸역 입에 음식을 집어넣었다.'
    '어제처럼 맛있는 밥이지만, 뭔가 부담스럽네.'
    '식사가 끝나니 관리자가 왔다.'

    show Hyeyeon_Normal at admin_standsize_ms with Dissolve(.5)
    admin '"응? 이자벨이랑 스칼렛은 어디 갔어?"'

    hide Yun_Sad with None
    show Yun_Sad at yun_standsize_ms_L with Dissolve(.5)
    voice Yunsarang_229
    yun '"아.. 그게 말이죠..."'
    player '"다른 곳으로 갔는데..."'
    '어디로 갔는지 정확히 아는 사람이 없어 다들 말 끝을 흐렸다.'

    hide Hyeyeon_Normal with None
    show Hyeyeon_Sad at admin_standsize_ms with Dissolve(.5)
    admin '"이게 뭐야! 식사가 남다니. 내 음식이 별로였을 리 없는데..."'
    player '"스칼렛이랑 이자벨이 싸워서 말이지..."'

    hide Hyeyeon_Sad with None
    show Hyeyeon_Angry at admin_standsize_ms with Dissolve(.5)
    admin '"휴우, 다들 애도 아니고 식사 자리에서 싸우면 어떡해!"'

    show Hyeyeon_Angry at admin_one_jump with None
    admin '"해야 할 일도 있으니까, 빨리 가서 데려와!"'
    player '"응? 지금은 좀... 그런데 말이야."'

    hide Hyeyeon_Angry with None
    show Hyeyeon_Absurd at admin_standsize_bs with Dissolve(.5)
    admin '"식사는 꼬박꼬박 하면서 일은 안 하겠다는 거야?!"'
    player '"하, 할게..."'
    '다 같이 돌아다니며 찾는 것보다는 나눠서 찾는게 낫겠지?'
    '누굴 찾으러 갈까...'
    hide Hyeyeon_Absurd
    hide Yun_Sad
    hide Elice_Surprised
    with Dissolve(.5)


    menu:
        "스칼렛":
            $ s_D_2_Lunch = True
            player '"내가 스칼렛을 찾으러 가볼게, 둘은 이자벨을 찾아줘."'
            show Yun_huc at yun_standsize_ms_L with Dissolve(.5)
            voice Yunsarang_230
            yun '"네! 잘 살펴보고 올게요!"'
            show Elice_Difficulty at elice_standsize_ms_R with Dissolve(.5)
            voice Elice_205
            elice '"...그 시끄러운 녀석은 네가 담당하는게 낫겠지."'

            hide Yun_huc
            hide Elice_Difficulty
            with Dissolve(.5)
            play sound FootStep1
            '엘리스와 윤사랑이 식당 밖으로 나가는 걸 보고, 나도 스칼렛을 찾아 돌아다녔다.'

            play sound FootStep1
            scene bg black with Dissolve(2.0)
            player '"대체 어디 있는 거야..."'
            '스칼렛의 방, 연회장도 가봤지만 스칼렛의 꼬리털 하나 찾을 수 없었다. '
            '혹시나 하는 마음에 정원에도 나와봤는데, 아무도 없다.'
            player '"음... 설마?"'
            '머릿속을 스치는 장소가 한 곳 있었다.'
            '이곳에 있다는 확신은 없지만, 혹시 모르니 한 번 가보자.'
            '어두컴컴한 지하실 입구에 손을 올렸다.'
            '심장이 크게 쿵쾅거렸다.'
            player '"어두운 곳은 좀 무서운데..."'

            play sound DoorCreak1
            scene bg BG_Underoom with Dissolve(5.0)
            $renpy.pause(1.0, hard = True)
            play music Scarlet_1 fadein 2.0
            '끼익하는 소리와 함께 문이 열리고, 구석에 웅크리고 있는 붉은 머리카락이 보인다.'
            '이곳이 정답이었나 보다.'
            player '"저기 스칼렛?"'

            show Scarlet_tear at scarlet_standsize_ms with Dissolve(.5)
            voice Scarlet_208
            scarlet '"크응... 누구냐."'
            '눈가가 붉어진 스칼렛이 기침을 하며 나를 바라봤다.'

            voice Scarlet_209
            scarlet '"네 녀석은..."'
            player '"관리자가 찾아서 말이야."'

            hide Scarlet_tear with None
            show Scarlet_stare at scarlet_standsize_ms with Dissolve(.5)
            voice Scarlet_210
            scarlet '"무슨 일로 말이지?"'
            player '"또 시킬 일이 있는 모양이더라."'

            hide Scarlet_stare with None
            show Scarlet_jjajeung at scarlet_standsize_ms with Dissolve(.5)
            voice Scarlet_211
            scarlet '"흥, 그 녀석이 그렇지..."'

            play sound standup
            '손으로 거칠게 눈가를 비빈 스칼렛은 자리에서 일어났다.'
            '울었던 걸까? 확실히 이자벨의 말이 심하기는 했지만, 스칼렛이 워낙 여유롭게 맞받아쳐서 상처받았을 거라 생각하지 못했다.'
            player '"그, 조금만 여기 있다가 가도 괜찮지 않을까?"'

            hide Scarlet_jjajeung with None
            show Scarlet_nonSad at scarlet_standsize_ms with Dissolve(.5)
            voice Scarlet_212
            scarlet'"무슨 바보 같은 소리를 하는 거냐, 네놈."'
            player '"그냥... 시간이 조금 더 필요한 것 같아서."'

            hide Scarlet_nonSad with None
            show Scarlet_Sad at scarlet_standsize_ms with Dissolve(.5)
            voice Scarlet_213
            scarlet '"...."'
            play sound standup
            '스칼렛은 아무 말도 하지 않고 자리에 주저앉았다.'
            '스칼렛의 눈치를 보던 나는, 조심스럽게 스칼렛의 옆에 앉았다.'

            hide Scarlet_Sad with None
            show Scarlet_displease at scarlet_standsize_ms with Dissolve(.5)
            voice Scarlet_214
            scarlet '"나는 잘못한 게 없어."'
            player '"응."'
            voice Scarlet_215
            scarlet '"그 환자가 먼저 나에게 시비를 걸었다고."'
            player '"그래, 이자벨이 잘못했어."'
            '스칼렛은 나에게 자신이 했던 행동을 정당화하는 말을 여러 번 했다.'
            '나는 자동 응답기라도 된 것 마냥 응, 네 말이 맞아를 반복했다.'
            '솔직히 두 사람 다 이해가 가기 때문에, 어느 한 쪽 편을 들어주기가 애매한 걸.'

            hide Scarlet_displease with None
            show Scarlet_Sad at scarlet_standsize_ms with Dissolve(.5)
            voice Scarlet_216
            scarlet '"진짜로 죽을 것 같은 녀석에게는, 그런 말을 하면 안 되는데..."'
            player '"그 말이 오늘 했던 말 중에서 제일 나쁜 것 같아."'
            hide Scarlet_Sad with None
            show Scarlet_displease at scarlet_standsize_ms with Dissolve(.5)
            voice Scarlet_217
            scarlet '"크응... 나는 잘못한 것이 없지만, 그 환자에게 그런 식으로 대하면 안 되는 거였어."'
            player '"응?"'
            '스칼렛은 자기 손을 내려다보고 있었다.'

            hide Scarlet_displease with None
            show Scarlet_Angry at scarlet_standsize_ms with Dissolve(.5)
            voice Scarlet_218
            scarlet '"그 어린 녀석을 상대로 진심으로 화를 내다니, 연장자 답지 않은 행동이지..."'
            '스칼렛은 가끔, 이해하기 힘든 분위기를 내비친다.'
            player '"갑자기 이런 거 물어봐서 미안한데, 나이가 대체 어떻게 되는 거야?"'

            hide Scarlet_Angry with None
            show Scarlet_lookout at scarlet_standsize_ms with Dissolve(.5)
            voice Scarlet_219
            scarlet '"...글쎄. 적어도 네놈이 생각하는 것보단 많다."'

            hide Scarlet_lookout with None
            show Scarlet_stare at scarlet_standsize_ms with Dissolve(.5)
            voice Scarlet_220
            scarlet '"어설펐지만, 위로는 고맙군."'
            player '"아..."'

            play sound standup
            '자리에서 일어난 스칼렛은 내게 손을 내밀었다.'
            hide Scarlet_stare with None
            show Scarlet_inflate at scarlet_standsize_bs with Dissolve(.5)
            voice Scarlet_221
            scarlet '"크흠. 빨리 일어나라!"'
            player '"고마워."'

            play sound standup
            '나는 스칼렛의 손을 잡고 일어났다.'
            '스칼렛이 버티는 힘이 약해서 그냥 둘이 같이 넘어질 뻔했지만.'
            '먼저 손을 내밀어 줬다는 사실이 기뻐서 그저 웃었다.'
            pass
        "이자벨":

            $ i_D_2_Lunch = True
            player '"내가 이자벨을 찾아볼게, 둘은 스칼렛을 찾아줘."'
            show Yun_huc at scarlet_standsize_ms_L with Dissolve(.5)
            voice Yunsarang_230
            yun '"네! 잘 살펴보고 올게요!"'
            show Elice_Difficulty at elice_standsize_ms_R with Dissolve(.5)
            voice Elice_206
            elice '"...하아, 귀찮을 것 같은데."'

            hide Yun_huc
            hide Elice_Difficulty
            with Dissolve(.5)
            play sound FootStep1
            '엘리스와 윤사랑이 식당 밖으로 나가는 걸 보고, 나도 이자벨을 찾아 길을 나섰다..'
            play sound FootStep1
            scene bg black with Dissolve(2.0)
            '머릿속에 떠오르는 장소가 한 곳 있다.'
            play music Isabel_2
            scene bg BG_Adimroom with Dissolve(2.0)
            show Isabel_pout at isabel_standsize_ms with Dissolve(.5)
            '쥐 죽은 듯 조용한 서재 안에는 이자벨이 있었다.'
            '역시, 이자벨이라면 이곳에 올 줄 알았어.'
            hide Isabel_pout with None
            show Isabel_nodap at isabel_standsize_ms with Dissolve(.5)
            voice Isabel_200
            isabel '"...누구신가요."'
            player '"나야, 이자벨."'

            hide Isabel_nodap with None
            show Isabel_heung at isabel_standsize_ms with Dissolve(.5)
            voice Isabel_201
            isabel '"당신이군요."'
            player '"응, 아직도 많이 화났어?"'
            '이자벨은 읽고 있던 책을 덮고 나를 바라보았다.'

            hide Isabel_heung with None
            show Isabel_lookout  at isabel_standsize_ms with Dissolve(.5)
            voice Isabel_202
            isabel '"아뇨, 아까는 못 볼 꼴을 보였네요."'
            player '"괜찮아, 화나면 그럴 수 있지."'

            hide Isabel_lookout with None
            show Isabel_Sad at isabel_standsize_ms with Dissolve(.5)
            voice Isabel_203
            isabel '"식사시간이었는데... 다른 분들을 불편하게 해버렸잖아요?"'
            player '"괜찮아. 다들 알아서 잘 먹더라고... 엘리스가 그런 걸 신경 쓸 성격은 아니잖아?"'

            hide Isabel_Sad with None
            show Isabel_pout at isabel_standsize_ms with Dissolve(.5)
            voice Isabel_204
            isabel '"그래도 윤사랑 씨나 당신은 그런 걸 꽤나 신경 쓰시잖아요."'
            '이자벨의 말이 맞다. 실제로 나는 둘이 나간 후 체할 것 같은 기분으로 밥을 먹었으니까.'
            player '"그래도 나름 먹을만했어."'
            player '"그러고 보니, 넌 식사도 별로 안 했는데 괜찮아?"'

            hide Isabel_pout with None
            show Isabel_Normal at isabel_standsize_ms with Dissolve(.5)
            voice Isabel_205
            isabel '"네... 이곳에 와서 유독 많이 먹었던 거지, 평소 식사량은 저 정도예요."'
            player '"...뭐? 사람이 그것만 먹고 살 수 있어?"'

            hide Isabel_Normal with None
            show Isabel_Laughter at isabel_standsize_ms with Dissolve(.5)
            voice Isabel_206
            isabel '"침대에 누워서 잘 움직이지 못하는 사람에겐 충분해요."'
            '이자벨은 작게 웃으며 내 질문에 대답했다.'
            player '"그러고 보니, 아까는 왜 그렇게 화를 낸 거야?"'
            player '"너답지 않았어."'

            if i_D_2_Morning:
                hide Isabel_Laughter  with None
                show Isabel_soAngry at isabel_standsize_ms with Dissolve(.5)
                voice Isabel_207
                isabel '"..."'
                '이자벨은 손에 들고 있는 책을 매만지며 답을 고민했다.'
                '어두워진 표정이, 그리 유쾌한 이야기는 아니라는 걸 알려주었다.'

                hide Isabel_soAngry with None
                show Isabel_pout at isabel_standsize_ms with Dissolve(.5)
                voice Isabel_208
                isabel '"제가 예전부터 병원에 신세를 많이 졌는데..."'
                player '"응."'

                voice Isabel_209
                isabel '"그때 그런 식의 종교와 좋지 않은 일이 있었거든요..."'
                player '"아..."'
                '무어라 위로의 말을 건네야 할지, 감조차 잡히지 않는다.'

                hide Isabel_pout with None
                show Isabel_Sad at isabel_standsize_ms with Dissolve(.5)
                voice Isabel_210
                isabel '"그때 워낙 사건사고가 많았던 지라, 종교인을 보기만 해도 순간 화가 치밀어 오를 때가 있어요."'

                voice Isabel_211
                isabel '"그래서 오늘 별것 아닌 일에도 그리 화를 냈던 거예요."'

                hide Isabel_Sad with None
                show Isabel_pout at isabel_standsize_ms with Dissolve(.5)
                voice Isabel_212
                isabel '"어찌 보면 스칼렛 씨에게 화풀이를 한 것이죠..."'
                player '"아, 아니야. 스칼렛의 행동은 나도 곤란했는걸."'

                voice Isabel_213
                isabel '"그래도 당신은 알아서 적당히 거절할 수 있었잖아요?"'

                voice Isabel_214
                isabel '"유쾌한 이야기가 아니니, 이쯤에서 끝내죠."'

                hide Isabel_pout with None
                show Isabel_nodap at isabel_standsize_ms with Dissolve(.5)
                voice Isabel_215
                isabel '"저를 찾으러 온 데 이유가 있지 않았나요?"'
                '이자벨의 언급에 내가 이곳에 온 목적이 떠올랐다.'
                player '"관리자가 어제처럼 다 같이 모여서 청소를 하라고 해서 말이지."'

                hide Isabel_nodap with None
                show Isabel_Normal at isabel_standsize_ms with Dissolve(.5)
                voice Isabel_216
                isabel '"이곳은 환자라고 봐주는게 없네요..."'
                player '"뭐, 그런 편이지."'

                play sound standup
                '자리에서 일어난 이자벨은 먼저 가라는 듯 내게 턱짓을 했다.'
                hide Isabel_pout with None
                show Isabel_Laughter at isabel_standsize_ms with Dissolve(.5)
                voice Isabel_217
                isabel '"재미는 없겠지만, 제 이야기를 들어주실 생각이 있다면 저녁에 제 방으로 와주세요."'
            else:
                hide Isabel_Laughter  with None
                show Isabel_pout at isabel_standsize_ms with Dissolve(.5)
                voice Isabel_218
                isabel '"..."'

                hide Isabel_pout with None
                show Isabel_lookout at isabel_standsize_ms with Dissolve(.5)
                '이자벨은 무언가 말하려는 듯 입술을 달싹이다 말았다.'

                hide Isabel_lookout with None
                show Isabel_pout at isabel_standsize_ms with Dissolve(.5)
                '그 뒤로 이어지는 것은 침묵.'

                hide Isabel_pout with Dissolve(1.0)

                '이자벨은 나에게 말해줄 생각이 없는 것 같았다.'
                '내가 이자벨과 조금이라도 더 친했다면, 말해주었을까?'
                player '"식당으로 돌아가자."'
                show Isabel_nodap at isabel_standsize_ms with Dissolve(.5)
                '아무 말도 못하는 이자벨에게 나는 그리 말했고, 이자벨은 고개를 끄덕였다.'
            pass

    scene bg black with Dissolve(2.0)
    stop music fadeout 2.0
    $ renpy.pause(1.0)
    play music Normal_b fadein 5.0
    scene bg BG_Livingroom with Dissolve(2.0)
    show Hyeyeon_Normal at admin_standsize_ms with Dissolve(.5)
    admin '"자, 이제 전부 온 거 맞지?"'
    player '"응. 한 명도 빠짐없이 왔어."'
    '관리자는 우리의 손에 청소도구를 하나씩 쥐여주며 말했다.'
    hide Hyeyeon_Normal with Dissolve(.5)
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5)
    admin '"어제 해봐서 알지? 깨끗하게 하지 않으면 저녁은 없어!"'

    menu:
        "엘리스를 돕는다.":
            $ e_D_2_Dinner = True
            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0
            $ renpy.pause(1.0)
            play music Elicetheme fadein 2.0
            scene bg BG_Hall with Dissolve(1.0)
            show Elice_Angry_2 at elice_standsize_bs with Dissolve(1.0)
            voice Elice_207
            elice '"하... 그 붉은 똥개가 난리를 쳐놨어."'

            hide Elice_Angry_2 with None
            show Elice_Coloration at elice_standsize_bs with Dissolve(.5)
            voice Elice_208
            elice '"뭐해? 어서 돕지 않고."'

            hide Elice_Coloration with None
            show Elice_Surprised_2 at elice_standsize_bs with Dissolve(.5)
            voice Elice_209
            elice '"...아"'

            hide Elice_Surprised_2 with None
            show Elice_Gladness at elice_standsize_bs with Dissolve(.5)
            voice Elice_210
            elice '"잘하면 상을 주도록 하지."'
            scene bg black with Dissolve(1.0)
            stop music fadeout 1.0
            # play music MiniGame fadein 2.5

            call Trash_Game_Elice from _call_Trash_Game_Elice_1

            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0
            $renpy.pause (1.0)
            play music Elicetheme fadein 2.0
            scene bg BG_Hall with Dissolve(1.0)

            if CleaningPoint >= 23:
                show Elice_Normal_2 at elice_standsize_bs with Dissolve(1.0)
                voice Elice_211
                elice '"어제보다 시간이 오래 걸렸네."'

                hide Elice_Normal_2 with None
                show Elice_Difficulty at elice_standsize_bs with Dissolve(.5)
                voice Elice_212
                elice '"그 똥개가 난리를 쳐놨으니 어쩔 수 없지만."'

                hide Elice_Difficulty with None
                show Elice_Happy_2 at elice_standsize_bs with Dissolve(.5)
                voice Elice_213
                elice '"그래도 네가 잘했다는 건 달라지지 않으니까."'
                # 게임 아이템 획득

                show img_gradation
                show itemBack
                show get_Item_gif
                play sound Bell
                $ renpy.pause(0.325)
                show Elice_pendant:
                    xalign 0.49, yalign 0.46
                    rotate 00
                show screen item_TextScren
                $ renpy.pause(2.0, hard = True)
                show screen Click_Text
                pause
                hide screen item_TextScren
                hide screen Click_Text
                hide get_Item_gif
                hide itemBack
                hide Elice_pendant
                hide img_gradation
                with Dissolve(0.38, alpha = True)
                $ persistent.m_bgetpendant = True # 팬던트 획득

                hide Elice_Happy_2 with None
                show Elice_Normal_2 at elice_standsize_bs with Dissolve(.5)
                voice Elice_214
                elice '"식당으로 돌아가 볼까?"'

            else:
                show Elice_Strong at elice_standsize_bs with Dissolve(1.0)
                voice Elice_215
                elice '"망할 붉은 똥개..."'

                hide Elice_Strong with None
                show Elice_Difficulty at elice_standsize_bs with Dissolve(.5)
                voice Elice_216
                elice '"하, 네가 그리 잘못한 건 아니야."'

                hide Elice_Difficulty with None
                show Elice_coldsmiley at elice_standsize_bs with Dissolve(.5)
                voice Elice_217
                elice '"혼을 내진 않을 거니까, 식당으로 돌아가자."'

            play sound FootStep1
            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0

            pass
        "윤사랑을 돕는다.":

            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0
            $renpy.pause(1.0)
            play music Yunsarang_1 fadein 2.0
            scene bg BG_Livingroom with Dissolve(1.0)
            show Yun_fallinlove at yun_standsize_bs with Dissolve(1.0)
            voice Yunsarang_231
            yun '"아... 저를 도와주러 오셨군요."'
            hide Yun_fallinlove with None
            show Yun_pout at yun_standsize_bs with Dissolve(.5)
            voice Yunsarang_232
            yun '"스칼렛 씨나 이자벨 씨에게 갔을 줄 알았어요."'
            hide Yun_pout with None
            show Yun_Happy at yun_standsize_bs with Dissolve(.5)
            voice Yunsarang_233
            yun '"그래도 주인님이 도와주러 와주셔서 기뻐요."'
            scene bg black with Dissolve(1.0)
            stop music fadeout 1.0
            # play music MiniGame fadein 2.5

            call Trash_Game_Sarang from _call_Trash_Game_Sarang_1

            scene bg black with Dissolve(1.0)
            stop music fadeout 2.0
            $renpy.pause(1.0)
            play music Yunsarang_1 fadein 2.0
            scene bg BG_Livingroom with Dissolve(1.0)

            if CleaningPoint >= 23:
                show Yun_Happy at yun_standsize_bs with Dissolve(1.0)
                voice Yunsarang_234
                yun '"주인님과 함께 청소해서 즐겁네요."'
                hide Yun_Happy with None
                show Yun_pout at yun_standsize_bs with Dissolve(.5)
                voice Yunsarang_235
                yun '"혼자서 청소하면 많이 쓸쓸했을 거예요."'
                hide Yun_pout with None
                show Yun_huc at yun_standsize_bs with Dissolve(.5)
                voice Yunsarang_236
                yun '"이건 저의 보답이에요!"'
                # 아이템 추가

                show img_gradation
                show itemBack
                show get_Item_gif
                play sound Bell
                $ renpy.pause(0.325)
                show SarangRing:
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
                hide SarangRing
                hide img_gradation
                with Dissolve(0.38, alpha = True)
                $ persistent.m_bgetSarangRing= True # 사랑이의 반지 추가
                # 아이템 획득

                hide Yun_huc with None
                show Yun_Laughter at yun_standsize_bs with Dissolve(.5)
                voice Yunsarang_237
                yun '"이제 식당으로 갈까요?"'
            else:
                show Yun_Sad at yun_standsize_bs with Dissolve(.5)
                voice Yunsarang_238
                yun '"아..."'
                hide Yun_Sad with None
                show Yun_pout at yun_standsize_bs with Dissolve(.5)
                voice Yunsarang_239
                yun '"그, 그럴 수도 있다고 생각해요."'
                hide Yun_pout with None
                show Yun_pout2 at yun_standsize_bs with Dissolve(.5)
                voice Yunsarang_240
                yun '"식당으로 돌아갈까요?"'
            play sound FootStep1
            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0
            $ renpy.pause(1.0)
            pass

        "이자벨을 돕는다.":

            $ i_D_2_Dinner = True
            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0
            $renpy.pause (1.0)
            play music Isabel_1 fadein 2.0
            scene bg BG_Adimroom with Dissolve(1.0)
            show Isabel_nodap at isabel_standsize_bs with Dissolve(1.0)
            voice Isabel_219
            isabel '"제가 걱정돼서 오신 건가요?"'

            hide Isabel_nodap with None
            show Isabel_pout at isabel_standsize_bs with Dissolve(.5)
            voice Isabel_220
            isabel '"이제는 괜찮아요. 다른 메이드에게 가셨어도 괜찮은데..."'

            hide Isabel_pout with None
            show Isabel_lookout at isabel_standsize_bs with Dissolve(.5)
            voice Isabel_221
            isabel '"...[player_name] 씨가 와준 게 싫단 뜻은 아니예요."'

            scene bg black with Dissolve(1.0)
            stop music fadeout 1.0
            # play music MiniGame fadein 2.5

            call Trash_Game_Isabel from _call_Trash_Game_Isabel_1
            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0
            $renpy.pause(1.0)
            play music Isabel_1 fadein 2.0
            scene bg BG_Adimroom with Dissolve(1.0)


            if CleaningPoint >= 23:
                show Isabel_Laughter at isabel_standsize_bs with Dissolve(1.0)
                voice Isabel_222
                isabel '"덕분에 제시간 안에 청소를 끝냈네요."'

                hide Isabel_Laughter with None
                show Isabel_lookout at isabel_standsize_bs with Dissolve(.5)
                voice Isabel_223
                isabel '"고마워요, 도와주러 온 것도, 살피러 와준 것도."'

                hide Isabel_lookout with None
                show Isabel_Happy at isabel_standsize_bs with Dissolve(.5)
                voice Isabel_224
                isabel '"이건 감사 인사니까 받아주세요."'
                # 아이템 획득

                show img_gradation
                show itemBack
                show get_Item_gif
                play sound Bell
                $ renpy.pause(0.325)
                show IsabelRing:
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
                hide IsabelRing
                hide img_gradation
                with Dissolve(0.38, alpha = True)
                $ persistent.m_bgetIsabelRing= True # 이자벨의 반지 추가

                hide Isabel_Happy  with None
                show Isabel_Laughter at isabel_standsize_bs with Dissolve(.5)
                voice Isabel_225
                isabel '"식당 쪽에 일이 남았으니 이제 그쪽으로 가죠."'
            else:
                show Isabel_pout at isabel_standsize_bs with Dissolve(1.0)
                voice Isabel_226
                isabel '"...."'

                hide Isabel_pout with None
                show Isabel_nodap at isabel_standsize_bs with Dissolve(.5)
                voice Isabel_227
                isabel '"식당 쪽 일이 남았으니 그쪽으로 가죠."'

            play sound FootStep1
            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0
            $ renpy.pause(1.0)
            pass

        "스칼렛을 돕는다.":

            $ s_D_2_Dinner = True
            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0
            $renpy.pause(1.0)
            play music Scarlet_1 fadein 2.0
            scene bg BG_Underoom with Dissolve(1.0)
            show Scarlet_jjajeung at scarlet_standsize_bs with Dissolve(1.0)
            voice Scarlet_222
            scarlet '"...크릉."'

            hide Scarlet_jjajeung with None
            show Scarlet_inflate at scarlet_standsize_bs with Dissolve(.5)
            voice Scarlet_223
            scarlet '"이 몸은 고작 그런 일 하나 겪었다고 해야 하는 일을 못하는 사람이 아니다!"'

            hide Scarlet_inflate with None
            show Scarlet_Sad at scarlet_standsize_bs with Dissolve(.5)
            voice Scarlet_224
            scarlet '"...네 녀석의 도움은 기껍지만."'

            scene bg black with Dissolve(1.0)
            stop music fadeout 1.0
            # play music MiniGame fadein 2.5

            call Trash_Game_Scarlet from _call_Trash_Game_Scarlet_1

            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0
            $ renpy.pause (1.0)
            play music Scarlet_1 fadein 2.0
            scene bg BG_Underoom with Dissolve(1.0)

            if CleaningPoint >= 23:
                show Scarlet_Normal at scarlet_standsize_bs with Dissolve(1.0)
                voice Scarlet_225
                scarlet '"크릉, 네 녀석도 할 때는 하는 놈이군!"'

                hide Scarlet_Normal with None
                show Scarlet_Laughter at scarlet_standsize_bs with Dissolve(.5)
                voice Scarlet_226
                scarlet '"제대로 된 상을 주어야지, 네 녀석도 뿌듯하겠지?"'

                hide Scarlet_Laughter with None
                show Scarlet_Happy at scarlet_standsize_bs with Dissolve(.5)
                voice Scarlet_227
                scarlet '"이 몸은 부하를 잘 다룰 줄 아는 자니까."'
                # 아이템 추가

                show img_gradation
                show itemBack
                show get_Item_gif
                play sound Bell
                $ renpy.pause(0.325)
                show Dream_Catcher:
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
                hide Dream_Catcher
                hide img_gradation
                with Dissolve(0.38, alpha = True)
                $ persistent.m_bgetDreamcatcher= True # 드림캐쳐 팔찌 추가

                hide Scarlet_Happy with None
                show Scarlet_Laughter at scarlet_standsize_bs with Dissolve(.5)
                voice Scarlet_228
                scarlet '"이 몸을 좀 더 우러러보아도 좋다!"'
            else:
                show Scarlet_displease at scarlet_standsize_bs with Dissolve(1.0)
                voice Scarlet_229
                scarlet '"크릉.... 네놈만의 문제는 아니지."'

                hide Scarlet_displease with None
                show Scarlet_jjajeung at scarlet_standsize_bs with Dissolve(1.0)
                show Scarlet_jjajeung at scarlet_one_jump_bs with None
                voice Scarlet_230
                scarlet '"식당으로 돌아가도록 하지."'
            play sound FootStep1
            scene bg black with Dissolve(2.0)
            stop music fadeout 2.0
            pass


label D_2_Dinner:
    # scene bg black with Dissolve(.5)

    scene bg BG_Corridor with Dissolve(2.0)
    play music Normal_a fadein 2.0
    play sound FootStep1
    '청소가 끝난 후, 메이드 들은 다시 제멋대로 흩어졌다.'
    '관리자가 억지로 모으는 것이 아니면, 함께 시간을 보내는 녀석들이 없네...'
    '나는 누구를 찾으러 갈까.'

label D_2_Selected:
    menu:
        "윤사랑":
            call Select_Dinner_Yun from _call_Select_Dinner_Yun
        "엘리스":
            #  if e_D_1_Lunch == e_D_1_Dinner == e_D_2_Morning == True
            call Select_Dinner_Elice from _call_Select_Dinner_Elice
        "스칼렛" :
            # if s_D_1_Lunch == s_D_2_Morning == s_D_2_Lunch == True
            call Select_Dinner_Scarlet from _call_Select_Dinner_Scarlet
        "이자벨" :
            # if i_D_2_Lunch == i_D_2_Morning == True
            call Select_Dinner_Isabel from _call_Select_Dinner_Isabel
    stop music fadeout 2.0
    scene bg black with Dissolve(2.0)
    scene bg Myroom with Dissolve(2.0)

    play music Ending_Credit fadein 5.0
    '오늘도 역시 소란스러운 하루였다.'
    '누가 무고한 사람인지 어느 정도 윤곽이 잡히기는 했다.'
    '하지만... 확신을 할 수 있는 것은 아니기 때문에, 마지막 남은 내일 하루를 잘 써야겠다.'
    '만약 내가 틀린다면 악독한 죄인이 세상에 풀려나는 것이고...'
    '아무 죄 없는 메이드가 이 저택에 남아야 하는 것이니까.'
    '밑바닥에서부터 끓어오르는 사명감과는 반대로 눈꺼풀이 너무 무거웠다.'
    '너무 조급해하지 말고 차근차근 해내다 보면 분명, 잘할 수 있을 거다.'

    jump D_3_Morning

    scene bg black with Dissolve(2.0)
    $renpy.pause(2.0,hard = True)
    show screen Mini_Scene(DemoEnding, _x = 0.5, _y = 0.5) with Dissolve(2.0)
    $renpy.pause(2.0,hard = True)
    hide screen Mini_Scene with Dissolve(2.0)
    $renpy.pause(2.0,hard = True)

    show screen Mini_Scene(title_log, _x = 0.5, _y = 0.5) with Dissolve(2.0)
    $renpy.pause(2.0, hard = True)
    hide screen Mini_Scene with Dissolve(2.0)
    $renpy.pause(2.0, hard = True)

    return


label Select_Dinner_Yun:
    scene bg black with Dissolve(1.0)
    '윤사랑하고 좀 더 대화하고 싶었다.'

    play sound FootStep1
    $renpy.pause(1.5)
    scene bg BG_Corridor with Dissolve(2.0)
    '어디에 있을지 곰곰이 생각하다가, 윤사랑의 방으로 향했다.'

    # play sound 문 두두리는 소리
    play sound DoorKnock
    $renpy.pause(1.0)
    '방 문을 두드리자, 안에서 금방 윤사랑이 나왔다.'

    play sound DoorOpen2
    play music Yunsarang_1
    show Yun_huc at yun_standsize_ms with Dissolve(.5)
    voice Yunsarang_241
    yun '"어라? 무슨 일이신가요."'
    player '"그냥 대화를 하고 싶어서. 들어가도 괜찮을까?"'

    hide Yun_huc with None
    show Yun_panic at yun_standsize_ms with Dissolve(.5)
    voice Yunsarang_242
    yun '"잠시만... 잠시만 기다려주세요!"'

    hide Yun_panic with None
    # play sound 쾅 하고 문 닫는 소리
    play sound DoorClose_2
    with hpunch

    '윤사랑은 쾅 소리가 날 정도로 크게 문을 닫았다.'
    '언제쯤 문이 열릴까, 기다리던 도중 윤사랑이 뛰쳐나왔다.'

    play sound DoorOpen2
    show Yun_huc at yun_standsize_ms with Dissolve(.5)
    voice Yunsarang_243
    yun '"이제 들어오셔도 괜찮아요!"'
    player '"아, 응..."'

    scene bg BG_Maidroom with Dissolve(.5)
    '들어간 윤사랑의 방은 광이 날 정도로 깨끗했다.'
    player '"잠시 이야기를 나누고 싶어서 말이지."'
    player '"이야기가 조금 길어질 것 같은데 의자는 어디 있어?"'

    hide Yun_huc with None
    show Yun_lookout at yun_standsize_ms with Dissolve(.5)
    voice Yunsarang_244
    yun '"제 방에는 의자가 없는데요?"'
    '너무 뻔히 보이는 거짓말이라 웃음이 나올 지경이었다.'
    '윤사랑의 뒤에 있는 의자는 의자가 아닌가 보구나...'
    '입에 침도 바르지 않고 거짓말을 하는 모습이 귀여워, 그냥 속아주기로 했다.'
    player '"그렇구나..."'
    '그냥 이대로 계속 서있을지 고민하던 도중 윤사랑이 침대를 가리켰다.'

    hide Yun_lookout with None
    show Yun_wink at yun_standsize_ms with Dissolve(.5)
    voice Yunsarang_245
    yun '"침대에 앉아서 대화하면 되잖아요?"'
    player '"그래. 잠시 실례할게."'
    '다른 사람이 자는 공간에 앉는 다는게 굉장한 실례처럼 느껴졌지만, 어쩔 수 없었다.'
    '방에 의자가 없을 거라고는 전혀 생각 못 했는 걸...'

    play sound standup
    hide Yun_wink with Dissolve(.5)
    show Yun_Normal at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_246
    yun '"무슨 이야기를 하러 오신 거예요?"'
    '윤사랑은 자연스럽게 내 옆자리에 앉으며 물었다.'
    '좀 가깝지 않나?'
    '이 미묘한 거리를 굳이 말로 꺼냈다가는 더 어색해질 것 같아서 언급하지 않았다.'
    player '"그냥, 아까 일 때문에..."'

    hide Yun_Normal with None
    show Yun_pout at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_247
    yun '"아, 이자벨 씨와 스칼렛 씨 말이죠?"'
    player '"둘이 싸우게 될 줄 몰랐어."'
    player '"꽤나 사이좋아 보였는데 말이지."'

    hide Yun_pout with None
    show Yun_Sad at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_248
    yun '"그러게요... 어제 청소할 때는 손발이 척척 맞던데..."'
    '윤사랑은 고개를 끄덕이며 내 의견에 동조했다. '
    player '"내일 또 그런 식으로 싸우면 어쩌지?"'
    player '"눈치 보는 것도 힘들고, 중재하는 것도 어려운 데 말이야."'
    player '"다들 최대한 싸우지 않았으면 좋겠어."'

    hide Yun_Sad with None
    show Yun_huc at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_249
    yun '"저, 저도 같은 생각이에요."'
    player '"모두가 싸우지 않게 할 방법이 없을까?"'

    hide Yun_huc with None
    show Yun_pout at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_250
    yun '"음..."'
    '잠시 고민하던 윤사랑은 내게 말했다.'

    hide Yun_pout with None
    show Yun_wink at yun_standsize_bs with Dissolve(.5)
    show Yun_wink at yun_one_jump_bs with None
    play sound jump1
    voice Yunsarang_251
    yun '"저한테 방법이 하나 있어요!"'
    player '"뭔데?"'

    hide Yun_wink with None
    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_252
    yun '"그건 아직 말해드릴 수 없어요. 하지만..."'

    hide Yun_fallinlove with None
    show Yun_Happy at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_253
    yun '"이번 일을 잘 끝내면 소원 하나만 들어주시지 않을래요?"'
    player '"다른 애들이 싸우지 않을 방법을 찾아준 건데, 소원 하나 정도야."'

    hide Yun_Happy with None
    show Yun_huc at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_254
    yun '"야, 약속해 주세요!"'

    hide Yun_huc with Dissolve(1.0)
    show screen Mini_Scene(Yun_Yakusoku_2) with Dissolve(1.5)
    '윤사랑은 새끼손가락을 내밀었다.'
    player '"뭐, 이정도 쯤이야."'

    show screen Mini_Scene(Yun_Yakusoku_1) with Dissolve(1.0)
    '나는 윤사랑의 새끼손가락에 내 새끼손가락을 걸고 약속했다.'

    # hide Yun_huc with None
    hide screen Mini_Scene with Dissolve(1.0)
    show Yun_cuty at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_255
    yun '"히... 저는 이제 계획을 짜야 하니까..."'
    voice Yunsarang_256
    yun '"주, 주인님을 위한 일이니까 이해해 주세요."'
    player '"아... 벌써?"'
    voice Yunsarang_257
    yun '"주, 주인님을 위한 일이니까 이해해주세요."'
    player '"그렇게까지 말한다면야."'
    # 선택지 탈출!

    return

label Select_Dinner_Elice:
    if e_D_2_Dinner == False:
        play sound FootStep1
        '엘리스를 찾기 위해서 저택을 돌아다녔으나 엘리스를 찾을 수 없었다.'
        '엘리스와 친했다면, 지금 엘리스가 어디에 있는지 알 수 있었을 텐데...'
        jump D_2_Selected

    stop music fadeout 5.0
    scene bg black with Dissolve(2.0)
    '아침에 책을 읽던 엘리스가 떠올랐다.'
    play sound FootStep1
    '살짝 쓸쓸해 보이던 얼굴이 아른거렸기 때문에 서재에 왔다.'
    scene bg BG_Adimroom with Dissolve(3.0)
    show Elice_Gladness at elice_standsize_ms with Dissolve(.5)
    play music Isabel_2 fadein 5.0
    voice Elice_218
    elice '"아, 마침 잘 왔어. 하고 싶은 이야기가 있었는데."'
    player '"응? 뭐 때문에?"'

    hide Elice_Gladness with None
    show Elice_Difficulty at elice_standsize_ms with Dissolve(.5)
    voice Elice_219
    elice '"네가 살던 세계에서는 왕족을 포기할 수 있다고 말했잖아."'
    player '"아, 응. 그렇게 말했었지."'

    voice Elice_220
    elice '"왕족을 포기한 사람은 어떻게 되었는지 궁금해서... 그런 건 책에도 안 나와있더군."'
    '엘리스는 내가 세계사 교과서를 가리키며 말했다.'
    player '"왕족을 그만두는 건 비교적 최근의 일이니까..."'
    player '"음... 그냥 왕족의로써의 의무와 특혜가 사라진, 평범한 사람이 되었을 뿐이야."'
    player '"가족들이랑 여행도 가고, 일도 하면서 살지 않을까?"'
    '내 말을 듣던 엘리스가 물었다.'

    hide Elice_Difficulty with None
    show Elice_Difficulty_2 at elice_standsize_ms with Dissolve(.5)
    voice Elice_221
    elice '"왕족이 아니게 된 그한테, 무슨 가치가 있지?"'
    player '"왕족은 아니지만, 왕의 자식이라는 이름과 그 사람으로서의 가치가 남지 않을까?"'
    player '"왕족을 포기한 것이 사람을 포기한 것은 아니잖아."'

    hide Elice_Difficulty_2 with None
    show Elice_Surprised_2 at elice_standsize_ms with Dissolve(.5)
    voice Elice_222
    elice '"너는 그렇게 생각하는 군."'
    '엘리스는 책상 가득 펼쳐진 책을 만지며 말했다.'

    hide Elice_Surprised_2 with None
    show Elice_Difficulty at elice_standsize_ms with Dissolve(.5)
    voice Elice_223
    elice '"나는 이제 황제가 아닌 나를 생각할 수 없어."'

    hide Elice_Difficulty with None
    show Elice_coldsmiley_2 at elice_standsize_ms with Dissolve(.5)
    voice Elice_224
    elice '"홀가분하다고 말했지만, 무엇을 해야 할지 모르겠더라고."'
    player '"...모른다면 지금부터 찾아가면 되잖아?"'
    '아무거나 손에 잡히는 지도를 펼쳤다.'
    player '"나는 바다를 좋아해. 너는?"'
    player '"여행을 간다면 산이 좋아, 바다가 좋아?"'

    hide Elice_coldsmiley_2 with None
    show Elice_Pudency at elice_standsize_ms with Dissolve(.5)
    show BG_Sea_Past with Dissolve(2.0)
    voice Elice_225
    elice '"...바다 쪽이 더 좋아."'

    hide BG_Sea_Past with Dissolve(2.0)
    hide Elice_pudency with None
    scene bg black with Dissolve(2.0)
    '엘리스랑 이것저것 이야기를 나누었다.'
    '엘리스가 좋아하는 음식, 내가 좋아하는 음식.'
    '좋아하는 옷이나, 색깔 등등...'
    '정말 쓸모없고 사소한 것들만 잔뜩 이야기했다.'
    '드물게 엘리스가 어울려준 덕분이겠지만, 무척 즐거웠다.'

    scene bg BG_Adimroom with Dissolve(1.0)
    player '"집에 돌아가면, 나는 꼭 여행을 가볼 거야."'
    player '"모르는 사람을 만나서 이야기해보고, 모르는 장소를 구경해 보고 싶어."'
    player '"재밌지 않을까?"'

    show Elice_Difficulty at elice_standsize_ms with Dissolve(.5)
    voice Elice_226
    elice '"...모르는 장소라, 위험할 거라는 생각은 안 하나?"'
    player '"그 위험까지 여행의 즐거움이야!"'

    show Elice_CG_3_1 with Dissolve(2.0)
    hide Elice_Difficulty with None
    voice Elice_227
    elice '"...생각보다 나쁘지 않을지도 모르겠어."'
    '후후 웃은 엘리스는 책상 위의 책을 덮기 시작했다.'
    player '"정리하려고? 나도 도와줄게."'

    show Elice_CG_3_2 with None
    hide Elice_CG_3_1 with None
    voice Elice_228
    elice '"그래. 슬슬 자야 할 시간이잖아?"'
    player '"응... 일찍 자야지 내일 일어나지."'
    '책장에 책을 넣던 도중, 엘리스가 내게 말을 걸었다.'

    show Elice_CG_3_3 with Dissolve(1.0)
    hide Elice_CG_3_2 with None
    voice Elice_229
    elice '"어렸을 때의 나는 잠자는게 무서웠어."'
    voice Elice_230
    elice '"언제 한 번, 암살자가 침실에 왔던 적이 있는데..."'
    voice Elice_231
    elice '"죽을지도 모른다는게 무척이나 무섭더라고."'
    hide Elice_CG_3_3 with Dissolve(1.0)
    show Elice_Strong at elice_standsize_ms with Dissolve(.5)
    voice Elice_232
    elice '"잠들었을 때 죽을지도 모른다는 불안감 때문에 안 자고 버티던 날도 있었지."'
    player '"..."'
    player '"여기에 널 해칠 녀석은 없으니, 편히 자고 일어나."'
    player '"누가 와서 물을 뿌리지만 않는다면... 나도 편히 잘 수 있을 것 같은데."'

    hide Elice_Strong with None
    show Elice_Laughter at elice_standsize_ms with Dissolve(.5)
    voice Elice_233
    elice '"무슨 이야기를 하는 건지 나는 모르겠네."'

    voice Elice_234
    elice '"잘 자."'

    play sound FootStep1
    hide Elice_Laughter with Dissolve(1.0)
    '책 정리를 끝낸 엘리스는 서재 밖으로 나갔다.'
    '엘리스와 나는 자기 위해 방으로 돌아갔다.'
    # 선택지 탈출
    return

label Select_Dinner_Scarlet:
    if s_D_2_Dinner == False:
        play sound FootStep1
        '스칼렛과 대화하기 위해서 저택을 돌아다녔지만, 결국 찾지 못했다.'
        '늘 가던 지하실에도 없다면 스칼렛은 어디에 있는걸까...?'
        jump D_2_Selected

    scene bg black with Dissolve(.5)
    '청소를 하기 전에 이자벨과 싸웠던 스칼렛이 걱정됐다.'
    play sound FootStep1
    scene bg BG_Corridor with Dissolve(2.0)
    $renpy.pause(1.5)
    '늘 가던 지하실에도 없어서 어디에 갔는지 찾다가 방으로 돌아왔다.'
    show Scarlet_jjajeung at scarlet_standsize_ms with Dissolve(.5)
    play music Scarlet_1 fadein 2.0
    # vpunch?
    voice Scarlet_231
    scarlet '"크릉... 왜 이리 늦게 오는 거냐!"'
    player '"그야, 나는 너를 찾아다녔으니까?"'
    '방 문 앞에서 나를 기다리던 스칼렛과 마주쳤다.'
    '스칼렛은 나를 기다리고 있었던 듯, 늦게 방에 돌아온 내게 화를 냈다.'

    hide Scarlet_jjajeung with None
    show Scarlet_inflate at scarlet_standsize_ms with Dissolve(.5)
    play sound DoorOpen2
    voice Scarlet_232
    scarlet '"빨리 들어가도록 하지."'

    scene bg Myroom with Dissolve(1.5)
    '당당하게 문을 열고 방에 들어간 스칼렛은 침대에 앉았다.'
    '나는 불편한 의자에 앉아 스칼렛을 바라봤다.'

    show Scarlet_displease at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_233
    scarlet '"크음, 이 몸이 네게 온 이유는..."'
    voice Scarlet_234
    scarlet '"내가 믿고 있는 그분에 대해 알려주기 위해서다."'
    '갑작스러운 포교활동에 어떻게 대처해야 할지 감이 오지 않았다.'
    '할 말을 찾지 못했기 때문에 입을 다물고, 고개만 끄덕였다.'

    hide Scarlet_displease with None
    show Scarlet_heung at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_235
    scarlet '"여러 가지 이유로 그분의 이름은 말하지 못하지만, 그분은 무척이나 뛰어나신 분이다."'
    voice Scarlet_236
    scarlet '"죽었던 사람도 살려냈으니 말이지."'
    player '"응?"'

    hide Scarlet_heung with None
    show Scarlet_lookout at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_237
    scarlet '"어디서부터 이야기하는 것이 좋을까..."'
    '다리를 꼬고 앉은 스칼렛은 천천히 자기 이야기를 시작했다.'

    hide Scarlet_lookout with None
    show Scarlet_stare at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_238
    scarlet '"이 몸은 재수 없는 금발과 달리 천한 신분으로 태어났지."'
    voice Scarlet_239
    scarlet '"부모는 없었고, 돌봐주는 사람도 없어 도둑질로 살아남았어."'

    hide Scarlet_stare with None
    show Scarlet_nonSad at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_240
    scarlet '"뭐, 그런 우울한 어린 시절을 보낸 후 우연한 계기로 해적이 되었다."'
    voice Scarlet_241
    scarlet '"이 몸의 검술 실력이 제일 뛰어났기에 그들을 이끄는 해적이 되었지."'

    hide Scarlet_nonSad with None
    show Scarlet_displease at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_242
    scarlet '"워낙 강세였던 우리는 여왕의 개에게 사냥 당했고, 나는 그때 한 번 죽었었다."'
    player '"....그게 언제 적 일이야?"'
    voice Scarlet_243
    scarlet '"글쎄, 못해도 50년 전의 일이다."'
    '머리가 빠르게 돌아갔다. 그렇다는 말은...'
    player '"스칼렛 너... 나이가...?"'
    hide Scarlet_displease with None
    show Scarlet_ppagchim at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_244
    scarlet '"글쎄, 잘 생각해 보거라. 이 몸의 나이가 어떻게 되는지!"'
    '생각했던 것보다 훨씬 많은 스칼렛의 나이에 할 말을 잃었다.'

    hide Scarlet_ppagchim with None
    show Scarlet_nonSad at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_245
    scarlet '"그분의 기적 덕분에 나는 살아났고, 그분을 위해서 살아가고 있지."'
    voice Scarlet_246
    scarlet '"그분 앞에서 우린 모두 평등하다."'

    hide Scarlet_nonSad with None
    show Scarlet_lookout at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_247
    scarlet '"교주이며, 그분의 축복을 직접 목격한 이 몸은 어느 정도 특별 대우를 받을 수 있겠지만..."'

    hide Scarlet_lookout with None
    show Scarlet_nonSad at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_248
    scarlet '"적어도 그분은 이 몸의 귀나 꼬리를 보고 싫어하지는 않으시지."'
    '스칼렛은 덤덤하게 말했지만, 내 입장에서는 굉장히 충격적인 발언밖에 없다.'
    '죽었다 살아났다든지, 해적이라든지...'
    '영화나 만화에서만 봤을법한 일만 가득하다.'

    hide Scarlet_nonSad with None
    show Scarlet_Sad at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_249
    scarlet '"이곳에서는 그 분과의 연결이 약해진 만큼, 이 몸의 힘도 약해진다."'

    hide Scarlet_Sad with None
    show Scarlet_stare at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_250
    scarlet '"그 분과의 연결이 강해진다면 원래 세계로 돌아가는 건 일도 아니다!"'

    hide Scarlet_stare with None
    show Scarlet_ppagchim at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_251
    scarlet '"그러니까 네놈!"'
    player '"으응??"'

    hide Scarlet_ppagchim with None
    show Scarlet_Normal at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_252
    scarlet '"무사히 집으로 돌아가고 싶다면 내일 하루 동안 이몸에 협력해라."'
    voice Scarlet_253
    scarlet '"그분의 힘으로 집에 돌아갈 수 있게 해주지!"'
    '당당히 가슴을 펴고 말하는 스칼렛은 굉장히 멋졌다.'
    '자신감이 가득한 모습을 보고 있자면 나도 스칼렛의 뒤를 쫓아가고 싶었지만...'
    '나는 이미 원래 세계로 돌아가는 방법을 알고 있다.'
    player '"그래, 내일 열심히 너를 도울게."'

    hide Scarlet_Normal with None
    show Scarlet_Laughter at scarlet_standsize_ms with Dissolve(.5)
    show Scarlet_Laughter at scarlet_one_jump with None
    voice Scarlet_254
    scarlet '"현명한 판단이다!"'
    '스칼렛은 손을 들어서 내 머리를 잔뜩 쓰다듬었다.'
    '머릿속에 비상벨이 울리기 시작한다.'
    '스칼렛의 웃는 얼굴이 좋아서 계속 보고 싶어진다. 그 얼굴을 위해서라면 무엇이든 할 수 있을 것 같았다.'
    '자야 할 시간이었기에 스칼렛은 자기 방으로 돌아갔다.'
    # 선택지 탈출


    return

label Select_Dinner_Isabel:
    if e_D_2_Dinner == False:
        play sound FootStep1
        '나는 이자벨과 대화하고 싶었기 때문에, 이자벨을 찾아 저택을 돌아다녔지만 찾을 수 없었다.'
        '혹시나 하는 마음에 방 문을 두드렸지만, 들려오는 대답은 없었다.'
        jump D_2_Selected

    scene bg black with Dissolve(2.0)
    '청소를 하기 전에 스칼렛과 싸웠던 이자벨이 걱정됐다.'
    scene bg BG_Corridor with Dissolve(2.0)
    '평소와 전혀 다른 모습이었지, 이자벨...'
    '이자벨의 방 앞에서 문이 열렸고 나는 방 안으로 들어갔다.'

    play sound DoorOpen2
    scene bg BG_Maidroom with Dissolve(2.0)
    play music Isabel_2 fadein 5.0
    show Isabel_pout at isabel_standsize_ms with Dissolve(1.0)
    voice Isabel_228
    isabel '"어디서부터 이야기할까요..."'
    '작게 한숨을 내쉰 이자벨은 침대에 앉아있었다.'
    '나는 침대 옆으로 의자를 끌고 와 이자벨과 마주 앉았다.'

    hide Isabel_pout with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_229
    isabel '"제가 오늘 부끄러운 모습을 보였다는 자각은 있어요."'

    voice Isabel_230
    isabel '"하지만... 다시 그 상황으로 돌아가도 스칼렛 씨에게 화낼 것 같네요."'
    player '"그래?"'

    hide Isabel_pout with None
    show Isabel_lookout at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_231
    isabel '"네. 저는... 종교를 무척이나 싫어하거든요. 신도, 신을 믿는 신자도."'
    player '"무슨 일이라도 있었던 거야?"'

    hide Isabel_lookout with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_232
    isabel '"...네."'
    '이자벨은 자기 손을 만지작거리며 이야기를 시작했다.'

    hide Isabel_pout with None
    show Isabel_Laughter at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_233
    isabel '"당신도 아시다시피 저는 몸이 무척이나 안 좋잖아요?"'

    hide Isabel_Laughter with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_234
    isabel '"병원에 오래 입원해 있는동안 부모님은 제 몸을 낫게 하기 위해 별의별 걸 다 해보셨어요."'

    voice Isabel_235
    isabel '"미국의 유명한 의사에게도 가보고, 한의원도 가보고..."'

    voice Isabel_236
    isabel '"무당한테 굿도 해보고, 성당이나 절에 가서 기도도 해보고..."'

    hide Isabel_pout with None
    show Isabel_heung at isabel_standsize_bs with  Dissolve(.5)
    voice Isabel_237
    isabel '"사기꾼한테 당한 게 한두 번이 아니죠."'

    voice Isabel_238
    isabel '"부모님은 누가 저런 허술한 거짓말에 속아? 하는 것에도 전부 속아주셨어요."'

    hide Isabel_heung with None
    show Isabel_soAngry at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_239
    isabel '"딸이 나을 수 있다면 몇 번이고 속겠다면서 돌아다니셨는걸요."'
    player '"아..."'

    voice Isabel_240
    isabel '"그걸 보는 제 심정이 어땠는지 아시나요?"'

    voice Isabel_241
    isabel '"남의 절박한 마음을 이용해 먹는 사람들이 무척이나 미웠어요."'

    hide Isabel_soAngry with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_242
    isabel '"작정하고 접근한 사기꾼들이었지만, 솔직히 저는 그 사람들과 스칼렛의 큰 차이점을 못 느끼겠어요."'

    voice Isabel_243
    isabel '"적어도 제가 스칼렛에게 화를 내었던 그 순간에는 말이죠."'
    player '"...많이 힘들었겠네."'

    hide Isabel_pout with None
    show Isabel_heung at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_244
    isabel '"네... 얼마나 속이 답답하던지."'
    '주먹으로 가슴을 두드리는 이자벨에게 옆에 있던 물을 건네주었다.'

    hide Isabel_heung with None
    show Isabel_stare at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_245
    isabel '"그들이 말하는 신도 무척이나 싫었어요."'

    hide Isabel_stare with None
    show Isabel_soAngry at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_246
    isabel '"신이 존재한다면 내 몸을 먼저 낫게 해줘야 하는 거 아니에요?"'

    voice Isabel_247
    isabel '"대체 뭘 하는 무능한 작자길래, 나를 아직도 방치하는 거예요?"'
    '물을 벌컥벌컥 들이 마시는 이자벨을 보며, 이자벨의 속에 쌓인 게 많다는 걸 짐작했다.'
    player '"화가 나는 건 알지만, 스칼렛에게 또 그러면 안 된다?"'

    hide Isabel_soAngry with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_248
    isabel '"...알고 있어요."'
    player '"스칼렛은 정말 순수한 마음으로 그랬던 거니까..."'
    player '"이따가 화냈던 걸 사과하는게 어때?"'

    hide Isabel_pout with None
    show Isabel_heung at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_249
    isabel '"...하아."'

    voice Isabel_250
    isabel '"당신 말대로 스칼렛 씨한테 사과할게요."'

    show Isabel_heung at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_251
    isabel '"하지만, 좋아하는 여자애 앞에서 다른 여자애  이야기는 최대한 꺼내지 않는게 좋아요."'
    '이자벨이 갑자기 꺼낸 대화 주제에 잠시 머리가 굳었다.'
    '무슨 소리지? 좋아하는 여자애... 다른 여자애...?'
    player '"혹시 내가 널 좋아하는 거야?"'
    '이자벨은 한숨을 내쉬고 단호하게 대답했다.'

    hide Isabel_heung with None
    show Isabel_stare at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_252
    isabel '"네."'
    player '"그, 그렇구나... 나는 널 좋아하는구나..."'

    hide Isabel_stare with None
    show Isabel_soAngry at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_253
    isabel '"모르고 계셨던 것 같네요. 당신은 이런 부분에서는 둔하니까요."'

    hide Isabel_soAngry with None
    show Isabel_lookout at isabel_standsize_bs with Dissolve(.5)
    '이자벨이 손을 뻗어 내 손을 잡았다.'
    '살짝 서늘한 손에 따뜻한 내 손이 겹쳐져 온기가 전해졌다.'
    hide Isabel_lookout with None
    show Isabel_Laughter at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_254
    isabel '"좋은 밤 보내세요."'
    '잘 자라는 인사를 한 이자벨은, 장난스러운 미소를 지었다.'
    '자야 할 시간이었기에 나는 이자벨의 방을 나와, 내 방으로 돌아갔다.'
    # 선택지 탈출


    return
