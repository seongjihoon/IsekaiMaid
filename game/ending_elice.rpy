# 엘리스

label End_Elice:
    scene bg black
    $ renpy.pause(3.0, hard = True)

    play music Elice_horror fadein 2.0
    '문을 열었을 때 펼쳐진 세상은 무척이나 당혹스러웠다.'
    '원래의 세상이 아닌, 엘리스가 살던 세상.'
    '자신의 세계로 돌아온 엘리스의 표정이 무척이나 기뻐 보여서, 함께 웃는 것밖에 할 수 없었다.'
    '생전 겪어본 적 없는, 낯선 세상에서 살아가야 하는 현실이 무척이나 가혹하게 느껴졌다.'
    '그래도 사랑하는 사람과 함께라면 무엇이든 이겨낼 수 있을거라 생각했다.'
    '신분을 숨기고, 엘리스와 자유롭게 살아가려고 했다.'
    '제대로 할 줄 아는 건 없지만, 엘리스가 옆에 있으니 무엇이든 시도할 가치는 있다고 생각했다.'

    stop music

    '그러나.'
    play music horror_a fadein 2.0

    scene bg BG_Garden_Night with Dissolve(0.01, alpha = True)
    scene bg BG_Elice_Kingdom2 with Dissolve (1.0, alpha = True)
    voice Elice_298
    elice '"동생이 도망쳤다고?"'
    '기사' '"네, 반역자의 약혼자는 반역자가 도망칠 시간을 벌다 기사들에게 제압당했습니다."'

    voice Elice_299
    elice '"...약혼자의 목을 성문에 걸어두어라."'

    voice Elice_300
    elice '"자비는 없다. 다들 똑똑히 눈에 새기도록 해라."'
    voice Elice_301
    elice '"감히 누구에게 반기를 들었던 것인지."'

    scene bg BG_Kingdom with Dissolve(1.5)
    '저택에서 보낸 3일을 잊기라도 했는지, 엘리스는 곧장 황위를 되찾았다. '
    '황제의 자리를 되찾는 과정에서 이미 많은 피를 보았으나, 엘리스는 아직 멈출 생각이 없었다.'
    '황궁이 있는 수도에는 항상 피 냄새가 가득했다.'

    # 우열에게 요청, 황량한 까마귀 사운드.
    '어찌나 사람을 많이 죽였는지, 수도에 모여드는 까마귀가 가득하다.'
    '정말 내가 아는 엘리스가 맞는지 의심될 정도다.'
    player '"내가 엘리스를 의심하면 안 되지."'
    '아무리 시간을 보내도 황궁에 적응하지 못하는 나를 위해서 새로 저택을 지어주었다.'
    '우리가 3일이라는 시간을 보냈던 그 저택.'
    '이방인에 불과한 내가 이 세계에서 귀한 취급을 받을 수 있는 건 전부 엘리스 덕분이다.'
    '무력함을 견딜 수 없는 나는 곧장 꿈속으로 도망친다.'

    scene bg black with Dissolve(1.5)
    $renpy.pause(3.0, hard = True)
    player '"엘리스."'
    voice Elice_302
    elice '"이제야 일어났구나?"'
    player '"여긴 무슨 일이야. 바쁜 거 아니었어?"'
    voice Elice_303
    elice '"짐이야 항상 바쁘지만, 황후에게 줄 선물이 있어서."'
    # 우열에게 요청, 좌물쇠 차는 사운드
    player '"이건..."'
    '손목에 채워진 수갑. 이제서야 눈치를 챘지만, 발목에도 족쇄가 채워져 있었다.'
    player '"갑자기 왜 이러는 거야 엘리스!"'
    voice Elice_304
    elice '"어쩔 수 없잖아."'
    voice Elice_305
    elice '"갑작스럽게 얻게 된 것은, 언제 잃어버려도 이상하지 않은 법이야."'
    voice Elice_306
    elice '"나는 너를 잃어버리고 싶지 않으니까... 내가 할 수 있는 최선의 방법으로 너를 보호하는 거지."'
    '이제야 안심이 된다는 듯 편히 웃는 엘리스를 보니 말문이 막혔다.'
    '아무말도 못하는 나와 달리, 엘리스는 한결 편해진 자세로 호칭과 말투도 바꾼 상태로 계속 내게 말을 걸었다.'
    # Elice_CG_006.png ,

    # show Elice_CG
    show Elice_CG_4_2 with Dissolve(.5, alpha = True)
    voice Elice_307
    elice '"오늘은 밥을 좀 남겼더라. 이 나이에 편식이라니 어리광 피우는 거야?"'

    voice Elice_308
    elice '"네 어리광을 직접 받아줄 수 있으면 좋겠지만... 너도 알다시피 내가 너무 바빠서."'

    voice Elice_309
    elice '"시종들을 너무 귀찮게 하지 마."'

    # Elice_CG_007.png ,
    show Elice_CG_4_3 with Dissolve(.5)
    hide Elice_CG_4_2 with None
    voice Elice_310
    elice '"정확히 말하자면 질투 나지 않게 하는 게 좋을 거야."'
    voice Elice_311
    elice '"내가 그들을 죽여버릴지도 모르니까."'
    voice Elice_312
    elice '"넌 멍청해서 내가 직접 말해줘야지 알아듣지..."'
    scene bg black with Dissolve(1.0)
    '방 안에 들어오는 시종의 얼굴이 바뀔 때가 종종 있었다. '
    '설마... 그들도 죽여버린 건 아니겠지?'
    # Elice_CG_006.png , 디졸브 2초.
    show Elice_CG_4_2 with Dissolve(.5)
    hide Elice_CG_4_3 with None
    '식겁한 눈으로 보면, 엘리스는 후후 웃어 보일 뿐이었다.'
    # Elice_CG_007.png
    show Elice_CG_4_3 with Dissolve(.5)
    hide Elice_CG_4_2 with None
    voice Elice_313
    elice '"잘 판단하는 게 좋아."'
    scene bg black with Dissolve( 1.0)
    '나는 엘리스를 진심으로 사랑한다.'
    '남들은 피에 미친 황제라고 손가락질하지만, 나는 그러면 안 된다.'
    '믿었던 가족에게 배신당하고, 엘리스에게 충성하던 기사들은 엘리스를 지키려다 죽었다.'
    '엘리스가 마음을 놓을 상대는 나밖에 없었다.'
    '나를 잃으면, 엘리스에게 남는 것은 차가운 왕좌밖에 없겠지.'
    player '"네가 무슨 짓을 하든 나는 너를 사랑할 거야."'
    # Elice_CG_006.png , 디졸브 1초.
    show Elice_CG_4_2 with Dissolve(.5)
    voice Elice_314
    elice '"후후, 짐에게 바라는 것이라도 있나 황후?"'
    voice Elice_315
    elice '"원한다면 그대가 말했던 주지육림을 실현해주지."'
    # Elice_CG_005.png ,
    show Elice_CG_4_1 with Dissolve(.5)
    hide Elice_CG_4_2 with None
    voice Elice_316
    elice '"단, 다른 사람은 안 돼. 황후도 알겠지만 짐은 질투가 많아서."'
    player '"그런 건 필요 없어. 나한테 필요한 건 오직 너뿐인걸."'
    scene bg black with Dissolve(1.0)
    '생각을 포기하면, 이 현실을 받아들이기 쉽다.'
    '매일 같이 죽어가는 사람들의 비명을 못 들은 척하고, 향수로도 가려지지 않는 지독한 피 냄새는 무시하면 된다.'
    '엘리스가 나에게 보여주지 않으려는 모습을 보지 않으면 된다.'
    '그러면 사랑스러운 나의 연인만 존재한다.'
    '행복해하는 엘리스의 얼굴을 보다 보면, 지금의 삶이 그리 나쁘지 않다고 생각한다.'
    '잘 모르지만... 다른 세상 어딘가에는 이런 형태의 사랑이 있는 거겠지.'
    '나는 조용히 눈을 감고, 엘리스의 목소리를 들었다.'
    stop music fadeout 3.0
    $ renpy.pause(3.5, hard = True)
    jump endcredits



    pass
