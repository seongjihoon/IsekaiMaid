
label meet_Elice:

    scene bg Myroom with Dissolve(1.5)
    player '"아무래도 아침 식사는 힘들겠지?"'
    '그저께와 어제 먹었던 아침이 눈앞에 아른거린다.'
    '오늘은 딱 한 명의 메이드와 있어야 하는 만큼, 식당에서 식사하는 건 힘들 것 같았다.'
    '먹더라도 시간대를 피해서 가는 게 예의겠지.'
    '조금 허한 배를 모르는 척하고, 엘리스의 방으로 갔다.'
    scene bg black with Dissolve(1.0)
    play sound FootStep1 fadeout 1.0

    scene bg BG_Corridor_2 with Dissolve(1.5)
    play music Elicetheme fadein 1.0
    player '"엘리스, 있어?"'
    '안에서는 아무런 소리도 들리지 않았다.'
    '혹시 자고 있는 건 아닐까?'
    '기다려볼까? 잠시 고민하다 고개를 저었다.'
    '저택에서 보내는 마지막 날을 이리 허무하게 보낼 수 없다.'
    player '"들어갈게!"'

    scene bg BG_Maidroom with Dissolve(1.5)
    '마음을 굳게 먹고 엘리스의 방에 들어갔지만, 정작 방에는 아무도 없었다.'
    player '"어디 간거야...?"'

    scene bg BG_Corridor with slideawayright
    $renpy.pause(1.0, hard = True)
    scene bg BG_Library with slideawayright
    '엘리스의 방에서 나와 저택 이곳저곳을 돌아다녔다.'   # add. 연출 변경 의뢰
    '그러다 엘리스를 발견한 건 서재였다.'              #
    '엘리스보단 이자벨이 서재를 더 자주간다 생각했는데...'
    scene bg BG_Adimroom with Dissolve(1.5)
    player '"여기 있었구나."'
    show Elice_Surprised_2 at elice_standsize_ms with Dissolve(.5)
    voice Elice_235
    elice '"...!"'
    '엘리스는 무척이나 놀란 눈으로 나를 바라봤다.'

    hide Elice_Surprised_2 with None
    show Elice_Gladness at elice_standsize_ms with Dissolve(.5)
    voice Elice_236
    elice '"슬슬 깨우러 갈 생각이었는데."'
    voice Elice_237
    elice '"알아서 일어날 줄이야...'
    player '"내가 일찍 일어난게 그리 놀랄 일이야?"'

    hide Elice_Gladness with None
    show Elice_Normal at elice_standsize_ms with Dissolve(.5)
    '억울한 마음에 투덜거리자, 엘리스의 미소가 진해졌다.'
    player '"무슨 책 읽고 있었어?"'

    hide Elice_Normal with None
    show Elice_Gladness_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_238
    elice '"로맨스 소설."'

    hide Elice_Gladness_2 with None
    show Elice_Happy_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_239
    elice '"전에는 읽어본 적 없어서 한 번 읽어봤는데 재밌더라고."'

    hide Elice_Happy_2 with None
    show Elice_Ignore_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_240
    elice '"이해는 가지 않지만... 멀쩡하던 사람이 갑자기 바보가 되는게 웃기더라."'

    hide Elice_Ignore_2 with None
    show Elice_Happy at elice_standsize_bs with Dissolve(.5)
    '웃고 있는 엘리스의 얼굴은 또래 소녀와 비슷해보였다.'
    '자세히 얼굴을 들여다보면, 엘리스와 나의 나이차는 그렇게 크지 않아보였다.'
    '훨씬 연상이라 생각했던 이유는... 엘리스가 가지고 있는 아우라가 있어서겠지.'

    hide Elice_Happy with None
    show Elice_Pudency at elice_standsize_bs with Dissolve(.5)
    voice Elice_241
    elice '"넌 사랑을 해본 적 있어?"'
    player '"글쎄... 사랑을 해본 적은 없지만 연애는 해본 적 있어."'

    hide Elice_Pudency with None
    show Elice_Committed_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_242
    elice '"..."'

    hide Elice_Committed_2 with None
    show Elice_Committed at elice_standsize_bs with Dissolve(.5)
    voice Elice_243
    elice '"뭐?"'
    '엘리스의 얼굴이 순식간에 차가워졌다.'
    '새벽 특유의 몽글몽글하던 분위기가 싹 사라지고, 시베리아의 폭풍이 나를 감쌌다.'

    hide Elice_Committed with None
    show Elice_Committed_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_244
    elice '"너같은게, 연애를 해봤다고?"'
    player '"어... 응... "'

    hide Elice_Committed_2 with None
    show Elice_Strong_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_245
    elice '"네까짓게... 다른 사람이랑 연애를..."'

    hide Elice_Strong_2 with None
    show Elice_Angry_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_246
    elice '"..."'
    '말이 없는 엘리스는 무척이나 무서웠다. '
    '언제 기분이 풀리까 나는 엘리스의 눈치만 보고 있었다.'

    hide Elice_Angry_2 with None
    show Elice_Angry at elice_standsize_bs with Dissolve(.5)
    voice Elice_247
    elice '"지금은?"'

    hide Elice_Angry with None
    show Elice_Strong_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_248
    elice '"지금도 누군가와 사귀고 있어?"'
    player '"아니! 지금은 헤어졌어."'

    hide Elice_Strong_2 with None
    show Elice_Angry_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_249
    elice '"왜 헤어졌지?"'
    '나는 잠시 고민을 했다.'
    '진지한 관계가 아니었기 때문에, 그 애에 대한 기억은 별로 없다.'
    player '"좋아하지 않아서 그랬나봐."'
    player '"우정을 사랑으로 착각 했거든."'

    hide Elice_Angry_2 with None
    show Elice_Surprised at elice_standsize_bs with Dissolve(.5)
    voice Elice_250
    elice '"흐음..."'
    player '"사랑을 해보긴 했지만, 끝이 좋았던 적은 없어."'
    player '"누구를 좋아 했는지 이젠 기억도 안나."'
    '엘리스는 한결 부드러운 표정으로 나를 바라 봤다.'

    hide Elice_Surprised with None
    show Elice_Pudency at elice_standsize_bs with Dissolve(.5)
    voice Elice_251
    elice '"...사랑을 한다는 건, 어떤 느낌이야?"'
    player '"음..."'

    hide Elice_Pudency with None
    '굉장히 어려운 질문이다.'
    '사랑에는 여러 종류가 있었고, 사람마다 사랑을 하는 방법이 달랐다.'
    '나조차도 항상 같은 사랑을 한건 아니었으니까.'
    show Elice_Pudency at elice_standsize_bs with Dissolve(.5)
    player '"잘모르겠지만, 항상 상대방이 보고싶고."'
    player '"다른 사람이랑 이야기하며 웃고있는걸 보면 질투가 나고."'
    player '"언제나 내 옆에 있어주길 바라는거 아닐까?"'

    hide Elice_Pudency with None
    show Elice_Difficulty at elice_standsize_bs with Dissolve(.5)
    voice Elice_252
    elice '"질투...?"'
    voice Elice_253
    elice '"너도 질투라는걸 해?"'
    '웃음이 터져 나왔다.'
    player '"당연하지, 나도 사람인데."'
    player '"좋아하는 사람이 다른 사람과 있는걸 보면 무척이나 질투나."'
    player '"내가 여기 있는데 왜 다른 사람이랑 이야기 하는 건지."'

    player '"화가 나기도 하고, 대화 상대에게 터무니 없는걸 따지고 싶기도 하고."'
    player '"나는 그렇더라."'

    hide Elice_Difficulty with None
    show Elice_Coloration at elice_standsize_bs with Dissolve(.5)
    '엘리스는 아무말 없이 나를 바라보았다.'

    hide Elice_Coloration with None
    show Elice_Coloration_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_254
    elice '"그걸 아는 놈이..."'
    player '"응?"'

    hide Elice_Coloration_2 with None
    show Elice_Contempt_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_255
    elice '"하아..."'

    hide Elice_Contempt_2 with None
    show Elice_Contempt at elice_standsize_bs with Dissolve(.5)
    voice Elice_256
    elice '"어쩌다 이런놈을 좋아하게 돼서..."'
    player '"으응?"'
    stop music fadeout 2.0

    hide Elice_Contempt with None
    show Elice_Angry_2 at elice_standsize_bs with Dissolve(.5)
    '엘리스는 다시 싸늘한 눈으로 나를 봤다.'

    play music emotional_1 fadein 2.0
    '내가 무엇을 잘못했는지 다시한번 생각해 봤다.'
    '다른 메이드와 있을 때 느껴지던 따가운 눈빛'
    '그 눈빛의 주인이 엘리스였구나.'
    player '"엘리스, 나를 좋아해?"'

    hide Elice_Angry_2 with None
    show Elice_Surprised at elice_standsize_bs with Dissolve(.5)
    voice Elice_257
    elice '"..."'
    hide Elice_Surprised with None
    show Elice_Contempt at elice_standsize_bs with Dissolve(.5)
    voice Elice_258
    elice '"그래, 인정하기 싫지만 널 좋아해"'
    '영화 처럼 귀에서 종소리가 들리는 일은 없었다.'
    '하지만 웃음이 비실 새어나왔다.'
    '웃지 않을 수가 없었다.'
    '그 고고한 황제 폐하께서 나를 좋아한다고 하시지 않는가.'

    hide Elice_Contempt with None
    show Elice_Pudency_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_259
    elice '"자,잠시 산책이라도 할까?"'

    play sound FootStep1 fadeout 1.0
    hide Elice_Pudency_2 with Dissolve(1.0)
    '엘리스는 급한 걸음으로 서재 밖으로 나갔다.'
    '붉어진 얼굴이 무척이나 귀여웠다.'
    '부끄러워 하는 거겠지.'
    '나는 엘리스를 쫒아 정원으로 갔다.'

    stop music fadeout 2.0
    play sound FootStep1 fadeout 1.0
    scene bg black with Dissolve(1.0)
    scene bg BG_Garden_Morning with Dissolve(1.5)
    show Elice_Normal at elice_standsize_ms with Dissolve(.5)
    play music emotional_2 fadein 2.0
    '찬 바람에 열기가 식었는지 엘리스는 평소와 같은 얼굴로 나를 보았다.'
    '나는 엘리스와 나란히 서서 걸었다.'

    hide Elice_Normal with None
    show Elice_Contempt at elice_standsize_bs with Dissolve(.5)
    voice Elice_260
    elice '"내가 너를 사랑하는게 얼마나 말이 안되는 일인 줄 알아?"'

    hide Elice_Contempt with None
    show Elice_Surprised at elice_standsize_bs with Dissolve(.50)
    voice Elice_262
    elice '"왕족으로 태어났던 소녀는 살아남기 위해 오빠를 죽였어."'

    hide Elice_Surprised with None
    show Elice_Angry_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_263
    elice '"그리고 황제가 되었지."'

    hide Elice_Angry_2 with None
    show Elice_Difficulty_2 at elice_standsize_bs with Dissolve(.50)
    voice Elice_264
    elice '"역대 황제들 중 가장 뛰어났던 소녀는"'

    hide Elice_Difficulty_2 with None
    show Elice_Strong_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_265
    elice '"동료들에게 배신 당하고 낯선 장소에 오게 되었어."'
    voice Elice_266
    elice '"복수심을 불태우고 있어도 모자란 시간에..."'

    hide Elice_Strong_2 with None
    show Elice_Contempt_2 at elice_standsize_bs with Dissolve(.50)
    '엘리스는 힐끔 나를 바라보았다.'
    hide Elice_Contempt_2 with None
    show Elice_coldsmiley at elice_standsize_bs with Dissolve(.50)
    voice Elice_267
    elice '"평범한 사람을 만나 사랑에 빠졌지."'

    hide Elice_coldsmiley with None
    show Elice_Laughter at elice_standsize_bs with Dissolve(.5)
    voice Elice_268
    elice '"우리의 이야기를 소설로 쓰면, 아무도 믿지 않을거야."'
    player '"...그건 그래."'

    hide Elice_Laughter with Dissolve(.5)
    '엘리스의 말은 틀린 게 없었다.'
    '나도 이런 일을 써둔 소설을 보면 말이 되는지 따질거다.'
    '고작 3일의 시간 동안 사랑에 빠진다니.'
    '가족을 죽이고, 동료에게 배신당한, 인간불신증에 걸려도 이상하지 않을 황제가...'
    '나처럼 평범한 사람과 사랑에 빠지다니.'
    '소설보다 더 말이 안되는 일이 일어나고 있다는 사실이 무척이나 우스웠다. '
    '\'내 인생의 주인공은 나.\' 라는 말을 들어도 공감 못했던 나인데...'     # f. 오타 여부 확인
    '이번에는 로맨스 소설의 주인공이 된 것 같았다.'
    show Elice_Pudency at elice_standsize_bs with Dissolve(.50)
    voice Elice_269
    elice '"지금같은 상황이니까 사랑할 수 있는거지."'

    hide Elice_Pudency with None
    show Elice_Pudency_2 at elice_standsize_bs with Dissolve(.50)
    voice Elice_270
    elice '"원래 세상으로 돌아가면 절대로 지금처럼 사랑할 수 없을 거야."'
    player '"왜 그렇게 생각해?"'
    '엘리스는 단호하게 말했다.'

    hide Elice_Pudency_2 with None
    show Elice_Difficulty at elice_standsize_bs with Dissolve(.50)
    voice Elice_271
    elice '"너랑 내가 살아온 환경이 그만큼 다르니까."'
    hide Elice_Difficulty with Dissolve(.5)
    '살기 위해서는 오빠를 죽였어야 하는 엘리스.'
    '평범한 가정에서 부모님께 사랑 받으며 자란 나.'
    '엘리스를 만나기 전이라면 분명 동의했을거다.'
    '하지만... 지금의 나는 엘리스를 사랑하고 있다.'
    '쉽게 연인을 포기하고 싶지 않았다.'

    show Elice_Difficulty at elice_standsize_ms with Dissolve(.5)
    player '"우리가 로맨스 소설의 주인공이라면, 시련 몇 개쯤은 있어야 하지 않겠어?"'
    player '"평생 만날 일 없는 사람을 만나서 사랑하게 되었는데, 그 사람을 이해하는게 어려워봤자 얼마나 어렵겠어."'
    player '"네가 날 이해할 수 없다면 내가 널 이해하도록 노력할게."'
    player '"나도 널 좋아하니까."'
    '로맨스 소설의 흔한 클리셰는 사랑으로 모든 이겨낸다는 점이 있다.'

    hide Elice_Difficulty with None
    show Elice_coldsmiley_2 at elice_standsize_ms with Dissolve(.5)
    '아무런 근거도 없이 사랑으로 모든 걸 이길 수 있을거라 말하는 나를 보며 엘리스는 웃었다.'

    hide Elice_coldsmiley_2 with None
    show Elice_Laughter at elice_standsize_ms with Dissolve(.50)
    voice Elice_272
    elice '"왜 사랑에 빠지면 바보가 되는 지 알 것 같아."'

    hide Elice_Laughter with None
    show Elice_Laughter_2 at elice_standsize_ms with Dissolve(.5)
    voice Elice_273
    elice '"믿을 수 있는 이유가 하나도 없는 너의 말을 믿고 싶어져 버렸거든."'
    player '"사랑은 자기를 부정해야지 할 수 있거든."'
    '똑똑한 사람은 바보가 되고, 용감한 사랑은 겁쟁이가 되고.'
    '욕심쟁이는 헌신적이게 되고, 다른 사람을 먼저 생각하던 사람은 나만 생각하게 되어버리고.'
    '나를 내가 아니게 만드는 것이 바로 사랑이다.'

    hide Elice_Laughter_2 with None
    show Elice_Love at elice_standsize_ms with Dissolve(.5)
    voice Elice_274
    elice '"평범한 사람은 질색이라고 생각했는데..."'
    player '"나도 황제 폐하같은 권력자는 별로 좋아하지 않아."'

    hide Elice_Love with None
    show Elice_Love_2 at elice_standsize_ms with Dissolve(.5)
    voice Elice_275
    elice '"네가 원하는 건 무엇이든 이루어줄 수 있는데도?"'
    player '"내가 원하는 건 내 힘으로 이뤄야지 의미 있잖아."'
    '장난스럽게 웃는 엘리스에게 가까이 다가갔다.'

    hide Elice_Love_2 with None
    show Elice_Pudency at elice_standsize_bs with Dissolve(.5)
    voice Elice_276
    elice '"황제의 마음을 얻는 거, 아무나 못하는 거야."'

    hide Elice_Pudency with None
    show Elice_Laughter_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_277
    elice '"내가 너에게 무엇을 주던, 다 너의 힘으로 이룬거지."'
    '수줍은 미소로 하는 말 치고는, 꽤나 속세에 찌든 말이다.'
    '폭군이 되지 않도록 조심하라는 말을 해주고 싶은데, 그냥 웃음이 나왔다.'
    player '"나는 그냥... 너랑 함께 있는 게 제일 좋아."'
    player '"부귀영화가 없어도 함께 있는 시간이 긴게 좋아."'

    hide Elice_Laughter_2 with None
    show Elice_Laughter at elice_standsize_bs with Dissolve(.5)
    '내 말을 들은 엘리스는 크게 소리내어 웃었다.'
    '무엇이 웃긴 줄 몰랐기 때문에, 나는 어리둥절한 표정으로 엘리스만 보고 있었다.'

    hide Elice_Laughter with None
    show Elice_Laughter_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_278
    elice '"푸하하. 정말... 너를 보고 있으면 심심한 줄 모르겠어."'

    hide Elice_Laughter_2 with None
    show Elice_Impression at elice_standsize_bs with Dissolve(.5)
    voice Elice_279
    elice '"그런 말을 의도하지 않고 하다니..."'

    hide Elice_Impression with None
    show Elice_Impression_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_280
    elice '"첩에게 놀아난 폭군의 심정을 알 것 같아."'
    player '"...무슨 뜻이야?"'
    '내가 물러나지 않고 계속 물어보니, 그제서야 엘리스가 대답해줬다.'

    hide Elice_Impression_2 with None
    show Elice_Ignore_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_281
    elice '"물질이든, 권력이든, 명예든 욕심 가득한 눈으로 날 보던 사람들만 대하다가..."'

    hide Elice_Ignore_2 with None
    show Elice_Ignore at elice_standsize_bs with Dissolve(.5)
    voice Elice_282
    elice '"그런 것 다 필요없으니 옆에 있어달라는 사람을 보면 무슨 기분이 들겠어?"'

    hide Elice_Ignore with None
    show Elice_Gladness_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_283
    elice '"무엇이든 다 이루어주고 싶어지지."'
    player '"아..."'

    hide Elice_Gladness_2 with None
    show Elice_Laughter_2 at elice_standsize_bs with Dissolve(.5)
    '엘리스는 피식 웃었다.'

    hide Elice_Laughter_2 with None
    show Elice_Impression at elice_standsize_bs with Dissolve(.5)
    voice Elice_284
    elice '"정말 아무것도 모르는구나."'

    voice Elice_285
    elice '"좀 부족해도 괜찮아."'

    hide Elice_Impression with None
    show Elice_Impression_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_286
    elice '"내가 옆에서 잘 지켜주면 되는 일이잖아?"'
    '금방이라도 원래 세계로 돌아갈 사람처럼 나중을 말했다.'
    '내가 내일 돌아간다는 걸, 엘리스는 모를 텐데.'
    player '"엘리스, 만약 원래 세계로 돌아가지 못한다면..."'
    player '"내가 사는 세계로 함께 간다면 어쩔 거야?"'

    hide Elice_Impression_2 with None
    show Elice_Ignore_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_287
    elice '"...글쎄. 너의 세계라면 내가 너에게 해줄 수 있는 게 적겠네."'

    hide Elice_Ignore_2 with None
    show Elice_Gladness_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_288
    elice '"그 세계에는 왕도 그리 강하지 않고, 비교적 평화로운 세계라고 했지?"'

    hide Elice_Gladness_2 with None
    show Elice_Ignore at elice_standsize_bs with Dissolve(.5)
    '엘리스는 하늘을 바라보며 내가 말한 세상을 상상하는 것 같았다.'

    hide Elice_Ignore with None
    show Elice_Impression at elice_standsize_bs with Dissolve(.50)
    voice Elice_289
    elice '"여행을 해보고 싶어."'

    hide Elice_Impression with None
    show Elice_Impression_2 at elice_standsize_bs with Dissolve(.5)
    voice Elice_290
    elice '"황성 밖을 나가본 적이 별로 없거든."'
    player '"...바다를 보러가자."'
    player '"물에 뛰어들어서 실컷 놀고, 맛있는 것도 먹고."'

    hide Elice_Impression_2 with None
    show Elice_Laughter at elice_standsize_bs with Dissolve(.5)
    voice Elice_291
    elice '"내 입맛은 고급스러운데. 맞출 수 있겠어?"'
    player '"...노력은 해볼게."'

    hide Elice_Laughter with None
    show Elice_Laughter_2 at elice_standsize_bs with Dissolve(.50)
    '진중한 표정을 지은 날 보고 엘리스는 웃었다.'

    hide Elice_Laughter_2 with None
    show Elice_Love at elice_standsize_bs with Dissolve(.5)
    voice Elice_292
    elice '"너를 믿어볼테니까... 이번엔 나를 배신하지마."'
    player '"응. 난 절대로 널 배신하지 않아."'

    play sound FootStep1 fadeout 1.0
    hide Elice_Love with Dissolve(1.0)
    '엘리스의 손을 잡고 다시 저택 안으로 들어갔다.'
    '엘리스를 무고한 사람이라고 단정 짓기는 애매했다.'
    '엘리스는 자신의 오빠를 죽였으니까.'
    '하지만 오빠를 죽이지 않으면, 엘리스가 죽는 걸?'
    '권력과 죄는 매우 가까이에 있고, 정도의 차이는 있어도 나는 엘리스의 죄를 어쩔 수 없었다고 말할 수 있다.'
    '사람을 한 명이라도 죽였으면, 무조건 죄인이라고 말하는 사람도 있겠지만....'
    '나는 그런 성인 군자가 아니다.'
    '좋아하는 사람을 위해 이것저것 핑계를 만드는... 비열한 놈이다.'
    '그걸로 괜찮지 않을까?'
    '나는 엘리스를 좋아하니까.'
    stop music fadeout 2.0
    $ renpy.pause(2.0, hard = True)

    scene bg Myroom with Dissolve(1.5)
    play music serious_little
    '오늘도 나를 깨우러 오는 메이드는 없었다.'
    play sound standup

    '처음 이곳에 왔을 때와 같은 옷을 입고 방 밖으로 나오니 관리자가 나를 기다리고 있었다.'
    scene bg black with Dissolve(1.0)
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5)
    admin '"좋은 아침이야 주인님! 드디어 집으로 돌아가네, 기쁘지?"'
    player '"응. 더이상 네 얼굴을 보지 않아도 된다는 점에서 특히."'
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Absurd at admin_standsize_ms with Dissolve(.50)
    admin '"그런 말로 아쉬움을 숨기려고 해도 소용없어."'
    hide Hyeyeon_Absurd with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5)
    admin '"나는 유능해서 다 알아보거든~"'
    player '"뭐?"'
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(.5)
    show Hyeyeon_Laughter at admin_one_jump_bs with None
    admin '"나랑 헤어지는 게 무척 아쉽지? 응?"'
    player '"그럴 리가."'
    '갑자기 치근대는 관리자를 밀어냈다.'
    hide Hyeyeon_Laughter with None
    show Hyeyeon_Normal at admin_standsize_bs with Dissolve(.5)
    admin '"함께 돌아갈 사람은 정했어?"'
    admin '"저 잔인한 메이드들 사이에서 주인님이 무고하다고 생각하는 사람은 누구야?"'
    '더는 고민할 필요도 없다. 답은 정했으니까.'
    player '"나는 엘리스 함께 돌아갈 거야."'
    hide Hyeyeon_Normal with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.50)
    admin '"흐응~ 그게 주인님의 답이구나."'
    admin '"미리 지하실로 가있어, 주인님! 엘리스을 데려올 테니까."'
    player '"원래 이 타이밍에는 내가 맞았는지 틀렸는지 알려주지 않아?"'
    hide Hyeyeon_Laughter with None
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
    hide Hyeyeon_Normal with None
    scene bg BG_Underoom with Dissolve(2.0)
    '눈앞에서 관리자가 사라지고, 지하실로 향했다.'
    '지하실에는 그동안 본 적 없는 문이 있었다.'
    '잠겨있는 문, 너머에 뭐가 있는지 예상은 할 수 있었다.'

    show Elice_Difficulty_2 at elice_standsize_ms_L with Dissolve(.5)
    voice Elice_293
    elice '"... 여긴?"'
    '관리자의 손에 이끌려 내려온 엘리스가 나를 바라보며 물었다.'

    show Hyeyeon_Happy at admin_standsize_ms_R with Dissolve(.50)
    admin '"축하해, 엘리스!"'
    admin '"너는 주인님과 함께 주인님의 세상으로 갈거야!"'

    hide Elice_Difficulty_2 with None
    show Elice_Contempt_2 at elice_standsize_ms_L with Dissolve(.5)
    voice Elice_294
    elice '"그 이야기는...!"'
    player '"...내가 다른 사람이 아니라 너를 선택했다는 거야."'

    hide Elice_Contempt_2 with None
    show Elice_Pudency_2 at elice_standsize_ms_L with Dissolve(.5)
    voice Elice_295
    elice '"당연한 결과네."'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_ms_R with Dissolve(.5)
    admin '"휘휘~ 뜨거운 데?"'
    '관리자의 앞에서 말하려고 하니 더 부끄러워졌다.'
    hide Elice_Pudency_2
    hide Hyeyeon_Laughter
    with Dissolve(1.0)

    show screen Mini_Scene(elice_Hand) with Dissolve(.5)
    '한 손으로는 붉어진 얼굴을 가리고, 다른 한 손은 엘리스에게 내밀었다.'

    hide screen Mini_Scene with Dissolve(.5)
    player '"여행을 떠날 준비는 됐어?"'

    show Elice_Impression at elice_standsize_ms_L with Dissolve(.5)
    voice Elice_296
    elice '"그래."'
    '엘리스는 내 손을 붙잡았다.'

    hide Hyeyeon_Laughter with None
    show Hyeyeon_Happy at admin_standsize_ms_R with Dissolve(.5)
    admin '"잘 가, 주인님!"'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_ms_R with Dissolve(.5)
    admin '"다시는 보지 말자고?"'

    play sound DoorOpen2
    '관리자는 열쇠로 문을 열었다.'
    player '"누가 할 소리를!"'

    # hide Elice_Impression
    # hide Hyeyeon_Laughter
    # with Dissolve(1.0)
    scene bg BG_Door_Open with Dissolve(2.0)

    show screen Mini_Scene(Elice_Ending, 0.5, 0.1) with Dissolve(.5)
    '열린 문 너머에는 집에서 멀리 떨어져있는 미술관이 보였다.'
    '푸르스름한 새벽 밤 하늘에서 빛나는 별.'
    '낯설고, 익숙한 풍경에 나도 모르게 미소를 지었다.'
    hide screen Mini_Scene with Dissolve(.5)
    player '"다른 메이드랑은 인사도 못 하는 거야?"'

    show Elice_Coloration_2 at elice_standsize_ms with Dissolve(.5)
    voice Elice_297
    elice '"굳이 인사를 할 이유도 없지."'
    '저택에 남게 될 다른 메이드의 처분에 대해서는 관리자에게 듣지 못했다.'
    '최대한 좋은 방향으로 생각해서 엘리스는 무고하다고 생각했지만, 만약 엘리스가 아닌 다른 메이드가 무고했다면...'
    '고개를 흔들어 잡생각을 털어냈다. '
    player '"무슨 생각 하고 있어?"'
    hide Elice_Coloration_2 with Dissolve(.5)
    # add. 엘리스 이미지
    show screen Mini_Scene(elice_seeing) with Dissolve(.5)
    '시선을 돌려 엘리스를 바라보았다.'
    '엘리스의 푸른 눈동자와 눈이 마주쳤다.'
    '집에 돌아가는 길, 함께하는 사람은 사랑하는 연인이다.'
    '나는 연인을 위해서 타인을 희생할 수 있는 사람이었던가?'
    '마음속으로 죄책감을 가지고, 엘리스와 함께 원래 세계를 향해 나아갔다.'

    hide screen Mini_Scene with Dissolve(.5)
    # minus 엘리스 이미지
    stop music fadeout 5.0
    $renpy.pause(1.0)
    #엔딩 크레딧

    '아직 호러 엔딩 관련 기믹이 존재하지 않아 엔딩크래딧 이후 호러엔딩으로 진입합니다.'
    call endcredits from _call_endcredits_3

    jump End_Elice
    #메뉴로
    return
