label meet_Scarlet:

    scene bg Myroom with Dissolve(1.5)

    player '"아무래도 아침 식사는 힘들겠지?"'
    '그저께와 어제 먹었던 아침이 눈앞에 아른거린다.'
    '오늘은 딱 한 명의 메이드와 있어야 하는 만큼, 식당에서 식사하는 건 힘들 것 같았다.'
    '먹더라도 시간대를 피해서 가는 게 예의겠지.'
    '조금 허한 배를 모르는 척하고, 스칼렛의 방으로 갔다.'

    play sound FootStep1 fadeout 1.0
    scene bg black with Dissolve(1.0)


    scene bg BG_Corridor_2 with Dissolve(1.0)

    play music Scarlet_1 fadein 1.0
    '문을 두드리기도 전에 문이 활짝 열렸다.'
    play sound DoorOpen2
    show Scarlet_pout at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_255
    scarlet '"이제야 왔군!"'
    hide Scarlet_pout with None
    show Scarlet_ppagchim at scarlet_standsize_bs with Dissolve(.5)
    show Scarlet_ppagchim at scarlet_one_jump_bs with None
    voice Scarlet_256
    scarlet '"갓 태어난 거북이가 너보다 빠를거다!"'
    '스칼렛은 꼬리를 잔뜩 부풀리고서는 내게 화를 냈다.'
    player '"혹시, 기다리고 있었어?"'

    hide Scarlet_ppagchim with None
    show Scarlet_stare at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_257
    scarlet '"당연한 말을 하는 군."'

    hide Scarlet_stare with None
    show Scarlet_pout at scarlet_standsize_ms with Dissolve(.50)
    voice Scarlet_258
    scarlet '"약속을 했으면, 기다리는게 당연하지 않은가?"'

    hide Scarlet_pout with None
    show Scarlet_lookout at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_259
    scarlet '"그 파란 꼬맹이는 왜 방 밖으로 못 나가게 해서는..."'

    show Scarlet_lookout at scarlet_one_jump with None
    '스칼렛의 꼬리가 붕붕 흔들렸다.'
    '화가 난 것인지, 기분이 좋은 것인이 구분이 잘 가지 않았다.'
    player '"관리자가 무슨 말을 했는데?"'
    hide Scarlet_lookout with None
    show Scarlet_pout at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_260
    scarlet '"네가 오기 전까지 그 어떤 메이드도 방 밖으로 나갈 수 없다고 하는 군."'
    player '"뭐? 그럼 밥은..."'

    hide Scarlet_pout with Dissolve(1.0)
    '스칼렛의 등 뒤로 본 방 안에는... 바닥을 드러낸 접시들이 있었다.'
    '괜한 걱정을 했다.'

    show Scarlet_inflate at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_261
    scarlet '"기특하군. 이 몸을 걱정하기도 하고."'

    hide Scarlet_inflate with None
    show Scarlet_pout at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_262
    scarlet '"큼, 누가 들으면 안되니 어서 들어오거라."'

    hide Scarlet_pout with None
    play sound DoorOpen2
    scene bg BG_Maidroom with Dissolve(1.5)
    '스칼렛은 나를 끌고 방 안으로 들어갔다.'
    '고소한 스프 냄새가 코 끝을 맴돌았지만, 모르는 척 했다.'
    '배가 조금 고프긴 하지만, 한껏 진지해진 스칼렛에게 밥 달라는 이야기를 할 수는 없으니까...'

    show Scarlet_nonSad at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_263
    scarlet '"어제 이 몸이 했던 이야기를 기억 하느냐?"'
    '내가 고개를 끄덕이자 스칼렛은 만족스러운 표정을 지었다.'

    hide Scarlet_nonSad with None
    show Scarlet_lookout at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_264
    scarlet '"이 몸이 알아본 결과, 이곳은 보통의 세계와 다른 곳이더군."'
    voice Scarlet_265
    scarlet '"해도 제대로 뜨지 않는 걸 보고 예상은 했지만."'
    player '"그래서?"'

    hide Scarlet_lookout with None
    show Scarlet_stare at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_266
    scarlet '"이몸이 원래 있던 곳과 너무 멀어서 그 분께서 내가 이곳에 있다는 걸 아직 눈치채지 못하신 것 같다."'
    voice Scarlet_267
    scarlet '"나만이 진행 가능한 의식을 치뤄서 그분께 내가 이곳에 있단 것을 알릴거다."'
    '스칼렛의 말을 들으며 고개를 끄덕였다.'
    '대체 무슨 의식일려나.'

    hide Scarlet_stare with None
    show Scarlet_nonSad at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_268
    scarlet '"의식을 진행하기 위해서는 네 도움이 필요하다."'
    player '"내 도움?"'

    hide Scarlet_nonSad with None
    show Scarlet_displease at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_269
    scarlet '"그래. 이건 널 위한 의식이기도 하지."'

    hide Scarlet_displease with Dissolve(1.0)
    '스칼렛의 말이 슬슬 이해가지 않기 시작했다.'
    '자신의 위치를 스칼렛이 믿는 그분에게 알리기 위해 의식을 치른다는 것 까지는 이해했는데...'
    '그게 왜 날 위한거지?'
    player '"그 분의 힘이 있으면 내가 온 곳으로 돌려보내줄 수 있으니까?"'

    show Scarlet_lookout at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_270
    scarlet '"...그것도 있지만."'
    '스칼렛은 한 번 말을 멈췄다.'

    hide Scarlet_lookout with None
    show Scarlet_displease at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_271
    scarlet '"이몸은 아직 너를 완전히 믿지 못하고 있다."'

    hide Scarlet_displease with None
    show Scarlet_heung at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_272
    scarlet '"네가 이 의식을 치룬다면, 이몸을 사랑한다는 걸 믿어주겠다."'
    '이른바 사랑의 증명이라는 건가?'

    hide Scarlet_heung with None
    show Scarlet_inflate at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_273
    scarlet '"무섭다면 도망쳐도 좋다."'
    voice Scarlet_274
    scarlet '"네 놈은 고작 그것 밖에 안되는 녀석이라는 뜻이지만..."'

    hide Scarlet_inflate with None
    show Scarlet_Angry at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_275
    scarlet '"이 몸은 도망치는 놈을 붙잡지 않는다."'
    '나는...'
    player '"도망같은 거 가지 않아."'
    player '"널 두고 어디를 가겠어?"'

    hide Scarlet_Angry with None
    show Scarlet_panic at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_276
    scarlet '"...."'

    hide Scarlet_panic with None
    show Scarlet_inflate at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_277
    scarlet '"말만 번지르하긴."'

    hide Scarlet_inflate with Dissolve(1.0)
    '스칼렛은 먼저 자리에서 일어나 앞서나갔다.'
    player '"같이 가!"'

    play sound FootStep1 fadeout 1.0
    scene bg black with Dissolve(1.5)
    '스칼렛을 쫓아 지하실로 갔다.'

    scene bg BG_Underoom with Dissolve(1.5)
    '스칼렛이 미리 준비를 해두었는지, 못보던 것이 많이 늘어있었다.'
    '붉은 색 초라던가, 바닥에 그려진 마법진 등.'
    '평소와 달리 쉽게 들어갈 수 없었다.'
    '나를 보는 스칼렛의 시선을 느끼고서는 지하실 안으로 들어갔다.'

    show Scarlet_displease at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_278
    scarlet '"이 의식은 네가 그 분의 정식 신도가 되기 위한 의식이다."'
    voice Scarlet_279
    scarlet '"네가 평생 느꼈던 그 어떤 고통보다 괴로울 거야."'

    hide Scarlet_displease with None
    show Scarlet_stare at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_280
    scarlet '"도망가지 않는다면 나는 너를 믿을거다."'

    hide Scarlet_stare with None
    show Scarlet_nonSad at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_281
    scarlet '"네게 내 목숨도 맡길 수 있어."'

    hide Scarlet_nonSad with Dissolve(1.0)
    '입에 침이 고인다.'
    '스칼렛은 내가 돌아가기 위해서라도 의식에 참여한다고 생각할까?'
    '스칼렛이 말하는 위대한 그분의 도움이 없더라도, 내일이면 돌아갈 수 있지만...'
    '스칼렛의 신뢰가 퍽 탐났다. '

    stop music fadeout 2.0

    player '"정말로, 도망가지 않으면 날 믿어주는 거지?"'
    play music Scarlet_Cult
    show Scarlet_inflate at scarlet_standsize_ms with Dissolve(.5)
    '나는 스칼렛의 손을 잡고 물었다.'
    '여러가지 장신구를 낀 스칼렛의 손에는 굳은 살이 베겨 있었다.'
    '해적을 하면서 얼마나 많은 죽음을 봤을까.'

    hide Scarlet_inflate with None
    show Scarlet_Sad at scarlet_standsize_ms with Dissolve(.5)
    show Scarlet_Sad at scarlet_one_jump with None
    '스칼렛은 고개를 끄덕였고, 나는 바닥에 그려진 마법진 위에 누웠다.'

    stop music fadeout 2.0
    scene bg black with Dissolve(1.5)
    # 초에 불 붙이는 소리

    '스칼렛은 붉은 초 위에 불을 붙였다.'
    # 마법진이 작동하는 신비로운 소리
    '마법진에 빛나기 시작하며, 스칼렛이 알아듣기 힘든 주문들을 외웠다.'
    '눈 앞이 흐릿해지더니, 안개가 가득한 바다의 환상이 보이기 시작했다.'
    # 천둥번개가 치며 일렁이는 파도 소리

    '천둥 번개가 치는 하늘, 폭풍우치는 바다. 그 너머로 보이는...'
    '스칼렛이 그리 말했던 위대한 그분과 눈이 마주치는 순간.'
    # 기괴한 괴물의 소리
    # 빨간 화면 빠르게 등장 후 사라짐
    # 삐이 거리는 이명
    '찌르는 듯한 두통이 찾아왔다.'
    '머리가 반으로 쪼개지는 듯 했다.'
    '머리를 부여잡으려고 하니, 팔 다리가 추라도 달린 것처럼 무겁다.'
    '아니 나한테 팔 다리가 달려있기는 하던가?'
    voice Scarlet_282
    scarlet '"지금이라도 포기해라!"'
    voice Scarlet_283
    scarlet '"그러면 죽지는 않을거다!"'
    '포기라는 말에 가늘어진 이성이 잠깐동안 자리를 찾아왔다.'
    '이 고통에서 벗어날 수 있다고?'
    '포기하겠다는 말이 목 끝에 차올랐지만 차마 뱉을 수 없었다.'
    voice Scarlet_284
    scarlet '"어서 말해라!"'
    player '"..."'
    '포기할래, 한마디만 말하면 되는데 입에 추라도 달린 것 처럼 열리지 않았다.'
    '의식이 워낙 흐릿한지라, 이것이 나의 의지인지 다른 누군가의 의지인지 알 수 없었다.'
    '꾹 닫혀있던 입이 열렸다.'
    # 피를 토하는 효과음
    # 빨간 화면이 등장 후 사라짐 + vpunch
    player '"쿨럭."'

    scene bg BG_Underoom with Dissolve(1.5)
    show Scarlet_panic at scarlet_standsize_ms with Dissolve(.5)
    # voice Scarlet_284
    scarlet '"[player_name]"'
    '포기하겠다는 말 대신 튀어나온 것은 피였다.'
    '덩어리진 피를 토하는 나를 보며 스칼렛이 외쳤다.'
    hide Scarlet_panic with None
    show Scarlet_tear at scarlet_standsize_ms with Dissolve(.5)
    with vpunch

    show screen Mini_Scene(scarlet_crying) with Dissolve(.5)
    voice Scarlet_285
    scarlet '"이제, 이제 되었으니 빨리 포기하겠다고 말해라!"'
    voice Scarlet_286
    scarlet '"난 너를 믿으니까..."'
    '흐릿한 시야 속에서도 울고 있는 스칼렛이 보였다.'
    '눈물을 닦아주고 싶어 손을 뻗었지만 손은 닿지 못한다.'
    # 불 꺼지는 소리

    hide Scarlet_tear with Dissolve(.2)
    scene bg black with None
    $renpy.pause(5.0,hard = True)
    player '"으..."'
    play sound Clothes
    '깨질 듯이 아픈 머리를 부여잡고 일어났다.'
    '의식은 제대로 끝난 건가?'
    '그러고보니 스칼렛은...?'
    '놀란 나는 주변을 살펴보았다.'

    play music emotional fadein 2.0
    # 스칼렛 CG 004
    '놀란 마음이 무색하게도, 스칼렛은 바로 내 옆자리에서 곤히 자고 있었다.'
    player '"잘거면 제대로 눕지."'
    player '"왜 엎드려 있어서, 마음 쓰이게 하는 건지..."'
    '딱 배만 가린 이불을 보고 있자니 웃음이 나왔다. '
    '감기에 걸릴 걱정은 안해도 되겠네.'
    '이불을 똑바로 덮어주려고 할 때, 부스럭 거리는 소리 때문인지 스칼렛이 눈을 떴다.'
    # 눈 뜨는 일러스트 dissolve .5
    voice Scarlet_287
    scarlet '"으음..."'
    player '"아..."'
    '막 눈을 뜬 스칼렛과 정통으로 눈이 마주쳤다.'
    '잠에서 막 깬 눈은 초점이 제대로 잡히지 않았다.'
    '몇 번 눈을 깜빡이던 스칼렛은 살며시 웃으며 내게 말을 걸었다.'
    # 눈이 완전히 뜬 일러스트
    voice Scarlet_288
    scarlet '"이제야 눈을 뜨다니, 넌 모든 게 느리구나."'
    player '"미안, 많이 걱정했어?"'
    voice Scarlet_289
    scarlet '"괜찮다. 이 몸에게 주어진 시간은 많으니... 너 하나 기다리는 건 일도 아니지."'
    '부드러운 분위기에 괜히 입 안이 달았다.'
    '스칼렛과 같이 침대에 누워 얼굴을 마주하고 있는 이 순간.'
    '이대로 시간이 멈춘다면 얼마나 좋을까.'
    '나는 손을 뻗어 스칼렛의 손을 잡았다.'
    '엄지 손가락으로 스칼렛의 손등을 살살 쓸어내리며, 스칼렛의 반응을 살폈다.'
    '스칼렛은 아까처럼 미소지은 얼굴로 나를 바라볼 뿐이었다.'
    # 눈 완전히 뜬 상태에서 꼬리만 살랑이는
    '아니, 꼬리는 열심히 움직였다.'
    player '"의식은 제대로 끝난 거야?"'
    player '"어떻게 끝나는지 듣지도 못했고... 그냥 기절해버렸잖아."'
    # (미소를 없애고 정색하고 입을 닫은채로 주인공을 보는) , 디졸브 0.5초 - 이부분 아직 일러스트 드라이브에 없음, 추후 작업자분이 추가할 예정
    '스칼렛은 아무 말도 하지 않고 나를 바라봤다.'
    player '"음, 혹시 제대로 안 끝나서 다시 해야해?"'
    '잠시 심호흡을 한 스칼렛이 굳은 표정을 지었다.'
    # (죄책감으로 찡그려진 얼굴, 시선은 주인공을 보지 못하는) , 디졸브 0.5초 - 이부분 아직 일러스트 드라이브에 없음, 추후 작업자분이 추가할 예정
    voice Scarlet_290
    scarlet '"...네게 거짓말을 했었다."'
    '스칼렛이 낮은 목소리로 내게 말했다.'
    voice Scarlet_291
    scarlet '"네가 꼭 의식에 참여하지 않더라도, 의식은 진행할 수 있었어."'
    voice Scarlet_292
    scarlet '"이몸은 그저 네 각오를 볼 생각이었는데..."'
    # (주인공을 바라보며 눈물을 흘리는) , 디졸브 0.5초 - 이부분 아직 일러스트 드라이브에 없음, 추후 작업자분이 추가할 예정
    voice Scarlet_293
    scarlet '"네가 쉽게 포기 하지 않더군."'
    '스칼렛의 코 끝이 붉어졌다.'
    '붉어진 눈에서 눈물이 방울방울 흘러나왔다.'
    '나는 깍지를 끼지 않은 손으로 스칼렛의 눈물을 닦아주었다.'

    player '"내가 선택한 일인 걸."'
    player '"널 너무 좋아해서, 너에게 인정 받고 싶었어."'
    player '"바보같지 나?"'
    '스칼렛은 고개를 끄덕인다.'
    # (주인공을 바라보며 눈물을 흘리며 웃는) , 디졸브 0.5초 - 이부분 아직 일러스트 드라이브에 없음, 추후 작업자분이 추가할 예정
    voice Scarlet_294
    scarlet '"미련하고, 한심하고... 믿음직스럽더군."'
    voice Scarlet_295
    scarlet '"앞으로 어떤 일이 일어나도 나를 떠날 것 같지 않아서."'
    '인정 받았다는 뿌듯함이 마음 속을 꽉 채운다.'
    '거품이 보글보글 차오르는 기분.'
    '거품이 꺼지더라도, 그 무엇보다 달콤한 것이 그 자리에 남아있을 것 같다.'
    player '"스칼렛. 나도 하고싶은 말이 있어."'
    # (주인공을 바라보며 눈물을 흘리며 입을 닫은) , 디졸브 0.5초 - 이부분 아직 일러스트 드라이브에 없음, 추후 작업자분이 추가할 예정
    voice Scarlet_296
    scarlet '"..."'
    player '"내가 있던 원래 세계가 아니라, 네가 있던 세계로 같이 가고 싶어."'
    player '"너랑 떨어지고 싶지 않아."'
    '사랑에 빠지면 사람은 바보가 된다.'
    '눈 앞에 있는 스칼렛 이외의 것은 생각할 수 없게 되버렸다.'
    '학교, 친구, 가족, 꿈... 그런 건 전부 상관 없어진다.'
    # (주인공을 바라보며 눈물을 그치고 입을 닫은) , 디졸브 0.5초 - 이부분 아직 일러스트 드라이브에 없음, 추후 작업자분이 추가할 예정
    '내 말을 들은 스칼렛의 표정은 미묘했다.'
    '기뻐할 줄 알았는데, 씁쓸한 것 같았다.'
    player '"왜 그런 표정을 하는 거야?"'
    player '"혹시 내가 너를 쫓아가는게 방해야?"'
    # (죄책감으로 찡그려진 얼굴, 시선은 주인공을 보고 있는) , 디졸브 0.5초 - 이부분 아직 일러스트 드라이브에 없음, 추후 작업자분이 추가할 예정
    voice Scarlet_297
    scarlet '"...그건 너의 결정이지?"'
    '스칼렛은 엉뚱한 말을 내뱉었다.'
    player '"응. 내가 생각한 거야. 너랑 앞으로도 계속 함께하고 싶어."'
    play sound Clothes
    # CG 지우기
    '나는 몸을 옆으로 치우며 빈공간을 만들었다.'
    '스칼렛은 침대 위로 올라와 나를 바라봤다.'
    '우린 오랫동안 대화를 나누었다.'
    '나는 이제는 다시 가지 못할, 내가 원래 살던 세계에 대한 이야기를 했다.'
    '무척이나 사랑했던 어머니와 아버지. 하루를 함께했던 친구들.'
    '이제 졸업할 수 없는 고등학교 생활에 대해서도.'
    '다시는 만나지 못할 것을 이야기하면, 스칼렛은 대신할 것들을 말해준다.'
    # (눈 완전히 뜬 일러스트) , 디졸브 0.5초 - 이부분 아직 일러스트 드라이브에 없음, 추후 작업자분이 추가할 예정
    voice Scarlet_298
    scarlet '"네게도 새로운 가족이 생길 것이다."'
    voice Scarlet_299
    scarlet '"교단의 식구들과...내가, 그리고 그분께서 항상 너와 함께하겠지."'
    voice Scarlet_300
    scarlet '"네가 말하는 빌딩이라는 건물들을 보지 못하는 대신 거친 바다를 지겹도록 볼 수 있다."'
    voice Scarlet_301
    scarlet '"배도 뜨지 못하는 험한 바다를 네 멋대로 휘젓는 경험을 하게 해주지."'
    player '"항상 내 옆에 있어줄거지?"'
    voice Scarlet_302
    scarlet '"그래. 네가 내게 그런 신뢰를 보여준 이상. 나는 절대로 네 곁을 떠나지 않을 것이다."'
    # (눈 반쯤 뜬 일러스트) , 디졸브 0.5초 - 이부분 아직 일러스트 드라이브에 없음, 추후 작업자분이 추가할 예정
    '베개를 끌어안고 엎드려있던 스칼렛은 느리게 눈을 깜빡이며 말했다.'
    player '"졸려?"'
    voice Scarlet_303
    scarlet '"조금. 내일이면 이곳을 떠날 수 있다."'
    voice Scarlet_304
    scarlet '"...다른 녀석들에게 작별 인사를 할 건가?"'
    '스칼렛은 내 눈치를 보며 물었다.'
    player '"굳이 그래야 할까? 앞으로 다시는 만나지 않을 사람들인데."'
    # (눈을 감은 일러스트) , 디졸브 0.5초 - 이부분 아직 일러스트 드라이브에 없음, 추후 작업자분이 추가할 예정
    voice Scarlet_305
    scarlet '"네가 그러겠다면 말릴 이유는 없지."'
    voice Scarlet_306
    scarlet '"어서 자거라. 내일은 새로운 세상을 만나야 하니까..."'
    '눈을 감고 잠든 스칼렛은 무척이나 귀여웠다.'
    '나도 스칼렛처럼 죽음을 비껴간 삶을 사는 것일까?'
    '궁금했지만, 이미 자는 스칼렛에게 물을 수 없어서 질문은 속으로 삼켰다.'
    '관리자를 속이고, 다른 메이드들을 모르는 척 하는 건 미안하지만.'
    '나에게 제일 중요한 것은 스칼렛이니까.'
    '아, 언제부터 이렇게 스칼렛을 소중히 생각하게 된 걸까?'
    # cg hide

    stop music fadeout 2.0
    scene bg black with Dissolve(1.5)
    $renpy.pause(3.0, hard = True)
    play music emotional_2 fadein 2.0
    scene bg BG_Maidroom with Dissolve(1.5)
    show Scarlet_Happy at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_307
    scarlet '"일어나거라!"' with vpunch
    '나를 깨우는 메이드는 스칼렛이었다.'
    '둘이 함께 잠들었으니 당연한 일이지만.'

    hide Scarlet_Happy with None
    show Scarlet_Laughter at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_308
    scarlet '"떠날 준비는 했나?"'
    player '"아니. 옷도 못 갈아입었어."'

    hide Scarlet_Laughter with None
    show Scarlet_Normal at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_309
    scarlet '"네 방으로 갈아입은 후, 지하실로 오거라."'
    voice Scarlet_310
    scarlet '"미리 준비를 하고 있을테니."'
    player '"음... 관리자한테 들키지는 않겠지?"'
    '내 질문에 스칼렛은 크게 웃었다.'

    hide Scarlet_Normal with None
    show Scarlet_Happy at scarlet_standsize_ms with Dissolve(.5)
    show Scarlet_Happy at scarlet_one_jump with None
    voice Scarlet_311
    scarlet '"하하, 그 분의 힘이 완전히 돌아온 이상 더는 그 꼬맹이를 신경쓰지 않아도 된다!"'
    voice Scarlet_312
    scarlet '"아마 지금쯤 탈출할 수 없는 미로를 헤매고 있겠지!"'
    player '"그건 좀... 불쌍한데."'
    '조그만 관리자가 열심히 미로를 헤매는 모습을 생각하니 괜히 안쓰러웠다.'

    hide Scarlet_Happy with None
    show Scarlet_Normal at scarlet_standsize_ms with Dissolve(.5)
    voice Scarlet_313
    scarlet '"우리가 돌아가는 대로 미로에서 나갈 수 있을테니 괜히 걱정하지 말거라."'
    player '"그런 거라면 뭐."'

    hide Scarlet_Normal with None
    play sound FootStep1 fadeout 1.0
    scene bg black with Dissolve(2.0)
    '스칼렛의 말을 들은 나는 가벼운 걸음으로 내 방으로 돌아갔다.'
    scene bg BG_Corridor_2 with Dissolve(2.0)
    '처음 이곳에 왔을 때와 똑같은 옷을 입고 스칼렛이 말한 지하실로 향했다.'
    '그러고보니 무언가를 잊어버린 것 같은데...'
    '다른 메이드의 방 문을 지날때는 속에 무언가 얹힌 것 같았다.'
    '스칼렛을 돕는 것 이외에도 내 역할이 있었던 것 같은데.'
    '머리에 꼭 안개가 낀 것 같았다.'
    show Scarlet_pout at scarlet_standsize_bs with Dissolve(.5)
    voice Scarlet_314
    scarlet '"정말이지, 너는 얼마나 이 몸을 기다리게 할 생각이냐?"'
    '지하실로 내려가지 않고 있던 나를 데리러, 스칼렛이 올라왔다.'
    # (스칼렛이 손을 내미는 미니컷씬) (추후추가 현재 없음)
    '스칼렛은 어서 가자는 듯이 내게 손을 내밀었다.'
    '내민 손을 붙잡으니 머릿속을 가득 채우던 안개가 사라진다.'
    '잊어버린 것은 없다.'

    scene bg black with Dissolve(2.0)
    # 블랙홀 미니컷씬 페이드인  2초
    player '"이건..."'
    voice Scarlet_315
    scarlet '"우리를 원래 세계로 돌려보내줄 문이다!"'
    '스칼렛은 자랑스럽게 말했다.'
    '어제 의식을 진행했던 마법진 위에, 블랙홀 같은 것이 있었다.'
    '세계를 찢어놓은 틈 같기도 하고.'
    '괴이하다 느껴지는 동시에, 안락함이 느껴졌다.'
    '어제부터 내가 좀 이상한 것 같았다.'
    '낯선 것이 낯설지 않게 느껴진다.'
    '분명 스칼렛이 옆에 있기 때문이겠지.'

    scene bg BG_Underoom with Dissolve(1.0)
    show Scarlet_Normal at scarlet_standsize_bs with Dissolve(.5)
    voice Scarlet_316
    scarlet '"[player_name]. 마음의 준비는 끝났느냐?"'
    player '"물론이지. 어제 너에게 같이 가고 싶다고 말했을 때부터 내 준비는 끝났어."'

    hide Scarlet_Normal with None
    show Scarlet_inflate at scarlet_standsize_bs with Dissolve(.5)
    voice Scarlet_317
    scarlet '"그런 것치고는 영 정신을 다른 곳에 팔던데?"'
    player '"그건..."'
    '스칼렛의 추궁에 딱히 할 말이 없었다.'
    '눈 앞의 스칼렛에게 집중하지 못하고 딴 생각을 한 것은 사실이었으니까.'

    hide Scarlet_inflate with None
    show Scarlet_Laughter at scarlet_standsize_bs with Dissolve(.5)
    voice Scarlet_318
    scarlet '"걱정할 것 없다. 너와 이 몸이 함께라면 그 무엇도 이겨낼 수 있을거야."'
    '스칼렛은 자신이 말한 사실에 관해 조금도 의심하지 않는 눈치였다.'
    '내가 옆에 있다면 무엇이든 할 수 있다는 말이, 내 모험심을 자극한다.'
    '눈에 가득찬 신뢰는 어제의 내가 얻어낸 것이다.'
    player '"저곳에서도 잘 부탁할게."'
    # 스칼렛과 손 잡는 미니 컷씬
    '지하실로 내려올 때 잡았던 손에 슬쩍 깍지를 꼈다.'

    play sound sea_waves_3
    '멀리서 들려오는 파도소리와 바다의 짠내.'

    scene bg black with Dissolve(2.0)
    '앞으로의 미래는 조금도 예상할 수 없지만, 두려움은 없다.'

    play sound FootStep1
    '나는 스칼렛과 함께 다른 세계를 향해서 나아갔다.'
    $renpy.pause(2.0, hard = True)
    # 끝
    # 엔딩 크레딧

    '아직 호러 엔딩 관련 기믹이 존재하지 않아 엔딩크래딧 이후 호러엔딩으로 진입합니다.'
    call endcredits from _call_endcredits

    jump End_Scarlet


    return
