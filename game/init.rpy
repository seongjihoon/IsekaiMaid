screen Mini_Scene(m_image, _x = 0.5, _y = 0.4):
    add m_image:
        align(_x, _y)

screen scrolluptest:
    add "images/bg/main/BG_Corridor.png"
    vbox at scrollup_credit:
        xalign .5
        for n, i in enumerate(displays):
            add "gui/frame.png"
            text i xalign .5

init:

    define first_Game = False

    ######### 제작자
    define displays =["GAME DESIGN",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "ART",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "PROGRAMMING",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "MUSIC",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "SPECIAL THANKS"]


    ######### 캐릭터 define
    define yun = Character("윤사랑", color = "#fde2db", voice_tag = "v_yun")
    define admin = Character("관리자", color = "#E2EFFC", voice_tag = "v_admin")
    define scarlet = Character("스칼렛", color = "#F9DFE0", voice_tag = "v_scalret")
    define elice = Character("엘리스", color ="#FFFF00", voice_tag = "v_elice")
    define isabel = Character("이자벨", color ="#F5ECFC", voce_tag = "v_isabel")
    define unknown = Character("???" , color = "ffffff")
    define unknown_yun = Character("???", color = "#fde2db", voice_tag = "v_yun")
    define unknown_admin = Character("???", color = "#E2EFFC", voice_tag = "v_admin")
    define unknown_scarlet = Character("???", color = "#F9DFE0", voice_tag = "v_scalret")
    define unknown_elice = Character("???", color ="#FFFF00", voice_tag = "v_elice")
    define unknown_isabel = Character("???", color ="#F5ECFC", voice_tag = "v_isabel")

    define player = Character("[player_name]", color = "#b7e1cd")
    define UnknownPlayer = Character("당신", color = "#b7e1cd")
    define UnknownPlayer2 = Character("누군가", color = "#b7e1cd")
    define player_name = ""
    define default_name = "진우"


    define SayCount = 0         # 한 대사당 몇 번 입을 열었다 땔 것 인지 카운팅
    define nameCheck = False

    # 아침에 깨우러 오는 친?구
    define yun_f = 0.0
    define elice_f = 0.0
    define scarlet_f = 0.0
    define isabel_f = 0.0

    # 누굴 도와줄 것인가?
    define GetOut_YvE = None

    # 선택지 해금 조건들
    # 엘리스
    define e_D_1_Lunch = False
    define e_D_1_Dinner = False
    define e_D_2_Morning = False
    define e_D_2_Dinner = False

    # 윤사랑
    # define y_D_1_Lunch

    # 스칼렛
    define s_D_1_Lunch = False
    define s_D_2_Morning = False
    define s_D_2_Lunch = False
    define s_D_2_Dinner = False


    # 이자벨
    define i_D_2_Morning = False
    define i_D_2_Lunch = False
    define i_D_2_Dinner = False

    ######### Character_Standing

    ########### 아이템 관련

    # 아이템 관련
    define gif_time = 0.025
    image itemBack = "gui/overlay/confirm.png"
    image img_gradation = "gui/Gradation.png"
    image get_Item_gif:
        "images/Item/getItem/Get_item (1).png"
        pause gif_time
        "images/Item/getItem/Get_item (2).png"
        pause gif_time
        "images/Item/getItem/Get_item (3).png"
        pause gif_time
        "images/Item/getItem/Get_item (4).png"
        pause gif_time
        "images/Item/getItem/Get_item (5).png"
        pause gif_time
        "images/Item/getItem/Get_item (6).png"
        pause gif_time
        "images/Item/getItem/Get_item (7).png"
        pause gif_time
        "images/Item/getItem/Get_item (8).png"
        pause gif_time
        "images/Item/getItem/Get_item (9).png"
        pause gif_time
        "images/Item/getItem/Get_item (10).png"
        pause gif_time
        "images/Item/getItem/Get_item (11).png"
        pause gif_time
        "images/Item/getItem/Get_item (12).png"
        pause gif_time
        "images/Item/getItem/Get_item (13).png"
        pause gif_time
        "images/Item/getItem/Get_item (14).png"
        pause gif_time
        "images/Item/getItem/Get_item (15).png"
        pause gif_time
        "images/Item/getItem/Get_item (16).png"
        pause gif_time
        "images/Item/getItem/Get_item (17).png"
        pause gif_time
        "images/Item/getItem/Get_item (18).png"
        pause gif_time
        "images/Item/getItem/Get_item (19).png"
        pause gif_time
        "images/Item/getItem/Get_item (20).png"
        pause gif_time
        "images/Item/getItem/Get_item (21).png"
        pause gif_time
        "images/Item/getItem/Get_item (22).png"
        pause gif_time
        "images/Item/getItem/Get_item (23).png"
        pause gif_time
        "images/Item/getItem/Get_item (24).png"
        pause gif_time
        "images/Item/getItem/Get_item (25).png"
        pause gif_time
        "images/Item/getItem/Get_item (26).png"
        pause gif_time
        "images/Item/getItem/Get_item (27).png"
        pause gif_time
        "images/Item/getItem/Get_item (28).png"
        pause gif_time
        "images/Item/getItem/Get_item (29).png"
        pause gif_time
        "images/Item/getItem/Get_item (30).png"
        pause gif_time
        "images/Item/getItem/Get_item (31).png"
        pause gif_time
        "images/Item/getItem/Get_item (32).png"
        pause gif_time
        "images/Item/getItem/Get_item (33).png"
        pause gif_time
        "images/Item/getItem/Get_item (34).png"
        pause gif_time
        "images/Item/getItem/Get_item (35).png"
        pause gif_time
        "images/Item/getItem/Get_item (36).png"
        pause gif_time
        "images/Item/getItem/Get_item (37).png"
        pause gif_time
        "images/item/getItem/Get_item (38).png"
        pause gif_time
        "images/item/getItem/Get_item (39).png"
        pause gif_time
        "images/item/getItem/Get_item (40).png"
        pause gif_time
        "images/item/getItem/Get_item (41).png"
        pause gif_time
        "images/item/getItem/Get_item (42).png"
        pause gif_time
        "images/item/getItem/Get_item (43).png"
        pause gif_time
        "images/item/getItem/Get_item (44).png"
        pause gif_time
        "images/item/getItem/Get_item (45).png"
        pause gif_time
        "images/item/getItem/Get_item (46).png"
        pause gif_time
        "images/item/getItem/Get_item (47).png"
        pause gif_time
        "images/item/getItem/Get_item (48).png"
        pause gif_time
        "images/item/getItem/Get_item (49).png"
        pause gif_time
        "images/item/getItem/Get_item (50).png"
        pause gif_time
        "images/item/getItem/Get_item (51).png"
        pause gif_time
        "images/item/getItem/Get_item (52).png"
        pause gif_time
        "images/item/getItem/Get_item (53).png"
        pause gif_time
        "images/item/getItem/Get_item (54).png"
        pause gif_time
        "images/item/getItem/Get_item (55).png"
        pause gif_time
        "images/item/getItem/Get_item (56).png"
        pause gif_time
        "images/item/getItem/Get_item (57).png"
        pause gif_time
        "images/item/getItem/Get_item (58).png"
        pause gif_time
        "images/item/getItem/Get_item (59).png"
        pause gif_time
        "images/item/getItem/Get_item (60).png"


        #     "images/char/Alice/Normal_2.png" # 열
        #     pause 0.15
        #     "images/char/Alice/Normal.png" # 닫
        #     pause 0.15
        #     repeat SayCount

    image Flower = "images/item/물든꽃_small.png"
    image Wine = "images/item/와인잔_small.png"
    image Alcohol = "images/item/술_small.png"
    image Ribbon = "images/item/리본_small.png"
    image Paper = "images/item/찢어진종이_small.png"
    image Bear = "images/item/곰인형_small.png"
    image SarangRing = "images/item/사랑이의반지_small.png"
    image Elice_pendant = "images/item/엘리스펜던트_small.png"



    image IsabelRing = "images/item/이자벨반지_small.png"
    image Elice_Hairpin = "images/item/머리핀_small.png"
    image Fountain_Pen = "images/item/만년필_small.png"
    image Dream_Catcher = "images/item/드림캐쳐팔찌_small.png"
    image Flowerpot = "images/item/문어화분_small.png"

    define Elice_pendant_txt = "images/item/엘리스펜던트_on.png"


    define Select = 1



    define item1 = "name"           # 첫번째 아이템의 이름
    define m_iFlavor_Text_xpos = 1100
    define m_iFlavor_Text_ypos = 425
    define m_strRibbonText = ['윤사랑이 준 붉은 리본.',
                                '사용하고 있던 리본을 준 것으로,',
                                '보고 있으면 윤사랑이 ‘붉은색’을',
                                '좋아한다는 사실이 떠오른다.',]
    define m_strWineText = ["엘리스가 건네준 와인잔.",
                                "와인잔에 남아있는 와인은 분명 고급이지만,",
                                "맛보려고 하면 자꾸 어디선가 ",
                                "관리자가 나타난다.",]
    define m_strAlcoholText = ['스칼렛이 준 꽤 비싸 보이는 와인.',
                                '어디다 써야 할지 용도를 짐작할 수 없어서',
                                '방에 전시용으로 두고 있다.',
                                '다른 메이드들의 오해는 덤으로 얻었다.',]
    define m_strPaperText = ['이자벨이 기록용으로 쓰라고 준 종잇장.',
                            '기록할 수 있는 펜이 없어서 사용하지',
                            '못하고 있다.',]

    define m_strFlowerText = ['엘리스처럼 물에 젖은 장미가지.',
                            '한번 보면, 좀처럼 시선을 떼기 어렵다.',
                            '좋은 향기가 나서 방에 장식하고 있다.',]
    define m_strBearText = ['윤사랑이 도움의 보답으로 준 곰인형.',
                            '손에 들고 있는 붉은색',
                            '하트가 특히 귀엽다.',
                            '뒤에서 자꾸 지켜보는 듯한 느낌을 준다.',]
    define m_strSarangRing = ['윤사랑이 건네준 반지.',
                            '‘Blind for Love’라고 쓰여져 있다.',
                            '윤사랑은 특별한 의미가 있는 ',
                            '반지가 아니니 부담가지지 말라고 하는데…?',]
    define m_strPandant = ['엘리스가 상이라고 준 펜던트 목걸이.',
                        '안에는 엘리스의 초상화가 그려져 있다.',
                        '무려 황제의 초상화가 그려진',
                        '펜던트니 소중히 간직해야 한다.',]
    define m_strHairpin = ['엘리스가 상으로 준 머리핀.',
                            '박혀있는 보석 하나하나가',
                            '귀한 것이라고 한다.',
                            '살림이 나빠지면 보석을 하나씩',
                            '내다 팔라는 조언은 덤이다.']
    define m_strIsabelRing = [ '이자벨이 보답으로 건네준 결혼반지.',
                            '당장 줄 수 있는 것이 이것 뿐이며,',
                            '큰 의미가 없다고 하지만…',
                            '들여다 보고 있으면 심란해진다.']

    define m_strPen = ['이자벨이 보답으로 준 만년필.',
                    '오묘한 보랏빛이 이자벨을 떠올리게 한다.',
                    '가지고 있는 잉크가 없지만,',
                    '차마 이자벨에게 그 사실을 말하지 못했다.']

    define m_strDreamcatcher = ['스칼렛이 공치사로 준 팔찌.',
                            '장식으로 드림캐처가 있어서',
                            '묘한 느낌을 준다.',
                            '손목에 차고 자면 악몽을 꾸지 않을 것 같다.']

    define m_strFlowerpot = ['스칼렛이 공치사로 준 화분.',
                            '문어가 그려진 귀여운 머그컵처럼 보이나,',
                            '사실은 흙을 담은 화분이다.',
                            '스칼렛이 열심히 찾은 네잎 클로버가 꽂혀있다.']





    ## 윤사랑
    image Yun_Normal = "images/char/Yunsarang/Yun_Normal.png"
    image Yun_Normal2 = "images/char/Yunsarang/Yun_Normal2.png"
    image Yun_Happy = "images/char/Yunsarang/Yun_Happy.png"
    image Yun_pout2 = "images/char/Yunsarang/Yun_pout2.png"
    image Yun_Sad2 = "images/char/Yunsarang/Yun_Sad2.png"
    image Yun_Laughter = "images/char/Yunsarang/Yun_Laughter.png"
    image Yun_Laughter2 = "images/char/Yunsarang/Yun_Laughter2.png"
    image Yun_Sad = "images/char/Yunsarang/Yun_Sad.png"
    image Yun_Angry = "images/char/Yunsarang/Yun_Angry.png"
    image Yun_Angry2 = "images/char/Yunsarang/Yun_Angry2.png"
    image Yun_cuty = "images/char/Yunsarang/Yun_cuty.png"
    image Yun_fallinlove = "images/char/Yunsarang/Yun_fallinlove.png"
    image Yun_huc = "images/char/Yunsarang/Yun_huc.png"
    image Yun_lookout = "images/char/Yunsarang/Yun_lookout.png"
    image Yun_panic = "images/char/Yunsarang/Yun_panic.png"
    image Yun_pout = "images/char/Yunsarang/Yun_pout.png"
    # image Yun_SmallSad = "images/char/Yunsarang/Yun_SmallSad.png"
    image Yun_stare = "images/char/Yunsarang/Yun_stare.png"
    image Yun_tear = "images/char/Yunsarang/Yun_tear.png"
    image Yun_wink = "images/char/Yunsarang/Yun_wink.png"
    image Yun_zero = "images/char/Yunsarang/Yun_zero.png"
    image Yun_anxiety = "images/char/Yunsarang/Yun_anxiety.png"

    image yun_SD_face = "images/gallery/page/FacePage_sarang.png"
    ## 윤사랑

    ## 앨리스
    #### 애니메이션
    # image alice_Normal:
    #     "images/char/Alice/Normal_2.png" # 열
    #     pause 0.15
    #     "images/char/Alice/Normal.png" # 닫
    #     pause 0.15
    #     repeat SayCount
    # image alice_Angry:
    #     "images/char/Alice/angry_2.png" # 열
    #     pause 0.15
    #     "images/char/Alice/angry.png" # 닫
    #     pause 0.15
    #     repeat SayCount
    # image alice_Coldsmiley:
    #     "images/char/Alice/cold smiley_2.png" # 닫
    #     pause 0.15
    #     "images/char/Alice/cold smiley.png" # 열
    #     pause 0.15
    #     repeat SayCount
    # image alice_Coloration:
    #     "images/char/Alice/Coloration_2.png"
    #     pause 0.15
    #     "images/char/Alice/Coloration.png"
    #     pause 0.15
    #     repeat SayCount
    # image alice_Committed:
    #     "images/char/Alice/Committed_2.png"
    #     pause 0.15
    #     "images/char/Alice/Committed.png"
    #     pause 0.15
    #     repeat SayCount
    # image alice_Contempt:
    #     "images/char/Alice/Contempt_2.png"
    #     pause 0.15
    #     "images/char/Alice/Contempt.png"
    #     pause 0.15
    #     repeat SayCount
    # image alice_Difficulty:
    #     "images/char/Alice/Difficulty_2.png"
    #     pause 0.15
    #     "images/char/Alice/Difficulty.png"
    #     pause 0.15
    #     repeat SayCount
    # image alice_Gladness:
    #     "images/char/Alice/Gladness_2.png"
    #     pause 0.15
    #     "images/char/Alice/Gladness.png"
    #     pause 0.15
    #     repeat SayCount
    # image alice_Happy:
    #     "images/char/Alice/Happy_2.png"
    #     pause 0.15
    #     "images/char/Alice/Happy.png"
    #     pause 0.15
    #     repeat SayCount
    # image alice_Ignore:
    #     "images/char/Alice/Ignore_2.png"
    #     pause 0.15
    #     "images/char/Alice/Ignore.png"
    #     pause 0.15
    #     repeat SayCount
    # image alice_Impression:
    #     "images/char/Alice/Impression_2.png"
    #     pause 0.15
    #     "images/char/Alice/Impression.png"
    #     pause 0.15
    #     repeat SayCount
    # image alice_Laughter:
    #     "images/char/Alice/Laughter_2.png"
    #     pause 0.15
    #     "images/char/Alice/Laughter.png"
    #     pause 0.15
    #     repeat SayCount
    # image alice_Love:
    #     "images/char/Alice/Love_2.png"
    #     pause 0.15
    #     "images/char/Alice/Love.png"
    #     pause 0.15
    #     repeat SayCount
    # image alice_Pudency:
    #     "images/char/Alice/Pudency_2.png"
    #     pause 0.15
    #     "images/char/Alice/Pudency.png"
    #     pause 0.15
    #     repeat SayCount
    # image alice_Strong:
    #     "images/char/Alice/Strong_2.png"
    #     pause 0.15
    #     "images/char/Alice/Strong.png"
    #     pause 0.15
    #     repeat SayCount
    # image alice_Surprised:
    #     "images/char/Alice/Surprised_2.png"
    #     pause 0.15
    #     "images/char/Alice/Surprised.png"
    #     pause 0.15
    #     repeat SayCount
    #### 애니메이션

    image Elice_Normal = "images/char/Elice/Elice_Normal.png"
    image Elice_Angry = "images/char/Elice/Elice_Angry.png"
    image Elice_Happy = "images/char/Elice/Elice_Happy.png"
    image Elice_Happy_2 = "images/char/Elice/Elice_Happy_2.png"
    image Elice_Laughter = "images/char/Elice/Elice_Laughter.png"
    image Elice_Laughter_2 = "images/char/Elice/Elice_Laughter_2.png"
    image Elice_Love = "images/char/Elice/Elice_Love.png"
    image Elice_Love_2 = "images/char/Elice/Elice_Love_2.png"
    image Elice_Strong = "images/char/Elice/Elice_Strong.png"
    image Elice_Difficulty = "images/char/Elice/Elice_Difficulty.png"
    image Elice_coldsmiley_2 = "images/char/Elice/Elice_coldsmiley_2.png"
    image Elice_Contempt = "images/char/Elice/Elice_Contempt.png"
    image Elice_Coloration = "images/char/Elice/Elice_Coloration.png"
    image Elice_Normal_2 = "images/char/Elice/Elice_Normal_2.png"
    image Elice_Coloration_2 = "images/char/Elice/Elice_Coloration_2.png"
    image Elice_Gladness = "images/char/Elice/Elice_Gladness.png"
    image Elice_Surprised = "images/char/Elice/Elice_Surprised.png"
    image Elice_Strong_2 = "images/char/Elice/Elice_Strong_2.png"
    image Elice_Angry_2 = "images/char/Elice/Elice_Angry_2.png"
    image Elice_Difficulty_2 = "images/char/Elice/Elice_Difficulty_2.png"
    image Elice_Surprised_2 = "images/char/Elice/Elice_Surprised_2.png"
    image Elice_coldsmiley = "images/char/Elice/Elice_cold smiley.png"
    image Elice_Gladness_2 = "images/char/Elice/Elice_Gladness_2.png"
    image Elice_Ignore = "images/char/Elice/Elice_Ignore.png"
    image Elice_Ignore_2 = "images/char/Elice/Elice_Ignore_2.png"
    image Elice_Committed = "images/char/Elice/Elice_Committed.png"
    image Elice_Pudency = "images/char/Elice/Elice_Pudency.png"
    image Elice_Pudency_2 = "images/char/Elice/Elice_Pudency_2.png"
    image Elice_Committed_2 = "images/char/Elice/Elice_Committed_2.png"
    image Elice_Contempt_2 = "images/char/Elice/Elice_Contempt_2.png"
    image Elice_Impression = "images/char/Elice/Elice_Impression.png"
    image Elice_Impression_2 = "images/char/Elice/Elice_Impression_2.png"


    image elice_SD_Face = "images/gallery/page/FacePage_alice.png"


    ## 앨리스

    ## 관리자
    image Hyeyeon_Normal = "images/char/Admin/Hyeyeon_Normal.png"
    image Hyeyeon_Absurd = "images/char/Admin/Hyeyeon_Absurd.png"
    image Hyeyeon_Angry = "images/char/Admin/Hyeyeon_Angry.png"
    image Hyeyeon_Happy = "images/char/Admin/Hyeyeon_Happy.png"
    image Hyeyeon_Sad = "images/char/Admin/Hyeyeon_Sad.png"
    image Hyeyeon_Laughter = "images/char/Admin/Hyeyeon_Laughter.png"


    image admin_SD_Face = "images/gallery/page/FacePage_admin.png"
    ## 관리자

    ## 이자벨
    image Isabel_Normal = "images/char/isabella/Isabel_Normal.png"
    image Isabel_Angry = "images/char/isabella/Isabel_Angry.png"
    image Isabel_soAngry = "images/char/isabella/Isabel_soAngry.png"
    image Isabel_Happy = "images/char/isabella/Isabel_Happy.png"
    image Isabel_Laughter = "images/char/isabella/Isabel_Laughter.png"
    image Isabel_Laughter2 = "images/char/isabella/Isabel_Laughter2.png"
    image Isabel_Sad = "images/char/isabella/Isabel_Sad.png"
    image Isabel_anxiety = "images/char/isabella/Isabel_anxiety.png"
    image Isabel_contempt = "images/char/isabella/Isabel_contempt.png"
    image Isabel_fear = "images/char/isabella/Isabel_fear.png"
    image Isabel_heung = "images/char/isabella/Isabel_heung.png"
    image Isabel_lookout = "images/char/isabella/Isabel_lookout.png"
    image Isabel_moving = "images/char/isabella/Isabel_moving.png"
    image Isabel_nodap = "images/char/isabella/Isabel_nodap.png"
    image Isabel_panic = "images/char/isabella/Isabel_panic.png"
    image Isabel_pout = "images/char/isabella/Isabel_pout.png"
    image Isabel_soAngry = "images/char/isabella/Isabel_soAngry.png"
    image Isabel_stare = "images/char/isabella/Isabel_stare.png"
    image Isabel_tear = "images/char/isabella/Isabel_tear.png"

    image isabel_SD_Face = "images/gallery/page/FacePage_esabella.png"
    ## 이자벨

    ## 스칼렛
    image Scarlet_Normal = "images/char/scarlet/Scarlet_Normal.png"
    image Scarlet_Angry  = "images/char/scarlet/Scarlet_Angry_1.png"
    image Scarlet_Angry2 = "images/char/scarlet/Scarlet_Angry2.png"
    image Scarlet_contempt = "images/char/scarlet/Scarlet_contempt.png"
    image Scarlet_Happy = "images/char/scarlet/Scarlet_Happy.png"
    image Scarlet_Laughter = "images/char/scarlet/Scarlet_Laughter.png"
    image Scarlet_Laughter2 = "images/char/scarlet/Scarlet_Laughter2.png"
    image Scarlet_Sad = "images/char/scarlet/Scarlet_Sad.png"
    image Scarlet_Sad2 = "images/char/scarlet/Scarlet_Sad2.png"
    image Scarlet_displease = "images/char/scarlet/Scarlet_displease.png"
    image Scarlet_heung = "images/char/scarlet/Scarlet_heung.png"
    image Scarlet_inflate = "images/char/scarlet/Scarlet_inflate.png"
    image Scarlet_jjajeung = "images/char/scarlet/Scarlet_jjajeung.png"
    image Scarlet_lookout = "images/char/scarlet/Scarlet_lookout.png"
    image Scarlet_nonSad = "images/char/scarlet/Scarlet_nonSad.png"
    image Scarlet_panic = "images/char/scarlet/Scarlet_panic.png"
    image Scarlet_pout = "images/char/scarlet/Scarlet_pout.png"
    image Scarlet_ppagchim = "images/char/scarlet/Scarlet_ppagchim.png"
    image Scarlet_stare = "images/char/scarlet/Scarlet_stare.png"
    image Scarlet_tear = "images/char/scarlet/Scarlet_tear.png"
    image Scarlet_socontempt = "images/char/scarlet/Scarlet_socontempt.png"
    image Scarlet_sojiajeung = "images/char/scarlet/Scarlet_sojiajeung.png"
    image Scarlet_sotear = "images/char/scarlet/Scarlet_sotear.png"
    image Scarlet_soppagchim = "images/char/scarlet/Scarlet_soppagchim.png"



    image scarlet_SD_Face ="images/gallery/page/FacePage_scarlet.png"
    ## 스칼렛

    ## defualt Image
    image BG_Sea_Past = "images/bg/main/BG_Sea_Past.png"


    #
    # ## 호감도 관련
    # define yun_favorability = 0
    # define alice_favorability = 0
    # define admin_favorability = 0
    # define scarlet_favorability = 0
    # define isabel_favorability = 0

    ## 음악 관련
    define emotional = "audio/BGM/emotional_1.mp3"
    define serious_little = "audio/BGM/serious_little.mp3"
    define comic = "audio/BGM/comic.mp3"
    define comic_sound = "audio/BGM/comic_sound.mp3"
    define Elicetheme = "audio/BGM/Elicetheme.mp3"
    define Elice_horror = "audio/BGM/Elice_Horror.mp3"
    define MiniGame = "audio/BGM/MiniGame.mp3"
    define Yunsarang_1 = "audio/BGM/Yunsarang_1.mp3"
    define Yunsarang_2 = 'audio/BGM/Yunsarang_2.mp3'
    define Isabel_1 = "audio/BGM/Isabella_1.mp3"
    define Isabel_2 = "audio/BGM/Isabella_2.mp3"
    define Isabel_Love_Master = "audio/BGM/Isabel_Love_Master.mp3"
    define Isabel_Ending_Master = "audio/BGM/Isabel_Ending_Master.mp3"
    define Scarlet_1 = "audio/BGM/Scarlet_1.mp3"
    define Scarlet_Cult = "audio/BGM/Scarlet_Cult_Mastering.mp3"
    define horror_A_Done = "audio/BGM/horror_A_Done.mp3"
    define scarlet_Horror = "audio/BGM/Scarlet_Horror_Mastering.mp3"
    define Normal_b = "audio/BGM/normal_b.mp3"
    define Normal_a = "audio/BGM/normal_a.mp3"
    define horror_a = "audio/BGM/horror_a.mp3"
    define horror_b = "audio/BGM/horror_b.mp3"
    define Ending_Credit = "audio/BGM/Ending_Credit.mp3"
    define emotional_2 = "audio/BGM/emotional_2.mp3"
    define main = "audio/BGM/main.mp3"

    ## 효과음
    define standup = "audio/EffectSound/standup.mp3"
    define DoorCreak1 = 'audio/EffectSound/DoorCreak1.mp3'
    define DoorOpen2 = "audio/EffectSound/DoorOpen2.mp3"
    define DoorKnock = "audio/EffectSound/DoorKnock.mp3"
    define DoorClose_2 = "audio/EffectSound/DoorClose_2.mp3"
    define Clothes = "audio/EffectSound/Clothes.mp3"
    define Car_attack = "audio/EffectSound/car_attack.mp3"
    define Thud1 = "audio/EffectSound/Thud1.mp3"
    define Thud2 = "audio/EffectSound/Thud2.mp3"
    define FootStep1 = "audio/EffectSound/FootStep1.mp3"
    define Jump1 = "audio/EffectSound/Jump1.mp3"
    define Jump2 = "audio/EffectSound/Jump2.mp3"
    define Footstep_flower = 'audio/EffectSound/Footstep_flower.mp3'
    define Footstep_flower_2 = "audio/EffectSound/Footstep_flower_2.mp3"
    define footstep_couple = 'audio/EffectSound/footstep_couple.mp3'
    define book_flipping = "audio/EffectSound/book_flipping.mp3"
    define Bowl = "audio/EffectSound/Bowl.mp3"
    define Bell = "audio/EffectSound/Bell.mp3"
    define Water1 = 'audio/EffectSound/water1.mp3'
    define run = 'audio/EffectSound/run.mp3'
    define rain = 'audio/EffectSound/rain.mp3'
    define rain_car = 'audio/EffectSound/rain_car.mp3'
    define rain_car_stop = 'audio/EffectSound/rain_car_stop.mp3'
    define rain_footstep = 'audio/EffectSound/rain_footstep.mp3'
    define rain_run = 'audio/EffectSound/rain_run.mp3'
    define teleport_out = 'audio/EffectSound/teleport_out.mp3'
    define teleport_snap = 'audio/EffectSound/teleport_snap.mp3'
    define teleport_world = 'audio/EffectSound/teleport_world.mp3'
    define car_fast = 'audio/EffectSound/car_fast.mp3'
    define ThudReverb = 'audio/EffectSound/ThudReverb.mp3'
    define FootStep2 = 'audio/EffectSound/FootStep2.mp3'
    define footstep_group = 'audio/EffectSound/footstep_group.mp3'
    define footstep_Elice = 'audio/EffectSound/footstep_Elice.mp3'
    define Table = 'audio/EffectSound/Table.mp3'
    define sea_waves_3 = 'audio/EffectSound/sea_waves_3.mp3'
    define hallsound = 'audio/EffectSound/hallsound.mp3'
    define Glass = 'audio/EffectSound/Glass.mp3'
    define Wind = 'audio/EffectSound/Glass.mp3'

    define ScarletMagic = 'audio/EffectSound/Scarlet_Sound/마법진/magiccircle.mp3'
    define fireoff = 'audio/EffectSound/Scarlet_Sound/마법진/fireoff.mp3'
    define fireon = 'audio/EffectSound/Scarlet_Sound/양초 불/fireon.mp3'
    define tinnitus = 'audio/EffectSound/Scarlet_Sound/이명/tinnitus.mp3'
    define thunderwave = 'audio/EffectSound/Scarlet_Sound/천둥번개/thunderwave.mp3'
    define monstersound = 'audio/EffectSound/Scarlet_Sound/크툴루 괴물/monstersound.mp3'
    define  vomit = 'audio/EffectSound/Scarlet_Sound/피 토하는/vomit.mp3'

    ######### voice
    ## init_Voice.rpy로 감.



    ######### bg
    image bg BG_Garden_Morning = "images/bg/main/BG_Garden_Morning.png"
    image bg BG_Garden_Night = "images/bg/main/BG_Garden_Night.png"
    image bg BG_Hill = "images/bg/main/BG_Hill.png"
    image bg BG_Hall = "images/bg/main/BG_Hall.png"
    image bg Myroom = "images/bg/main/BG_Myroom.png"
    image bg BG_Livingroom = "images/bg/main/BG_Livingroom.png"
    image bg BG_Library = "images/bg/main/BG_Library.png"
    image bg BG_Underoom = "images/bg/main/BG_Underoom.png"
    image bg BG_Underoom_Blood = "images/bg/main/BG_Underoom_Blood.png"
    image bg BG_Swirl = "images/bg/main/BG_Swirl.png"
    image bg BG_Adimroom = "images/bg/main/BG_Adimroom.png"
    image bg BG_Maidroom ="images/bg/main/BG_Maidroom.png"
    image bg BG_Corridor_2 = "images/bg/main/BG_Corridor_2.png"
    image bg BG_Corridor = "images/bg/main/BG_Corridor.png"
    image bg BG_Corridor_credit = "images/bg/main/BG_Corridor_credit.png"
    image bg BG_Door = "images/bg/main/BG_Door.png"
    image bg BG_Door_Open = "images/bg/main/BG_Door_2.png"
    image bg BG_Hall_dark = "images/bg/main/BG_Hall_dark.png"
    image bg BG_Sickroom = "images/bg/main/BG_Sickroom.png"
    # image bg BG_006_1 = "images/bg/main/BG_006_1.png"
    # image bg BG_006_2 = "images/bg/main/BG_006_2.png"
    # image bg BG_005 = "images/bg/main/BG_005.png"
    image bg BG_Reality_Truck = "images/bg/main/BG_Reality_Truck.png"
    image bg BG_light_Red = "images/bg/main/BG_light_Red.png"
    image bg BG_Elice_Ending = "images/bg/main/BG_Elice_Ending.png"
    image bg BG_Elice_Kingdom2 = "images/bg/main/BG_Elice_Kingdom2.png"
    image bg BG_Kingdom = "images/bg/main/BG_Kingdom.png"
    # image BG BG_Sea_Past = "images/bg/main/BG_Sea_Past.png"

    ########## BG_Cleaning_room
    image bg CleaningRoom_Isabel = "images/minigame/Isabel_Room/Minigame_Isabel_Background.png"
    image bg CleaningRoom_Scarlet = "images/minigame/Scarlet_Room/Minigame_Scarlet_Background.png"
    image bg CleaningRoom_Yun = "images/minigame/Sarang_Room/Minigame_Yun_Background.png"
    image bg CleaningRoom_Elice = "images/minigame/Elice_Room/Minigame_Elice_Background.png"

    ########## Mini_Cut_Scene
    define Yun_Yakusoku_1 = "images/Mini_Cut_Scene/사랑이 약속 최종_1.png"
    define Yun_Yakusoku_2 = "images/Mini_Cut_Scene/사랑이 약속 최종_2.png"
    define pail = "images/Mini_Cut_Scene/양동이.png"
    define Book = "images/Mini_Cut_Scene/책.png"
    define prayer = "images/Mini_Cut_Scene/스칼렛 기도 최종.png"
    define bag = "images/Mini_Cut_Scene/이자벨가방.png"
    image Food_Defualt = "images/Mini_Cut_Scene/음식_기본.png"
    define Food_Defualt_mini = "images/Mini_Cut_Scene/음식_기본_small.png"
    image Food_Clean = "images/Mini_Cut_Scene/음식_뚝딱.png"
    define Food_Clean_mini = "images/Mini_Cut_Scene/음식_뚝딱_small.png"
    define elice_Hand = "images/Mini_Cut_Scene/day3_elice_hand.png"
    define elice_seeing = "images/Mini_Cut_Scene/day3_elice_seeing.png"
    define Elice_Ending = "images/Mini_Cut_Scene/BG_Elice_Ending.png"
    define GlassBottle = "images/Mini_Cut_Scene/유리병.png"

    define scarlet_crying = "images/Mini_Cut_Scene/day3_scarlet_crying.png"
    define scarlet_hand = "images/Mini_Cut_Scene/day3_scarlet_hand.png"
    define scarlet_background = "images/Mini_Cut_Scene/day3_scarlet_background.png"

    image Elice_Mini = "images/Mini_Cut_Scene/엘리스미니컷씬.png"
    image BG_Garden_Night_Sky = "images/mini_cut_scene/BG_Garden_Night_Sky.png"

    define DemoEnding = "images/DemoEnding.png"
    define title_log = "gui/title_log2.png"



    image bg black = Solid("#000")
    image bg white = Solid("#fff")
    image bg red = Solid("#FF0000")

    ########## CharacterScene
    # image bg Elice_CG_001 = "images/Gallery/Elice/Elice_CG_001.png"
    # image bg Yun_CG_1 = "images/Gallery/Sarang/Yun_CG_001.png"
    # image bg Yun_CG_2 = "images/Gallery/Sarang/Yun_CG_002.png"
    # image bg_video = Movie(size=(1920, 1080), channel = "movie", play = "video/Chapter.avi", loop = False)
    # image bg_chapter1_ogg = Movie(size = (1920, 1080), channel = "movie", play = "video/챕터 폭탄/Chapter-01.avi", loop = False)
    # image bg_chapter2_ogg = Movie(size = (1920, 1080), channel = "movie", play = "video/챕터 폭탄/Chapter-02.avi", loop = False)
    # image bg_chapter3_ogg = Movie(size = (1920, 1080), channel = "movie", play = "video/챕터 폭탄/Chapter-03.avi", loop = False)
    # image bg_chapter4_ogg = Movie(size = (1920, 1080), channel = "movie", play = "video/챕터 폭탄/Chapter-04.avi", loop = False)
    image bg_chapter1_avi = Movie(size = (1920, 1080), channel = "movie", play = "video/챕터 폭탄/Chapter-01.avi", loop = False)
    image bg_chapter2_avi = Movie(size = (1920, 1080), channel = "movie", play = "video/챕터 폭탄/Chapter-02.avi", loop = False)
    image bg_chapter3_avi = Movie(size = (1920, 1080), channel = "movie", play = "video/챕터 폭탄/Chapter-03.avi", loop = False)
    image bg_chapter4_avi = Movie(size = (1920, 1080), channel = "movie", play = "video/챕터 폭탄/Chapter-04.avi", loop = False)
    image bg_Isekai_avi = Movie(size = (1920, 1080), channel = "movie", play = "video/챕터 폭탄/gogo.avi", loop = False)
    image bg_Isekai_ogg = Movie(size = (1920, 1080), channel = "movie", play = "video/gogo.ogg", loop = False)

    ######### transform

    ## 윤사랑
    transform yun_standsize_ms:
        xzoom .3
        yzoom .3
        align (.5, 2.00) # 낮을수록 캐릭터가 아래로 내려감3
    transform yun_standsize_ms_R:
        xzoom .3
        yzoom .3
        align (1.0, 2.00)
    transform yun_standsize_ms_L:
        xzoom .3
        yzoom .3
        align (.05, 2.00)
    transform yun_ms_to_down:
        xzoom .3
        yzoom .3
        align (.5, 0.30)
        linear .1 rotate -15
        linear .1 rotate 15
        linear .2 rotate -25 align (.5, .0)
        linear .1 rotate 25 align (.5, -.5)
        linear .1 rotate 90 align (.5, -3.5)
    transform yun_ms_to_Rout:   # 중앙 -> 오른쪽 화면 밖
        xzoom .3
        yzoom .3
        align (.5, 2.00)
        linear 0.8 align (1.9, 2.00)
    transform yun_ms_to_Lout:   # 중앙 -> 완쪽 화면 밖
        xzoom .3
        yzoom .3
        align (.5, 2.00)
        linear 0.8 align (-0.9, 2.00)


    transform yun_Lms_to_Lout_walk:
        xzoom .3
        yzoom .3
        align (.05, 2.00)
        linear .2 align (.01, 1.50)         # 1
        linear .2 align (-.03, 2.00)        # 2
        linear .2 align (-0.07, 1.50)       # 3
        linear .2 align (-0.11, 2.00)       # 4
        linear .2 align (-.15, 1.50)        # 5
        linear .2 align (-.19, 2.00)        # 6
        linear .2 align (-.23, 1.50)        # 7
        linear .2 align (-.27, 2.00)        # 8
        linear .2 align (-.31, 1.50)        # 9
        linear .2 align (-.35, 2.00)        # 10
        linear .2 align (-.39, 1.50)        # 11
        linear .2 align (-.43, 2.00)        # 12
        linear .2 align (-.47, 1.50)        # 13
        linear .2 align (-.51, 2.00)        # 14
        linear .2 align (-.55, 1.50)        # 15
        linear .2 align (-.59, 2.00)        # 16
        linear .2 align (-.63, 1.50)        # 17
        linear .2 align (-.67, 2.00)        # 18

    transform yun_Lout_to_Lms_Fast:
        xzoom .3
        yzoom .3
        align (-1.0, 2.00)
        linear 0.5 align (.05, 2.00)

    transform yun_Lms_to_Lout_Fast:
        xzoom .3
        yzoom .3
        align (0.05, 2.00)
        linear 0.5 align (-1.0, 2.00)

    transform yun_standsize_bs:
        xzoom 0.45
        yzoom 0.45
        align (.5,0.225) # 낮을수록 캐릭터가 아래로 내려감
    transform yun_standsize_bs_L:
        xzoom 0.45
        yzoom 0.45
        align (.5, .225)
    transform yun_one_jump:
        xzoom .3
        yzoom .3
        align (.5, 2.00)
        linear .1 align (.5 , 1.0)
        linear .1 align (.5 , 2.00)
    transform yun_one_jump_L:
        xzoom .3
        yzoom .3
        align (.05, 2.00)
        linear .1 align (.05, 1.0)
        linear .1 align (.05, 2.00)
    transform yun_one_jump_bs:
        xzoom .45
        yzoom .45
        align (.5, .255)
        linear 0.1 align (.5, .355)
        linear .1 align (.5, .225)
    transform yun_ms_L_to_ms:
        xzoom .3
        yzoom .3
        align (.05, 2.00)
        linear .5 align (.5 ,2.00)
    ## 윤사랑

    ## 엘리스
    transform elice_standsize_ms:
        xzoom .3
        yzoom .3
        align (.5, 2.0)
    transform elice_standsize_ms_L:
        xzoom .3
        yzoom .3
        align (.05, 2.0)
    transform elice_standsize_ms_R:
        xzoom .3
        yzoom .3
        align (0.9, 2.0)
    transform elice_standsize_bs:
        xzoom .45
        yzoom .45
        align (.4, -.20)
    transform elice_standsize_bs_R:
        xzoom .45
        yzoom .45
        align (0.95, -.20)
    transform elice_standsize_bs_L:
        xzoom .45
        yzoom .45
        align (-0.05, -.20)
    transform elice_bs_to_bs_L:
        xzoom .45
        yzoom .45
        align (.4, -.20)
        linear 1.0 align (-0.05, -.20)
    transform elice_one_jump_C:
        xzoom .3
        yzoom .3
        align (.5, 2.0)
        linear .1 align (.5, 1.5)
        linear .1 align (.5, 2.0)
    transform elice_bs_to_top:
        align (0.0, 1.0)
        linear 2.5 align (0.0, 0.25)

    ## 앨리스

    ## 스칼렛
    transform scarlet_standsize_ms:
        xzoom .35
        yzoom .35
        align (.5, .0)
    transform scarlet_standsize_ms_R:
        xzoom .35
        yzoom .35
        align (1.0, .0)
    transform scarlet_standsize_ms_L:
        xzoom .35
        yzoom .35
        align (.0, 0.0)
    transform scarlet_standsize_bs:
        xzoom 0.5
        yzoom .5
        align (.5, 0.15)

    transform scarlet_standsize_bs_L:
        xzoom 0.5
        yzoom .5
        align (-0.1, 0.15)

    transform scarlet_one_jump:
        xzoom .35
        yzoom .35
        align (.5, .0)
        linear 0.1 align (.5, .3)
        linear .1 align (.5, .0)
    transform scarlet_one_jump_Lms:
        xzoom .35
        yzoom .35
        align (.0, .0)
        linear 0.1 align (.0, .3)
        linear .1 align (.0 ,.0)
    transform scarlet_one_jump_Lbs:
        xzoom .5
        yzoom .5
        align (-.1, .15)
        linear 0.1 align (-.1, .3)
        linear .1 align (-.1 ,.15)
    transform scarlet_one_jump_bs:
        xzoom .5
        yzoom .5
        align (.5, .15)
        linear .1 align (.5, .3)
        linear .1 align (.5, .15)

    transform scarlet_ms_to_down:
        xzoom .35
        yzoom .35
        align (.5, .0)
        linear .4 align(.5, -1.0)
        # linear .1
        # linear .2 rotate -25 align (.5, .0 - .30)
        # linear .1 rotate 25 align (.5, -.5 - 0.30)
        # linear .1 rotate 90 align (.5, -3.5 - 0.30)

    ## 스칼렛

    ## 이자벨
    transform isabel_standsize_ms:
        xzoom .3
        yzoom .3
        align (.5, 1.0)
    transform isabel_one_jump_ms:
        xzoom .3
        yzoom .3
        align (.5, 1.0)
        linear 0.1 align (.5, .5)
        linear 0.1 align (.5, 1.0)
    transform isabel_standsize_ms_L:
        xzoom 0.3
        yzoom 0.3
        align (.01, 1.0)
    transform isabel_standsize_ms_R:
        xzoom 0.3
        yzoom .3
        align (1.0, 1.0)
    transform isabel_standsize_bs:
        xzoom .4
        yzoom .4
        align (.5, 0.05)

    transform isabel_one_jump_bs:
        xzoom 0.4
        yzoom 0.4
        align (.5, 0.05)
        linear 0.1 align (.5, 0.17)
        linear .1 align (.5, 0.05)

    transform isabel_standsize_bs_R:
        xzoom 0.4
        yzoom 0.4
        align (0.9, 0.05)
    transform isabel_standsize_bs_L:
        xzoom 0.4
        yzoom 0.4
        align (.01, 0.05)

    ## 이자벨

    ## 관리자
    transform admin_standsize_ms:
        xzoom .3
        yzoom .3
        align(.5, 1.00)
    transform admin_standsize_ms_L:
        xzoom .3
        yzoom .3
        align (.0,  1.00)
    transform admin_standsize_ms_R:
        xzoom .3
        yzoom .3
        align (1.0,  1.00)
    transform admin_standsize_bs:
        xzoom .5
        yzoom .5
        align (.5, .45)
    # transform admin_bs_to_bs_R:
    #     xzoom .5
    #     yzoom .5
    #     align (.5, .45)
    #     linear 1.0 align (1.2, .45)
    transform admin_standsize_bs_R:
        xzoom .5
        yzoom .5
        align (1.2, .45)
    transform admin_standsize_bs_L:
        xzoom .5
        yzoom .5
        align (-0.2, .45)
    transform admin_bs_to_bs_R:
        xzoom .5
        yzoom .5
        align (.5, .45)
        linear .2 align (1.2, .45)
    transform admin_ms_Rout_to_R:       # 빼꼼 들어오기
        xzoom .3
        yzoom .3
        align (2.5, 0.5)
        rotate -45
        linear 1.1 align (1.9, 0.5)    # 최종 이동 위치
    transform admin_ms_R_to_Rout:       # 빼꼼 나가기
        xzoom .3
        yzoom .3
        align(1.9, 0.5)
        rotate -45
        linear 1.1 align(2.5, .5)
    transform admin_one_jump:
        xzoom .3
        yzoom .3
        align (.5, 1.00)
        linear 0.1 align (.5, .00)
        linear .1 align (.5, 1.00)
    transform admin_one_jump_bs:
        xzoom .5
        yzoom .5
        align (.5 ,.45)
        linear .1 align (.5, .60)
        linear .1 align (.5, .45)
    transform admin_two_jump:
        xzoom .3
        yzoom .3
        align (.5, 1.00)
        linear 0.1 align (.5, .00)
        linear .1 align (.5, 1.00)
        linear 0.1 align (.5, .00)
        linear .1 align (.5, 1.00)


    transform admin_ms_L_to_Lout:
        xzoom .3
        yzoom .3
        align (-0.8, .5)
        rotate 45
        linear 1.1 align (-1.35, .5)

    transform admin_ms_Lout_to_L:
        xzoom .3
        yzoom .3
        align (-1.35, .5)
        rotate 45
        linear 1.1 align (-.8, .5)

    ## 관리자

    transform scrollup_credit:
        ypos 1. yanchor .0
        linear 50. ypos .0 yanchor 1.


    transform Scene_bs_to_top:
        # xzoom .95
        # yzoom .95
        align (.5, 1.0)
        linear 3.0 align (0.5, 0.2)


