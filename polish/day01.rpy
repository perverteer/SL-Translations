# game/day01.rpy:10
translate polish day01_cf4be568:

    # m "Oh, hi [p_name]! You're right on time."
    m "Oh, [p_name]! Cześć! Jesteś w samą porę."

# game/day01.rpy:13
translate polish day01_0084a533:

    # p "{i}(Damn, it has been so long. Should I just call her mom, or use her name?)"
    p "Cześć mamo. Dobrze znowu Cię widzieć."

    menu:
        "Hug her":

            scene day01_hug_m with dissolve

            p "Naprawdę się cieszę, że pozwoliłaś mi tu zamieszkać. Tęskniłem za Tobą mamo."

            jump enter_apartment
        "Kiss her":

            scene day01_kiss_m with dissolve

            p "{b}*Cmok*{/b} Kocham Cię mamo!"

            jump enter_apartment


# game/day01.rpy:31
translate polish day01_2fa97392:

    # p "I'm really glad you're letting me stay. I've missed you, [m_name]."
    p "Naprawdę się cieszę, że pozwoliłaś mi tu zamieszkać. Tęskniłem za Tobą mamo."

# game/day01.rpy:38
translate polish day01_a0838d85:

    # p "{b}*Kiss*{/b} Love you, [m_name]!"
    p "{b}*Cmok*{/b} Kocham Cię mamo!"

# game/day01.rpy:45
translate polish enter_apartment_91967824:

    # m "That's sweet! Let's go inside and I'll show you your room."
    m "Jesteś słodki! Chodźmy do środka, pokażę Ci Twój pokój."

# game/day01.rpy:51
translate polish enter_apartment_ab8e699c:

    # m "Your youngest sister is also home, she's very eager to meet you!"
    m "Twoja najmłodsza siostra też jest w domu, nie może się doczekać, żeby Cię spotkać!"

# game/day01.rpy:56
translate polish enter_apartment_1a962617:

    # p "({i}My youngest sister... That would be...)"
    p "({i} Moja najmłodsza siostra... Czyli...)"
    p "({i}Rachel, tak miała na imię.)"

    scene day01_p_room_day_m with dissolve

    m "Więc, to będzie Twój pokój. Nie jest duży, ale mam nadzieję, że Ci się spodoba."
    p "Dzięki mamo, jest świetny."
    m "Łazienka jest w dole korytarza. Jeśli chcesz, możesz pójść się trochę odświeżyć."
    m "No dobrze. Zostawię Cię samego, żebyś mógł się rozpakować i zadomowić."
    "{i}Słyszysz odgłosy dochodzące z korytarza."

    if game.is_special:
        r "Czy to on mamo?"
    else:
        r "Czy to on mamo?"

    scene day01_p_room_day_m_r with dissolve

    m "Tak kochanie, to właśnie [p_name]. Gdzie są Twoje maniery?"
    r "Oh, no tak. Cześć, jestem Rachel!"

    if game.is_special:
        p "({i}Wow. Rachel wyrosła. Wygląda bardzo ładnie! Małżeństwo mamy i taty może nie było udane, ale połączenie ich genów wręcz przeciwnie.)"
    else:
        p "({i}Wow. Rachel wygląda bardzo ładnie!)"

    menu:
        "Hug her":
            scene day01_p_room_hug_r with dissolve

            p "Miło Cię poznać Rachel."

            jump day01_leave_p_room
        "Kiss her":

            scene day01_p_room_kiss_r with dissolve

            p "{b}*Cmok*{/b} Cześć Rachel!"

            jump day01_leave_p_room


# game/day01.rpy:107
translate polish day01_leave_p_room_33cb256e:

    # p "{i}(She smells nice too.)"
    p "{i}(Pachnie też ładnie.)"

# game/day01.rpy:108
translate polish day01_leave_p_room_c1e2490f:

    # r "Well, I'm sure we'll have lots to talk about."
    r "Cóż, jestem pewna, że będziemy mieli o czym rozmawiać."

# game/day01.rpy:111
translate polish day01_leave_p_room_11976dd9:

    # r "And you have to see your other sisters of course, but they aren't home at the moment. And..."
    r "I oczywiście musisz jeszcze poznać resztę swoich sióstr, ale nie ma ich teraz w domu. I..."

# game/day01.rpy:115
translate polish day01_leave_p_room_95f96816:

    # m "Let's give [p_name] some time to unpack [r_name]. I'm sure he's tired from his trip."
    m "Dajmy Twojemu bratu trochę czasu, żeby się rozpakował Rachel. Jestem pewna, że jest zmęczony po podróży."

# game/day01.rpy:116
translate polish day01_leave_p_room_ae1146ed:

    # r "Right. Of course."
    r "No tak. Oczywiście."

# game/day01.rpy:117
translate polish day01_leave_p_room_e3959a5f:

    # m "See you at dinner, [p_name]!"
    m "Dobrze, [p_name]. No to widzimy się na kolacji!"

# game/day01.rpy:127
translate polish empty_p_room_c6556e2b:

    # p "{i}(Well. That went all right, I think.)"
    p "{i}(Cóż. Myślę, że poszło nie najgorzej.)"

# game/day01.rpy:128
translate polish empty_p_room_15204d95:

    # p "{i}(I wonder why dad was so adamant about avoiding any contact with them. Both [m_name] and [r_name] seem so friendly and understanding.)"
    p "{i}(Ciekawe dlaczego tata aż tak bardzo unikał z nimi kontaktu. Zarówno Susan jak i Rachel wydają się być bardzo przyjazne i wyrozumiałe.)"

# game/day01.rpy:129
translate polish empty_p_room_26e7b5d2:

    # p "{i}(They're really good-looking too...)"
    p "{i}(Są też bardzo ładne...)"

# game/day01.rpy:131
translate polish empty_p_room_6350e699:

    # p "{i}(I'd better unpack.)"
    p "{i}(Lepiej się rozpakuję.)"

