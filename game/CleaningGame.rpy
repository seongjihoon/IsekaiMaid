###by 7dots Ruslan Nebykov
###license: cc by-sa
###free use, when specifying the author
# This is a mini-game to find items
# save this code to the game.rpy file in the root of the game

# Called like this:
# $ InitGame("bg_room", 5.0, True, (735, 300), "figure1", (640, 226), "figure2", (288, 38), "figure3", (115, 260), "figure4")
# $ StartGame()
# where bg_room is the name of the background file without an extension .jpg
# 5.0 - the number of seconds to execute the search (if <= 0, the timer is disabled)
# (735, 300), "figure1" - coordinates and file name of the object
# without extension .png
# items can be as many as you like
# all backgrounds and pictures of objects should be in the images folder
# at the exit - true or false (met within the allotted time or not)
# number of items found in the variable oLen
# total number of items in the variable maxLen

# $ GameAsBG () # shows the screen with pictures as a background, not clickable

# in the sounds folder should be the sound of "click.mp3"
# or, if it does not, then comment out the line:
# renpy.play ("sounds / click.mp3", channel = "sound")


init:
    image BG1 = "images/BG_Hall.png"
    default rand = 0
    default Scarlet_Trash1 = "images/minigame/Scarlet_Room/Respawn_Trash/Minigame_Item_Trash_1.png"
    default Scarlet_Trash2 = "images/minigame/Scarlet_Room/Respawn_Trash/Minigame_Item_Trash_2.png"
    default Scarlet_Trash3 = "images/minigame/Scarlet_Room/Respawn_Trash/Minigame_Item_Trash_Scarlet_Bread.png"
    default Scarlet_Special = "images/minigame/Scarlet_Room/Special_Object/Minigame_Item_Trash_Scarlet_chair.png"
    default Scarlet_Special_On = "images/minigame/Scarlet_Room/Special_Object/Minigame_Item_Trash_Scarlet_chair_on.png"

    default Scarlet_SD_Default = "images/char/Scarlet_SD/Scarlet_SD_Default.png"
    default Scarlet_SD_Fail = "images/char/Scarlet_SD/Scarlet_SD_Fail.png"
    default Scarlet_SD_Success = "images/char/Scarlet_SD/Scarlet_SD_Success.png"

    default Scarlet_TrashGame_BG = "images/minigame/Scarlet_Room/Minigame_Scarlet_Background.png"

    default Elice_Trash1 = "images/minigame/Elice_Room/Respawn_Trash/Minigame_Item_Trash_Alice_Foot.png"
    default Elice_Trash2 = "images/minigame/Elice_Room/Respawn_Trash/Minigame_Item_Trash_Alice_Statue3.png"
    default Elice_Trash3 = "images/minigame/Elice_Room/Respawn_Trash/Minigame_Item_Trash_Alice_Stone.png"
    default Elice_Special_1 = "images/minigame/Elice_Room/Special_Object/Minigame_Item_Trash_Alice_Frame1.png"
    default Elice_Special_1_on = "images/minigame/Elice_Room/Special_Object/Minigame_Item_Trash_Alice_Frame1_on.png"
    default Elice_Special_2 = "images/minigame/Elice_Room/Special_Object/Minigame_Item_Trash_Alice_Frame2.png"
    default Elice_Special_2_on = "images/minigame/Elice_Room/Special_Object/Minigame_Item_Trash_Alice_Frame2_on.png"
    default Elice_Special_3 = "images/minigame/Elice_Room/Special_Object/Minigame_Item_Trash_Alice_Frame3.png"
    default Elice_Special_3_on ="images/minigame/Elice_Room/Special_Object/Minigame_Item_Trash_Alice_Frame3_on.png"
    default Elice_Special_4 = "images/minigame/Elice_Room/Special_Object/Minigame_Item_Trash_Alice_Statue.png"
    default Elice_Special_4_on = "images/minigame/Elice_Room/Special_Object/Minigame_Item_Trash_Alice_Statue_on.png"
    default Elice_Special_5 = "images/minigame/Elice_Room/Special_Object/Minigame_Item_Trash_Alice_Statue2.png"
    default Elice_Special_5_on = "images/minigame/Elice_Room/Special_Object/Minigame_Item_Trash_Alice_Statue2_on.png"

    default Elice_SD_Default = "images/char/Elice_SD/Elice_SD_Default.png"
    default Elice_SD_Fail = "images/char/Elice_SD/Elice_SD_Fail.png"
    default Elice_SD_Success = "images/char/Elice_SD/Elice_SD_Success.png"

    default Elice_TrashGame_BG = "images/minigame/Elice_Room/Minigame_Elice_Background.png"

    default Yun_Trash1 = "images/minigame/Sarang_Room/Respawn_Trash/Minigame_Item_Trash_Yun_Food.png"
    default Yun_Trash2 = "images/minigame/Sarang_Room/Respawn_Trash/Minigame_Item_Trash_Yun_Plate.png"
    default Yun_Special_1 = "images/minigame/Sarang_Room/Special_Object/Minigame_Item_Trash_Yun_candle.png"
    default Yun_Special_1_on = "images/minigame/Sarang_Room/Special_Object/Minigame_Item_Trash_Yun_candle_on.png"
    default Yun_Special_2 = "images/minigame/Sarang_Room/Special_Object/Minigame_Item_Trash_Yun_chair.png"
    default Yun_Special_2_on = "images/minigame/Sarang_Room/Special_Object/Minigame_Item_Trash_Yun_chair_on.png"
    default Yun_Special_3 = "images/minigame/Sarang_Room/Special_Object/Minigame_Item_Trash_Yun_chair2_.png"
    default Yun_Special_3_on = "images/minigame/Sarang_Room/Special_Object/Minigame_Item_Trash_Yun_chair2_on.png"

    default Yun_Object1 = "images/minigame/Sarang_Room/Special_Object/Minigame_Item_Trash_Yun_chair.png"
    default Yun_Object2 = "images/minigame/Sarang_Room/Special_Object/Minigame_Item_Trash_Yun_chair2.png"
    default Yun_Table = "images/minigame/Sarang_Room/Special_Object/Minigame_Item_Trash_Yun_Desk.png"

    default Sarang_SD_Default = "images/char/Yunsarang_sd/Yun_SD_Default.png"
    default Sarang_SD_Fail = "images/char/Yunsarang_sd/Yun_sd_fail.png"
    default Sarang_SD_Success = "images/char/Yunsarang_SD/Yun_sd_success.png"

    default Sarang_TrashGame_BG = "images/minigame/Sarang_Room/Minigame_Yun_Background.png"

    default Isabel_Trash1 = "images/minigame/Isabel_Room/Respawn_trash/Minigame_Item_Trash_Isabel_Book.png"
    default Isabel_Trash2 = "images/minigame/Isabel_Room/Respawn_trash/Minigame_Item_Trash_Isabel_key1.png"
    default Isabel_Trash3 = "images/minigame/Isabel_Room/Respawn_trash/Minigame_Item_Trash_Isabel_key2.png"
    default Isabel_Trash4 = "images/minigame/Isabel_Room/Respawn_trash/Minigame_Item_Trash_Isabel_Paper.png"
    default Isabel_Trash5 = "images/minigame/Scarlet_Room/Respawn_Trash/Minigame_Item_Trash_1.png"

    default Isabel_SD_Default = "images/char/Isabel_sd/Isabel_SD_Default.png"
    default Isabel_SD_Fail = "images/char/Isabel_sd/Isabel_sd_fail.png"
    default Isabel_SD_Success = "images/char/Isabel_SD/Isabel_sd_success.png"

    default Isabel_TrashGame_BG = "images/minigame/Isabel_Room/Minigame_Isabel_Background.png"


    default pos_x = 150
    default pos_y = 400