init 2:
    ## gallery 이미지 계열
    # elice
    image Elice_CG_1:
        im.FactorScale("images/Gallery/Elice/Elice_CG_001.png", 1)
        yalign 0.0
    image Elice_CG_2:
        im.FactorScale("images/Gallery/Elice/Elice_CG_009.png",1)
        yalign 0.0
    image Elice_CG_3_1:
        im.FactorScale("images/Gallery/Elice/Elice_CG_002.png",1)
        yalign 0.0
    image Elice_CG_3_2:
        im.FactorScale("images/Gallery/Elice/Elice_CG_003.png",1)
        yalign 0.0
    image Elice_CG_3_3:
        im.FactorScale("images/Gallery/Elice/Elice_CG_004.png",1)
        yalign 0.0
    image Elice_CG_4_1:
        im.FactorScale("images/Gallery/Elice/Elice_CG_005.png", 1)
        yalign 0.0
    image Elice_CG_4_2:
        im.FactorScale("images/Gallery/Elice/Elice_CG_006.png", 1)
        yalign 0.0
    image Elice_CG_4_3:
        im.FactorScale("images/Gallery/Elice/Elice_CG_007.png", 1)
        yalign 0.0
    image Elice_CG_3_4:
        im.FactorScale("images/Gallery/Elice/Elice_CG_008.png", 1)
        yalign 0.0
    # sarang
    image Sarang_CG_1_1:
        im.FactorScale("images/Gallery/Sarang/Yun_CG_001.png", 1)
        yalign 0.0

    image Sarang_CG_1_2:
        im.FactorScale("images/Gallery/Sarang/Yun_CG_002.png", 1)
        yalign 0.0
    image Sarang_CG_2:
        im.FactorScale("images/Gallery/Sarang/Yun_CG_003.png", 1)
        yalign 0.0

    image Sarang_CG_4:
        im.FactorScale  ("images/Gallery/Sarang/Yun_CG_004.png", 1)
        yalign 0.0

    image Sarang_CG_5:
        im.FactorScale("images/Gallery/Sarang/Yun_CG_005.png", 1)
        yalign 0.0

    # isabel
    image Isabel_CG_1:
        im.FactorScale("images/Gallery/isabel/Isabel_CG_001.png", 1)
        yalign 0.0

    image Isabel_CG_2_1:
        im.FactorScale("images/Gallery/isabel/Isabel_CG_002.png", 1)
        yalign 0.0

    image Isabel_CG_2_2:
        im.FactorScale("images/Gallery/isabel/Isabel_CG_003.png", 1)
        yalign 0.0

    image Isabel_CG_2_3:
        im.FactorScale("Images/Gallery/isabel/Isabel_CG_004.png", 1)
        yalign 0.0

    image Isabel_CG_2_4:
        im.FactorScale("Images/Gallery/isabel/Isabel_CG_005.png", 1)
        yalign 0.0

    image Isabel_CG_3:
        im.FactorScale("Images/Gallery/isabel/Isabel_CG_006.png", 1)
        yalign 0.0

    image Isabel_CG_4:
        im.FactorScale("Images/Gallery/isabel/Isabel_CG_007.png", 1)
        yalign 0.0

    #Scarlet
    image Scarlet_CG_1 :
        im.FactorScale("images/Gallery/scarlet/Scarlet_CG_001.png", 1)
        yalign 0.0
    image Scarlet_CG_2_1:
        im.FactorScale("images/Gallery/scarlet/Scarlet_CG_002.png", 1)
        yalign 0.0

    image Scarlet_CG_2_2:
        im.FactorScale("images/Gallery/scarlet/Scarlet_CG_003.png", 1)
        yalign 0.0

    image Scarlet_CG_2_3:
        im.FactorScale("images/Gallery/scarlet/Scarlet_CG_004.png", 1)
        yalign 0.0

    image Admin_CG_1:
        im.FactorScale("images/Gallery/Admin/Manager_CG_001.png", 1)
        yalign 0.0

    image Unknown:
        im.FactorSacle("images/Gallery/gal-locked.png", 1)
        yalign 0.0