# game/day01.rpy:149
translate polish day01_p_room_action_menu_0fdbe80f:

    # p "{i}(I wonder where my other sisters are. From what I understood, both of them are still living here as well.)"
    p "{i}(Ciekawe gdzie są moje pozostałe siostry. Z tego co zrozumiałem, obie dalej tu mieszkają.)"
    p "{i}(Pamiętam, że Bella i ja zawsze się kłóciliśmy. Jest trochę starsza ode mnie i kiedy rodzice byli jeszcze razem potrafiła być czasami naprawdę wredna.)"
    p "{i}(Moja najstarsza siostra Liza zawsze była najbardziej odpowiedzialna z całej naszej czwórki. Ciekawe, czy to się zmieniło.)"
    jump day01_p_room_action_menu


# game/day01.rpy:180
translate polish day01_p_room_action_menu_4da67f69:

    # p "{i}(Damn. I needed that.)"
    p "{i}(Cholera. Tego mi było trzeba.)"

# game/day01.rpy:181
translate polish day01_p_room_action_menu_68eb2ccc:

    # "{i}As you turn off the water, the bathroom door suddenly opens."
    "{i}Kiedy wyłączasz wodę, nagle otwierają się drzwi łazienki."

# game/day01.rpy:185
translate polish day01_p_room_action_menu_347f6801:

    # r "WHAT THE FUCK [p_name]!!! Didn't you learn to lock the bathroom door?!"
    r "CO JEST KURWA [p_name]!!! Dlaczego nie zamykasz drzwi?!"

# game/day01.rpy:186
translate polish day01_p_room_action_menu_4ac95b16:

    # p "Oh shit. [r_name], I'm sorry... I..."
    p "O cholera. Rachel, przepraszam... Ja..."

# game/day01.rpy:190
translate polish day01_p_room_action_menu_d6540229:

    # "{i}But [r_name] has already stormed down the hallway."
    "{i}Ale Rachel już wybiegła z łazienki"

# game/day01.rpy:194
translate polish post_shower_choices_f6c64a4e:

    # "{i}You wrap a towel around your nether regions and sprint after her."
    "{i}Owijasz się ręcznikiem i biegniesz za nią."

# game/day01.rpy:201
translate polish post_shower_choices_faf85feb:

    # "{i}As soon as you lie down you fall asleep. Your journey and the events of today have certainly taken their toll."
    "{i}Zasypiasz natychmiastowo po położeniu się. Twoja podróż i dzisiejsze wydarzenia naprawdę Cię wyczerpały."

# game/day01.rpy:203
translate polish post_shower_choices_38b77e69:

    # "{i}You awake a few hours later at the beginning of the evening."
    "{i}Budzisz się pod wieczór, kilka godzin później."

# game/day01.rpy:209
translate polish day01_r_bedroom_d1beb9e8:

    # "{i}[r_name]'s door is closed."
    "{i}Drzwi od jej pokoju są zamknięte."

# game/day01.rpy:213
translate polish day01_r_bedroom_04531581:

    # "{i}No answer."
    "{i}Nie odpowiada."

# game/day01.rpy:216
translate polish day01_r_bedroom_9955fb1c:

    # p "I'm so sorry [r_name]! At dad's we always left the doors unlocked..."
    p "Naprawdę przepraszam Rachel! U taty nigdy nie zawracaliśmy sobie głowy zamykaniem drzwi..."

# game/day01.rpy:220
translate polish day01_r_bedroom_2ba9e26e:

    # r "JUST GO AWAY [p_name]!!!"
    r "IDŹ SOBIE!!!"

# game/day01.rpy:221
translate polish day01_r_bedroom_85da1649:

    # p "{i}(Fuck, so much for first impressions...)"
    p "{i}(Kurwa, to by było na tyle jeśli chodzi o dobre pierwsze wrażenie...)"

# game/day01.rpy:222
translate polish day01_r_bedroom_4db5f92d:

    # "{i}You go back to your room to dress yourself."
    "{i}Wracasz do swojego pokoju, żeby się ubrać."

# game/day01.rpy:225
translate polish day01_r_bedroom_1ac62488:

    # r "{i}(Shit, that was embarrassing. But who leaves a bathroom unlocked anyway?!)"
    r "{i}(Cholera, to było niezręczne. Ale kto normalny zostawia otwarte drzwi do łazienki?!)"

# game/day01.rpy:228
translate polish day01_r_bedroom_b7538ba9:

    # r "{i}(Now I'm all riled up. Have to relieve the tension a bit.)"
    r "{i}(Teraz jestem cała spięta. Muszę się trochę rozluźnić.)"

# game/day01.rpy:231
translate polish day01_r_bedroom_d2cd3598:

    # r "{i}(Despite the awkwardness, [p_name] looked kinda hot. Nicely toned body...)"
    r "{i}(Pomijając tą niezręczną sytuację, [p_name] wyglądał naprawdę dobrze. Ma ładnie wyrzeźbione ciało...)"

# game/day01.rpy:235
translate polish day01_r_masturbation_108963ca:

    # r "{i}(I shouldn't be thinking of my brother this way. But he's more like a total stranger anyway.)"
    r "{i}(Nie powinnam tak myśleć o własnym bracie. Ale w praktyce jest dla mnie obcą osobą.)"

# game/day01.rpy:245
translate polish day01_r_masturbation_5e7968a6:

    # r "{i}(*gasp* Oh, that feels good.)"
    r "{i} *Wzdycha* (Oh, to przyjemne.)"

# game/day01.rpy:246
translate polish day01_r_masturbation_68f18001:

    # r "{i}(He's well-endowed too...)"
    r "{i}(Jest też dobrze wyposażony...)"

# game/day01.rpy:247
translate polish day01_r_masturbation_37832683:

    # r "{i}(Oooooooh, I'm cumming...)"
    r "{i}(Oooooooh, dochodzę...)"

# game/day01.rpy:250
translate polish day01_r_masturbation_edcc4ac3:

    # r "{i}(Aaaaah!!! All better now.)"
    r "{i}(Aaaaah!!! Tak lepiej.)"

