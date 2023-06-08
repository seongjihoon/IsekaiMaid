label intro:

    play sound "audio/BGM/chapter.wav"
    show bg_chapter1_avi
    $ renpy.pause(7.0, hard = True )
    hide bg_chapter1_avi with Dissolve(1.0, alpha = True)
    scene bg black with Dissolve(2.0, hard = True)
    play music main fadein 2.0
    $ renpy.pause(3.0, hard = True)
    stop sound

    '어렸을 적의 나는 무지개 너머에 다른 세계가 있다고 생각했다.'
    '별에게 빌었던 소원이 이루어지고, 모든 괴로움이 레몬 사탕처럼 녹아내릴 곳.'
    '파랑새를 쫓아가면 무지개 너머로 갈 수 있을까.'
    '시계를 든 바쁜 토끼를 쫓아가면 갈 수 있을까.'
    '크면서 자연스럽게 잊었던 무지개 너머가 떠올랐다.'
    '평소에는 보기 어려운 별과 파란 꽃을 보고 있으니, 이곳이 어린 내가 꿈꾸던 무지개 너머가 아닐까 하는 생각이 들었다'
    # play sound 풀이 스치는 소리
    play sound standup
    '바스락 거리는 소리가 들렸다.'
    '눈을 떠보면, 처음보는 아이가 나를 내려다보고 있었다.'

    show Admin_CG_1 with Dissolve(4.0,hard = True)
    $renpy.pause(.5,hard = True)
    '살짝 미소를 지은 아이는 나를 보며 말했다.'
    unknown_admin '"어서와, 주인님"'
    unknown_admin '"인사하는 건 이번이 두번째지?"'
    '무슨 소리를 하는 걸까? 아이의 말은 도무지 이해가 안됐다.'
    scene bg black with Dissolve(1.0)
    $renpy.pause(1.0, hard = True)
    play sound teleport_snap

    scene bg BG_Garden_Night with Dissolve(0.01, alpha = True)
    # scene bg Black with None
    # show screen quick_menu
    '몽롱한 잠기운을 떨치기 위해 눈을 감았다 뜨니, 아이가 사라져 있었다.'
    '꿈이라도 꾼 건지, 귀신이라도 본 건지. '
    '신비로웠던 파란 머리의 아이는 꼭 요정 같았다.'
    '요정을 믿을 나이는 아닌데.'
    player '"..."'
    play sound standup

    player '"그나저나 여기가 어디야?"'

    "천천히 기억을 되짚어 보았다.\n"
    extend "아침에 일어나 집을 나와서, 학교에 가고..."
    "......."

    player '"차에 치였지."'
    '나를 향해 달려들었던 트럭이 기억 속에 선명하다.'
    '정면으로 달려와서 아무리 운이 좋아도 병원 생활을 할 줄 알았는데.'
    '오래 누워있을 때 느낄 수 있는 뻐근함을 제외하면, 딱히 아픈 부위는 없다.'

    player '"어쩌지..."'
    '납치당한 건가? 아니면 영화 속에서 흔히 보았던 사고로 인한 기억상실?'
    '사고가 났던 날 이후로 시간이 많이 흐른 건 아닌지 걱정 되었다.'
    '주변에 누가 있다면 물어라도 볼 텐데, 아무도 없었다.'

    "사람을 찾으러 가볼까?"

    menu:
        "그 자리에서 기다린다.":
            "괜히 돌아다니다 모르는 곳에서 미아가 되는 것보단 낫겠지."
            "누가 데리러 올지도 모르니까..."
            "그렇게 계속 기다렸지만, 누구도 나를 찾으러 오지 않았다."
            call walkway from _call_walkway
        "돌아다녀 본다.":
            call walkway from _call_walkway_1

    scene bg BG_Hill with Dissolve(1, alpha = True)
    play sound sea_waves_3
    player '"정원 끝이 절벽이라니... 신기하네 진짜."'
    "꿈을 꾸고 있는 기분이었다. 푸른 장미가 가득한 정원의 끝에 있는게 절벽이라니."
    "절벽에서 떨어지면 꿈에서 깰까 궁금했지만, 진짜로 죽으면 곤란하니 하지\n말아야지."
    "밑을 내려다보니 지상과 많이 떨어진 바다가 보였다."
    "물감을 풀어놓은 듯 진한 보라색 바다는 색이 선명했고, 그만큼 불길했다.
    밤하늘의 별이 반사되는 모습은 꼭 사람이 뛰어든 흔적 같았다."
    player '"진짜로 납치라도 된 건가."'

    "보라색 바다 위에서 날고 있는 섬과 푸른 장미가 가득한 정원.\n"
    extend "정상적인 방법으로는 이 섬을 나가는 것이 불가능할 것 같다."
    play sound FootStep2

    scene bg black with Dissolve(2, alpha = True)
    "달리 돌아볼 곳이 없어서, 있었던 곳으로 돌아가자 저택이 보였다."
    "왜 지금에서야 저택의 존재를 알게 된 건지 의문이 들 정도로 큰 저택."

    scene bg BG_Door with Dissolve(2.0)
    play sound DoorKnock
    "조심스럽게 저택의 문을 두드린 다음, 문을 열었다."
    stop music fadeout 1.0
    jump Day_0_1_Edit