init python:
    config.default_text_cps = 0.05



    credits = ('    ', 'Sim Hye-yeon', 'DIRECTOR, ARTDIRECTOR, PM, UI/UX DESIGNER, BACKGROUND ARTIST, CHARACTER ARTIST,  ITEM/OBJECT ARTIST'), ('기획', 'Kim Janghwan', 'MAIN SCENARIO WRITER'), ('기획', 'Jeon Jin-woo', 'GAME DESIGNER'),('아트', 'Choi Bo-young', 'CHARACTER ARTIST'), ('아트', 'Jeon Se-jin', 'CHARACTER ARTIST'), ('아트','Kwak Min-ju', 'CHARACTER ARTIST'), ('아트', 'MR.PARK', 'EFFECT DESINGER'), ('프로그래밍', 'Seong Ji_Hun', 'PROGRAMMER '), ('사운드', 'Choi Woo-yeol', 'MUSIC', 'DIRECTOR , COMPOSER'), ('사운드', 'Park Seolbin', 'SUPPORT COMPOSER')
    credits_s = "{size=80}TEAM. 청소도구함\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=50}" + c[1] + "\n"
        credits_s += "{size=30}" + c[2] + "\n"
        c1=c[0]
        credits_s += "\n\n\n\n"
    credits_s += "\n{size=40}Engine\n{size=60}" + renpy.version() #Nevermind. It's all good. :P