init python:
    # window in the center of the screen
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    # automatic sprites
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '_', '/']
    config.automatic_images_strip = ["images"]

    oXY = []
    oSXY = []

    oN = []
    oSN1 = []
    oSN2 = []

    oSConbo = []

    oTrashSeet  = []       # 이 공간에는 어떤 쓰레기를 생성 할 것인지 알려줌
    oTrashPos = []         # 이 공간에는 어느 위치에 생성 할 것인지 알려줌
    oCombo = []
    oArea_X_1 = []
    oArea_X_2 = []
    oArea_Y_1 = []
    oArea_Y_2 = []

    oCg = []

    oBg = []

    oLen = 0
    maxLen = 0
    nowCount = 0
    CleaningPoint = 0

    oLast = -1
    oTime = 0.0
    oMaxTime = 5.0
    needTimer = False
    oActive = False
    oRes = False


    ExitMenu = False

    # SetPos와 SetTrash를 통해 랜덤으로 배치 할 아이템의 png와 position을 가져옴 최대 갯 수의 제한은 없음.
    def SetGame(*args):
        global oTrashSeet, oTrashPos
        oTrashSeet  = []       # 이 공간에는 어떤 쓰레기를 생성 할 것인지 알려줌
        oTrashPos = []         # 이 공간에는 어느 위치에 생성 할 것인지 알려줌

        for xy, obj_name in zip(args[0::2], args[1::2]):
            oTrashSeet.append(obj_name)
            oTrashPos.append(xy)

    def SetTrash(*args ):
        global oTrashSeet
        oTrashSeet = []

        for obj_name in args:
            oTrashSeet.append(obj_name)

    def SetPos_1(*args) :
        global oTrashPos
        oTrashPos= []

        for xy in args:
            oTrashPos.append(xy)

    def SetBoxPos(*args):
        #  박스 형태의 포지션을 가짐 args[0] x_0, y_0, args[1] x_1, y_1
        global oArea_X_1, oArea_X_2, oArea_Y_1, oArea_Y_2
        oArea_X_1 = []
        oArea_X_2 = []
        oArea_Y_1 = []
        oArea_Y_2 = []

        for x1, x2, y1, y2 in zip(args[0::4], args[1::4], args[2::4], args[3::4]):
            # randx = renpy.random.randint(x1, x2)
            # randy = renpy.random.randint(y1, y2)
            oArea_X_1.append(x1)
            oArea_X_2.append(x2)
            oArea_Y_1.append(y1)
            oArea_Y_2.append(y2)

    def SetSpacialObject(*args):
        global oSN1, oSN2, oSXY, oSCombo
        oSN1 = []
        oSN2 = []
        oSXY = []
        oSCombo = []

        for n1, n2, xy, combo in zip(args[0::4], args[1::4], args[2::4], args[3::4]):
            oSN1.append(n1)
            oSN2.append(n2)
            oSXY.append(xy)
            oSCombo.append(combo)


    # 1, 2, 3, 4로 bg page를 구분하고 그에 맞는 변수에 각 매개변수들을 삽입
    # Initialize the game, placing items on the screen
    def InitGame(bg, time):
        global oBg, oCg, oXY, oN, oCombo, oLen, maxLen, oLast, oTime, oMaxTime, oActive, needTimer, oRes, nowCount
        global oTrashSeet, oTrashPos, CleaningPoint, oArea_X_1, oArea_X_2, oArea_Y_1, oArea_Y_2
        oXY = []
        oN = []
        oCombo = []
        oLen = 0
        oBg = bg
        randArea = 0


        oLast = -1
        oTime = time
        oMaxTime = time
        maxLen = 0
        nowCount = 0
        oActive = True
        oRes = False
        CleaningPoint =0

        if oTime > 0.0:
            needTimer = True
        # for문으로 range를 이용하여 1 ~ 4의 숫자를 i에 대입
        # 그리고 1 ~ 4까지 반복.
        # for i in range(0, 4):
        #     rand = renpy.random.randint(0, 5)    # 랜덤으로 값을 하나 산출
        #     # trashseet와 trashPos Rand값을 가져와 oXY, oN에 대입
        #     if 1:
        #         # 여긴 중복을 막는 구간
        #
        #     oN.append(oTrashSeet[rand])
        #     oXY.append(oTrashPos[rand])
        #     # combo를 랜덤으로 설정함
        #     oCombo.append(renpy.random.randint(0, 2))
        #     maxLen += 1
        #     # rand =

        # for i in range(0, 4):
        #     rand = renpy.random.randint(0, len(oTrashSeet) - 1)
        #     oN.append(oTrashSeet[rand])
        #     oXY.append(oTrashPos[i])
        #     # combo를 랜덤으로 설정함
        #     oCombo.append(renpy.random.randint(0, 3))
        #     nowCount += 1
        for i in range(0, 10):
            rand = renpy.random.randint(0, len(oTrashSeet) - 1)
            oN.append(oTrashSeet[rand])
            randin = renpy.random.randint(0, len(oArea_X_2) - 1)
            # randin = renpy.random.randrange(0, 1)
            # 몰?루
            # 4개의 좌표를 기준으로 랜덤 값을 산출
            randX = renpy.random.randint(oArea_X_1[randin], oArea_X_2[randin])
            randY = renpy.random.randint(oArea_Y_1[randin], oArea_Y_2[randin])
            oXY.append((randX, randY))
            # oXY.append(oTrashPos[i])
            # combo를 랜덤으로 설정함
            oCombo.append(renpy.random.randint(0, 3))
            nowCount += 1
        maxLen = 50

    def InitGame2(bg, time, *args):
        global oBg, oXY, oN, oCombo, oLen, maxLen, oLast, oTime, oMaxTime, oActive, needTimer, oRes
        oXY = []
        oN = []
        oCombo = []
        oLen = 0
        oBg = bg

        oLast = -1
        oTime = time
        oMaxTime = time
        maxLen = 0
        oActive = True
        oRes = False

        if oTime > 0.0:
            needTimer = True
        for xy, obj_name, hit_combo in zip(args[0::3], args[1::3], args[2::3]):
            oXY.append(xy)
            oN.append(obj_name)
            oCombo.append(hit_combo)
            maxLen += 1
    def SetStanding(*args):
        global oCg
        oCg = []

        for cgs in args:
            oCg.append(cgs)     # CG를 순서대로 저장


    # Running the game
    def StartGame():
        global oActive, ExitMenu
        oActive = True
        need = True
        while need:
            renpy.call_screen("game_page", _layer="master")
            need = oRes == False         # 클릭 후 oRes(전부 다 찾았는지?)가 False일 경우 need를 True인 상태로 진행
            if needTimer and (oTime <= .0):
                need = False

        ExitMenu = True


    # Show the game screen as an inactive background
    # Items already found will not be displayed
    # 시작을 여기서 하므로 윤사랑의 청소구역 페이지를 띄워줌
    def GameAsBG():
        global oActive
        oActive = False
        renpy.show_screen("game_page", _layer="master")


    # The click handler for the item
    def o_click(i):
        global oLen, oRes, oTrashSeet, oTrashPos, oN, oXY, oCombo, nowCount, CleaningPoint
        if i >= 0:
            if oN[i] and  oCombo[i] <= 1:
                temp = oN[i]
                oN[i] = ""
                oLen += 1
                nowCount -= 1
                renpy.play('audio/EffectSound/ui_mouse.mp3', channel="sound")
                renpy.restart_interaction()
                CleaningPoint += 1
                if needTimer:
                    if oLen >= maxLen:
                        oRes = True
                else:
                    oRes = temp
            else:
                # renpy.play('audio/EffectSound/ui_mouse.mp3', channel="sound")
                oCombo[i] -= 1;
        if nowCount <= 5:
            for i in range(0, 5):
                randSeet = renpy.random.randint(0, len(oTrashSeet) - 1)

                oN.append(oTrashSeet[randSeet])

                randin = renpy.random.randint(0, len(oArea_X_2) - 1)
                randX = renpy.random.randint(oArea_X_1[randin], oArea_X_2[randin])
                randY = renpy.random.randint(oArea_Y_1[randin], oArea_Y_2[randin])
                oXY.append((randX, randY))

                oCombo.append(renpy.random.randint(0, 2))
                nowCount += 1
            # 여기는 현재 count가 2 이하일 경우 랜덤한 위치에 생성인데...
    # 렌파이에서 action으로 호출이 가능하게 함.
    oClick = renpy.curry(o_click)
    def o_specal_click(i):
        # umm
        global oSN1, oSN2, oSCombo, oSXY, CleaningPoint, oLen
        if i >= 0:
            if oSN1[i] and oSCombo[i] == 1:
                # tmep = oSN1[i]
                oSN1[i] = oSN2[i]
                oLen += 1
                renpy.play('audio/EffectSound/ui_mouse.mp3', channel = 'sound')
                renpy.restart_interaction()
                CleaningPoint += 1
                oSCombo[i] -= 1
            else:
                renpy.play('audio/EffectSound/ui_mouse.mp3', channel="sound")
                oSCombo[i] -= 1

    oSClick = renpy.curry(o_specal_click)

