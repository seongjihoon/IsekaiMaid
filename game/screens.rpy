﻿################################################################################
## 초기화
################################################################################

init offset = -1


################################################################################
## 스타일
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style outlineText:
    properties gui.text_properties()
    language gui.language
    # outlines [ (absolute(1), "#a9a094", absolute(0), absolute(0)) ]
    outlines [ (3, "#B8AEA1", 0, 0) ]
style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")
    # outlines [ (absolute(1), "#a9a094", absolute(65), absolute(65)) ]

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame_2.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 게임내 스크린
################################################################################


## Say 스크린 #####################################################################
##
## Say 스크린은 플레이어에게 대사를 출력할 때 씁니다. 화자 who와 대사 what, 두
## 개의 매개변수를 받습니다. (화자 이름이 없으면 who는 None일 수 있음)
##
## 이 스크린은 id "what"을 가진 텍스트 디스플레이어블을 생성해야 합니다. (이 디
## 스플레이어블은 렌파이의 대사 출력에 필요합니다.) id "who" 와 id "window" 디스
## 플레이블이 존재할 경우 관련 스타일 속성이 적용됩니다.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    add "gui/Gradation.png":
        alpha 0.84
    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## 사이드 이미지가 있는 경우 글자 위에 표시합니다. 휴대폰 환경에서는 보이지
    ## 않습니다.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Character 객체를 통해 스타일을 지정할 수 있도록 namebox를 사용할 수 있게 만듭
## 니다.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is outlineText
style say_thought is say_dialogue

style namebox is default
style namebox_label is default

style gradation:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/Gradation.png", xalign = 0.5, yalign = 1.0)


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign= 1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    yanchor gui.name_yalign
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    # xalign gui.name_xalign
    xalign 0.35
    yalign 0.35

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input 스크린 ###################################################################
##
## 플레이어 입력을 받는 renpy.input을 출력할 때 쓰이는 스크린입니다. prompt 매개
## 변수를 통해 입력 지문을 표시할 수 있습니다.
##
## 이 스크린은 id "input"을 가진 input 디스플레이어블을 생성해야 합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice 스크린 ##################################################################
##
## menu 명령어로 생성된 게임내 선택지를 출력하는 스크린입니다. 한 개의 매개변수
## items를 받고, 이는 선택지 내용(caption)과 선택지 결과(action)이 있는 오브젝트
## 가 들어있는 리스트입니다.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton (i.caption):
                align (0.5, .5)
                action i.action


## True일 경우 narrator 캐릭터를 통해 지문을 표시합니다. False일 경우 지문이 비
## 활성화 선택지로 표시됩니다.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text :
    ypos 45

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu 스크린 ##############################################################
##
## 퀵메뉴는 게임 외 메뉴 접근성을 높여주기 위해 게임 내에 표시됩니다.


screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.965
            style 'quick_button_text'

            textbutton _("대사록") action ShowMenu('history')
            textbutton _("넘기기") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("자동진행") action Preference("auto-forward", "toggle")
            textbutton _("저장") action ShowMenu('save')
            textbutton _("불러오기") action ShowMenu("load")
            textbutton _("설정") action ShowMenu('preferences')

            # key "mousedown_1" activate_sound 'audio/EffectSound/ui_mouse.mp3'

## 플레이어가 UI(스크린)을 일부러 숨기지 않는 한 퀵메뉴가 게임 내에 오버레이로
## 출력되게 합니다.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main과 Game Menu 스크린
################################################################################

## Navigation 스크린 ##############################################################
##
## 이 스크린은 메인메뉴와 게임외 메뉴에 포함되어 다른 메뉴로 이동하거나 게임을
## 시작/종료할 수 있게 합니다.