label Day_0_1_Edit:
    play music horror_a
    play sound DoorCreak1
    scene bg BG_Door_Open with Dissolve(2.0)
    # scene bg BG_Corridor with Dissolve(2.0)
    $renpy.pause(3.0, hard = True)
    scene bg BG_Hall_dark with Dissolve(2.0)
    $renpy.pause(2.0, hard = True)
    '저택에 들어서니 보이는 것은 어두운 복도였다.'
    player '"아무도 없나?"'
    '조심히 주변을 둘러보던 중, 어디선가 말소리가 들려왔다.'
    voice Yunsarang_002
    unknown_yun '"그 말을 우리 보고 믿으라는 거예요?"'

    voice Isabel_001
    unknown_isabel '"...조금 당황스럽네요."'

    with vpunch
    voice Scarlet_01
    unknown_scarlet '"감히 어떤 자식이!"'
    voice Elice_01
    unknown_elice '"이 무슨 치욕적인..."'
    '들려오는 네 개의 목소리는 각각 분노와 경악에 차있었다.'
    # play sound hallsound.mp3
    '다른 상황이었다면 얼씬도 하지 않았겠지만, 지금은 선택지가 없었다.'
    '목소리가 들리는 곳으로 가는 나를 누군가 가로막았다.'
    play sound teleport_snap
    show Hyeyeon_Normal at admin_standsize_bs with None
    stop music
    admin '"잠깐 기다려!"'
    player '"어?"'
    '처음 눈을 떴을 때 보았던, 파란 머리의 아이다.'
    '분명 헛 것을 본 거라 생각했는데 실존하는 사람이었구나.'
    hide Hyeyeon_Normal with None
    show Hyeyeon_Angry at admin_standsize_ms with Dissolve(.5)
    play music comic_sound fadein 3.0
    admin '"주인님은 아직 메이드랑 만나면 안돼!"'
    player '"주인님이라니, 나한테 한 말이야?"'
    '주변을 둘러보면 나와 이 아이 밖에 없다.'

    hide Hyeyeon_Angry with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5)
    admin '"그럼! 여기 주인님 말고 다른 사람은 없잖아?"'
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Happy at admin_standsize_ms with Dissolve(.5)
    admin '"벌써 세 번째 만남이네. 다시 만나서 반가워!"'

    player '"세 번째라니... 그게 무슨 소리야?"'
    '이 아이를 본 건 지금이 두 번째다.'
    '정원에서 눈을 떴을 때와 지금.'
    '아이는 대답을 하지 않고 그저 미소만 지을 뿐이다.'
    player '"넌 누구야?"'
    '아이가 제대로 된 설명을 해주지 않아, 내가 먼저 물었다.'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5)
    show Hyeyeon_Laughter at admin_one_jump with None
    admin '"넌 누구야! 하고 물으신다면, 대답해 드리는게 인지상정!"'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Laughter at admin_standsize_ms_L with Dissolve(0.5, alpha = True)
    admin '"이 저택의 파괴를 막기 위해"'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Laughter at admin_standsize_ms_R with Dissolve(0.5, alpha = True)
    admin '"이 저택의 평화를 지키기 위해."'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Happy at admin_standsize_ms  with Dissolve(0.5, alpha = True)
    admin   '"사랑과 진실 어둠을 뿌리고 다니는\n'
    extend '이 게임의 감초, 귀염둥이 관리자입니다☆"'
    player '"과, 관리자?"'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(.5)
    admin '"그래, 이 저택의 모든 일을 관리하는 대단한 사람이지."'

    '이 큰 곳을 저렇게 작은 아이가 관리한다고?'
    hide Hyeyeon_Normal with None
    show Hyeyeon_Angry at admin_standsize_bs with Dissolve(.5)
    '믿을 수가 없다는 시선으로 보자, 관리자는 조금 화가난 표정을 지었다.'
    admin '"그 눈은 뭐야? 나를 의심하는 거야?!"'
    player '"그런게 아니라..."'

    hide Hyeyeon_Angry with None
    show Hyeyeon_Sad at admin_standsize_bs with Dissolve(.5)
    admin '"나는 저택에서는 못하는게 없는 신과 같은 존재라고!"'

    hide Hyeyeon_Sad with None
    show Hyeyeon_Absurd at admin_standsize_bs with Dissolve(.5)
    admin '"완벽한 건 아니지만.. 여튼..!" '

    hide Hyeyeon_Absurd with None
    show Hyeyeon_Angry at admin_standsize_bs with Dissolve(.5)
    admin '"내가 얼마나 유능한지 알려주지!"'

    play sound teleport_snap
    scene bg BG_Underoom with None
    '관리자가 손가락을 튕기자 장소가 바뀌었다.'
    # '(연회장 이외의 아무 장소로 이동)'
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(.5)
    admin '"주인님을 이렇게 이동시키는 것 이외에도, 저택 안의 물건은 모두 내 마음대로 움직일 수 있어!"'
    # '바닦을 쓰는 싸운드'
    '관리자가 손짓하자 빗자루들이 알아서 바닥을 쓸고, 걸레가 창문을 닦는 마법같은 일이 벌어졌다.'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(.5)
    admin '"나 혼자서도 얼마든지 이 저택을 관리할 수 있어."'
    player '"어... 응. 의심해서 미안."'

    hide Hyeyeon_Normal with None
    show Hyeyeon_Happy at admin_standsize_bs with Dissolve(.5)
    admin '"나는 착하니까 특별히 용서해줄게."'

    play sound teleport_snap
    scene bg BG_Hall_dark with None
    show Hyeyeon_Happy at admin_standsize_bs with None
    '자화자찬을 한 관리자는 다시 한 번 손가락을 튕겨서 원래 있던 장소로 돌아왔다.'
    player '"그래서... 여긴 어디야?"'
    player '"넌 누구고, 왜 날 주인님이라 불러?"'
    player '"아까 다른 사람들 목소리도 들었는데..."'

    # 굳은 표정
    hide Hyeyeon_Happy with None
    show Hyeyeon_Absurd at admin_standsize_bs with Dissolve(.5)
    '나의 질문 세례에 관리자의 표정이 점점 굳어갔다.'
    hide Hyeyeon_Absurd with None
    show Hyeyeon_Angry at admin_standsize_bs with Dissolve(.5)

    admin '"주인님!"'
    player '"응?"'
    hide Hyeyeon_Absurd with None
    show Hyeyeon_Angry at admin_one_jump with None
    admin '"질문 하나에 대답 하나야! 하나씩 말해!"'
    player '"아... 미안."'
    # 굳은 표정
    '내 사과에 관리자의 표정이 조금은 풀렸다.'

    hide Hyeyeon_Angry with None
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(.5)
    admin '"지금 다른 메이드가 주인님을 기다리고 있거든?"'
    admin '"걔네를 더 기다리게 하면 안되니까 간단하게 설명해줄게."'
    player '"어..."'

    hide Hyeyeon_Normal with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(.5)
    admin '"나는 저택의 관리자야. 그 이외의 정보 값은 줄 수 없으니 궁금해하지마!"'
    player '"으, 응."'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Angry at admin_standsize_bs with Dissolve(.5)
    admin '"더 크게 대답해!"'
    player '"네!"'

    hide Hyeyeon_Angry with None
    show Hyeyeon_Happy at admin_standsize_bs with Dissolve(.5)
    # 굳은 표정
    '재밌다는 표정을 짓는 관리자를 보니, 관리자의 장단에 놀아난 것 같다는 기분이 든다.'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Normal at admin_standsize_ms with Dissolve(.5)
    admin '"주인님을 주인으로 선택한 건 저택이야."'

    hide Hyeyeon_Normal with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5)
    admin '"어떤 기준으로 정해졌는지 나도 몰라."'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Absurd at admin_standsize_bs with Dissolve(.5)
    admin '"하지만... 메이드는 다르지."'
    player '"응?"'
    '관리자는 의미심장한 미소를 지으며 말을 이었다.'

    hide Hyeyeon_Absurd with None
    show Hyeyeon_Happy at admin_standsize_bs with Dissolve(.5)
    admin '"메이드 네 명은 끔찍한 죄를 지은 아~주 무서운 사람들이야."'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(.5)
    admin '"주인님의 역할은 이곳에서 3일이라는 시간을 보내며 네 명중 한 명을 선택하는 거야."'
    admin '"선택을 받은 메이드는 주인님과 같이 원래 세계로 돌아갈 수 있어."'
    player '"그 말인즉슨... 3일 후에야 집에 갈 수 있다는 거지?"'

    hide Hyeyeon_Normal with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(.5)
    admin '"응, 이건 주인님만 알고 있어야하는 사실이야."'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Absurd at admin_standsize_bs with Dissolve(.5)
    admin '"주인님의 선택을 받아야 나갈 수 있다는 걸 알게된 넷이 어떤 짓을 저지를지 나도 모르겠네."'
    player '"뭐, 더 알려줘야할 게 기억나면 나중에 알려줄게!"'

    hide Hyeyeon_Absurd with None
    show Hyeyeon_Happy at admin_standsize_bs with Dissolve(.5)
    admin '"지금은 주인님을 기다리는 네 명의 메이드를 만나러 가자고!"'
    '관리자는 내 등을 떠밀며 연회장의 문을 열었다.'

    scene bg black with Dissolve(2.0)
    stop music fadeout 2.0
    $renpy.pause(1.0,hard = True)
    jump FirstMeet

