label meet_Isabel:
    scene bg Myroom with Dissolve(1.5)

    player '"아무래도 아침 식사는 힘들겟지?"'
    '그저께와 어제 먹었던 아침이 눈앞에 아른거린다.'
    '오늘은 딱 한 명의 메이드와 있어야 하는 만큼, 식당에서 식사하는 건 힘들 것 같았다.'
    '먹더라도 시간대를 피해서 가는 게 예의겠지.'
    scene bg black with Dissolve(1.0)
    play sound FootStep1 fadeout 1.0
    '조금 허한 배를 모르는 척하고, 이자벨의 방으로 가던 중이었다.'
    '창 밖으로 정원을 산책 중인 이자벨이 보였다.'
    '걸음을 옮겨, 이자벨이 있는 정원으로 향했다.'
    play sound FootStep1 fadeout 1.0

    $renpy.pause(1.0)
    scene bg BG_Garden_Morning with Dissolve(1.0)
    play music Isabel_Love_Master fadein 1.0
    '멍한 표정으로 걷고 있는 이자벨은 내가 정원에 온 것도 모르는 것 같았다.'
    '그저 시간을 떼우고 있는 걸까? 나는 이자벨을 향해 소리쳤다.'
    player '"이자벨!"'
    show Isabel_pout at isabel_standsize_ms with Dissolve(.5)
    voice Isabel_255
    isabel '"..."'

    hide Isabel_pout with None
    show Isabel_nodap at isabel_standsize_ms with Dissolve(.5)
    voice Isabel_256
    isabel '"...아."'
    '나를 발견한 이자벨은 눈에 띄게 달라진 표정을 지으며 내 쪽으로 걸어왔다.'

    hide Isabel_nodap with None
    show Isabel_Happy at isabel_standsize_ms with Dissolve(.50)
    voice Isabel_257
    isabel '"좋은 아침이에요."'
    player '"응, 너도 좋은 아침이야."'
    '오늘 나누는 인사는 전혀 어색하지 않았다.'

    hide Isabel_Happy with None
    show Isabel_Laughter at isabel_standsize_ms with Dissolve(.5)
    voice Isabel_258
    isabel '"같이 걸으실래요?"'
    player '"얼마든지."'

    play sound FootStep1 fadeout 1.0

    hide Isabel_Laughter with None
    '이자벨의 걸음걸이에 맞춰 천천히 정원을 걸었다.'
    '아무런 대화도 없었지만, 이 침묵이 어색하지 않았다.'

    '온화한 미소를 지으며 꽃을 보고 있는 이자벨은 죄인과 거리가 멀어 보였다.'
    '이자벨은 어떻게 자신이 저택에 온 이유를 알아차린 걸까?'
    '솔직히 자포자기하는 심정으로 뱉었던 말이겠지만, 메이드를 선택하는 기준이 죄인이란 건 관리자에게 들었다.'
    '좀 더 자세한 이야기를 이자벨에게 듣고 싶었다.'

    player '"이자벨."'
    show Isabel_Laughter at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_259
    isabel '"무슨 일이신가요."'
    player '"어제 절벽에서 했던 이야기 기억해?"'
    player '"왜 너 스스로를 죄인이라 생각하는지 이유를 알고 싶어."'

    hide Isabel_Laughter with None
    show Isabel_panic at isabel_standsize_bs with Dissolve(.5)
    '이자벨의 얼굴에서 미소가 지워졌다.'
    '예민한 주제지만, 저택에서 보내는 날은 오늘이 마지막인 만큼 꼭 이야기 해야했다.'
    player '"관리자는 주인과 메이드가 선택되는 기준에 대해서 말한 적 없어."'
    player '"너는 네가 죄인이기 때문에 이곳에 온 것 같다고 말했지."'
    player '"어쩌다 그런 결론을 내린 거야?"'
    player '"다른 메이드는 자기가 죄인이라고 생각하지 않는 것 같던데..."'

    hide Isabel_panic with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_260
    isabel '"..."'
    '이자벨은 나를 뚫어져라 쳐다보았다.'
    '꾹 닫힌 입술은 열릴 줄 몰랐고, 그렇게 잠시동안의 시간이 지났다.'
    player '"네가 말해주지 않으면 난 몰라."'

    hide Isabel_pout with None
    show Isabel_soAngry at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_261
    isabel '"...제가 꼭 당신에게 알려줘야 하나요?"'
    player '"응. 너의 답이 꼭 필요해."'

    hide Isabel_soAngry with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_262
    isabel '"...하아."'

    hide Isabel_pout with None
    show Isabel_Sad at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_263
    isabel'"최대한 남에게 말하고 싶지 않았어요."'

    voice Isabel_264
    isabel '"그 누구에게도 말하지 않았던 거니까... 진지하게 들어주세요."'
    player '"당연하지."'
    '나와 이자벨은 정원에 있는 벤치에 앉았다.'

    hide Isabel_Sad with None
    show Isabel_lookout at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_265
    isabel '"당신은 제가 왜 스스로를 죄인이라고 정의 내렸는지, 그 이유를 알고 싶은 거죠?"'
    player '"응."'

    hide Isabel_pout with None
    show Isabel_soAngry at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_266
    isabel '"...제가 이 저택에 온 이유는, 스스로의 목숨을 포기했기 때문일 거예요."'
    voice Isabel_267
    isabel '"많은 종교에서 말하잖아요, 자살은 큰 죄라고."'
    voice Isabel_268
    isabel '"당신은 오기 전의 상황이 기억나시나요?"'

    player '"응. 학교에 가던 길에 트럭에 치였어."'
    player '"눈을 떠보니 저택의 정원이었고..."'
    player '"...유쾌한 이야기는 아니지?"'
    '나와 이자벨 사이에 어색한 침묵이 맴돌았다.'

    hide Isabel_soAngry with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_269
    isabel '"저는 오기 전에 있었던 일이 분명히 기억나요."'
    voice Isabel_270
    isabel '"호흡 곤란이 왔었어요. 그냥 두면 분명 죽었을 거예요."'
    voice Isabel_271
    isabel '"너스콜을 눌러야 하는 상황인데... 저는 누르지 않았어요."'
    voice Isabel_272
    isabel '"너무 힘들었거든요. 그동안."'

    hide Isabel_pout with None
    show Isabel_Sad at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_273
    isabel '"그냥... 다 힘들었어요. 가족들이 나 때문에 고생하는 것도 싫고..."'
    voice Isabel_274
    isabel '"괜찮아질거라던 몸은 나아질 기미가 보이지 않고..."'
    voice Isabel_275
    isabel '"아픈 건 익숙하지만 아무도 없는 낮 시간에는 무엇을 해야 하는 지 모르겠었어요."'
    voice Isabel_276
    isabel '"계속 병원에만 있어서 친구는 없어요. 같이 아파하던 아이들은 나아서 학교에 가거나, 죽어서 땅으로 가거나."'
    player '"..."'

    hide Isabel_Sad with None
    show Isabel_soAngry at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_277
    isabel '"살아야 할 이유를 모르겠더라고요."'
    voice Isabel_278
    isabel '"더는 추하게 발버둥 치고 싶지 않아서... 혼자 병실에 있었는데..."'
    player '"눈을 떠보니 이곳이었다?"'

    hide Isabel_soAngry with None
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_279
    isabel '"네. 그런 거죠."'
    hide Isabel_pout with None
    '이자벨의 담담한 목소리가 가슴을 찔렀다.'
    '병이라는 건 참 무섭다. 당사자도, 주변 사람들도 아프게 하니까.'
    '어릴 적부터 병원에 신세를 진 이자벨은 주변 사람들이 얼마나 힘들어하는지도 잘 봤었겠지.'
    '차마 내가 위로할 주제가 아니라고 생각한다.'
    '그럼에도 나는 주제넘게 입을 열었다.'
    show Isabel_pout at isabel_standsize_bs with Dissolve(.5)
    player '"너는 정말 그게 죄라고 생각해?"'
    player '"신이 없다고 생각한다며."'
    player '"네가 믿지 않는 신의 교리를 내세우며, 너 스스로를 죄인이라고 단정하는 이유가 뭐야?"'
    hide Isabel_pout with None
    show Isabel_Sad at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_280
    isabel '"... 글쎄요. 제가 낫기를 바라는 부모님의 마음을 배반한 것이 죄라고 생각했나 보죠."'
    player '"나는 죄라고 생각하지 않아."'
    player '"어쩔 수 없었던 거잖아."'

    hide Isabel_Sad with None
    '아무리 강한 사람이라도, 병에 걸리면 약해진다.'
    '이자벨이 여태껏 견딜 수 있었던 이유는 이자벨이 강한 사람이라서다.'
    '스스로가 나을 거라는 마음은 진작에 사라졌음에도, 주변 사람들의 기대 때문에 포기하지 않았던거다.'
    '난 그런 이자벨이 죄인이라 생각하지 않는다.'

    show Isabel_Sad at isabel_standsize_bs with Dissolve(.5)
    player '"너는 죄인이 아니야, 이자벨."'
    player '"그게 어떻게 죄가 될 수 있어!"'
    player '"너는 아픈 게 싫었고, 주변 사람들이 고통스럽지 않길 원했던 거잖아..."'

    hide Isabel_Sad with None
    show Isabel_panic at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_281
    isabel '"하지만..."'
    player '"삶을 포기했다던 네가 다시 돌아갈 방법을 찾는 이유가 뭐야?"'
    player '"꼬박꼬박 식사하면서, 네 몸 상태를 돌본 이유는 뭔데?"'
    player '"이곳에 오기 전까지는 죽으려고 했던 네가 다시 사는 이유가 있잖아."'
    player '"그건..."'

    voice Isabel_282
    isabel '"가족들을 다시 만나고 싶으니까."'

    '이자벨은 금방이라도 울 것 같은 얼굴로 내게 말했다.'

    voice Isabel_283
    isabel '"사실 이 저택에 오고 난 후로 몸이 눈에 띄게 좋아졌어요."'
    voice Isabel_284
    isabel '"저택에 오기 전이었다면 당신과 이렇게 산책하는 것도 힘들었을 거예요."'
    voice Isabel_285
    isabel '"소화하기 힘들다는 이유로 관리자가 차려준 밥도 먹지를 못했겠죠."'
    voice Isabel_286
    isabel '"병원 침대에 누워있던 그때보다 지금이 훨씬 나아요."'
    voice Isabel_287
    isabel '"어쩌면 여기서 계속 지내도 나쁘지 않겠다고 생각했지만..."'

    '이자벨은 잠시 뜸을 들였다. 가족들 생각으로 마음이 미워진 것 같았다.'

    voice Isabel_288
    isabel '"가족들이 걱정됐어요."'
    voice Isabel_289
    isabel '"식물인간인 저를 보고 울다 쓰러지는 건 아닌지."'
    voice Isabel_290
    isabel '"부모님의 가슴에 나을 수 없는 상처를 입힐까 봐."'

    '이자벨은 울지 않았지만, 보는 이로 하여금 그게 더 안쓰러운 마음이 들게 하였다.'
    '울지 않도록 스스로를 진정시킨 이자벨은 천천히 내게 말을 건넸다.'

    voice Isabel_291
    isabel '"계속 고민했어요. 원래 세계로 돌아갈 방법을 찾는 게 옳은 일인 걸까?"'
    voice Isabel_292
    isabel '"가족들은 제가 아프지 않다면 어디에 있든 좋아할 거예요."'
    voice Isabel_293
    isabel '"그동안 모두가 원했던걸... 가족들이 그립다는 이유 하나만으로 포기해도 될까요?"'

    player '"...포기해도 괜찮아!"'
    player '"단순히 네가 건강해지길 만을 바란 게 아니잖아."'
    player '"건강해진 몸으로 함께 일상을 보내길 바란거지."'

    voice Isabel_294
    isabel '"..."'

    player '"아무리 몸이 나아졌다지만, 계속 가족들을 그리워하면 병이 날 거야."'
    player '"너희 부모님은 네가 자신들이 보지 못하는 곳에서 아파하는 모습을 보고 싶지 않아 하실걸?"'

    '내 말이 위로되는지 이자벨의 표정이 한결 밝아졌다.'

    player '"무엇보다, 여기에 온 건 네 영혼뿐이라는 거 잊었어?"'
    player '"네가 여기서 잘 지내봤자, 네 몸은 식물인간 상태라고."'

    voice Isabel_295
    isabel '"... 그래서 아프지 않았군요."'

    '살짝 맹한 표정을 지은 이자벨은 고개를 끄덕였다.'

    voice Isabel_296
    isabel '"바, 방금 한 말은 잊어주세요."'
    voice Isabel_297
    isabel '"제가 잘못 생각했으니까..."'

    '갑자기 이자벨은 뺨을 붉히며 부끄러워했다.'
    '한껏 올라가던 감정들에 찬물이 끼얹어졌다.'

    voice Isabel_298
    isabel '"가족들이랑 이렇게 오랜 시간 동안 떨어져 있는 것도 처음이고, 낯선 곳에서 자는 것도, 또래의 사람과 오래 대화하는 것도 다 처음이라서."'
    voice Isabel_299
    isabel '"단순히 소설책을 읽는 것이 아니라 혼자서 추리해야 하는 것도 처음이고."'
    voice Isabel_300
    isabel '"처음 접하는 세계라서! 어쩔 수 없이 헷갈린 거예요!"'
    '잔뜩 변명 하던 이자벨은 갑자기 나에게 화를 냈다.'
    voice Isabel_301
    isabel '"아무튼! 저택에 계속 남아있을 생각 따위는 없어요."'
    voice Isabel_302
    isabel '"꼭 나갈 방법을 찾을 거예요."'
    voice Isabel_303
    isabel '"제 소중한 가족들에게 돌아갈 거니까."'

    '그리 말한 이자벨은 작게 한숨을 내쉬었다.'
    '우리는 한동안 대화를 하지 않고 밤하늘을 올려다보았다.'
    '낮이든, 밤이든 예쁜 별을 볼 수 있다는 건 나름 장점인 것 같았다.'

    voice Isabel_304
    isabel '"저는 당신을 좋아해요."'

    '별을 보던 이자벨은 내게 뜬금없는 말을 했다.'

    player '"응?"'

    voice Isabel_305
    isabel '"지금이 아니면 말할 때가 없을 것 같았어요."'
    voice Isabel_306
    isabel '"서재에서 봤던 주인의 기록은 모두 3일밖에 되지 않아요."'

    player '"그 말인 즉슨..."'

    voice Isabel_307
    isabel '"내일이면 당신은 저택을 떠난다는 거죠."'

    player '"...."'

    voice Isabel_308
    isabel '"반응을 보니 이미 알고 계셨던 것 같네요."'

    player '"아, 응. 관리자가 첫날에 말해줬어."'

    voice Isabel_309
    isabel '"그러니 그렇게 태평했군요..."'

    player '"그, 그래도 네 실험에 참여할 때는 진지했어!"'

    '이자벨은 살짝 붉어진 눈으로 나를 쳐다보았다.'

    player '"...진짜야."'

    voice Isabel_310
    isabel '"그런 거 의심한 적 없어요."'

    '이자벨은 새초롬한 표정으로 말했다.'

    voice Isabel_311
    isabel '"그래도 당신이 저와 같은 세계에서 와서 다행이에요."'
    voice Isabel_312
    isabel '"적어도 부모님께 제 안부를 전해줄 수 있잖아요?"'

    '내일 저택을 떠나는 건 나 혼자가 아니라는 이야기를 해주고 싶어서 입이 근질거렸다.'

    voice Isabel_313
    isabel '"꼭 직접 만나서 말할 필요는 없어요. 편지라도 한 통 보내는 걸로 충분하니까..."'

    player '"너무 걱정하지 마. 꼭 전달할 테니까."'

    voice Isabel_314
    isabel '"그리 말해주시니 안심이 되네요."'
    voice Isabel_315
    isabel '"제가 만난 주인님이 당신이라서 다행이에요."'
    voice Isabel_316
    isabel '"당신은 꽤나 다정하고, 바보 같으면서도 사랑스러워요."'
    voice Isabel_317
    isabel '"책에서 보던 영웅과는 거리가 멀지만... 평범하게 연애하기에는 딱 좋은 상대죠."'

    player '"...으응?"'

    voice Isabel_318
    isabel '"제가 원래 세계로 돌아가는 방법을 찾을 때까지 기다리세요."'
    voice Isabel_319
    isabel '"제가 당신의 연인이 될 거니까."'

    player '"아직은 연인으로 안쳐주는 거야?"'

    '내 질문에 이자벨은 피식 웃었다.'

    voice Isabel_320
    isabel '"당연하죠. 제가 춘향이도 아니고 떠날 사람하고 왜 연인 관계를 맺어요?"'

    player '"날 좋아하는 게 아니었어?"'

    voice Isabel_321
    isabel '"좋아하죠. 하지만 당신은 내일 떠나고, 저는 언제 돌아갈지 모르잖아요?"'

    player '"...나보고 기다리라며."'

    '이자벨은 \'걸렸다.\'라는 표정을 지었다.'
    '자기는 아무런 책임도 안 지고서는, 날 마냥 기다리게 하려고 했던 건가?'
    '함께 돌아갈 거라 생각하면 그리 화낼 일은 아니지만, 이자벨이 무슨 생각을 하는지 궁금했다.'

    voice Isabel_322
    isabel '"제가 당신의 다정에 기대어 심술부린 거예요."'
    voice Isabel_323
    isabel '"제게 친한 사람은 당신밖에 없지만, 당신은 그렇지 않잖아요?"'
    voice Isabel_324
    isabel '"원한다면 얼마든지 새로운 사람을 만나고, 연인도 만들 수 있겠죠."'
    voice Isabel_325
    isabel '"자유로운 당신을 구속하고 싶지만, 정식으로 연인이 될 자신은 없어서..."'

    '오늘따라 이자벨의 새로운 모습을 많이 보는 것 같았다.'
    '나는 씨익 웃으면서 이자벨에게 물었다.'

    player '"원래 세계에서 만나면, 네가 나한테 고백해줄 거야?"'

    voice Isabel_326
    isabel '"...네. 제, 제가 먼저 고백할게요!"'

    '말을 끝마친 이자벨은 자리에서 벌떡 일어나 저택 쪽으로 뛰어가기 시작했다.'

    player '"이자벨! 어디가?"'

    voice Isabel_327
    isabel '"바, 밤이 늦었으니 어서 자러 가야죠!"'

    '"여긴 항상 밤이잖아?"'
    '이자벨은 대답도 하지 않고 도망갔다.'
    '내일 진실을 알게 된 이자벨은 어떤 표정을 지을까?'



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
    show Hyeyeon_Absurd at admin_standsize_ms with Dissolve(.5)
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
    admin '"돌아갈 사람은 이미 정한거지?"'
    player '"응, 나는 이자벨과 함께 돌아갈 거야."'

    hide Hyeyeon_Normal with None
    show Hyeyeon_Laughter at admin_standsize_bs with Dissolve(.5)
    admin '"흐응~ 그게 주인님의 답이구나."'
    admin '"미리 지하실로 가있어, 주인님! 이자벨을 데려올 테니까."'

    hide Hyeyeon_Laughter with None
    scene bg BG_Underoom with Dissolve(.5)
    '눈앞에서 관리자가 사라지고, 지하실로 향했다.'
    '지하실에는 그동안 본 적 없는 문이 있었다.'
    '잠겨있는 문, 너머에 뭐가 있는지 예상은 할 수 있었다.'

    show Isabel_panic at isabel_standsize_ms with Dissolve(.5)
    voice Isabel_328
    isabel '"여긴?"'
    '관리자의 손에 이끌려 내려온 이자벨이 나를 바라보며 물었다.' # f.

    show Hyeyeon_Happy at admin_standsize_ms_L with Dissolve(.5)
    admin '"축하해, 이자벨!"'
    admin '"너는 주인님과 함께 집에 돌아갈 수 있게 되었어!"'

    hide Isabel_panic with None
    show Isabel_moving at isabel_standsize_ms with Dissolve(.5)
    voice Isabel_329
    isabel '"..."'
    player '"집으로 돌아가자."'

    hide Isabel_moving with None
    show Isabel_Laughter at isabel_standsize_ms with Dissolve(.5)
    voice Isabel_330
    isabel '"네"'
    '이자벨은 내 손을 붙잡았다.'
    hide Isabel_Laughter
    hide Hyeyeon_Happy
    with Dissolve(.5)
    show Hyeyeon_Happy at admin_standsize_ms with Dissolve(.5)
    admin '"잘 가, 주인님!"'

    hide Hyeyeon_Happy with None
    show Hyeyeon_Laughter at admin_standsize_ms with Dissolve(.5)
    admin '"다시는 보지 말자고?"'

    play sound DoorOpen2
    '관리자는 열쇠로 문을 열었다.'
    player '"누가 할 소리를!"'

    hide Hyeyeon_Laughter with None
    scene bg black with Dissolve(1.0)
    '열린 문 너머에는 내가 그동안 봐왔던 빌딩들이 보였다.'
    '해가 뜨는 새벽인지, 달과 해가 동시에 뜬 하늘은 무척이나 신비로워 보였다.'
    '조금 낯선 풍경이지만, 익숙한 건물을 보니 미소가 지어졌다.'
    player '"다른 메이드랑은 인사도 못 하는 거야?"'

    voice Isabel_331
    isabel '"그런 것 같죠?"'
    '저택에 남게 될 다른 메이드의 처분에 대해서는 관리자에게 듣지 못했다.'
    '무고한 사람은 이자벨로 확정이지만... 다른 메이드들은 대체 어떤 죄를 지었기에....'
    '고개를 흔들어 잡생각을 털어냈다. '
    player '"무슨 생각 하고 있어?"'

    show Isabel_Normal at isabel_standsize_ms with Dissolve(.5)
    '시선을 돌려 이자벨을 바라보았다.'
    '미소를 지은 이자벨은 내 손을 좀 더 꽉 쥐며 말햇다.'
    hide Isabel_Normal with None
    show Isabel_Laughter at isabel_standsize_bs with Dissolve(.5)
    voice Isabel_332
    isabel '"돌아가서도 당신과 이야기 할 수 있으면 좋겠다는 생각을 했어요."'
    player '"나도... 그곳에서도 너와 친하게 지내고 싶어."'
    player '"메이드와 주인님이 아닌, 친구로써 말이야."'
    '나와 이자벨은 잡은 손을 놓지 않은체, 원래 세계를  향해 걸어갔다.'
    hide Isabel_Laughter with None
    stop music fadeout 5.0
    $renpy.pause(1.0)
    # 엔딩 크레딧
    # 메뉴로


    '아직 호러 엔딩 관련 기믹이 존재하지 않아 엔딩크래딧 이후 호러엔딩으로 진입합니다.'
    call endcredits from _call_endcredits_2


    jump End_Isabel


    pass