# init 5 python:

# Actually the game screen, run from the function StartGame ()
screen game_page:
    modal True
    if oActive and needTimer:
        timer 0.01 repeat True action [SetVariable("oTime", oTime-.01), If(oTime <= .0, true=[Return()])]
    add oBg

    # text str(CleaningPoint):
    #     pos (0, 0)
    #     color '#ffffff'


    # image Yun_Special_3_on:
    #     pos(720, 490)
    #
    # image Yun_Special_3_on:
    #     pos(1000, 490)

    for i in range(0, len(oSN1)):
        if oSN1[i]: # special Node
            imagebutton:
                focus_mask True
                pos (oSXY[i])
                idle oSN1[i]
                hover oSN1[i]
                if oSCombo[i] > 0:
                    action [oSClick(i), Return()]
                else:
                    action []



    for i in range(0, len(oN)):
        if oN[i]:
            imagebutton:
                focus_mask True
                pos(oXY[i])
                idle oN[i]
                hover oN[i]
                if oActive:
                    action [oClick(i), Return()]
                else:
                    action []

    # image Yun_Special_2_on:
    #     pos(750, 600)
    #
    # image Yun_Special_2_on:
    #     pos(1060, 600)

    # image Yun_Special_1:
    #     pos(930, 425)


    # 스탠딩 출력하는 조건문
    if oActive:
        # if oActive and needTimer:
            # $ pos_x += 1
            # $ pos_y += 1
        add oCg[0]:
            pos (pos_x, pos_y)
            size (450, 540)
    else:
        if CleaningPoint < 7:          ## 밸런스 패치
            add oCg[1]:
                pos (pos_x, pos_y)
                size (450, 540)
        else:
            add oCg[2]:
                pos (pos_x, pos_y)
                size (450, 540)
    # add Clock_UI:

    if oActive and needTimer:
        add "images/minigame/공용 UI/Minigame_UI_TimeFrame.png":
            # pos (100, 100)
            align (.15, .1)

        bar value StaticValue(oTime, oMaxTime):
            # align(.25, .1)
            align (.186, 0.121)
            xmaximum  600
            ymaximum 45
            left_bar Frame("images/minigame/공용 UI/Minigame_UI_TimeFrame_bar.png", 50, 50)
            right_bar Frame("images/minigame/공용 UI/Minigame_UI_TimeFrame_bar_under.png", 50, 50)
            thumb None
            thumb_shadow None


    add "images/minigame/공용 UI/Minigame_UI_Frame.png"


# 튜토리얼 스크린
screen Cleaning_game_Tutorial:
    modal True
    add "gui/overlay/confirm.png"

    # imagebutton:
    #     idle "gui/overlay/confirm.png"
    #     hover "gui/overlay/confirm.png"
    #     hover_sound "audio/EffectSound/paper.wav"
    #     activate_sound "audio/EffectSound/paper2.wav"
    #     action Hide ("Cleaning_game_Tutorial")

    add "images/minigame/공용 UI/Minigame_UI_Startpage.png":
        pos (542, 271)


    # 나가기 버튼
    imagebutton:
        align (.5, .85)
        # xpos 920 ypos 850
        idle "gui/frame_ok_button.png"
        hover "gui/frame_ok_button_in.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action [Hide ("Cleaning_game_Tutorial"), Play("music", MiniGame)]

# 결과창 스크린
screen End_Window:
    modal True

    add "gui/nvl.png"

    text "끄읏~":
        xpos 885 ypos 100

    # 나가기 버튼
    imagebutton:
        xpos 1600 ypos 960
        idle "gui/button_main/back.png"
        hover "gui/button_main/back_in.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action [Hide ("End_Window"), Return()]