screen navigation(false_menu = False):

    vbox:
        style_prefix "navigation"
        if false_menu == False:
            xpos gui.navigation_xpos        # x축 간격
            yalign 0.647                     # y축 간격
        if false_menu == True:
            xpos gui.navigation_xpos_1
            yalign 0.55
        # ypos gui.navigation_ypos      # y축 간격

        spacing gui.navigation_spacing  # 상하 간격
        if main_menu:
            # textbutton _("시작하기") action Start()
            imagebutton:
                idle "gui/button_main/newgame.png"
                hover "gui/button_main/newgame_in.png"
                hover_sound "audio/EffectSound/paper.wav"
                activate_sound "audio/EffectSound/paper2.wav"
                action Start()
        else:

            # textbutton _("대사록") action ShowMenu("history")
            imagebutton:
                idle "gui/button_main/script.png"
                hover "gui/button_main/script_in.png"
                hover_sound "audio/EffectSound/paper.wav"
                activate_sound "audio/EffectSound/paper2.wav"
                action ShowMenu("history")

            # textbutton _("저장하기") action ShowMenu("save")
            imagebutton:
                idle "gui/button_main/save.png"
                hover "gui/button_main/save_in.png"
                hover_sound "audio/EffectSound/paper.wav"
                activate_sound "audio/EffectSound/paper2.wav"
                action ShowMenu("save")

        # textbutton _("불러오기") action ShowMenu("load")
        imagebutton:
            idle "gui/button_main/loadgame.png"
            hover "gui/button_main/loadgame_in.png"
            hover_sound "audio/EffectSound/paper.wav"
            activate_sound "audio/EffectSound/paper2.wav"
            action ShowMenu("load")
        # 갤러리 사진첩
        imagebutton:
            idle "gui/button_main/album.png"
            hover "gui/button_main/album_in.png"
            hover_sound "audio/EffectSound/paper.wav"
            activate_sound "audio/EffectSound/paper2.wav"
            action ShowMenu("Sarang_Gallery")                     ## 시작은 윤사랑의 페이지

        imagebutton:
            idle "gui/button_main/collection.png"
            hover "gui/button_main/collection_in.png"
            hover_sound "audio/EffectSound/paper.wav"
            activate_sound "audio/EffectSound/paper2.wav"
            action ShowMenu("Item_Gallery1")

        # textbutton _("환경설정") action ShowMenu("preferences")
        imagebutton:
            idle "gui/button_main/setting.png"
            hover "gui/button_main/setting_in.png"
            hover_sound "audio/EffectSound/paper.wav"
            activate_sound "audio/EffectSound/paper2.wav"
            action ShowMenu("preferences")

        if _in_replay:

            textbutton _("리플레이 끝내기") action EndReplay(confirm=True)

        elif not main_menu:

            # textbutton _("메인 메뉴") hover_sound "audio/EffectSound/paper.wav" activate_sound "audio/EffectSound/paper2.wav" action MainMenu()
            imagebutton:
                idle "gui/button_main/mainmenu.png"
                hover "gui/button_main/mainmenu_in.png"
                hover_sound "audio/EffectSound/paper.wav"
                activate_sound "audio/EffectSound/paper2.wav"
                action MainMenu()

        # textbutton _("버전정보") action ShowMenu("about")


        # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## 도움말 메뉴는 모바일 디바이스와 맞지 않아 불필요합니다.
            # textbutton _("조작방법") action ShowMenu("help")
            # imagebutton:
            #     idle "gui/button_main/Help.png"
            #     hover "gui/button_main/Help_in.png"
            #     hover_sound "audio/EffectSound/paper.wav"
            #     activate_sound "audio/EffectSound/paper2.wav"
            #     action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            # textbutton _("종료하기") action Quit(confirm=not main_menu)
            imagebutton:
                idle "gui/button_main/end.png"
                hover "gui/button_main/end_in.png"
                hover_sound "audio/EffectSound/paper.wav"
                activate_sound "audio/EffectSound/paper2.wav"
                action Quit(confirm = not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu 스크린 ###############################################################
##
## 렌파이가 시작할 때 메인메뉴를 출력합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    # add gui.main_menu_background_png

    ## This empty frame darkens the main menu

    add TrackCursor("gui/main_menu.png", 100)

    frame:
        style "main_menu_frame"

    add TrackCursor("gui/main_menu_Butterfly.png", 10)
    imagebutton:
        idle "gui/button/main_menu_Button_Homepage.png"
        hover "gui/button/main_menu_Button_Homepage.png"
        align (.04, .945)
        # rotate
        action OpenURL("https://twitter.com/ctb_maid")
    ## use 명령어로 스크린 내에 다른 스크린을 불러옵니다. 메인 메뉴 스크린의 내
    ## 용물은 navigation 스크린에 있습니다.

    use navigation

# screen main_menu2():
#     tag menu
#     add gui.main_menu_background_png
#
#     frame:
#         style "main_menu_frame"
#
#     ## use 명령어로 스크린 내에 다른 스크린을 불러옵니다. 메인 메뉴 스크린의 내
#     ## 용물은 navigation 스크린에 있습니다.
#
#     use navigation



style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu 스크린 ###############################################################
##
## 게임 메뉴의 기본 틀입니다. 매개변수 title로 스크린 제목을 정하고, 배경, 제목,
## 그리고 navigation 스크린을 출력합니다.
##
## scroll 매개변수는, None, "viewport" 혹은 "vpgrid" 중 하나여야 합니다.
## transclude 명령어를 통해 다른 스크린을 이 스크린 내부에 불러옵니다.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background_png
    else:
        add gui.game_menu_background

    frame:
        if title == "과거시":
            style "game_menu_outer_frame_history"
        else:
            style "game_menu_outer_frame"


        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True


                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation(True)

    # textbutton _("돌아가기"):
    #     style "return_button"
    #
    #     action Return()

    imagebutton:
        # style "return_button"
        xalign .05
        yalign 0.9
        idle "gui/button_main/back_1.png"
        hover "gui/button_main/back_1_in.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action Return()

    image "gui/title_log.png":
        xalign 0.03
        yalign 0.035


    text "[title]":
        xalign 0.618
        yalign 0.231
        size 65
        font "경기천년바탕_Bold.ttf" color "#50271e"
        # outlines [ (3, "#eddcbe", 0, 0) ]

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_outer_frame_history is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 180
    top_padding 190

    background "gui/overlay/game_menu.png"

style game_menu_outer_frame_history:
    bottom_padding 180
    top_padding 280

    background "gui/overlay/game_menu.png"


style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.label_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About 스크린 ###################################################################
##
## 이 스크린은 게임과 렌파이 엔진 크레딧과 저작권 정보를 표시합니다.
##
## 특별할 것이 없으므로 스크린을 새로 커스터마이징하여 만드는 예제이기도 합니다.

screen about():

    tag menu

    ## 이 use 명령어로 game_menu 스크린을 이 스크린 내에 불러옵니다. use 명령어
    ## 하위블럭(vbox 내용)은 game_menu 스크린 내 transclude 명령어가 있는 곳에
    ## 다시 불려집니다.
    use game_menu(_("버전정보"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("버전 [config.version!t]\n")

            ## gui.about 의 내용은 보통 options.rpy에 있습니다.
            if gui.about:
                text "[gui.about!t]\n"

            text _("{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 으로 만들어진 게임.\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load 그리고 Save 스크린 ###########################################################
##
## 이 스크린은 세이브/로드에 쓰입니다. 거의 동일하기 때문에, file_slots 스크린을
## 불러와서 씁니다.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("기록하기"))


screen load():

    tag menu

    use file_slots(_("불러오기"))


screen file_slots(title):

    # default page_name_value = FilePageNameInputValue(pattern=_("{} 페이지"), auto=_("자동 세이브"), quick=_("퀵세이브"))

    use game_menu(title):

        fixed:

            ## input이 세이브/로드 버튼보다 먼저 엔터에 반응하도록 합니다.
            order_reverse True

            # ## 페이지 제목을 플레이어가 수정할 수 있음.
            # button:
            #     style "page_label"
            #
            #     key_events True
            #     xalign 0.5
            #     action page_name_value.Toggle()
            #
            #     input:
            #         style "page_label_text"
            #         value page_name_value

            ## 파일 슬롯 그리드.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.25
                yalign 2.0

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("\n{#file_time}%A, %B %d %Y, %H:%M"), empty=_("\n빈 슬롯")):
                            style "slot_time_text"


                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            # 페이지 이동 버튼.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.2

                spacing gui.page_spacing

                # textbutton _("<") action FilePagePrevious()

                # if config.has_autosave:
                #     textbutton _("{#auto_page}자동") action FilePage("auto")
                #
                # if config.has_quicksave:
                #     textbutton _("{#quick_page}퀵") action FilePage("quick")

                ## 범위(1, 10)는 1부터 9까지 숫자를 제공합니다.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                # textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences 스크린 #############################################################
##
## Preferences 스크린에서는 각종 환경설정을 플레이어가 지정할 수 있습니다.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("환경설정"), scroll="viewport"):

        vbox:
            hbox:
                pos 200, 100
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("화면 모드")
                        textbutton _("창 화면") action Preference("display", "window")
                        textbutton _("전체 화면") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("측면 되감기")
                    yalign 2.0
                    textbutton _("비활성화") action Preference("rollback side", "disable")
                    textbutton _("화면 왼쪽 클릭") action Preference("rollback side", "left")
                    textbutton _("화면 오른쪽 클릭") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("넘기기")
                    textbutton _("읽지 않은 지문") action Preference("skip", "toggle")
                    textbutton _("선택지 이후") action Preference("after choices", "toggle")
                    textbutton _("화면 전환 효과") action InvertSelected(Preference("transitions", "toggle"))
                    yalign 2.0

                ## "radio_pref" 나 "check_pref" 를 추가하여 그 외에도 환경설정
                ## 항목을 추가할 수 있습니다.

            null height (4 * gui.pref_spacing)

            hbox:
                pos 50, 50
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("텍스트 속도")

                    bar value Preference("text speed")

                    label _("자동 진행 시간")

                    bar value Preference("auto-forward time")

                    # label _("사랑이 보이스")
                    #
                    # bar value SetCharacterVolume("v_yun")
                    #
                    # label _("스칼렛 보이스 ")
                    #
                    # bar value SetCharacterVolume("v_scalret")

                vbox:

                    if config.has_music:
                        label _("배경음 음량")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("효과음 음량")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("테스트") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("음성 음량")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("테스트") action Play("voice", config.sample_voice)


                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("모두 음소거"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History 스크린 #################################################################
##
## 지난 대사록을 출력합니다. _history_list 에 저장된 대사 기록을 확인합니다.
##
## https://www.renpy.org/doc/html/history.html

define a = 0

screen history():

    tag menu

    ## 이 스크린은 내용이 아주 많을 수 있으므로 prediction을 끕니다.
    predict False

    use game_menu(_("과거시"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"
        $ name = " "

        for h in _history_list:

            window:
                ## history_height 이 None일 경우 레이아웃이 틀어지지 않게 합니
                ## 다.
                has fixed:
                    yfit True

                if h.who != name and h.who:
                    add "gui/NameTag.png":
                        size (200, 45)
                    label h.who:
                        style "history_name"

                        substitute False

                        ## 화자 Character에 화자 색깔이 지정되어 있으면 불러옵니
                        ## 다.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute True
                    color "#341717"
                $ name = h.who

        if not _history_list:
            label _("대사가 없습니다.")


screen Ending_Credit():
    pass

## 이것은 대사록 화면에 표시할 수 있는 태그를 결정합니다.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help 스크린 ####################################################################
##
## 입력장치의 기능을 설명합니다. 각 입력장치별 설정은 keyboard_help, mouse_help,
## gamepad_help 스크린을 각각 불러와서 출력합니다.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("조작방법"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("키보드") action SetScreenVariable("device", "keyboard")
                textbutton _("마우스") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("게임패드") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("엔터(Enter)")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("스페이스(Space)")
        text _("대사를 진행하되 선택지는 선택하지 않음.")

    hbox:
        label _("화살표 키")
        text _("UI 이동.")

    hbox:
        label _("이스케이프(Esc)")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("컨트롤(Ctrl)")
        text _("누르고 있는 동안 대사를 스킵.")

    hbox:
        label _("탭(Tab)")
        text _("대사 스킵 토글.")

    hbox:
        label _("페이지 업(Page Up)")
        text _("이전 대사로 롤백.")

    hbox:
        label _("페이지 다운(Page Down)")
        text _("이후 대사로 롤포워드.")

    hbox:
        label "H"
        text _("UI를 숨김.")

    hbox:
        label "S"
        text _("스크린샷 저장.")

    hbox:
        label "V"
        text _("{a=https://www.renpy.org/l/voicing}대사 읽어주기 기능{/a} 토글.")


screen mouse_help():

    hbox:
        label _("클릭")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("가운데 버튼이나 휠버튼 클릭")
        text _("UI를 숨김.")

    hbox:
        label _("우클릭")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("휠 위로\n롤백 클릭")
        text _("이전 대사로 롤백.")

    hbox:
        label _("휠 아래로")
        text _("이후 대사로 롤포워드.")


screen gamepad_help():

    hbox:
        label _("오른쪽 트리거(RT)\nA버튼/아래 버튼")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("이전 대사로 롤백.")

    hbox:
        label _("오른쪽 범퍼(RB)")
        text _("이후 대사로 롤포워드.")


    hbox:
        label _("D-Pad, 아날로그 스틱")
        text _("UI 이동.")

    hbox:
        label _("스타트 버튼/가이드 버튼")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("Y버튼/위 버튼")
        text _("UI를 숨김.")

    textbutton _("조정") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## 그 외 스크린
################################################################################

## Gallery 스크린 ##############################################################
##
## 인 게임에서의 일러스트를 수집하고 수집한 일러스트를 볼 수 있는 스크린을 표시

screen Sarang_Gallery():
    tag menu

    add "gui/overlay/Gallery_menu.png"

    imagebutton:
        idle "gui/button_main/Setting_Arrow_R.png"
        hover "gui/button_main/Setting_Arrow_on_R.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action ShowMenu("Elice_Gallery")
        align (.97, .55)

    grid 3 2:
        xfill True
        yfill True
        add g.make_button("cg1", "images/Gallery/Sarang/Yun_CG_001_small.png", xalign = 1.2, yalign = 1.2)
        add g.make_button("cg2", "images/Gallery/Sarang/Yun_CG_003_small.png", xalign = 0.5, yalign = 1.2)
        add g.make_button("cg3", "images/Gallery/gal-locked.png", xalign = -0.2, yalign = 1.2)
        add g.make_button("cg4", "images/Gallery/gal-locked.png", xalign = 1.2, yalign = 0.3)
        add g.make_button("cg5", "images/Gallery/gal-locked.png", xalign = 0.5, yalign = 0.3)
        add g.make_button("cg6", "images/Gallery/gal-locked.png", xalign = -0.2, yalign = 0.3)

    add "gui/Setting_word_ui.png":
        align (.5, .88)
    imagebutton:
        # style "return_button"
        xalign .05
        yalign 0.9
        idle "gui/button_main/back_1.png"
        hover "gui/button_main/back_1_in.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action Return()
    # imagebutton:
    #     idle "gui/button_main/back.png"
    #     hover "gui/button_main/back_in.png"
    #     hover_sound "audio/EffectSound/paper.wav"
    #     activate_sound "audio/EffectSound/paper2.wav"
    #     action Return()

screen Elice_Gallery():
    tag menu

    add "gui/overlay/Gallery_menu.png"

    imagebutton:
        idle "gui/button_main/Setting_Arrow_L.png"
        hover "gui/button_main/Setting_Arrow_on_L.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action ShowMenu("Sarang_Gallery")
        align (.03, .55)

    imagebutton:
        idle "gui/button_main/Setting_Arrow_R.png"
        hover "gui/button_main/Setting_Arrow_on_R.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action ShowMenu("Isabel_Gallery")
        align (.97, .55)

    grid 3 2:
        xfill True
        yfill True
        add g.make_button("cg7", "images/Gallery/Elice/Elice_CG_001_small.png", xalign = 1.2, yalign = 1.2)
        add g.make_button("cg8", "images/Gallery/Elice/Elice_CG_009_small.png", xalign = 0.5, yalign = 1.2)
        add g.make_button("cg9", "images/Gallery/Elice/Elice_CG_002_small.png", xalign = -0.2, yalign = 1.2)
        add g.make_button("cg10", "images/Gallery/Elice/Elice_CG_005_small.png", xalign = 1.2, yalign = 0.3)
        add g.make_button("cg11", "images/Gallery/Elice/Elice_CG_001_small.png", xalign = 0.5, yalign = 0.3)
        add g.make_button("cg12", "images/Gallery/Elice/Elice_CG_001_small.png", xalign = -0.2, yalign = 0.3)

    add "gui/Setting_word_ui.png":
        align (.5, .88)



    imagebutton:
        # style "return_button"
        xalign .05
        yalign 0.9
        idle "gui/button_main/back_1.png"
        hover "gui/button_main/back_1_in.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action Return()

screen Isabel_Gallery():
    tag menu

    add "GUI/overlay/Gallery_menu.png"

    imagebutton:
        idle "gui/button_main/Setting_Arrow_L.png"
        hover "gui/button_main/Setting_Arrow_on_L.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action ShowMenu("Elice_Gallery")
        align (.03, .55)

    imagebutton:
        idle "gui/button_main/Setting_Arrow_R.png"
        hover "gui/button_main/Setting_Arrow_on_R.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action ShowMenu("Scarlet_Gallery")
        align (.97, .55)
    # cg 13 ~ 18
    grid 3 2:
        xfill True
        yfill True
        add g.make_button("cg13", "images/Gallery/Isabel/Isabel_CG_001_small.png", xalign = 1.2, yalign = 1.2)
        add g.make_button("cg100", "images/Gallery/gal-locked.png", xalign = 0.5, yalign = 1.2)
        add g.make_button("cg100", "images/Gallery/gal-locked.png", xalign = -0.2, yalign = 1.2)
        add g.make_button("cg100", "images/Gallery/gal-locked.png", xalign = 1.2, yalign = 0.3)
        add g.make_button("cg100", "images/Gallery/gal-locked.png", xalign = 0.5, yalign = 0.3)
        add g.make_button("cg100", "images/Gallery/gal-locked.png", xalign = -0.2, yalign = 0.3)

    add "gui/Setting_word_ui.png":
        align (.5, .88)



    imagebutton:
        # style "return_button"
        xalign .05
        yalign 0.9
        idle "gui/button_main/back_1.png"
        hover "gui/button_main/back_1_in.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action Return()

screen Scarlet_Gallery():
    tag menu

    add "gui/overlay/Gallery_menu.png"
    imagebutton:
        idle "gui/button_main/Setting_Arrow_L.png"
        hover "gui/button_main/Setting_Arrow_on_L.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action ShowMenu("Isabel_Gallery")
        align (.03, .55)

    # imagebutton:
    #     idle "gui/button_main/Setting_Arrow_R.png"
    #     hover "gui/button_main/Setting_Arrow_on_R.png"
    #     hover_sound "audio/EffectSound/paper.wav"
    #     activate_sound "audio/EffectSound/paper2.wav"
    #     action ShowMenu("Scarlet_Gallery")
    #     align (.97, .55)    # cg 19 ~ 24
    grid 3 2:
        xfill True
        yfill True
        add g.make_button("cg19", "images/Gallery/Scarlet/Scarlet_CG_001_small.png", xalign = 1.2, yalign = 1.2)
        add g.make_button("cg20", "images/Gallery/Scarlet/Scarlet_CG_002_small.png", xalign = 0.5, yalign = 1.2)
        add g.make_button("cg21", "images/Gallery/gal-locked.png", xalign = -0.2, yalign = 1.2)
        add g.make_button("cg22", "images/Gallery/gal-locked.png", xalign = 1.2, yalign = 0.3)
        add g.make_button("cg23", "images/Gallery/gal-locked.png", xalign = 0.5, yalign = 0.3)
        add g.make_button("cg24", "images/Gallery/gal-locked.png", xalign = -0.2, yalign = 0.3)

    add "gui/Setting_word_ui.png":
        align (.5, .88)

    imagebutton:
        # style "return_button"
        xalign .05
        yalign 0.9
        idle "gui/button_main/back_1.png"
        hover "gui/button_main/back_1_in.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action Return()
#
# screen Admin_Gallery():
#     tag menu
#
#     add "gui/overlay/Gallery_menu.png"
#
#     imagebutton:                                    # 사랑
#         idle "gui/button/game_menu_button_salang.png"
#         hover "gui/button/game_menu_idle_button_salang.png"
#         hover_sound "audio/EffectSound/paper.wav"
#         activate_sound "audio/EffectSound/paper2.wav"
#         pos (240, 60)
#         action ShowMenu("Sarang_Gallery")
#     imagebutton:                                    # 앨리스
#         idle "gui/button/game_menu_button_alice.png"
#         hover "gui/button/game_menu_idle_button_alice.png"
#         hover_sound "audio/EffectSound/paper.wav"
#         activate_sound "audio/EffectSound/paper2.wav"
#         action ShowMenu("Elice_Gallery")
#         pos (400, 60)
#     imagebutton:                                    # 이자벨
#         idle "gui/button/game_menu_button_Isabelle.png"
#         hover "gui/button/game_menu_idle_button_Isabelle.png"
#         hover_sound "audio/EffectSound/paper.wav"
#         activate_sound "audio/EffectSound/paper2.wav"
#         action ShowMenu("Isabelle_Gallery")
#         pos (540, 60)
#     imagebutton:                                    # 스칼렛
#         idle "gui/button/game_menu_button_scarlet.png"
#         hover "gui/button/game_menu_idle_button_scarlet.png"
#         hover_sound "audio/EffectSound/paper.wav"
#         activate_sound "audio/EffectSound/paper2.wav"
#         action ShowMenu("Scalet_Gallery")
#         pos (680, 60)
#     # imagebutton:                                    # 관리자
#     #     idle "gui/button/game_menu_idle_button_manager.png"
#     #     hover "gui/button/game_menu_idle_button_manager.png"
#     #     hover_sound "audio/EffectSound/paper.wav"
#     #     activate_sound "audio/EffectSound/paper2.wav"
#     #     action ShowMenu("Admin_Gallery")
#     #     pos (820, 60)
#
#     grid 3 2:
#         xfill True
#         yfill True
#         add g.make_button("cg100", "images/Gallery/1.png", xalign = 1.2, yalign = 1.2)
#         add g.make_button("cg100", "images/Gallery/2.png", xalign = 0.5, yalign = 1.2)
#         add g.make_button("cg100", "images/Gallery/3.png", xalign = -0.2, yalign = 1.2)
#         add g.make_button("cg100", "images/Gallery/4.png", xalign = 1.2, yalign = 0.3)
#         add g.make_button("cg100", "images/Gallery/5.png", xalign = 0.5, yalign = 0.3)
#         add g.make_button("cg100", "images/Gallery/6.png", xalign = -0.2, yalign = 0.3)
#
#
#     imagebutton:
#         xpos 1600 ypos 960
#         idle "gui/button_main/back.png"
#         hover "gui/button_main/back_in.png"
#         hover_sound "audio/EffectSound/paper.wav"
#         activate_sound "audio/EffectSound/paper2.wav"
#         action Return()


screen Item_Gallery3():
    tag menu
    add "gui/overlay/game_menu.png"
    use game_menu(_("컬렉션")):
        grid 3 2:
            xfill True
            yfill True
            if(persistent.m_bgetFlowerpot == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign 0.8 yalign 2.0
            else:
                imagebutton:
                    idle "gui/button/item.png"
                    xalign 0.8 yalign 2.0
                    action [Function(renpy.show_screen, "ShowItemInfo", 13)]

            if(persistent.m_unknown == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign 0.2 yalign 2.7
            else:
                imagebutton:
                    idle "gui/button/item.png"
                    xalign 0.2 yalign 2.7
                    action [Function(renpy.show_screen, "ShowItemInfo", 14)]

            if(persistent.m_unknown == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign -0.3 yalign 2.0
            else :
                imagebutton:
                    idle "gui/button/item.png"
                    xalign -0.3 yalign 2.0
                    action [Function(renpy.show_screen, "ShowItemInfo", 15)]

            if(persistent.m_unknown == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign 0.8 yalign 1.0
            else :
                imagebutton :
                    idle "gui/button/item.png"
                    xalign 0.8 yalign 1.0
                    action [Function(renpy.show_screen, "ShowItemInfo", 16)]

            if(persistent.m_unknown == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign 0.2 yalign 1.7
            else:
                imagebutton:
                    idle "gui/button/item.png"
                    xalign 0.2 yalign 1.7
                    action [Function(renpy.show_screen, "ShowItemInfo", 17)]

            if(persistent.m_unknown == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign -0.3 yalign 1.0
            else:
                imagebutton:
                    idle "gui/button/item.png"
                    xalign -0.3 yalign 1.0
                    action [Function(renpy.show_screen, "ShowItemInfo", 18)]
        grid 3 2:
            xfill True
            yfill True

            if(persistent.m_bgetFlowerpot == True):
                add "images/item/문어화분_small.png":
                    xalign 0.7 yalign 1.5
                    xzoom .9
                    yzoom .9
            else:
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign 0.8 yalign 2.0

            if(persistent.m_unknown == True):
                add "images/item/사랑이의반지_small.png":
                    xalign 0.35 yalign 1.6
                    xzoom .8
                    yzoom .8
            else:
                add "gui/button/item_in.png":
                    xalign 0.2 yalign 2.7

            if(persistent.m_unknown == True):
                add "images/item/엘리스펜던트_small.png":
                    xalign -0.05 yalign 1.4
            else:
                add "gui/button/item_in.png":
                    xalign -0.3 yalign 2.0

            if(persistent.m_unknown == True):
                add "images/item/이자벨반지_small.png":
                    xalign 0.65 yalign 0.9
                    xzoom .9
                    yzoom .9
            else:
                add "gui/button/item_in.png":
                    xalign 0.8 yalign 1.0

            if(persistent.m_unknown == True):
                add "images/item/만년필_small.png":
                    xalign 0.3 yalign 1.5
                    xzoom .9
                    yzoom .9
            else:
                add "gui/button/item_in.png":
                    xalign 0.2 yalign 1.7

            if(persistent.m_unknown == True):
                add "images/item/드림캐쳐팔찌_small.png":
                    xalign 0.0 yalign 1.0
                    xzoom .9
                    yzoom .9
            else:
                add "gui/button/item_in.png":
                    xalign -0.3 yalign 1.0

    imagebutton:
        xalign 0.05
        yalign 0.9
        idle "gui/button_main/back_1.png"
        hover "gui/button_main/back_1_in.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action Return()

    imagebutton:
        idle "gui/button_main/Setting_Arrow_L.png"
        hover "gui/button_main/Setting_Arrow_on_L.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action ShowMenu("Item_Gallery2")
        align (.25, .55)

    # imagebutton:
    #     idle "gui/button_main/Setting_Arrow_R.png"
    #     hover "gui/button_main/Setting_Arrow_on_R.png"
    #     hover_sound "audio/EffectSound/paper.wav"
    #     activate_sound "audio/EffectSound/paper2.wav"
    #     action ShowMenu("Scarlet_Gallery")
    #     align (.97, .55)


screen Item_Gallery2():
    tag menu
    add "gui/overlay/game_menu.png"
    use game_menu(_("컬렉션")):
        grid 3 2:
            xfill True
            yfill True
            if(persistent.m_bgetBear == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign 0.8 yalign 2.0
            else:
                imagebutton:
                    idle "gui/button/item.png"
                    xalign 0.8 yalign 2.0
                    action [Function(renpy.show_screen, "ShowItemInfo", 7)]

            if(persistent.m_bgetSarangRing == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign 0.2 yalign 2.7
            else:
                imagebutton:
                    idle "gui/button/item.png"
                    xalign 0.2 yalign 2.7
                    action [Function(renpy.show_screen, "ShowItemInfo", 8)]

            if(persistent.m_bgetpendant == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign -0.3 yalign 2.0
            else :
                imagebutton:
                    idle "gui/button/item.png"
                    xalign -0.3 yalign 2.0
                    action [Function(renpy.show_screen, "ShowItemInfo", 9)]

            if(persistent.m_bgetIsabelRing == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign 0.8 yalign 1.0
            else :
                imagebutton :
                    idle "gui/button/item.png"
                    xalign 0.8 yalign 1.0
                    action [Function(renpy.show_screen, "ShowItemInfo", 10)]

            if(persistent.m_bgetpen == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign 0.2 yalign 1.7
            else:
                imagebutton:
                    idle "gui/button/item.png"
                    xalign 0.2 yalign 1.7
                    action [Function(renpy.show_screen, "ShowItemInfo", 11)]

            if(persistent.m_bgetDreamcatcher == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign -0.3 yalign 1.0
            else:
                imagebutton:
                    idle "gui/button/item.png"
                    xalign -0.3 yalign 1.0
                    action [Function(renpy.show_screen, "ShowItemInfo", 12)]
        grid 3 2:
            xfill True
            yfill True

            if(persistent.m_bgetBear == True):
                add "images/item/곰인형_small.png":
                    xalign 0.7 yalign 1.5
                    xzoom .9
                    yzoom .9
            else:
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign 0.8 yalign 2.0

            if(persistent.m_bgetSarangRing == True):
                add "images/item/사랑이의반지_small.png":
                    xalign 0.35 yalign 1.6
                    xzoom .8
                    yzoom .8
            else:
                add "gui/button/item_in.png":
                    xalign 0.2 yalign 2.7

            if(persistent.m_bgetpendant == True):
                add "images/item/엘리스펜던트_small.png":
                    xalign -0.05 yalign 1.4
            else:
                add "gui/button/item_in.png":
                    xalign -0.3 yalign 2.0

            if(persistent.m_bgetIsabelRing == True):
                add "images/item/이자벨반지_small.png":
                    xalign 0.65 yalign 0.9
                    xzoom .9
                    yzoom .9
            else:
                add "gui/button/item_in.png":
                    xalign 0.8 yalign 1.0

            if(persistent.m_bgetpen == True):
                add "images/item/만년필_small.png":
                    xalign 0.3 yalign 1.5
                    xzoom .9
                    yzoom .9
            else:
                add "gui/button/item_in.png":
                    xalign 0.2 yalign 1.7

            if(persistent.m_bgetDreamcatcher == True):
                add "images/item/드림캐쳐팔찌_small.png":
                    xalign 0.0 yalign 1.0
                    xzoom .9
                    yzoom .9
            else:
                add "gui/button/item_in.png":
                    xalign -0.3 yalign 1.0

    imagebutton:
        xalign 0.05
        yalign 0.9
        idle "gui/button_main/back_1.png"
        hover "gui/button_main/back_1_in.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action Return()

    imagebutton:
        idle "gui/button_main/Setting_Arrow_L.png"
        hover "gui/button_main/Setting_Arrow_on_L.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action ShowMenu("Item_Gallery1")
        align (.25, .55)

    imagebutton:
        idle "gui/button_main/Setting_Arrow_R.png"
        hover "gui/button_main/Setting_Arrow_on_R.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action ShowMenu("Item_Gallery3")
        align (.97, .55)

screen Item_Gallery1():
    tag menu
    add "gui/overlay/game_menu.png"
    use game_menu(_("컬렉션")):
        grid 3 2:
            xfill True
            yfill True
            if(persistent.m_bgetFlower == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign 0.8 yalign 2.0
            else:
                imagebutton:
                    idle "gui/button/item.png"
                    xalign 0.8 yalign 2.0
                    action [Function(renpy.show_screen, "ShowItemInfo", 1)]

            if(persistent.m_bgetAlcohol == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign 0.2 yalign 2.7
            else:
                imagebutton:
                    idle "gui/button/item.png"
                    xalign 0.2 yalign 2.7
                    action [Function(renpy.show_screen, "ShowItemInfo", 2)]

            if(persistent.m_bgetWine == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign -0.3 yalign 2.0
            else :
                imagebutton:
                    idle "gui/button/item.png"
                    xalign -0.3 yalign 2.0
                    action [Function(renpy.show_screen, "ShowItemInfo", 3)]

            if(persistent.m_bgetPaper == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign 0.8 yalign 1.0
            else :
                imagebutton :
                    idle "gui/button/item.png"
                    xalign 0.8 yalign 1.0
                    action [Function(renpy.show_screen, "ShowItemInfo", 4)]

            if(persistent.m_bgetRibbon == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign 0.2 yalign 1.7

            else:
                imagebutton:
                    idle "gui/button/item.png"
                    xalign 0.2 yalign 1.7
                    action [Function(renpy.show_screen, "ShowItemInfo", 5)]

            if (persistent.m_bgethairpin == False):
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign -0.3 yalign 1.0
            else:
                imagebutton:
                    idle "gui/button/item.png"
                    xalign -0.3 yalign 1.0
                    action [Function(renpy.show_screen, "ShowItemInfo", 6)]

        grid 3 2:
            xfill True
            yfill True

            if(persistent.m_bgetFlower == True):
                add "images/item/물든꽃_small.png":
                    xalign 0.6 yalign 1.1
            else:
                imagebutton:
                    idle "gui/button/item_in.png"
                    xalign 0.8 yalign 2.0

            if(persistent.m_bgetAlcohol == True):
                add "images/item/술_small.png":
                    xalign 0.35 yalign 1.7
            else:
                add "gui/button/item_in.png":
                    xalign 0.2 yalign 2.7

            if(persistent.m_bgetWine == True):
                add "images/item/와인잔_small.png":
                    xalign 0.2 yalign 1.1
            else:
                add "gui/button/item_in.png":
                    xalign -0.3 yalign 2.0

            if(persistent.m_bgetPaper == True):
                add "images/item/찢어진종이_small.png":
                    xalign 0.65 yalign 0.6
            else:
                add "gui/button/item_in.png":
                    xalign 0.8 yalign 1.0

            if(persistent.m_bgetRibbon == True):
                add "images/item/리본_small.png":
                    xalign 0.3 yalign 0.8
            else:
                add "gui/button/item_in.png":
                    xalign 0.2 yalign 1.7


            if(persistent.m_bgethairpin == True):
                add "images/item/머리핀_small.png":
                    xalign -0.1 yalign 0.8
            else:
                add "gui/button/item_in.png":
                    xalign -0.3 yalign 1.0

    imagebutton:
        xalign 0.05
        yalign 0.9
        idle "gui/button_main/back_1.png"
        hover "gui/button_main/back_1_in.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action Return()


    imagebutton:
        idle "gui/button_main/Setting_Arrow_R.png"
        hover "gui/button_main/Setting_Arrow_on_R.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action ShowMenu("Item_Gallery2")
        align (.97, .55)

screen ShowItemInfo(_itemNum):
    modal True
    $ m_iFlaver_Text_ypos = 425 ## 탐색이 끝나면 초기화 해서 원래 위치로 이동

    add "gui/overlay/black_skin.png"
    add "gui/overlay/Flavor_page.png"

    $ dummyPosY = m_iFlaver_Text_ypos


    if _itemNum == 1:
        image "images/item/물든꽃.png":
            size 500, 500
            pos 350, 320
        transform:
            rotate -8
            xalign 0.7
            yalign 0.16
            text "젖은 장미가지":
                color u"#000000"
                size 60
                font "경기천년바탕_Regular.ttf"
        text m_strFlowerText[0]:
            size 37
            font "경기천년바탕_Regular.ttf"
            pos m_iFlavor_Text_xpos, dummyPosY
        $dummyPosY += 37
        text m_strFlowerText[1]:
            size 37
            font "경기천년바탕_Regular.ttf"
            pos m_iFlavor_Text_xpos, dummyPosY
        $dummyPosY += 37
        text m_strFlowerText[2]:
            size 37
            font "경기천년바탕_Regular.ttf"
            pos m_iFlavor_Text_xpos, dummyPosY
        $dummyPosY += 37

    elif _itemNum == 2:
        image "images/item/술.png":
            size 450, 800
            pos 350, 130
        transform:
            rotate -8
            xalign 0.61
            yalign 0.255
            text "와인":
                color u"#000000"
                size 60
                font "경기천년바탕_Regular.ttf"
        for txt in m_strAlcoholText:
            text txt:
                size 37
                font "경기천년바탕_Regular.ttf"
                pos m_iFlavor_Text_xpos, dummyPosY
            $ dummyPosY += 37

    elif _itemNum == 3:
        image "images/item/와인잔.png":
            size 400, 537
            pos 400, 320
        transform:
            rotate -8
            xalign 0.63
            yalign 0.24
            text "와인잔":
                color u"#000000"
                size 60
                font "경기천년바탕_Regular.ttf"
        for txt in m_strWineText:
            text txt:
                size 37
                font "경기천년바탕_Regular.ttf"
                pos m_iFlavor_Text_xpos, dummyPosY
            $ dummyPosY += 37

    elif _itemNum == 4:
        image "images/item/찢어진종이.png":
            size 870, 580
            pos 80, 50
            rotate -5
        transform:
            rotate -8
            xalign 0.67
            yalign 0.195
            text "찢어진종이":
                color u"#000000"
                size 60
                font "경기천년바탕_Regular.ttf"
        for txt in m_strPaperText:
            text txt:
                size 37
                font "경기천년바탕_Regular.ttf"
                pos m_iFlavor_Text_xpos, dummyPosY
            $ dummyPosY += 37

    elif _itemNum == 5:
        image "images/item/리본.png":
            size 697, 354
            pos 220, 400
        transform:
            rotate -8
            xalign 0.65
            yalign 0.215
            text "붉은 리본":
                color u"#000000"
                size 60
                font "경기천년바탕_Regular.ttf"
        for txt in m_strRibbonText:
            text txt:
                size 37
                font "경기천년바탕_Regular.ttf"
                pos m_iFlavor_Text_xpos, dummyPosY
            $ dummyPosY += 37
    elif _itemNum == 6:

        image "images/item/머리핀.png":
            size 750, 750
            pos 220, 200
        transform:
            rotate -8
            xalign 0.65
            yalign 0.225
            text "머리핀":
                color u"#000000"
                size 60
                font "경기천년바탕_Regular.ttf"
        for txt in m_strHairpin:
            text txt:
                size 37
                font "경기천년바탕_Regular.ttf"
                pos m_iFlavor_Text_xpos, dummyPosY
            $ dummyPosY += 37

    elif _itemNum == 7:
        image "images/item/곰인형.png":
            size 750, 750
            pos 220, 200
        transform:
            rotate -8
            xalign 0.65
            yalign 0.225
            text "곰인형":
                color u"#000000"
                size 60
                font "경기천년바탕_Regular.ttf"
        for txt in m_strBearText:
            text txt:
                size 37
                font "경기천년바탕_Regular.ttf"
                pos m_iFlavor_Text_xpos, dummyPosY
            $ dummyPosY += 37
    elif _itemNum == 8:
        image "images/item/사랑이반지.png":
            # rotate 90
            size 750, 750
            pos 220, 200
        transform:
            rotate -8
            xalign 0.70
            yalign 0.165
            text "사랑이의 반지":
                color u"#000000"
                size 60
                font "경기천년바탕_Regular.ttf"
        for txt in m_strSarangRing:
            text txt:
                size 37             ## 나중에 폰트 사이즈 물어보기
                font "경기천년바탕_Regular.ttf"
                pos m_iFlavor_Text_xpos, dummyPosY
            $ dummyPosY += 37
    elif _itemNum == 9:
        image Elice_pendant_txt:
            size 750, 750
            pos 240, 100

        transform:
            rotate 000
            xalign 0.70
            yalign 0.165
            text "엘리스펜던트":
                color u"#000000"
                size 60
                font "경기천년바탕_Regular.ttf"
        for txt in m_strPandant:
            text txt:
                size 37             ## 나중에 폰트 사이즈 물어보기
                font "경기천년바탕_Regular.ttf"
                pos m_iFlavor_Text_xpos, dummyPosY
            $ dummyPosY += 37

    elif _itemNum == 10:
        image "images/item/이자벨반지.png":
            size 750, 750
            pos 240, 220
        transform:
            rotate -8
            xalign 0.70
            yalign 0.165
            text "이자벨의 반지":
                color u"#000000"
                size 60
                font "경기천년바탕_Regular.ttf"
        for txt in m_strIsabelRing:
            text txt:
                size 37             ## 나중에 폰트 사이즈 물어보기
                font "경기천년바탕_Regular.ttf"
                pos m_iFlavor_Text_xpos, dummyPosY
            $ dummyPosY += 37

    elif _itemNum == 11:
        image "images/item/만년필.png":
            size 750, 750
            pos 240, 220
        transform:
            rotate -8
            xalign 0.66
            yalign 0.22
            text "만년필":
                color u"#000000"
                size 60
                font "경기천년바탕_Regular.ttf"
        for txt in m_strPen:
            text txt:
                size 37             ## 나중에 폰트 사이즈 물어보기
                font "경기천년바탕_Regular.ttf"
                pos m_iFlavor_Text_xpos, dummyPosY
            $ dummyPosY += 37

    elif _itemNum == 12:
        image "images/item/드림캐쳐팔찌.png":
            size 750, 750
            pos 240, 220
        transform:
            rotate -8
            xalign 0.70
            yalign 0.165
            text "드립캐쳐팔찌":
                color u"#000000"
                size 60
                font "경기천년바탕_Regular.ttf"
        for txt in m_strDreamcatcher:
            text txt:
                size 37             ## 나중에 폰트 사이즈 물어보기
                font "경기천년바탕_Regular.ttf"
                pos m_iFlavor_Text_xpos, dummyPosY
            $ dummyPosY += 37

    elif _itemNum == 13:
        image "images/item/문어화분.png":
            size 750, 750
            pos 240, 220
        transform:
            rotate -8
            xalign 0.65
            yalign 0.23
            text "화분":
                color u"#000000"
                size 60
                font "경기천년바탕_Regular.ttf"
        for txt in m_strDreamcatcher:
            text txt:
                size 37             ## 나중에 폰트 사이즈 물어보기
                font "경기천년바탕_Regular.ttf"
                pos m_iFlavor_Text_xpos, dummyPosY
            $ dummyPosY += 37


    imagebutton:
        xalign 0.05
        yalign 0.9
        idle "gui/button_main/back_1.png"
        hover "gui/button_main/back_1_in.png"
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action Hide('ShowItemInfo')


## NameInput 스크린 ############################################################
##
## 게임 시작 시 이름을 입력 받고 재차 이름이 확실한지 물음
##
##
screen item_TextScren:
    text "아이템 획득":
        xalign 0.5
        yalign 0.277
        color u'#FFEAC5'
        font "경기천년바탕_Bold.ttf"
screen Click_Text:

    text "▶ 클릭하여 진행":
        xalign 0.5
        yalign 0.825
        font "경기천년바탕_Regular.ttf"
        color u'969696'
        # outlines [ (3, "#eddcbe", 0, 0) ]


screen nameInput:

    text "플레이어의 이름을 입력해주세요. (5자 이하)":
        align (.51, .3)
        color '#ffffff'
    add "gui/Name_input_frame.png":
        align (.5, .48)
        size (640, 360)

    input id "player_name":
        align (.505, .5) size (45) length 5 font "KoPubBatangLight.ttf" color "#ffffff"

    imagebutton :
        idle "gui/frame_ok_button.png"
        hover "gui/frame_ok_button_in.png"
        align (.505, .68)
        hover_sound "audio/EffectSound/paper.wav"
        activate_sound "audio/EffectSound/paper2.wav"
        action GetText("nameInput", "player_name")


screen Succese:
    modal True

    add "gui/frame_5.png":
        xalign 0.5
        yalign 0.5
        size (900, 375)

    text "정말 [player_name](이)가 맞습니까?\n" :
        xalign 0.5
        yalign 0.5
        color '#ffffff'
    vbox:
        align (0.5 ,.58)
        hbox:
            textbutton _("네!"):
                align (0.45, 0.5)
                action Return(True)

            textbutton _("아니요"):
                align (0.55, 0.4)
                action Return(False)
            align (0.5 ,.5)

## Item Info 스크린 ############################################################
##
## 갤러리에서 아이템을 마우스로 클릭하면 아이템 소환
##


## Confirm 스크린 #################################################################
##
## 게임 입력 관련 예/아니오 질문을 플레이어에게 할 때 이 스크린을 표시합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 이 스크린이 출력 중일 때 다른 스크린과 상호작용할 수 없게 합니다.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("네") action yes_action
                textbutton _("아니오") action no_action

    ## 우클릭과 esc는 '아니오'를 입력하는 것과 같습니다.
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator 스크린 ##########################################################
##
## Skip_indicator 스크린은 스킵 중일 때 "스킵 중"을 표시하기 위해 출력됩니다.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("넘기는 중")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 이 transform으로 화살표를 순서대로 페이드인/페이드아웃합니다.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## BLACK RIGHT-POINTING SMALL TRIANGLE 글리프가 있는 글꼴을 사용해야 합니다.
    font "DejaVuSans.ttf"


## Notify 스크린 ##################################################################
##
## Notify 스크린으로 플레이어에게 메시지를 출력합니다. (예를 들어 '퀵세이브 완
## 료'나 '스크린샷 저장 완료')
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 스크린 #####################################################################
##
## NVL모드 대사와 선택지를 출력합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## vpgrid나 vbox 내에 대사를 출력합니다.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 선택지가 있을 경우, 선택지 출력. config.narrator_menu가 True일 경우
        ## 선택지가 비정상적으로 출력될 수 있습니다. (디폴트는 True입니다.)
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 동시에 출력될 수 있는 NVL 대사의 최대치를 조정합니다.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## 모바일 버전
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## 마우스가 없고 화면이 작을 가능성이 높으므로, 퀵메뉴 버튼의 크기를 키우고 가짓
## 수를 줄입니다.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("되감기") action Rollback()
            textbutton _("넘기기") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("자동진행") action Preference("auto-forward", "toggle")
            textbutton _("메뉴") action ShowMenu()



style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"
style game_menu_outer_frame_history:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