init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, font = "경기천년바탕_Regular.ttf", text_align=0.5, color="#D6D6D6")
    image theend = Text("{size=80}The end", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5, color = "D6D6D6")

init 1 python:


    class GetText(Action):
        def __init__(self,screen_name,input_id):
            self.screen_name=screen_name
            self.input_id=input_id
        def __call__(self):
            if renpy.get_widget(self.screen_name,self.input_id):
                return str(renpy.get_widget(self.screen_name,self.input_id).content)
    g = Gallery()

    g.locked_button = "images/Gallery/gal-locked.png"

    # sarang

    g.button("cg1")
    g.unlock_image("images/Gallery/Sarang/Yun_CG_001_small.png")

    g.button("cg2")
    g.unlock_image("images/Gallery/Sarang/Yun_CG_003_small.png")

    g.button("cg3")
    g.unlock_image("images/3.png")
    # g.unlock_image("images/Gallery/Sarang/Yun_CG_004_small.png")

    g.button("cg4")
    g.unlock_image("images/4.png")

    g.button("cg5")
    g.unlock_image("images/5.png")

    g.button("cg6")
    g.unlock_image("images/6.png")

    # elice

    g.button("cg7")
    g.unlock_image("images/Gallery/Elice/Elice_CG_001_small.png")
    g.button("cg8")
    g.unlock_image("images/Gallery/Elice/Elice_CG_009_small.png")
    g.button("cg9")
    g.unlock_image("images/Gallery/Elice/Elice_CG_002_small.png")
    g.button("cg10")
    g.unlock_image("images/Gallery/Elice/Elice_CG_005_small.png")
    g.button("cg11")
    g.unlock_image("images/Gallery/Elice/Elice_CG_001_small.png")
    g.button("cg12")
    g.unlock_image("images/Gallery/Elice/Elice_CG_001_small.png")

    # isabel
    g.button("cg13")
    g.unlock_image("images/Gallery/Isabel/Isabel_CG_001_small.png")
    g.button("cg14")
    g.unlock_image("images/Gallery/Isabel/Isabel_CG_001_small.png")
    g.button("cg15")
    g.unlock_image("images/Gallery/Isabel/Isabel_CG_001_small.png")
    g.button("cg16")
    g.unlock_image("images/Gallery/Isabel/Isabel_CG_007_small.png")
    g.button("cg17")
    g.unlock_image("images/Gallery/Isabel/Isabel_CG_001_small.png")
    g.button("cg18")
    g.unlock_image("images/Gallery/Isabel/Isabel_CG_001_small.png")

    # scarlet
    g.button("cg19")
    g.unlock_image("images/Gallery/Scarlet/Scarlet_CG_001_small.png")
    g.button("cg20")
    g.unlock_image("images/Gallery/Scarlet/Scarlet_CG_002_small.png")
    g.button("cg21")
    g.unlock_image("images/Gallery/Scarlet/Scarlet_CG_003_small.png")
    g.button("cg22")
    g.unlock_image("images/Gallery/Scarlet/Scarlet_CG_004_small.png")
    g.button("cg23")
    g.unlock_image("images/Gallery/Scarlet/Scarlet_CG_001_small.png")
    g.button("cg24")
    g.unlock_image("images/Gallery/Scarlet/Scarlet_CG_001_small.png")


    # sarng
    g.button("cg1")
    g.unlock_image("Sarang_CG_1_1")
    g.unlock_image("Sarang_CG_1_2")

    g.button("cg2")
    g.unlock_image("Sarang_CG_2")

    g.button("cg3")
    g.unlock_image("Sarang_CG_3")

    g.button("cg4")
    g.unlock_image("Sarang_CG_4")
    g.unlock_image("Sarang_CG_5")

    g.button("cg5")
    g.unlock_image("Unknown")

    g.button("cg6")
    g.unlock_image("Unknown")

    # elice

    g.button("cg7")
    g.unlock_image("Elice_CG_1")

    g.button("cg8")
    g.unlock_image("Elice_CG_2")

    g.button("cg9")
    g.unlock_image("Elice_CG_3_1")
    g.unlock_image("Elice_CG_3_2")
    g.unlock_image("Elice_CG_3_3")

    g.button("cg10")
    g.unlock_image("Elice_CG_4_1")
    g.unlock_image("Elice_CG_4_2")
    g.unlock_image("Elice_CG_4_3")

    g.button("cg11")
    g.unlock_image("Unknown")
    g.button("cg12")
    g.unlock_image("Unknown")

    # isabel
    g.button("cg13")
    g.unlock_image("Isabel_CG_1")
    g.button("cg14")
    g.unlock_image("Unknown")
    g.button("cg15")
    g.unlock_image("Unknown")
    g.button("cg16")
    g.unlock_image("Unknown")
    g.button("cg17")
    g.unlock_image("Unknown")
    g.button("cg18")
    g.unlock_image("Unknown")

    # scarlet
    g.button("cg19")
    g.unlock_image("Scarlet_CG_1")
    g.button("cg20")
    g.unlock_image("Scarlet_CG_2_1")
    g.unlock_image("Scarlet_CG_2_2")
    g.unlock_image("Scarlet_CG_2_3")
    g.button("cg21")
    g.unlock_image("Unknown")
    g.button("cg22")
    g.unlock_image("Unknown")
    g.button("cg23")
    g.unlock_image("Unknown")
    g.button("cg24")
    g.unlock_image("Unknown")

    # dummy
    g.button("cg100")
    g.unlock_image("")


    g.transition = dissolve # 디졸브 효과로 나타냄