label FirstMeet:

    scene bg BG_Hall with Dissolve(2, alpha = True)

    # play music normal_b.mp3 fadein 2.0

    show Hyeyeon_Normal at admin_standsize_ms  with Dissolve(0.5, alpha = True)
    play music Normal_b

    admin '"다들 오래 기다렸지~?"'
    admin '"너희들이 기다리던 주인님을 모셔왔다고!"'

    hide Hyeyeon_Normal with None
    show Yun_fallinlove at yun_standsize_ms  with Dissolve(0.5, alpha = True)
    voice Yunsarang_003
    yun '"너는...?"'

    play sound Thud2
    with hpunch

    hide Yun_fallinlove with None
    show Scarlet_jjajeung at scarlet_standsize_ms  with Dissolve(0.5, alpha = True)

    voice Scarlet_02
    scarlet '"누구 마음대로 주인님이야\n' with hpunch
    voice Scarlet_03
    extend '내 주인님은 오직 한 분뿐이라고 말했을 텐데?"'

    show Elice_Strong at elice_standsize_ms_L with Dissolve(0.5, alpha = True)

    # 추가 바람
    voice Elice_02
    elice '"...주인? 그 녀석이?"'

    voice Elice_04
    elice '"이봐, 농담하는 거지? 너무 평범해 보이잖아."'

    show Isabel_soAngry at isabel_standsize_ms_R with Dissolve(0.5 ,alpha = True)
    voice Isabel_002
    isabel '"하아... 대뜸 사람을 데려다 놓고 주인으로 모시라길래, 어떤 사람인지 얼굴이라도 볼까 싶었는데..."'
    voice Isabel_003
    isabel '"이렇게 평범한 사람이라니..."'
    player '"평범한 사람이라 미안하네..."'

    # 캐릭터 전부 숨김

    hide Scarlet_jjajeung
    hide Elice_Strong
    hide Isabel_soAngry
    with Dissolve(0.5, alpha = True)

    show Scarlet_contempt at scarlet_standsize_ms with Dissolve(0.5, alpha = True)

    play sound Thud2
    with vpunch

    voice Scarlet_04
    scarlet '"죄송하면 죽어!"' with hpunch
    player '"갑자기?! 내가 무슨 잘못을 했다고!"'

    hide Scarlet_contempt with None
    show Elice_Strong at elice_standsize_ms with Dissolve(0.5, alpha = True)
    voice Elice_05
    elice '"우리의 주인이 되겠다고 얼굴을 들이민 것만으로도 큰 잘못이지..."'

    hide Elice_Strong with None
    show Yun_panic at yun_standsize_ms with Dissolve(0.5, alpha = True)
    voice Yunsarang_004
    yun '"[player]도 원해서 이곳에 온 건 아닐 거야... 그치?"'
    player '"어, 어! 나도 원해서 이런 곳에 온 게 아니야!"'

    show Scarlet_heung at scarlet_standsize_ms_L with Dissolve(0.5, alpha = True)
    play sound Thud2
    voice Scarlet_05
    scarlet '"그래도 짜증 나는 건 변하지 않으니까 죽어!"' with hpunch

    show Elice_Strong at elice_standsize_ms_R with Dissolve(0.5, alpha = True)
    voice Elice_06
    elice '"뻔뻔스럽기도 하지..."'

    hide Yun_panic with None
    show Isabel_contempt at isabel_standsize_ms with Dissolve(0.5 ,alpha = True)
    voice Isabel_004
    isabel'"머리 울리니까 다들 조용히 좀 해요.\n관리자님? 다 모였다면 설명 좀 해주시죠."'

    hide Isabel_contempt
    hide Scarlet_heung
    hide Elice_Strong
    with Dissolve(0.5, alpha = True)

    show Hyeyeon_Happy at admin_standsize_ms with Dissolve(0.5, alpha = True)
    admin '"다들 활기차서 보기 좋네!"'
    player '"모르는 사람한테 대뜸 죽으라고 말하는게 보기 좋아...?"'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(0.5, alpha = True)

    admin '"난 두 번 설명하지 않을 테니까, 귓구멍 똑바로 열고 들어?"'
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(0.5 ,alpha = True)
    admin '"이곳에 오기 전 마지막 기억에 대해서 떠올려 볼 사람?"'

    hide Hyeyeon_Normal with dissolve
    show Elice_Angry_2 at elice_standsize_ms_R with Dissolve(0.5, alpha = True)
    voice Elice_07
    elice '"..."'

    show Scarlet_displease at scarlet_standsize_ms_L with Dissolve(0.5, alpha = True)
    voice Scarlet_06
    scarlet'"..."'

    hide Hyeyeon_Happy with None
    show Yun_anxiety at yun_standsize_ms with Dissolve(0.5, alpha = True)
    voice Yunsarang_005
    yun '"...그게..."'

    hide Yun_anxiety
    hide Elice_Angry_2
    hide Scarlet_displease
    with Dissolve(0.5, alpha = True)

    show Isabel_heung at isabel_standsize_ms with Dissolve(0.5, alpha = True)
    voice Isabel_005
    isabel '"..."'
    '다들 관리자의 시선을 피하며, 대답을 회피했다.'
    '나랑 다르게 다들 기억나는게 있는 것 같은데...'

    hide Isabel_heung with None
    show Hyeyeon_Happy at admin_standsize_bs with Dissolve(0.5, alpha = True)
    admin '"굳이 말하지 않아도 괜찮아. 궁금한 게 아니었거든!"'

    hide Hyeyeon_Happy with None
    show Scarlet_contempt at scarlet_standsize_ms with Dissolve (0.5, alpha = True)
    voice Scarlet_07
    scarlet '"뭐야, 너...!"'

    hide Scarlet_contempt with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(0.5, alpha = True)
    admin '"후후... 너희의 육체는 저마다의 이유로 죽어가고 있는 상황이지..."'
    admin '"이 저택에 온 것은 오직 정신뿐,\n너희의 정신이 육체로 돌아가지 않으면..."'

    show Isabel_soAngry at isabel_standsize_ms_R with Dissolve(0.5, alpha = True)
    voice Isabel_006
    isabel '"육체는 죽어버리겠죠."'

    hide Hyeyeon_Laughter
    hide Isabel_soAngry
    with Dissolve(0.5, alpha = True)


    show Hyeyeon_Angry at admin_standsize_bs with Dissolve(0.5, alpha = True)
    play sound Thud2
    admin '"아직 내가 설명하고 있잖아! 내 말 끊지 마!"' with hpunch

    hide Hyeyeon_Angry with None
    show Isabel_panic at isabel_standsize_ms with Dissolve(0.5, alpha = True)
    voice Isabel_007
    isabel '"...죄송해요."'

    hide Isabel_panic with None
    show Hyeyeon_Angry at admin_standsize_bs with Dissolve(0.5, alpha = True)
    admin '"요즘 아이들은 이게 문제라니까. 어른이 말하는데 함부로 끼어들고."' # 꼰이네 이거
    hide Hyeyeon_Angry with None
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(0.5, alpha = True)
    admin '"아무튼 너희는 저택의 선택을 받아서 이곳에 오게 되었어."'
    admin '"저택은 너희 넷에게는 메이드라는 역할을 부여했고,\n주인님에게는 너희의 주인이라는 역을 주었지."'

    hide Hyeyeon_Normal with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(0.5, alpha = True)
    admin '"각자의 역할을 충실히 이행하다 보면 나갈 방법을 알게 될 거야~"'

    ############################### 01.16 수정

    hide Hyeyeon_Laughter with None
    show Elice_Strong at elice_standsize_ms_L with  Dissolve(0.5, alpha = True)
    # 누락
    voice Elice_08
    elice '"네 말을 들으면 저택이 어떤 의지를 가지고 있는 것 같군. 꼭 생명체처럼 말이야."'

    show Hyeyeon_Normal at admin_standsize_ms with Dissolve(0.5, alpha = True)
    admin '"네 말이 맞아. 이 저택은 살아있어. 너희를 메이드와 주인으로 고른 건 이 저택의 의지지."'

    show Isabel_pout at isabel_standsize_ms_R with Dissolve(0.5, alpha = True)
    voice Isabel_008
    isabel '"저택이 살아있다면, 저택에게 잘 보이면 이곳에서 나갈 수 있는 거잖아요?"'
    voice Scarlet_08
    scarlet '"아무리 살아있다지만 저택에게 잘 보인다고?"'
    voice Isabel_009
    isabel '"저택을 깨끗이 청소한다던가..."'

    admin '"푸하하, 재밌는 발상이지만 저택은 그런 걸 원하지 않아! 저택이 원하는 건 오직 주인님과 메이드 역할에 충실할 것!"'

    # show Isabel_pout at isabel_standsize_ms_R with Dissolve(.5)
    voice Isabel_010
    isabel '"그러면 주인님이 하는 말은 모두 들어야 하는 건가요? 별 괴상한 명령일지라도?"'
    admin '"글쎄... 그건 알아서 판단해!"'

    ############################### 01.16 수정

    #캐릭터 전체 숨김 , 디졸브 0.5초
    hide Hyeyeon_Normal
    hide Elice_Strong
    hide Isabel_pout
    with Dissolve(0.5, alpha = True)

    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(0.5, alpha = True)
    admin '"아니! 주인님의 명령을 꼭 들어야 한다는 규칙은 이 저택에 없어."'
    admin '"다만... 주인님의 명령을 거부할수록 저택에서 나가는 길은 멀어질걸~"'

    hide Hyeyeon_Laughter with Dissolve(0.5, alpha = True)
    show Scarlet_heung at scarlet_standsize_ms_L with Dissolve(0.5, alpha = True)
    voice Scarlet_09
    scarlet '"크릉... 난 마음에 안 들어! 저런 나약해 보이는 녀석이 주인이라니!"'

    voice Scarlet_10
    scarlet '"이런 곳 따위 그냥 나가면...!"'
    show Hyeyeon_Laughter at admin_standsize_ms_R with Dissolve(0.5, alpha =True)
    admin '"아직도 그런 생각을 하는 거야?"'
    admin '"멍청한 아이일수록 귀엽다지만... 이건 너무 심한데~"'

    play sound Thud2
    voice Scarlet_11
    scarlet '"뭐!? 감히 이 몸 보고 멍청하다고 해!"' with hpunch

    show Elice_coldsmiley_2 at elice_standsize_ms with Dissolve(0.5, alpha = True)
    voice Elice_09
    elice '"사실을 말한 것 같은데?"'

    voice Scarlet_12
    scarlet '"야!"' with hpunch

    hide Scarlet_heung
    hide Hyeyeon_Laughter
    hide Elice_coldsmiley_2
    with Dissolve(0.5, alpha = True)

    show Yun_panic at yun_standsize_ms with Dissolve(0.5, alpha = True)
    voice Yunsarang_006
    yun '"싸, 싸우지 마세요! 우리끼리 싸워봤자 득 될 것도 없고..."'

    hide Yun_panic with None  # 화면에서 지우는
    show Isabel_stare at isabel_standsize_ms with Dissolve(0.5, alpha = True) # 화면에 출력
    voice Isabel_013
    isabel '"다들 생각이 있는 건지 없는 건지..."' # 캐릭터 이름 ' 대사 '
    voice Isabel_011
    isabel '"이곳이 어떤 곳인지도 모르면서 쉽게 나갈 수 있을 거라 생각하는 거예요?"'
    voice Isabel_012
    isabel '"관리자의 설명을 들었다면 이곳에 온 건 정신뿐이란 걸 아실 텐데.\n육체가 어디에 있는 줄 알고 나간다고 말하는 거예요?"'

    show Scarlet_panic at scarlet_standsize_ms_L with Dissolve(0.5, alpha = True)

    voice Scarlet_13
    scarlet '"읏...!"'
    player '"애초에 이 섬이랄까... 저택 밖으로 나가는 것도 불가능해."'
    voice Scarlet_14
    scarlet '"뭐?"'
    player '"다들 밖으로 나가본 적 없는 거야?"'

    show Yun_fallinlove at yun_standsize_ms_R with Dissolve(0.5, alpha = True)
    voice Yunsarang_007
    yun '"으, 응! 일어나자 모이라고 관리자님께 안내받아서 계속 여기 있었어."'
    player '"그렇다면 바깥 상황은 모르겠네.\n이 저택 바깥으로 나가는 건 불가능에 가까워."'
    player '"저택이 있는 곳은 바다 위에 떠 있는 섬이야."'

    hide Yun_fallinlove
    hide Scarlet_panic
    hide Isabel_stare
    with Dissolve(0.5, alpha = True)
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(0.5, alpha =True)
    admin '"맞아! 이곳에서 나갈 방법은 하나도 없다고?"'
    admin '"그러니까 쓸모없이 힘 빼지 말고~"'
    admin '"이 저택에는 거스를 수 없는 규칙이 있지만, 너희는 몰라도 상관없어."'
    # admin '"이걸 알려주는 이유는, 귀찮게 굴지 말라는 뜻에서 말하는 거야~"'
    admin '"이상한 일이 일어나면 그냥 저택이 하는 거라고 생각해."'
    show Hyeyeon_Laughter at admin_bs_to_bs_R with None
    $renpy.pause(.2)
    show Elice_Contempt at elice_standsize_bs_L with Dissolve(0.5, alpha = True)
    voice Elice_10
    elice '"설명이 지나치게 생략되어 있지 않아?"'
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Happy at admin_standsize_bs_R with Dissolve(.5, alpha = True)
    admin '"더 궁금한 게 있다면 너희 주인님에게 물어보라고?"'
    player '"어, 나? 물어보면 최대한 아는 만큼 대답해 줄게...?"'

    hide Hyeyeon_Happy
    hide Elice_Contempt
    with Dissolve(0.5, alpha = True)

    show Scarlet_inflate at scarlet_standsize_ms with Dissolve(0.5, alpha = True)
    voice Scarlet_15
    scarlet '"왜 저 자식이 주인인 거지?"'

    hide Scarlet_inflate with None
    show Elice_Difficulty at elice_standsize_ms with Dissolve(0.5, alpha = True)
    voice Elice_11
    elice '"도대체 무슨 기준으로 정한 건지..."'

    hide Elice_Difficulty with None
    show Hyeyeon_Happy at admin_standsize_ms with Dissolve (0.5, alpha = True)
    admin '"밤이 늦었으니, 다들 자기소개만 하고 자러 가자!"'
    admin '"좋든 싫든, 함께 시간을 보내야 할 사이잖아?"'

    show Elice_Difficulty at elice_standsize_ms_L with Dissolve(0.5, alpha = True)
    voice Elice_12
    elice '"...하아."'

    show Isabel_pout at isabel_standsize_ms_R with Dissolve(0.5, alpha = True)
    voice Isabel_014
    isabel '"...별로 마음에 들진 않지만."'

    hide Hyeyeon_Happy with None
    show Scarlet_displease at scarlet_standsize_ms with Dissolve(0.5, alpha = True)
    play sound Thud2
    voice Scarlet_16
    scarlet '"젠장... 그분의 목소리가 들리지 않아!"' with hpunch
    '다들 자기 할 말만 하기 바쁜 와중, 윤사랑이 조용히 손을 들었다.'

    hide Elice_Difficulty
    hide Isabel_pout
    hide Scarlet_displease
    with Dissolve(0.5, alpha = True)

    show Yun_Normal at yun_standsize_bs with Dissolve(0.5, alpha = True)
    voice Yunsarang_008
    yun '"음... 먼저 시작하는 분이 없으면 제가 해도 괜찮을까요?"'
    admin '"그래그래, 다들 주목!"'

    hide Yun_Normal with None
    show Yun_Happy at yun_standsize_bs with Dissolve(0.5, alpha = True)
    voice Yunsarang_009
    yun '"제 이름은 윤 사랑! 평생 사랑받고 살라는 의미로 어머니가 지어주셨어요!"'

    hide Yun_Happy with None
    show Yun_Normal at yun_standsize_bs with Dissolve(0.5, alpha = True)
    voice Yunsarang_010
    yun '"음... 평범하다고 말하면 평범했던 학생이었고요!"'

    hide Yun_Normal with None
    show Yun_lookout at yun_standsize_bs with Dissolve(.5 , alpha = True)
    voice Yunsarang_011
    yun '"더 말씀드릴 게 없네요..."'

    hide Yun_lookout with None
    show Yun_Happy at yun_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Yunsarang_012
    yun '"같이 지내는 동안 사이좋게 지냈으면 좋겠어요!"'
    '자기소개를 하는 시간이라서 존댓말을 쓰는 건가?'
    '분명 아까 나한테는 반말했던 것 같은데...'

    hide Yun_Happy with Dissolve(0.5, alpha = True)
    show Isabel_Normal at isabel_standsize_ms with Dissolve(0.5, alpha = True)
    voice Isabel_015
    isabel '"다들 그닥 의욕이 없어 보이니 다음은 제가 하죠."'

    hide Isabel_Normal with None
    show Isabel_Normal at isabel_standsize_bs with Dissolve(0.5, alpha = True)
    voice Isabel_016
    isabel '"제 이름은 이자벨, 보시다시피 환자예요."'

    hide Isabel_Normal with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Isabel_017
    isabel'"남들보다 체력이 약해서 빨리 자러 가야 하니까..."'
    voice Isabel_018
    isabel '"다른 분들도 자기소개를 끝내고 갔으면 좋겠네요."'

    hide Isabel_pout with None
    show Elice_Surprised_2 at elice_standsize_bs with Dissolve(0.5, alpha = True)
    voice Elice_13
    elice '"흥... 내 이름은 엘리스. 이거면 충분하지?"'
    voice Elice_14
    elice '"하찮은 너희와 어울릴 생각 따위 없어."'

    hide Elice_Surprised_2 with None
    show Scarlet_displease at scarlet_standsize_ms with Dissolve(0.5, alpha = True)
    voice Scarlet_17
    scarlet '"크흥... 이 몸의 이름은 스칼렛 아나스타샤!"'
    voice Scarlet_18
    scarlet '"위대하신 그분을 모시는 몸으로, 그분께서 가장 아끼는 신도지."'

    voice Scarlet_19
    scarlet '"네 놈들과 어울릴 생각 따위는 없다!"'
    hide Scarlet_displease with None
    show Scarlet_Angry at scarlet_standsize_bs with Dissolve(0.5, alpha = True)
    voice Scarlet_20
    scarlet '"특히 너!"'
    player '"에, 나?"'
    hide Scarlet_Angry with None
    show Scarlet_contempt at scarlet_standsize_bs with Dissolve(.5 ,alpha = True)
    voice Scarlet_21
    scarlet '"그래 네놈! 나의 주인은 오직 위대하신 그분뿐이다!\n'
    voice Scarlet_22
    extend '감히 이 몸의 주인이 되었다는 착각 따위 하지 마라."'

    voice Scarlet_23
    scarlet '"만약 그런 착각 속에 빠져 산다면...'
    voice Scarlet_24
    extend'그분의 힘을 맛보게 해주지."'
    player '"나를 대체 어떤 사람으로 보는 거야..."'

    hide Scarlet_contempt with Dissolve(0.5, alpha = True)
    show Hyeyeon_Happy at admin_standsize_bs with Dissolve (0.5, alpha  = True)
    admin '"다들 사회성은 나빠 보이네~\n주인님도 같이 소개해 보는게 어때?"'
    player '"아... 그게 좋을 것 같네."'

    hide Hyeyeon_Happy with Dissolve(0.5, alpha = True)
    show Scarlet_Angry at scarlet_standsize_ms with Dissolve(0.5, alpha = True)
    show Elice_Strong at elice_standsize_ms_L with Dissolve(0.5, alpha = True)
    show Isabel_soAngry at isabel_standsize_ms_R with Dissolve(0.5, alpha = True)

    menu:
        "평범한 자기소개":
            player '"음, 내 이름은 [player]. 평범한 고등학생이야."'
            player '"어쩌다보니 너희의 주인이 되었지만,  괴상한 명령을 내릴 생각은 없어."'
            player '"그... 이 정도면 되는 거지?"'
            '내 말을 들은 이자벨이 미묘한 표정을 지었다.'

        "활기찬 자기소개":
            player '"다들 안녕! 난 [player]. 평범한 고등학생이었지만, 갑자기 이런 저택에 와버렸어."'
            player '"사랑이 말처럼 여기 있는 동안은 모두랑 사이좋게 지내고 싶어."'
            player '"궁금한 게 있으면 뭐든지 물어봐!"'
            '내 자기소개를 들은 윤사랑은 환하게 웃었다.'
            '다른 메이드들의 표정은 복잡했다. '
            '의심, 비웃음, 같잖음... 전부 부정적인 감정 뿐이다.'
        "사회 부적응자 자기소개":
            player '"...... 내 이름은 [player]"'
            player '"너희들처럼 어울릴 생각은 딱히 없으니까, 싸우지만 말자?"'
            '내 자기소개를 들은 스칼렛은 금방이라도 덤빌 것처럼 으르렁 거렸다.'
            '엘리스는 비웃음을 지었지만, 크게 거슬리지는 않았다.'


    hide Isabel_soAngry with None

    show Isabel_Normal at isabel_standsize_ms_R with Dissolve(0.5, alpha = True)
    voice Isabel_019
    isabel '"이제 소개가 끝났으니 자러 가도 되나요?"'

    hide Scarlet_Angry
    hide Elice_Strong
    hide Isabel_Normal
    with Dissolve(0.5, alpha = True)

    show Hyeyeon_Happy at admin_standsize_ms with Dissolve(0.5, alpha = True)
    admin '"그래, 2층에 각자의 방이 있으니 거기 가서 자!"'
    admin '"아침에 일어나는 대로 연회장으로 오면 아침을 줄 테니까~"'

    hide Hyeyeon_Happy with None
    '관리자의 말이 끝나기 무섭게 다들 자기 방으로 가버렸다.'
    '모두 나를 싫어하는 걸까? 라는 생각을 하다 윤사랑과 눈이 마주쳤다.'

    show Yun_cuty at yun_standsize_ms with Dissolve(0.5, alpha = True)

    '이상하게 낯이 익은 아이. 같은 학생이라서 그런걸까?'
    '윤사랑은 나를 빤히 쳐다보고 있었다.'
    '민망해진 나는 서둘러 자리에서 벗어났다.'

    hide Yun_cuty with Dissolve(0.5, alpha = True)
    play sound FootStep2
    scene bg black with Fade(1.0, 0.0, 1.0)
    stop music fadeout 2.0
    $ renpy.pause (2.5, hard = True)
    scene bg Myroom with Dissolve(2.0, alpha = True)
    play music Normal_a fadein 2.0
    '모두와 헤어지고 난 후, 내게 배정된 방으로 들어왔다.'
    '주인님이라길래 큰 방을 주나 기대했는데,\n학교 기숙사와 크게 다를 바가 없었다.'
    '"밖이 이렇게 밝은데 밤이라니..."'
    '해가 떠있는 창 밖은 무척이나 환했다.'
    '해가 지지않는걸 백야현상이라 하던가?'
    '실제로 보는건 처음이라 신기하기도 하지만... 편히 잠들기 어려울 것 같았다.'
    '"저택에 머무는 3일동안 해가 지는 일은 없을 거라 했으니... 내가 적응하는 수 밖에."'
    '그래도 관리자가 수면안대를 주고 갔기 때문에, 아예 잠들지 못하는 상황은 면할 수 있을 것 같다.'
    player '"하아... 이게 대체 무슨 일인지."'
    '평범한 고등학생이었던 난 어떤 이유에서인지 죽을 위기에 처했고\n저택이라 불리는 의문의 공간에 갇히게 되었다.'
    '관리자의 말대로라면 3일 후에 돌아갈 수 있지만...'
    '저 4명 중 누가 선량한 사람인 걸까?'
    player '"확실한 건, 스칼렛은 아닌 것 같아."'
    '위대한 그분이니, 신도니 하는 걸 보면...\n아무리 생각해도 사이비 신도다.'
    '그나마 평범하던 윤사랑과 이자벨... 묘하게 거만한 엘리스.'
    player '"관리자 말마따나 다들 매력적이긴 하네."'
    '윤사랑을 빼면 다들 성격이 나빠 보여서 그렇지.'
    '곰곰이 생각해 보았지만, 누가 관리자가 말하는 선량한 사람인지 명확하게\n짚을 수 없었다.'
    player '"아직 인사만 나눠본 거니까..."'
    '내일 메이드들과 이야기를 나누며 누가 무고한 시민인지 알아내 보자.'
    '다들 본인이 죄를 지어서 끌려온 걸 모르는 것 같았으니까.'
    '내가 멋대로 선량한 사람과 죄인을 구분할 자격이 있는가 의문이 들지 않았던 건 아니다.'
    '하지만 무고한 시민과 범죄자를 가릴 판단 능력 정도는 있지.'
    play sound Clothes
    '고민 탓에 지끈거리는 머리를 무시한 채 침대에 몸을 뉘었다.'
    '저택이라는 이름과 달리 평범한 천장은 집을 떠올린다.'
    '돌아가지 못하면 어쩌지... 아침까지 인사를 나눴던 어머니와 아버지가 떠오른다. '
    player '"하... 진짜..."'
    '눈앞이 흐려졌다. 옷소매로 눈가를 꾹꾹 눌러보아도, 여전히 흐렸다.'
    player '"3일만 있으면 집에 갈 수 있다고 했으니까..."'
    '지금은 관리자의 말을 믿는 수밖에 없다.'
    '잠들기 위해서 눈을 감으니, 곧 의식이 흐려졌다.'
    '그렇게 돌아다녔으니 지쳤던 거겠지...'
    '난 금방 잠들었다.'

    scene bg black with Fade(1.0 , 0.0 , 1.0 )
    stop music fadeout 2.0
    $ renpy.pause( 3.0)

    jump WakeUp_Event


label walkway:
    "이대로 누군가를 기다려봤자 달라지는 건 없을 거다.\n"
    extend "누가 데리러 온다는 것도 가정에 불과하니까..."
    "만날 사람이 있다면 돌아다니다 만날 수 있겠지."
    "하늘을 잔뜩 수놓은 별이 괴상하고, 불길하게 느껴졌다."
    play sound FootStep2
    "어디로 가야 할지 몰라 별을 따라서 발길 닫는 대로, 마음 가는 대로 움직였다."
    # play sound 걷는 사운드
    "정원은 무척이나 넓고, 신비했다.\n"
    extend "평소에는 못 보던 색의 꽃도 많았고, 잘 모르는 내가 봐도 관리가 잘된 곳이다."
    "얼마나 걸었는지 모르지만, 벌써 정원의 끝에 도착했다."