# game/day01.rpy:258
translate polish day01_r_masturbation_41a154ac:

    # r "Wuh what?"
    r "C- Co?"

# game/day01.rpy:260
translate polish day01_r_masturbation_20e46b26:

    # r "LEAVE ME THE FUCK ALONE [p_name]!!! Are you crazy?!"
    r "ZOSTAW MNIE KURWA SAMĄ [p_name]!!! Zwariowałeś?!"

# game/day01.rpy:270
translate polish day01_dinner_ef37f788:

    # m "[p_name]! Dinner is ready!"
    m "[p_name]! Kolacja gotowa!"

# game/day01.rpy:274
translate polish day01_dinner_df7f3780:

    # p "Hi [m_name], [r_name]."
    p "Cześć mamo, Rachel."

# game/day01.rpy:275
translate polish day01_dinner_e479695b:

    # p "{i}(Damn, I was hoping [r_name] wouldn't be here. Things could get embarrassing...)"
    p "{i}(Cholera, miałem nadzieję, że Rachel tu nie będzie. Może się zrobić niezręcznie...)"

# game/day01.rpy:276
translate polish day01_dinner_b87b4fdf:

    # p "{i}(Let's just pretend nothing happened.)"
    p "{i}(Po prostu udawajmy, że nic się nie stało.)"

# game/day01.rpy:277
translate polish day01_dinner_521cd3b1:

    # r "{i}(Why is he looking at me so intently?)"
    r "{i}(Dlaczego tak na mnie patrzy?)"

# game/day01.rpy:280
translate polish day01_dinner_df7f3780_1:

    # p "Hi [m_name], [r_name]."
    p "Cześć mamo, Rachel."

# game/day01.rpy:282
translate polish day01_dinner_d1df93fd:

    # m "So [p_name], how are you settling in?"
    m "Więc [p_name], jak Ci idzie zadomowianie się?"

# game/day01.rpy:286
translate polish day01_dinner_36290f04:

    # p "Everything is great!"
    p "Wszystko idzie świetnie!"

# game/day01.rpy:287
translate polish day01_dinner_adae0f8b:

    # m "That's good to hear!"
    m "Dobrze to słyszeć!"

# game/day01.rpy:293
translate polish day01_dinner_ea1cda53:

    # p "Well, I still have some adjusting to do."
    p "Cóż, dalej mam kilka rzeczy do poprawy."

# game/day01.rpy:294
translate polish day01_dinner_0d184ff9:

    # m "That's understandable, this is your first day."
    m "To zrozumiałe, w końcu to dopiero pierwszy dzień."

# game/day01.rpy:299
translate polish day01_dinner_7b13c025:

    # m "Have you thought about what you're going to do while you're staying here?"
    m "Myślałeś już o tym, co będziesz robił, teraz gdy już tu jesteś?"

# game/day01.rpy:300
translate polish day01_dinner_d45c55fb:

    # p "I haven't really thought about it."
    p "Nie, jeszcze nie."

# game/day01.rpy:303
translate polish day01_dinner_733f9be3:

    # p "Of course, I'd like to see my other sisters first."
    p "Oczywiście, chcę najpierw poznać resztę moich sióstr."

# game/day01.rpy:307
translate polish day01_dinner_d84496dd:

    # p "But apart from that I haven't got a clue. I don't really know anyone in the area."
    p "Ale poza tym, nie mam pojęcia. Tak naprawdę nie znam nikogo z tej okolicy."

# game/day01.rpy:309
translate polish day01_dinner_0c1f818d:

    # m "Hmmm, maybe you can meet some of [r_name]'s friends."
    m "Hmmm, może mógłbyś się poznać z jakimiś znajomymi Rachel."

# game/day01.rpy:311
translate polish day01_dinner_731ef28f:

    # m "Doesn't Ana have a brother who is [p_name]'s age, [r_name]?"
    m "Czy Ana nie ma brata, który jest w jego wieku, Rachel?"

# game/day01.rpy:313
translate polish day01_dinner_4f6b4283:

    # r "James?! He's a complete dork. Ana is always complaining about him."
    r "Jamesa?! Jest kompletnym baranem. Ana ciągle na niego narzeka."

# game/day01.rpy:314
translate polish day01_dinner_c42773e2:

    # m "Now now. James is always very friendly to me."
    m "Przesadzasz. James zawsze jest dla mnie bardzo miły."

# game/day01.rpy:316
translate polish day01_dinner_e93989c7:

    # r "Yes mom... very friendly..."
    r "Tak mamo... Bardzo miły..."


# game/day01.rpy:319
translate polish day01_dinner_6137ccb4:

    # p "{i}(Whatever does she mean by that?)"
    p "{i}(Co ona sugeruje?)"

# game/day01.rpy:320
translate polish day01_dinner_6873c1c4:

    # m "Just ask Ana if she will bring James around next time she comes over."
    m "Po prostu poproś Anę, żeby przy następnej okazji przyprowadziła ze sobą Jamesa."

# game/day01.rpy:321
translate polish day01_dinner_f7948b4a:

    # m "By that time [p_name] will probably want to talk to a fellow man, after spending too much time with us women."
    m "Do tego czasu [p_name] pewnie będzie chciał pogadać z innym facetem, po spędzeniu tak długiego czasu z nami, kobietami."

# game/day01.rpy:322
translate polish day01_dinner_2db39562:

    # r "If you say so... You've been warned though, [p_name]!"
    r "Skoro tak mówisz... Ale ostrzegałam Cię [p_name]!"

# game/day01.rpy:333
translate polish day01_dinner_conversation_95327668:

    # p "So when is [b_name] coming home?"
    p "Więc, kiedy wróci Bella?"

# game/day01.rpy:334
translate polish day01_dinner_conversation_06a0c73d:

    # m "She should be home tonight. [b_name] always works long shifts and eats at work."
    m "Powinna być w domu jakoś pod wieczór. Bella zawsze długo pracuje i zwykle je w pracy."

