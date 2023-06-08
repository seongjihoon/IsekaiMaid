
label meet_Sarang:
    scene bg Myroom with Dissolve(1.5)
    player '"아무래도 아침 식사는 힘들겠지?"'
    '그저께와 어제 먹었던 아침이 눈앞에 아른거린다.'
    '오늘은 딱 한 명의 메이드와 있어야 하는 만큼, 식당에서 식사하는 건 힘들 것 같았다.'
    '먹더라도 시간대를 피해서 가는 게 예의겠지.'
    scene bg black with Dissolve(1.0)
    play sound FootStep1 fadeout 1.0
    '조금 허한 배를 모르는 척하고, 윤사랑의 방으로 향했다.'
    '마음의 준비를 단단히 하고, 방문을 두드렸다.'
    play sound FootStep1
    player '"저기, 있어?"'

    with vpunch
    '우당탕탕, 누군가 구르는 소리가 방 안에서 들려왔다.'
    voice Yunsarang_258
    yun '"네, 네! 있어요!"'
    voice Yunsarang_259
    yun '"저 있어요 주인님!"'
    play sound DoorOpen2

    '방 안에서 소리치는 소리가 들리고, 금방 방문이 열렸다.'
    play music Yunsarang_2
    show Yun_Happy at yun_standsize_bs with Dissolve(.5)
    '세상 그 어느 때보다 행복한 얼굴을 한 윤사랑이 나를 반겼다.'

    hide Yun_Happy with None
    show Yun_huc at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_260
    yun '"오늘은 주인님이 저를 깨우러 와주시는 건가요?"'
    player '"아, 그렇게 되나? 응. 좋은 아침이야."'

    hide Yun_huc with None
    show Yun_Laughter at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_261
    yun '"좋은 아침이에요 주인님!"'
    '해맑게 웃는 윤사랑은 무척이나 순수해 보였다.'
    '가끔 수상한 모습을 보이긴 했지만...'
    '이런 모습을 보면, 나쁜 사람이라는 생각이 들지 않는다.'

    hide Yun_Laughter with None
    show Yun_wink at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_262
    yun '"아침 먹으러 갈까요? 오늘은 저희가 제일 먼저 도착해 있겠네요!"'
    player '"아, 잠시만."'
    '식당으로 향하려는 윤사랑을 붙잡았다.'
    player '"부탁이 있는데."'

    hide Yun_wink with None
    show Yun_lookout at yun_standsize_bs with Dissolve(.5)
    '나를 빤히 바라보는 윤사랑을 보니, 얼굴에 열이 올랐다.'
    '괜히 첫날 관리자가 내게 했던 말이 떠올랐다.'
    '좋아하지 않도록 조심하라고 하는 이유가 있구나.'
    '이렇게 귀여운 여자아이가, 나를 좋아한다고 온몸으로 말하는데...'

    stop music fadeout 1.0
    player '"오늘 하루의 시간을 나한테 줄 수 있어?"'

    hide Yun_lookout with None
    show Yun_panic at yun_standsize_bs with Dissolve(.5)
    with vpunch
    voice Yunsarang_263
    yun '"...네에?"'
    play music Yunsarang_1
    player '"너에 대해서 좀 더 자세히 알고 싶어."'
    player '"다른 사람들에게 방해받지 않고, 단둘이서만."'
    player '"그러니까... 너의 하루를 나에게 주지 않을래?"'

    hide Yun_panic with None
    show Yun_fallinlove at yun_standsize_bs with Dissolve(.5)
    '말을 하는 나의 얼굴도, 내 이야기를 듣는 윤사랑의 얼굴도 사과만큼 붉게 달아올랐다.'
    '툭 건드리면 터질 것 같은 우리는 방 앞에 서서 서로를 바라보고 있었다.'
    '항상 조잘조잘 여러 가지 이야기를 하던 윤사랑은 아무 말도 못 하고 나만 바라보고 있었다.'
    '고개를 끄덕이는 것으로 윤사랑은 대답을 대신했다.'
    '그걸로 충분하다. 잡고 있는 윤사랑의 손을 놓지 않고, 정원을 향해 걸어갔다.'

    hide Yun_fallinlove with None
    play sound FootStep1
    $renpy.pause(1.0)
    scene bg BG_Garden_Morning with Dissolve(1.0)
    play music emotional fadein 1.0
    '푸른 장미로 가득한 정원은 언제와도 신기해 보였다.'
    '아무리 봐도 익숙해지지 않을 것 같은 풍경.'
    '푸른색으로 가득 찬 정원에서 분홍 머리인 윤사랑은 눈에 띄면서도, 굉장히 잘 어울려 보였다.'

    show Yun_lookout at yun_standsize_ms with Dissolve(.5)
    voice Yunsarang_264
    yun '"이 정원의 장미는 다들 시들 줄 모르네요."'
    player '"진짜 장미가 아닌 걸지도 모르지."'

    hide Yun_lookout with None
    show Yun_pout at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_265
    yun '"조화인 걸까요? 그런 것 치고는 제대로 향이 나는데..."'
    '윤사랑은 고개를 숙여서 꽃의 향기를 맡았다.'

    hide Yun_pout with None
    show Yun_lookout at yun_standsize_ms with Dissolve(.5)
    voice Yunsarang_266
    yun '"뭐, 별로 중요한 건 아니지만요.."'

    hide Yun_lookout with None
    show Yun_Normal at yun_standsize_ms with Dissolve(.5)
    voice Yunsarang_267
    yun '"그러고 보니까, 주인님과 제가 처음 여기에 왔을 때 물어봤었죠?"'
    voice Yunsarang_268
    yun '"주인님은 어떤 색을 좋아하는지.."'

    hide Yun_Normal with None
    show Yun_lookout at yun_standsize_ms with Dissolve(.5)

    yun '"주인님... 제가 좋아하는 색이 뭔지 기억하시나요?"'
    player '"그건..."'

    menu :
        "선택지 1 분홍색":
            call select_Pink_Blue from _call_select_Pink_Blue
            pass

        "선택지 2 붉은색":
            hide Yun_lookout with None
            show Yun_Happy at yun_standsize_ms with Dissolve(.5)
            voice Yunsarang_273
            yun '"맞아요. 제가 제일 좋아하는 색은 붉은색이에요."'
            hide Yun_Happy with None
            pass

        "선택지 3 파란색":
            call select_Pink_Blue from _call_select_Pink_Blue_1
            pass

        "선택지 4 보라색":
            hide Yun_lookout with None
            show Yun_panic at yun_standsize_ms with Dissolve(.5)
            voice Yunsarang_271
            yun '"...저는 보라색을 제일 싫어해요."'

            hide Yun_panic with None
            show Yun_pout at yun_standsize_ms with Dissolve(.5)
            voice Yunsarang_272
            yun '"그러니까, 다음에는 보라색을 고르지 않으셨으면 좋겠어요."'
            hide Yun_pout with None
            pass

    show Yun_Sad2 at yun_standsize_ms with Dissolve(.5)
    voice Yunsarang_274
    yun '"주인님이 저에 대해서 많이 기억하셨으면 좋겠어요."'
    voice Yunsarang_275
    yun '"제가 주인님에 대해 기억하는 만큼 말이죠."'
    '씁쓸한 미소를 짓는 윤사랑을 보니, 무언가 이상했다.'
    player '"뭐라도 기억 난 거야?"'
    hide Yun_Sad2 with None
    show Yun_Normal at yun_standsize_ms with Dissolve(.5)
    voice Yunsarang_276
    yun '"...네. 어젯밤 주인님, 그러니까... [player_name], 네가 돌아간 후에 모두 다 기억났어."'
    '윤사랑은 마주 잡고 있던 손에 조금 힘을 주었다.'
    player '"걸으면서 이야기할까?"'
    hide Yun_Normal with None
    show Yun_pout2 at yun_standsize_ms with Dissolve(.5)
    voice Yunsarang_277
    yun '"...그래."'

    hide Yun_pout2 with None
    show Yun_pout2 at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_278
    yun '"연회장에 들어온 너를 봤을 때 무척이나 익숙하다고 생각했어."'
    voice Yunsarang_279
    yun '"굉장히 옛날부터 알고 있었던 사람인 것 같았지."'
    voice Yunsarang_280
    yun '"목소리도, 얼굴도, 이름도 다 내가 아는 건데 네가 나의 어떤 사람이었는지 떠오르지 않아서 얼마나 답답했는지 몰라."'

    hide Yun_pout2 with None
    show Yun_Sad at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_281
    yun '"기억이 없는 나는, 나라고 생각하지 않았으니까..."'
    voice Yunsarang_282
    yun '"네가 아는 내가 아닐까 봐 걱정했어."'
    player '"그건..."'

    hide Yun_Sad with None
    show Yun_Normal at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_283
    yun '"너도 나에 대한 기억이 없다는 걸 알았을 때 얼마나 안심했는지 몰라."'

    hide Yun_Normal with None
    show Yun_Sad2 at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_284
    yun '"그런데, 우습게도 좀 서글퍼지더라."'
    '담담하게 이어지는 목소리에 슬픔이 서렸다.'
    '뺨을 타고 흘러내린 눈물은 땅에 떨어졌다.'

    hide Yun_Sad2 with None
    show Yun_Sad at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_285
    yun '"우리가 연인처럼 거창한 사이였던 건 아니야."'
    '윤사랑은 손을 들어 눈물을 닦아냈다.'
    voice Yunsarang_286
    yun '"하지만, 쉽게 잊을 사이는 아니라고 생각해."'

    hide Yun_Sad with None
    show Yun_pout2 at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_287
    yun '"친구였거든. 기억도 안 날 만큼 어릴 때부터 알고 지내던 사이."'
    player '"...응."'
    voice Yunsarang_288
    yun '"기억나? 놀이터에서 같이 그네를 타려다가 넘어졌던 일?"'
    '윤사랑의 말을 듣고 기억을 더듬었다.'
    '혼자 타야 하는 그네를 둘이서 타려다가 넘어지다니... 크게 다쳤던 게 아니라면 별로 기억나지 않을 것 같았다.'

    player '"잘 모르겠어."'
    player '"너무 어릴 때 일이라서 그런가?"'

    hide Yun_pout2 with None
    show Yun_pout at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_289
    yun '"그러면 초등학교 때 책상 서랍에 있던 녹아버린 초콜렛 때문에 교과서가 더러워진 건?"'
    voice Yunsarang_290
    yun '"그때 엄청 울었잖아. 누가 괴롭히는 것 같다고."'

    hide Yun_pout with None
    show Yun_lookout at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_291
    yun '"사실 그거 나였는 데..."'
    '확실히 이번 일은 쉽게 잊어버리지 못할 일 같았다.'
    '하지만... 정말로 기억나지 않는걸?'
    '누군가 윤사랑의 기억만 깔끔히 도려내기라도 한 듯, 아무것도 떠오르지 않았다.'
    player '"...미안, 정말로 아무것도 기억나지 않아."'

    hide Yun_lookout with None
    show Yun_anxiety at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_292
    yun '"아..."'
    voice Yunsarang_293
    yun '"이런 곳에 와버렸으니까, 기억이 좀 없어지는 건 어쩔 수 없다는 거 알지만..."'

    hide Yun_anxiety with None
    show Yun_Sad at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_294
    yun '"조금 많이 슬프네. 나는 다 되찾았는데 왜 너는 기억하지 못하는 걸까."'
    '윤사랑의 손이 떨리는 것이 느껴졌다.'

    hide Yun_Sad with None
    show Yun_tear at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_295
    yun '"미안하다는 말은 하지 마. 너는 잘못한 게 없으니까."'
    voice Yunsarang_296
    yun '"나 혼자서 아무리 옛날 일을 이야기해도, 네가 기억하지 못한다면 소용없어."'
    player '"..."'

    hide Yun_tear with None
    show Yun_Sad at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_297
    yun '"다시 내 친구가 되어달라는 말은 하지 않을 거야."'

    hide Yun_Sad with None
    show Yun_tear at yun_standsize_bs with Dissolve(.5)
    # add. 일러스트 삽입하는 부분
    voice Yunsarang_298
    yun '"왜냐면... 나, 너를 좋아하거든."'
    voice Yunsarang_299
    yun '"이곳에 오기 전부터, 훨씬 옛날부터 좋아했어."'
    '눈물로 범벅이 된 얼굴로 윤사랑은 내게 고백했다.'
    '귀여운 얼굴이 엉망이 되었지만, 그 어느 때보다 귀여워 보였다.'
    # add. 일러스트 입을 여는 것으로 변경 (페이드 하면 부드러운 연출이 될 듯)

    hide Yun_tear with None
    show Yun_Sad2 at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_300
    yun '"차라리 기억을 잊어서 다행이야."'
    voice Yunsarang_301
    yun '"가족이라고 생각할 만큼 가까웠던 사이니까..."'

    # add. 시선을 돌리는 것으로 변경 (페이드)
    hide Yun_Sad2 with None
    show Yun_Sad at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_302
    yun '"그때도 우리 사이가 너무 가까워서 고백할 생각을 하지 못했어."'
    voice Yunsarang_303
    yun '"지금이라면, 네가 기억을 잃어버린 지금이라면 말할 수 있어."'
    '시간이 멈추는 듯한 착각이 든다.'
    '느리게 눈을 감았다 뜬 윤사랑은 결심을 한 표정으로 내게 말한다.'
    # add. 결단에 찬 표정으로 주인공을 똑바로 쳐다보는 일러스트로 변경 (페이드)

    hide Yun_Sad with None
    show Yun_Sad2 at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_304
    yun '"좋아해, [player_name]."'
    voice Yunsarang_305
    yun '"너의 연인이 되고 싶어."'

    hide Yun_Sad2 with None
    show Yun_pout2 at yun_standsize_bs with Dissolve(.5)
    # add. 표정을 찡그리며 웃는?
    voice Yunsarang_306
    yun '"너는 어때? 내가 너의 연인이 되었으면 좋겠어?"'
    '잠깐 숨이 막혔다. 내가 할 수 있는 대답은 하나로 정해져 있다.'
    player '"...나도 너를 좋아해."'
    player '"네가 내 연인이 되어주었으면 좋겠어."'
    '윤사랑의 얼굴은 살짝 찡그러졌다가 이내 환해졌다.'
    # add. 일러스트 지우기
    hide Yun_pout2 with None

    '윤사랑의 고백은 조금 당황스럽지만, 이해하지 못할 것은 아니다.'
    '3일 만에 사랑에 빠진 나보다는, 예전의 기억을 되찾은 윤사랑이 더 설득력 있겠지.'
    '어쩌면, 예전의 감정에 나도 영향을 받은 게 아닐까?'
    '이곳에 오기 전의 나도 윤사랑을 좋아하지 않았을까?'
    '그런 생각을 하면서 품에 안겨 오는 윤사랑을 끌어안았다.'
    '이제는 확실하다.'
    '윤사랑은 절대로 흉악한 범죄자 따위가 아니다.'
    '대한민국에 살고있는 여고생 중에서 끔찍한 범죄를 저지를 만할 사람이 몇 명이나 되겠는가?'
    '현실적으로 불가능할 뿐만 아니라, 사랑 앞에서는 이렇게 솔직한 애가... 사람을 죽일 수 있을리 없잖아.'
    '윤사랑이 내게로 손을 뻗는다.'

    scene bg black with Dissolve(1.0)
    '뺨을 감싼 손길을 따로 고개를 움직여, 눈을 감으면...'
    '부드러운 입술의 촉감이 느껴진다.'

    scene bg black with Dissolve(1.0)
    $renpy.pause(1.0, hard = True)
    '우리만의 시간이 끝난 후, 분위기는 어색해졌다.'

    scene bg Myroom with Dissolve(1.5)
    player '"춥지 않아? 이제 슬슬 들어가는 게 어때?"'

    show Yun_pout2 at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_307
    yun '"...좋아요."'
    '싱긋 웃은 윤사랑은 마주 잡은 손을 흔들며 나와 함께 저택으로 걸어갔다.'

    stop music fadeout 3.0
    scene bg black with Dissolve(4.0)
    $renpy.pause(2.0, hard = True)
    scene bg Myroom with Dissolve(.5)
    play music serious_little

    '오늘도 나를 깨우러 오는 메이드는 없었다.'
    play sound standup
    '처음 이곳에 왔을 때와 같은 옷을 입고 방 밖으로 나오니 관리자가 나를 기다리고 있었다.'
    
    scene bg black with Dissolve(1.0)
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5)
    admin '"좋은 아침이야 주인님! 드디어 집으로 돌아가네, 기쁘지?"'
    player '"응. 더이상 네 얼굴을 보지 않아도 된다는 점에서 특히."'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Absurd at admin_standsize_ms with Dissolve(.5)
    admin '"그런 말로 아쉬움을 숨기려고 해도 소용없어."'

    hide Hyeyeon_Absurd with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5)
    admin '"나는 유능해서 다 알아보거든~"'
    player '"뭐?"'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5)
    show Hyeyeon_Laughter at admin_one_jump_bs with None
    admin '"나랑 헤어지는 게 무척 아쉽지? 응?"'
    player '"그럴 리가."'
    '갑자기 치근대는 관리자를 밀어냈다.'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(.5)
    admin '"함께 돌아갈 사람은 정했어?"'
    admin '"저 잔인한 메이드들 사이에서 주인님이 무고하다고 생각하는 사람은 누구야?"'
    '더는 고민할 필요도 없다. 답은 정했으니까.'
    player '"나는 윤사랑과 함께 돌아갈 거야."'

    hide Hyeyeon_Normal with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5)
    admin '"흐응~ 그게 주인님의 답이구나."'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Happy at admin_standsize_ms with Dissolve(.5)
    admin '"미리 지하실로 가있어, 주인님! 윤사랑을 데려올 테니까."'
    player '"원래 이 타이밍에는 내가 맞았는지 틀렸는지 알려주지 않아?"'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5)
    admin '"응? 내가 그런 것도 알려줘야 해?"'
    '관리자는 고개를 갸웃거리며 내게 물었다.'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Angry at admin_standsize_ms with Dissolve(.5)
    show Hyeyeon_Angry at admin_one_jump with None
    admin '"주인님의 답이 맞는지 틀렸는지는 주인님이 직접 확인해야지."'
    admin '"남한테 모든 걸 떠넘기는 건 좋지 않은 습관이야!"'
    player '"...허."'
    '하도 어이가 없어서 웃음이 나올 지경이다.'

    hide Hyeyeon_Angry with None
    show Hyeyeon_Normal at admin_standsize_ms with Dissolve(.5)
    admin '"자, 쓸데없이 시간 끌지 말고 돌아가자고~"'

    scene bg BG_Underoom with Dissolve(.5)
    '눈앞에서 관리자가 사라지고, 지하실로 향했다.'
    '지하실에는 그동안 본 적 없는 문이 있었다.'
    '잠겨있는 문, 너머에 뭐가 있는지 예상은 할 수 있었다.'

    show Yun_fallinlove at yun_standsize_ms with Dissolve(.5)
    voice Yunsarang_308
    yun '"주인님... 여긴?"'
    '관리자의 손에 이끌려 내려온 윤사랑이 나를 바라보며 물었다.'

    show Hyeyeon_Happy at admin_standsize_ms_L with Dissolve(.5)
    admin '"축하해, 윤사랑!"'
    admin '"너는 주인님과 함께 집에 돌아갈 수 있게 되었어!"'

    hide Yun_fallinlove with None
    show Yun_huc at yun_standsize_ms with Dissolve(.5)
    voice Yunsarang_309
    yun '"그 이야기는...!"'
    player '"...내가 다른 사람이 아니라 너를 선택했다는 거야."'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_ms_L with Dissolve(.5)
    admin '"휘휘~ 뜨거운 데?"'
    '관리자의 앞에서 말하려고 하니 더 부끄러워졌다. '
    '한 손으로는 붉어진 얼굴을 가리고, 다른 한 손은 윤사랑에게 내밀었다.'
    player '"집으로 돌아가자."'

    hide Yun_huc with None
    show Yun_Sad2 at yun_standsize_bs with Dissolve(.5)
    voice Yunsarang_310
    yun '"응!"'
    '윤사랑은 내 손을 붙잡았다.'

    hide Hyeyeon_Laughter
    hide Yun_Sad2
    with Dissolve(.5)
    show Hyeyeon_Happy at yun_standsize_ms with Dissolve(.5)
    admin '"잘 가, 주인님!"'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at yun_standsize_ms with Dissolve(.5)
    admin '"다시는 보지 말자고?"'

    play sound DoorOpen2
    '관리자는 열쇠로 문을 열었다.'
    player '"누가 할 소리를!"'

    scene bg black with Dissolve(1.0)

    '열린 문 너머에는 내가 그동안 봐왔던 빌딩들이 보였다.'
    '조금 뿌연 하늘을 날아가는 흰색 비둘기, 구름을 가로지으며 나아가는 비행기.'
    '익숙한 풍경에 나도 모르게 미소가 지어졌다.'
    player '"다른 메이드랑은 인사도 못 하는 거야?"'

    voice Yunsarang_311
    yun '"그, 그런가 봐."'
    '저택에 남게 될 다른 메이드의 처분에 대해서는 관리자에게 듣지 못했다.'
    '윤사랑이 무고하다고 확신했기 때문에, 다른 메이드 중 무고한 사람이 있을 거라 생각하지는 않지만....'
    '고개를 흔들어 잡생각을 털어냈다. '
    player '"무슨 생각 하고 있어?"'

    show Yun_Normal at yun_standsize_bs with Dissolve(.5)
    '시선을 돌려 윤사랑을 바라보았다.'
    '귀여운 분홍색 머리카락, 나를 바라보는 사랑스러운 표정.'
    '집으로 돌아가는 길은 소중한 친구와 함께다.'
    '내 친구를 되찾았으니, 그걸로 충분한 거겠지?'
    '마음속으로 작은 의문을 품은 체, 윤사랑과 함께 원래 세계를 향해 나아갔다.'

    hide Yun_Normal with None

    stop music fadeout 5.0
    $renpy.pause(1.0, hard = True)

    # 엔딩 크레딧

    # 메뉴로

    '아직 호러 엔딩 관련 기믹이 존재하지 않아 엔딩크래딧 이후 호러엔딩으로 진입합니다.'
    call endcredits from _call_endcredits_1

    jump End_Sarang
    return






label select_Pink_Blue:
    hide Yun_lookout with None
    show Yun_Normal at yun_standsize_ms with Dissolve(.5)
    voice Yunsarang_269
    yun '"..."'
    voice Yunsarang_270
    yun '"제가 좋아하는 색은 붉은색이에요."'

    hide Yun_Normal with None