init 1 python:

    style.default.color = "#000"

    mr = MusicRoom(fadeout = 1.0)

    mr.add("audio/EffectSound/paper.wav", always_unlocked = True)

    if persistent.m_bgetFlower == True:
        persistent.m_bgetFlower = True
    else:
        persistent.m_bgetFlower = False

    if persistent.m_bgetRibbon == True:
        persistent.m_bgetRibbon = True
    else:
        persistent.m_bgetRibbon = False

    if persistent.m_bgetAlcohol == True:
        persistent.m_bgetAlcohol = True
    else:
        persistent.m_bgetAlcohol = False

    if persistent.m_bgetWine == True:
        persistent.m_bgetWine = True
    else:
        persistent.m_bgetWine = False

    if persistent.m_bgetPaper == True:
        persistent.m_bgetPaper = True
    else:
        persistent.m_bgetPaper = False

    if persistent.m_bgetBear == True:
        persistent.m_bgetBear = True
    else:
        persistent.m_bget_Bear = False

    if persistent.m_bgetSarangRing == True:
        persistent.m_bgetSarangRing = True
    else:
        persistent.m_bgetSarangRing = False

    if persistent.m_bgetpendant == True:
        persistent.m_bgetpendant = True
    else:
        persistent.m_bgetpendant = False

    if persistent.m_bgetIsabelRing == True:
        persistent.m_bgetIsabelRing = True
    else:
        persistent.m_bgetIsabelRing = False

    if persistent.m_bgethairpin == True:
        persistent.m_bgethairpin = True
    else:
        persistent.m_bgethairpin = False

    if persistent.m_bgetpen == True:
        persistent.m_bgetpen = True
    else:
        persistent.m_bgetpen = False

    if persistent.m_bgetDreamcatcher == True:
        persistent.m_bgetDreamcatcher = True
    else:
        persistent.m_bgetDreamcatcher = False

    if persistent.m_bgetFlowerpot:
        persistent.m_bgetFlowerpot = True
    else:
        persistent.m_bgetFlowerpot = False

    persistent.m_unknown = False


    # quick text button color setting
    style.quick_button_text = Style(style.button_text)
    style.quick_button_text.color = "#FF0000"
    style.quick_button_text.hover_color = "#B80202"
    style.quick_button_text.selected_color = "#00FF00"

    res = False;