# game/day01.rpy:336
translate polish day01_dinner_conversation_1d1a2678:

    # r "I really don't understand why [b_name] insists on working so much. It's not that we need the money."
    r "Naprawdę nie rozumiem, dlaczego Bella aż tak chce pracować. Przecież nie brakuje nam pieniędzy."

# game/day01.rpy:337
translate polish day01_dinner_conversation_0d132150:

    # m "She is a very independent girl. There's nothing wrong with that."
    m "Jest bardzo niezależną dziewczyną. Nie ma w tym nic złego."

# game/day01.rpy:338
translate polish day01_dinner_conversation_cbcb3638:

    # m "In fact, you could use a bit of her spirit. Have you found a job yet?"
    m "Prawdę mówiąc, mogłabyś wziąć z niej przykład. Może znalazłabyś sobie jakąś pracę?"

# game/day01.rpy:340
translate polish day01_dinner_conversation_8029a0c8:

    # r "No mom. Besides, my summer holiday time is too precious to be spent at work."
    r "Nie mamo. Moje wakacje są zbyt cenne, żebym marnowała czas w pracy."

# game/day01.rpy:344
translate polish day01_dinner_conversation_9e90990b:

    # r "Before you know it, I'll be back in college and if I work over the summer I won't get to have any fun."
    r "Zanim się zorientuję będzie pora wrócić do szkoły i jeśli spędzę wakacje w pracy, to nawet nie wypocznę."

# game/day01.rpy:345
translate polish day01_dinner_conversation_5c306d44:

    # r "I just don't love working as much as you and [b_name] seem to..."
    r "Po prostu nie kocham pracować tak bardzo jak Ty, czy Bella..."

# game/day01.rpy:350
translate polish day01_dinner_conversation_d9af8bfc:

    # p "Will I see [l_name] today?"
    p "Zobaczę się dzisiaj z Lizą?"

# game/day01.rpy:351
translate polish day01_dinner_conversation_72bd41ba:

    # m "I believe she's at Brody's. Her boyfriend. So I'm not really sure."
    m "Chyba jest u Brody'iego. Swojego chłopaka. Więc nie jestem pewna. "

# game/day01.rpy:353
translate polish day01_dinner_conversation_1b7d8ff7:

    # r "Ugh. Brody. I can't believe she's going to be engaged to that guy."
    r "Ugh. Brody. Nie mogę uwierzyć, że zaręczy się z tym gościem."

# game/day01.rpy:354
translate polish day01_dinner_conversation_bcb6f977:

    # m "My, my, it seems you really dislike boys."
    m "Oho, no proszę, wygląda na to, że naprawdę nie lubisz chłopaków."

# game/day01.rpy:355
translate polish day01_dinner_conversation_3cce0856:

    # r "No... Er.. It's not like that... Pfff..."
    r "Nie... Emm... To nie tak... Pfff..."

# game/day01.rpy:356
translate polish day01_dinner_conversation_d5a1eb52:

    # r "Brody and [l_name] have been together forever and I think he's a real dick."
    r "Brody i Liza są razem od zawsze, a myślę, że jest strasznym fiutem."

# game/day01.rpy:357
translate polish day01_dinner_conversation_c438e3fd:

    # m "Language, young lady!"
    m "Wyrażaj się młoda damo!"

# game/day01.rpy:362
translate polish day01_dinner_conversation_1cadbee1:

    # p "What are your plans for tonight?"
    p "Jakieś plany na ten wieczór?"

# game/day01.rpy:363
translate polish day01_dinner_conversation_c0d386ca:

    # m "Oh, nothing much. Luckily I don't have to work today."
    m "Oh, nic specjalnego. Całe szczęście nie muszę dziś iść do pracy."

# game/day01.rpy:365
translate polish day01_dinner_conversation_01394e7f:

    # r "Wow, that doesn't happen often."
    r "Wow, to nieczęsto się zdarza."

# game/day01.rpy:368
translate polish day01_dinner_conversation_f8cbe56a:

    # r "You better get used to it, [p_name], mom's a real workaholic."
    r "Lepiej się do tego przyzwyczaj, [p_name]. Mama jest prawdziwą pracoholiczką."

# game/day01.rpy:369
translate polish day01_dinner_conversation_18ea06cb:

    # m "Somebody has to provide for this family."
    m "Ktoś musi zapewniać byt tej rodzinie."

# game/day01.rpy:379
translate polish day01_dinner_conversation_55a3b703:

    # p "Thank you for dinner. I didn't know you could cook so well."
    p "Dzięki za kolację. Nie wiedziałem, że tak dobrze gotujesz."

# game/day01.rpy:380
translate polish day01_dinner_conversation_40c25a62:

    # m "Thank you!"
    m "Dziękuję!"

# game/day01.rpy:383
translate polish day01_dinner_conversation_9f54eb4a:

    # r "Very smooth, [p_name]..."
    r "Bardzo subtelnie, [p_name]..."

# game/day01.rpy:384
translate polish day01_dinner_conversation_d4a2fcd3:

    # p "Hehe, may I be excused?"
    p "Hehe, mogę już iść?"

# game/day01.rpy:385
translate polish day01_dinner_conversation_9e6a3995:

    # m "Certainly. I'll do the dishes with [r_name]."
    m "No jasne. Ja i Rachel pozmywamy po kolacji."

# game/day01.rpy:387
translate polish day01_dinner_conversation_786f97ce:

    # r "Mooooom!"
    r "Maaaamoooo!"

# game/day01.rpy:390
translate polish day01_dinner_conversation_628a50e2:

    # p "Thanks for dinner, may I be excused?"
    p "Dzięki za kolację, mogę już iść?"

# game/day01.rpy:392
translate polish day01_dinner_conversation_9e6a3995_1:

    # m "Certainly. I'll do the dishes with [r_name]."
    m "No jasne. Ja i Rachel pozmywamy po kolacji."

