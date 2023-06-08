label D_3_Morning:
    $ renpy.pause(3.0, hard = True)
    play music 'audio/BGM/Yunsarang_1.mp3'
    scene bg Myroom with Dissolve(1.5)
    play sound 'audio/EffectSound/DoorKnock.mp3'
    '똑똑똑, 문을 두드리는 소리가 들렸다.'
    '아마 메이드 중 하나겠지.'
    '굳이 대답하지 않고 다시 눈을 감았다.'
    play sound DoorOpen2

    '곧이어 철컥하고 문이 열리는 소리가 들렸다.'
    '오늘은 어제와 다른 메이드가 깨우러 왔을가?'
    '두근거리는 마음으로 눈을 꼬옥 감고 있었다.'
    '동화처럼 입을 맞추는 방식으로 깨워주지는 않겠지만...'
    '나도 사람이다 보니 어쩔 수 없게 기대하는 부분이 있잖아?'
    '가볍게 어깨를 두드리는 손길에 눈을 떠보면...'
    play sound Thud1
    play music comic_sound
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(.5)
    admin'"까꿍!"'
    '대뜸 얼굴을 들이민 관리자가 눈 앞에 있었다.'
    play sound Thud1
    player '"으아악!"' with vpunch
    '관리자를 보고 너무 놀란 나머지, 나도 모르게 소리를 질러버렸다.'
    '왜, 이 재수 없는 꼬맹이가 내 방에 들어온 거야!'
    '잔뜩 놀란 얼굴로 관리자를 바라보니, 관리자는 말없이 웃으며 나를 보고 있었다.'
    player '"무슨 일로 나를 깨우러 온 거야?"'
    player '"혹시 밥 먹으라고...?"'
    hide Hyeyeon_Normal with None
    show Hyeyeon_Angry at admin_standsize_bs with Dissolve(.5)
    admin '"그런 시시한 일로 주인님을 깨우러 왔을 리가 없잖아!"'
    hide Hyeyeon_Angry with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(.5)
    admin '"내일이 무슨 날인지 잊은 건 아니지?"'
    player '"내일이라면...."'
    hide Hyeyeon_Laughter with Dissolve(.5)
    '분명, 집으로 돌아갈 수 있는 날이다.'
    '그와 동시에 무고한 사람을 선택해야 하는 날...'
    '머릿속에 떠오르는 사람이 한 명 있지만, 그가 정말로 무고한 사람이 맞는지에 대한 확신은 없다.'
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(.5)
    admin '"내일은 주인님이 메이드 한 명을 고르는 날이지."'
    hide Hyeyeon_Normal with None
    show Hyeyeon_Absurd at admin_standsize_bs with Dissolve(.5)
    admin '"어떤 메이드인지는... 알고 있지?"'
    player '"그야 물론, 죄가 없는 사람을 찾는 거잖아."'
    hide Hyeyeon_Absurd with None
    show Hyeyeon_Happy at admin_standsize_bs with Dissolve(.5)
    '내 대답을 들은 관리자는 밝게 웃었다.'
    admin '"기억하고 있어서 다행이야."'
    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(.5)
    admin '"워낙 재밌게 놀고 있어서, 집으로 돌아가는 것도 포기하고 여기서 계속 살려고 하는 줄 알았다니까?"'
    player '"...그럴리가 없잖아."'
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(.5)
    admin '"그래~ 어차피 여기 남아있어봤자 주인님이 할 수 있는 것도 적고 말이야..."'
    player '"여기에 계속 머무를 수 있어?"'
    hide Hyeyeon_Normal with None
    show Hyeyeon_Happy at admin_standsize_bs with Dissolve(.5)
    admin '"글쎄? 어떨까나~"'
    hide Hyeyeon_Happy with None
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(.5)
    admin '"내가 이렇게 주인님을 찾아온 건 알려줘야하는 규칙이 있어서야!"'
    admin '"마지막 날이니만큼 매우 매우 특별한 규칙이지!"'
    player '"특별한 규칙?"'
    '관리자는 자연스럽게 말을 돌렸지만, 이전의 주제보다 지금의 이야기에 훨씬 관심이 갔다.'
    hide Hyeyeon_Normal with None
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(.5)
    admin '"마지막 날에는 딱 한 명의 메이드만 만날 수 있어."'
    admin '"선대 관리자들이 남긴 규칙이야. 좀 고리타분 할 수도 있지만, 나름의 이유가 있거든~"'
    player '"응?"'
    hide Hyeyeon_Normal with None
    show Hyeyeon_Absurd at admin_standsize_bs with Dissolve(.5)
    admin '"마지막 날에 여러 아이를 만나면, 동요하는 바람에 결정을 못 내린 사람이 꽤 있었거든."'
    admin '"걔 중 몇 명은 이곳에 남았다가 메이드 손에 죽기도 했지만..."'
    player '"메이드가 주인을 해칠 수도 있어?"'
    hide Hyeyeon_Absurd with None
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(.5)
    admin '"떠나야 할 때 떠나지 않으면, 더는 주인이 아니게 되니까."'
    hide Hyeyeon_Normal with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(.5)
    admin '"주인이 아닌 인간을 죽이는 건 저택이 금지하지 않는걸?"'
    
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Happy at admin_standsize_bs with Dissolve(.5)
    admin '"그러니까 주인님도 죽기 싫다면 빨리 돌아가는 게 좋아!"'
    '해맑게 웃는 관리자의 표정이 어딘가 섬뜩했다.'
    '잊고 지냈지만, 이 저택에 있는 메이드는 한 명을 제외한 모두가 흉악한 범죄자...'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(.5)
    admin '"그리고 말이야, 이미 주인님은 마음을 굳혔잖아?"'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(.5)
    stop music fadeout 1.0
    admin '"누가 무고한 사람인지."'
    player '"..."'

    hide Hyeyeon_Normal with None
    '나는 대답을 하지 않고, 어젯밤 만났던 그를 떠올렸다.'
    '마지막인 오늘 제대로 대화한 후, 그가 무고한 사람이란 것에 대한 확신을 가지고 싶었다.'
    player '"응... 그 녀석을 오늘 다시 만나고 싶어."'

    show Hyeyeon_Happy at admin_standsize_bs with Dissolve(.5)
    admin '"좋아. 다른 메이드들이랑 만나지 못하도록 손을 써둘 테니까, 너무 당황하지는 마?"'
    '담당자는 꺄르륵 웃는 소리를 내며 사라졌다.'
    '자... 이제 어제저녁에 만났던 그녀를 다시 만나러 가볼까?'
    scene bg black with Dissolve(2.0)
    # 호감도 관련해서 다음 문단으로 이동하나 현재는 선택지로 구현
    menu:
        "윤사랑을 만나러 간다.":
            jump meet_Sarang
            pass
        "이자벨을 만나러 간다.":
            jump meet_Isabel
            pass
        "엘리스를 만나러 간다.":
            jump meet_Elice
            pass
        "스칼렛을 만나러 간다.":
            jump meet_Scarlet
            pass