# game/day01.rpy:394
translate polish day01_dinner_conversation_786f97ce_1:

    # r "Mooooom!"
    r "Maaaamoooo!"

# game/day01.rpy:400
translate polish day01_p_room_post_dinner_707dd433:

    # p "{i}(I'm stuffed. [m_name] sure knows how to cook.)"
    p "{i}(Ale się napchałem. Susan bez wątpienia zna się na gotowaniu.)"

# game/day01.rpy:403
translate polish day01_p_room_post_dinner_db3d73c1:

    # p "{i}(Luckily [r_name] didn't mention the incident to [m_name].)"
    p "{i}(Całe szczęście Rachel nie powiedziała mamie o tym małym incydencie.)"

# game/day01.rpy:417
translate polish day01_p_room_choices_17aed6d5:

    # "[m_name] is reading a book."
    "{i}Susan czyta książkę."

# game/day01.rpy:418
translate polish day01_p_room_choices_4a5eb0ba:

    # p "What are you reading, [m_name]?"
    p "Co czytasz mamo?"

# game/day01.rpy:422
translate polish day01_p_room_choices_ba13b2ac:

    # m "Oh, just some book about management. It's a bit boring to be honest."
    m "Oh, taką tam książkę o zarządzaniu. Nic ciekawego."

# game/day01.rpy:423
translate polish day01_p_room_choices_8ce7c3c3:

    # p "Mind if I talk to you?"
    p "Mogę z Tobą porozmawiać?"

# game/day01.rpy:424
translate polish day01_p_room_choices_c1078f47:

    # m "Not at all."
    m "Oczywiście."

# game/day01.rpy:431
translate polish day01_m_talk_48acea0b:

    # p "It's weird, but this is already starting to feel a bit like home."
    p "To dziwne, ale już zaczynam czuć się jak w domu."

# game/day01.rpy:434
translate polish day01_m_talk_372ef361:

    # m "I hope that feeling will only grow and that we can be a real family again."
    m "Mam nadzieję, że dalej będziesz tak się czuł i będziemy mogli znowu być prawdziwą rodziną"

# game/day01.rpy:442
translate polish day01_m_talk_f63ef81b:

    # p "Why did you guys never visit?"
    p "Dlaczego nigdy nas nie odwiedzałyście?"

# game/day01.rpy:446
translate polish day01_m_talk_760e1324:

    # m "Oh we tried, the first few years. But your father always denied us any contact."
    m "Oh, próbowałyśmy, przez pierwszych parę lat. Ale Twój ojciec zawsze odmawiał nam prób kontaktu."

# game/day01.rpy:447
translate polish day01_m_talk_e873f53f:

    # m "Didn't you receive the letters we sent you?"
    m "Nie dostałeś listów, które Ci wysyłałyśmy?"

# game/day01.rpy:448
translate polish day01_m_talk_1b7b218f:

    # p "Er, no..."
    p "Emm, nie..."

# game/day01.rpy:449
translate polish day01_m_talk_6a82c153:

    # m "We sent quite a lot of them, but after a while, when we received nothing back, we stopped trying."
    m "Wysłałyśmy ich całkiem sporo, ale po pewnym czasie, kiedy nie otrzymywałyśmy żadnej odpowiedzi, to przestałyśmy próbować."

# game/day01.rpy:450
translate polish day01_m_talk_3012c691:

    # p "But why though? Why was father so adamant about us not having contact?"
    p "Ale dlaczego? Dlaczego ojciec aż tak bardzo chciał nas utrzymać z dala od siebie?"

# game/day01.rpy:453
translate polish day01_m_talk_d7f38d8e:

    # p "I mean, he was rather hands off in the whole upbringing department, but avoiding you, [r_name], [l_name] and [b_name] was high on his list of priorities, apparently..."
    p "Znaczy, nie bardzo interesowało go wychowywanie dzieci, ale widocznie unikanie Ciebie, Rachel, Lizy i Belli było dla niego ważne..."

# game/day01.rpy:455
translate polish day01_m_talk_d225771b:

    # p "I mean, he was rather hands off in the whole upbringing department, but avoiding you was high on his list of priorities, apparently..."
    p "Znaczy, nie bardzo interesowało go wychowywanie dzieci, ale widocznie unikanie was było dla niego ważne..."

# game/day01.rpy:457
translate polish day01_m_talk_8d54f725:

    # m "The only thing I know is that we grew apart over the years and that distance grew into something bitter... until I... we... just couldn't go on."
    m "Jedyne co wiem, to że z biegiem lat oddaliliśmy się od siebie i zaczęła narastać między nami niechęć... Aż ja... My... Już nie mogliśmy tego ciągnąć."

# game/day01.rpy:463
translate polish day01_m_talk_father_cf59409d:

    # p "I don't get it, there must have been something else."
    p "Nie rozumiem, musiało być coś jeszcze."

# game/day01.rpy:464
translate polish day01_m_talk_father_4787b806:

    # m "Well if you want to doubt me, be my guest..."
    m "Cóż, jeśli mi nie wierzysz, to nic na to nie poradzę..."

# game/day01.rpy:469
translate polish day01_m_talk_father_8ae97135:

    # p "That happens sometimes."
    p "Tak już czasem bywa."

# game/day01.rpy:472
translate polish day01_m_talk_father_98cf6b15:

    # m "Thank you."
    m "Dzięki."

# game/day01.rpy:480
translate polish day01_m_talk_father_d282540b:

    # "{i}[r_name] is reading a magazine."
    "{i}Rachel czyta magazyn."

# game/day01.rpy:485
translate polish day01_m_talk_father_9bbba74a:

    # r "Dinner was nice, mom is hardly ever here."
    r "Na kolacji było miło, mama niestety rzadko tu jest."

# game/day01.rpy:489
translate polish day01_m_talk_father_e56dcbe8:

    # p "Is she working that much?"
    p "Aż tyle pracuje?"

# game/day01.rpy:490
translate polish day01_m_talk_father_59dc3e5d:

    # r "Yeah, too much... Even in the evening hours and during the weekends."
    r "Tak, zbyt dużo... Nawet wieczorami i w weekendy."

# game/day01.rpy:491
translate polish day01_m_talk_father_9c4c0437:

    # p "I guess she has an important job."
    p "Pewnie ma ważną pracę."

# game/day01.rpy:492
translate polish day01_m_talk_father_a840e209:

    # r "Guess so. Of course she has to provide for us and pay for this nice house we're all living in, so I shouldn't complain!"
    r "Pewnie tak. I oczywiście musi nas utrzymywać i zarabiać na ten dom, w którym wszyscy żyjemy, więc nie powinnam narzekać!"

# game/day01.rpy:493
translate polish day01_m_talk_father_1f46eb1d:

    # r "Did you want something?"
    r "Potrzebujesz czegoś?"

# game/day01.rpy:498
translate polish day01_r_talk_87ca374f:

    # p "That guy, James..."
    p "Ten gość, James..."

# game/day01.rpy:499
translate polish day01_r_talk_f5e99613:

    # r "I already told you he's a total dork. But it's fine if you want to hang out with him."
    r "Już Ci mówiłam, że to baran. Ale w porządku jeśli chcesz się z nim poznać."

# game/day01.rpy:500
translate polish day01_r_talk_7cbef1c6:

    # r "Ana is coming over tomorrow, so she'll bring James and you guys can talk about dork stuff, while we go shopping."
    r "Ana wpadnie jutro mnie odwiedzić. Powiem jej, żeby przyprowadziła Jamesa, będziecie mogli pogadać o tych waszych głupotach, a my pójdziemy na zakupy."

# game/day01.rpy:501
translate polish day01_r_talk_7a48df1e:

    # r "Ana is the coolest! She's dated all the hot guys at college and she knows so much about stuff, you know."
    r "Ana jest super! Umawiała się ze wszystkimi fajnymi chłopakami ze szkoły i tak dużo wie o związkach."

# game/day01.rpy:502
translate polish day01_r_talk_91c9efb1:

    # p "{i}(She sounds a bit slutty, if you ask me...)"
    p "{i}(Dla mnie to brzmi jakby po prostu była łatwa...)"

# game/day01.rpy:503
translate polish day01_r_talk_2c11705b:

    # r "You'll meet Alina as well, she's just as popular as Ana, but so far she's turned down all the guys who want to date her."
    r "Poznasz też Alinę, jest praktycznie tak popularna jak Ada, ale póki co spławiała wszystkich facetów, którzy chcieli się z nią umówić."

# game/day01.rpy:507
translate polish day01_r_talk_aafe51d0:

    # p "So you're relaxing until the end of the summer holiday?"
    p "Więc, odpoczywasz aż do końca wakacji?"

# game/day01.rpy:508
translate polish day01_r_talk_550848ff:

    # r "Yup! Best time of the year."
    r "Nom! Najlepszy czas w roku."

# game/day01.rpy:509
translate polish day01_r_talk_ff4d4e44:

    # r "What are you going to do?"
    r "A Ty co będziesz robił?"

# game/day01.rpy:511
translate polish day01_r_talk_40341116:

    # p "Nothing much really. Getting to know you guys, probably."
    p "Raczej nic takiego. Przede wszystkim chcę was poznać."

# game/day01.rpy:523
translate polish day01_b_talk_521bd564:

    # "{i}After a couple of hours of mindless clicking on cat videos you hear sounds coming from the kitchen."
    "{i}Po paru godzinach bezmyślnego oglądania filmików z kotami, słyszysz odgłosy dobiegające z kuchni."

# game/day01.rpy:527
translate polish day01_b_talk_8474ea5a:

    # p "{i}(Could be [b_name] or burglars. Better go check it out.)"
    p "{i}(To albo Bella, albo włamywacz. Lepiej to sprawdzę.)"

# game/day01.rpy:531
translate polish day01_b_talk_557646e1:

    # p "Oh, hi."
    p "Oh, cześć."

# game/day01.rpy:535
translate polish day01_b_talk_357fa026:

    # b "Fuck, you startled me!"
    b "Kurwa, wystraszyłeś mnie!"

# game/day01.rpy:537
translate polish day01_b_talk_7ab592da:

    # b "You must be the long lost brother..."
    b "Musisz być tym dawno zaginionym bratem..."

# game/day01.rpy:538
translate polish day01_b_talk_b7c252f4:

    # b "Do you sneak up on women often, [p_name]?"
    b "Często podkradasz się tak do kobiet, [p_name]?"

# game/day01.rpy:539
translate polish day01_b_talk_ee4861d8:

    # p "{i}(Ah, [b_name]. Still a bitch apparently. She's hot though.)"
    p "{i}(Ah, Bella. Dalej wredna. Ale muszę przyznać, że też wyrosła na niezłą laskę.)"

# game/day01.rpy:545
translate polish day01_b_talk_44194c8b:

    # b "What are you gawking at? Did you lose your tongue?"
    b "Co się tak gapisz? Zapomniałeś języka w gębie?"

# game/day01.rpy:552
translate polish day01_b_conversation_f4d3967c:

    # b "What the fuck do you think you're doing?"
    b "Co Ty sobie kurwa myślisz?"

# game/day01.rpy:555
translate polish day01_b_conversation_3fa6b452:

    # b "You think you can just come back, hug me and make everything right again?"
    b "Myślisz, że możesz tak po prostu wrócić, przytulić mnie i wszystko będzie dobrze?"

# game/day01.rpy:557
translate polish day01_b_conversation_5fc7f7ca:

    # b "You think you can just hug someone you've never met?"
    b "Myślisz, że możesz tak po prostu przytulać się do kogoś kogo nigdy wcześniej nie spotkałeś?"

# game/day01.rpy:559
translate polish day01_b_conversation_57b7a714:

    # b "Don't you dare touch me!"
    b "Nie waż się mnie dotykać!"

# game/day01.rpy:560
translate polish day01_b_conversation_05ac596e:

    # b "Get out of my face, you creep!"
    b "Zejdź mi z oczu, świrze!"

# game/day01.rpy:569
translate polish day01_b_conversation_a9102e59:

    # p "It's good to see you too, sis."
    p "Ciebie też miło poznać, siostrzyczko."

# game/day01.rpy:572
translate polish day01_b_conversation_bb49548c:

    # p "It's nice to meet you too."
    p "Ciebie też miło poznać."

# game/day01.rpy:576
translate polish day01_b_conversation_27540380:

    # b "Hmpf! Don't think you can just waltz in here and we're going to accept you."
    b "Pff! Nie myśl sobie, że możesz tak po prostu się tu pojawić i wszyscy Cię zaakceptujemy."

# game/day01.rpy:577
translate polish day01_b_conversation_a2e8d095:

    # b "We've managed fine without you all these years."
    b "Świetnie sobie radziłyśmy bez Ciebie."

# game/day01.rpy:580
translate polish day01_b_conversation_795cb6e8:

    # b "Mom has struggled to support us and now she has another mouth to feed as well."
    b "Mama ciężko pracowała, żeby zapewnić nam byt, a teraz ma kolejną gębę do wyżywienia."

# game/day01.rpy:584
translate polish day01_b_conversation_e87b15b6:

    # p "{i}(What the hell is her problem?)"
    p "{i}(Z czym ona do cholery ma problem?)"

# game/day01.rpy:587
translate polish day01_b_conversation_4d565716:

    # p "Dad left me a lot of money after his death, so [m_name] doesn't have to provide me anything!"
    p "Tata zostawił mi sporo pieniędzy w spadku, więc Susan nie musi mnie 'żywić'."

# game/day01.rpy:594
translate polish day01_b_conversation_850ef128:

    # b "..."
    b "..."

# game/day01.rpy:597
translate polish day01_b_conversation_918417b9:

    # b "Fucking Dad... Well, don't get in my way and I won't get in yours."
    b "Jebany tatuś... Cóż, nie wchodź mi w drogę, to ja nie będę wchodzić Tobie."

# game/day01.rpy:599
translate polish day01_b_conversation_02d24429:

    # b "Well, don't get in my way and I won't get in yours."
    b "Cóż, nie wchodź mi w drogę, to ja nie będę wchodzić Tobie."

# game/day01.rpy:603
translate polish day01_b_conversation_8031467f:

    # b "Now leave!"
    b "A teraz idź już sobie!"

# game/day01.rpy:604
translate polish day01_b_conversation_8f405f50:

    # p "Good night, [b_name]!"
    p "Dobranoc Bella!"

# game/day01.rpy:605
translate polish day01_b_conversation_1978dc2b:

    # b "Yeah yeah."
    b "Ta, ta."

# game/day01.rpy:609
translate polish day01_b_conversation_a81e5530:

    # "{i}You go back to your room. Despite having slept already you fall asleep very quickly."
    "{i}Wracasz do swojego pokoju. Mimo, że wcześniej już spałeś, to zasypiasz bardzo szybko."

translate polish strings:

    # game/day01.rpy:3
    old "Day 1"
    new "Dzień 1"

    # game/day01.rpy:27
    old "Hug her"
    new "Przytul ją"

    # game/day01.rpy:27
    old "Kiss her"
    new "Pocałuj ją"

    # game/day01.rpy:143
    old "Unpack your bag"
    new "Rozpakuj się"

    # game/day01.rpy:143
    old "Take a shower"
    new "Weź prysznic"

    # game/day01.rpy:143
    old "Sleep in your bed"
    new "Idź spać"

    # game/day01.rpy:192
    old "Go after her"
    new "Pobiegnij za nią"

    # game/day01.rpy:192
    old "Leave her be"
    new "Zostaw ją w spokoju"

    # game/day01.rpy:211
    old "Knock on her door"
    new "Zapukaj"

    # game/day01.rpy:211
    old "Open her door"
    new "Wejdź"

    # game/day01.rpy:284
    old "Lie"
    new "Kłamstwo"

    # game/day01.rpy:284
    old "Truth"
    new "Prawda"

    # game/day01.rpy:330
    old "[b_name]"
    new "Bella"

    # game/day01.rpy:330
    old "[l_name]"
    new "Liza"

    # game/day01.rpy:330
    old "Plans"
    new "Plany"

    # game/day01.rpy:330
    old "Leave dinner"
    new "Wyjdź"

    # game/day01.rpy:377
    old "Compliment"
    new "Komplement"

    # game/day01.rpy:377
    old "Just leave"
    new "Po prostu wyjdź"

    # game/day01.rpy:411
    old "Go to [m_name]"
    new "Idź do Susan"

    # game/day01.rpy:411
    old "Go to [r_name]"
    new "Idź do Rachel"

    # game/day01.rpy:411
    old "Surf the web"
    new "Poserfuj po internecie"

    # game/day01.rpy:428
    old "Adjusting"
    new "Nowa sytuacja"

    # game/day01.rpy:428
    old "Father"
    new "Ojciec"

    # game/day01.rpy:428
    old "I'll let you read."
    new "Pozwolę Ci czytać"

    # game/day01.rpy:459
    old "Challenge"
    new "Nalegaj"

    # game/day01.rpy:459
    old "Accept"
    new "Zgoda"

    # game/day01.rpy:495
    old "James"
    new "James"

    # game/day01.rpy:495
    old "Holiday plans"
    new "Plany na wakacje"

    # game/day01.rpy:495
    old "Leave"
    new "Wyjdź"

    # game/day01.rpy:548
    old "Greet"
    new "Przywitaj się"

# game/day01.rpy:15
translate polish day01_c34069a0:

    # p "{i}(Should I just call her Mrs. Smith, or use her first name?)"
    p ""

# game/day01.rpy:25
translate polish day01_b3663d81:

    # p "Hi [m_name]. Good to see you again."
    p ""

# game/day01.rpy:48
translate polish enter_apartment_c28d0f18:

    # m "Come in! I've told you about the three girls living with me, haven't I?"
    m ""

# game/day01.rpy:53
translate polish enter_apartment_2f71ea59:

    # m "The youngest girl is also home, she's very eager to meet you!"
    m ""

# game/day01.rpy:58
translate polish enter_apartment_4e3071e9:

    # p "({i}Wonder what her name is...)"
    p ""

# game/day01.rpy:68
translate polish enter_apartment_f9ae8e23:

    # m "So this will be your room. It's not that big, but I hope you like it."
    m ""

# game/day01.rpy:69
translate polish enter_apartment_71d3888a:

    # p "Thanks [m_name], this is great!"
    p ""

# game/day01.rpy:70
translate polish enter_apartment_968da184:

    # m "The bathroom is just down the hall, if you want to take a shower and freshen up a little."
    m ""

# game/day01.rpy:71
translate polish enter_apartment_04373cf8:

    # m "All right. I'll leave you to unpack and settle in."
    m ""

# game/day01.rpy:72
translate polish enter_apartment_c63e1e7f:

    # "{i}You hear noises in the hallway."
    ""

# game/day01.rpy:75
translate polish enter_apartment_ac9ed951:

    # r "Is this him, mother?"
    r ""

# game/day01.rpy:77
translate polish enter_apartment_7a5b5858:

    # r "Is this him, Mrs. Smith?"
    r ""

# game/day01.rpy:81
translate polish enter_apartment_981e998f:

    # m "Yes dear, this is [p_name]. Where are your manners?"
    m ""

# game/day01.rpy:82
translate polish enter_apartment_4e807dd5:

    # r "Oh, right. Hi, I'm [r_name]!"
    r ""

# game/day01.rpy:85
translate polish enter_apartment_2494dc32:

    # p "({i}Woah. [r_name] has grown. She looks very nice! Mom and dad's marriage might not have been successful, but their mix of genes certainly was.)"
    p ""

# game/day01.rpy:87
translate polish enter_apartment_d90fb484:

    # p "({i}Woah. [r_name] looks very nice!)"
    p ""

# game/day01.rpy:93
translate polish enter_apartment_4f22f0ef:

    # p "Good to meet you, [r_name]."
    p ""

# game/day01.rpy:100
translate polish enter_apartment_953b0ac8:

    # p "{b}*Kiss*{/b} Hi [r_name]!"
    p ""

# game/day01.rpy:113
translate polish day01_leave_p_room_3e7394a0:

    # r "And you have to meet the other girls of course, but they aren't home at the moment. And..."
    r ""

# game/day01.rpy:151
translate polish day01_p_room_action_menu_fb37e775:

    # p "{i}(I wonder where the other girls are.)"
    p ""

# game/day01.rpy:160
translate polish day01_p_room_action_menu_f87ce940:

    # p "{i}(I remember that [b_name] and I were always arguing. She isn't that much older than me and could be a real bitch sometimes, back when mom and dad were still together.)"
    p ""

# game/day01.rpy:162
translate polish day01_p_room_action_menu_cf29b774:

    # p "{i}(From what I heard, [b_name] is always arguing with the others. Sounds a bit like a bitch to me.)"
    p ""

# game/day01.rpy:171
translate polish day01_p_room_action_menu_f09d49b0:

    # p "{i}(My eldest sister [l_name] was always the most responsible of the four of us. I wonder if that's changed.)"
    p ""

# game/day01.rpy:173
translate polish day01_p_room_action_menu_440551ce:

    # p "{i}(From what [m_name] told me, [l_name] is the most responsible of the three girls.)"
    p ""

# game/day01.rpy:218
translate polish day01_r_bedroom_5756765a:

    # p "I'm so sorry [r_name]! At my dad's we always left the doors unlocked..."
    p ""

# game/day01.rpy:305
translate polish day01_dinner_12b4fa08:

    # p "Of course, I'd like to meet the other girls first."
    p ""

# game/day01.rpy:318
translate polish day01_dinner_6f99e4f6:

    # r "Yes Mrs. Smith... very friendly..."
    r ""

# game/day01.rpy:342
translate polish day01_dinner_conversation_e470abff:

    # r "No Mrs. Smith. Besides, my summer holiday time is too precious to be spent at work."
    r ""

# game/day01.rpy:371
translate polish day01_dinner_conversation_7f8f23a6:

    # r "You better get used to it, [p_name], Mrs. Smith is a real workaholic."
    r ""

# game/day01.rpy:372
translate polish day01_dinner_conversation_611fe71f:

    # m "Somebody has to provide for this shelter. It's all volunteer work, you know."
    m ""

# game/day01.rpy:436
translate polish day01_m_talk_5e69b70d:

    # m "I hope that feeling will only grow!"
    m ""

# game/day01.rpy:444
translate polish day01_m_talk_521153a1:

    # p "Why did you guys never visit? I mean, you were good friends at first, right?"
    p ""

# game/day01.rpy:487
translate polish day01_m_talk_father_8ecf6043:

    # r "Dinner was nice, Mrs. Smith is hardly ever here."
    r ""

# game/day01.rpy:541
translate polish day01_b_talk_fbcbe4fb:

    # b "You must be the new guest..."
    b ""

# game/day01.rpy:542
translate polish day01_b_talk_e785b58d:

    # b "Do you sneak up on women often?"
    b ""

# game/day01.rpy:543
translate polish day01_b_talk_c1061d39:

    # p "{i}(Ah, [b_name]. Truly a bitch apparently. She's hot though.)"
    p ""

# game/day01.rpy:582
translate polish day01_b_conversation_ceb23932:

    # b "Mrs. Smith has struggled to support us and now she has another mouth to feed as well."
    b ""

# game/day01.rpy:589
translate polish day01_b_conversation_48766f28:

    # p "My dad left me a lot of money after his death, so [m_name] doesn't have to provide me anything!"
    p ""