# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define n = Character("Nami ", color = "#095ce2", who_color="#095ce2")
define a = Character("Aida ", color = "#000000",who_color="#DDF")
define al = Character("Alis ", color="#a31a1a",who_color="#a31a1a")
define m = Character("Mushi ", color = "#8c6406",who_color="#8c6406")
define d = Character("Danny", color = "#470fd6",who_color="#470fd6")
define g = Character("Girl", color = "#a31a1a",who_color="#a31a1a")
define f = Character("Farhan", color = "#000000",who_color="#000000")
define pm = Character("Phone Message", color = "#000000",who_color="#000000")
define an = Character("Annnoucer", color = "#fc0303",who_color="#fc0303")

image n_sad = "n_dissapointed.png"
label start:
#SYNC CHECK
    #Show a background. This uses a placeholder by default, but you can
    #add a file (named either "bg room.png" or "bg room.jpg") to the
    #images directory to show it."""

    scene bg room
    show n_sad
    #show eileen happy
    n "I love you so much! Please accept my love for you!"
    g "Ummmmm, no?"

    n "But why? I have a lot of money to spend on you. Just name it!"
    g "Pffft… Money? Why would I ask you for it?"
    g "I can just dig it up for myself. I don’t need no lousy man like you."
    n "No! My love for you is genuine so please… At least give me a chance?"
    g "How dare you even speak with me, you filth! Did you even do so much as take a look at yourself? You’re fat plus ugly! Ugh, you just plain disgust me. Try better, creep."
    n "But…"
    g "Ciao, Fatty. Good luck with your ugly, miserable and loveless life. Hahahahaha!"
    "The girl yeeted herself out of Nami’s sight."
    n "(thinking to himself)"
    n "What did I do to deserve this? This is the ump teenth time I’ve been rejected. This time, they’re giving me the nickname ‘Fatty’?"
    n "(sighs) What a day.. I gave up on searching for someone who could possibly love a joke like me. Just f*ck love, man. I’ll always be alone, no matter what."

    #scene one
    m "Hey… Hey you! You over there! You sorry sap of a man who just got rejected!"
    "(taken aback)"
    n "Wha-- what do you want? Wait, who even are you?! What's up with the mask, bro? To hide an ugliness like the one I have? Oh boy, if that’s the case, I 	wish I had a mask just like that."
    m "What, my mask? Oh no no no, my good man -- it’s not to hide any ol’ ugliness. Why would a charming, lavishing young man such as myself need to hide some non-existent hideousness? "
    m "What I’m hiding is… (whispers) Come closer."
    "Nami leans closer to the masked stranger."
    m "… Fame. Hehehehe."
    n "… What."
    m "Wherever I go, the mask stays with me. Just like a river with a turtle."
    n "What you just said makes no sense--"
    "(delighted grin)"
    m "Even my mom approved of it too!"
    n "Okay, you know what? Just stay away from me, man. I’m already having a bad day. I just got rejected by yet another girl so I’ve got no time for your jargon."
    m "Awww, you just got rejected? C’mon, being fat is not the worst. You’re all kinds of chubby, and that’s considered cute to some people."
    m "Have an optimistic outlook, man. Besides, didn’t you hear of that old wife’s tale? ‘There are plenty of fish in the sea’!"
    n "Just shut up, man. And plus, that’s an idiom, not some old wife’s tale."
    m "Hey hey hey. Whoaaaa, man. Okay, I’m going to tell you a lil’ secret. Y’know, a bro-to-bro kind of secret. Lean closer, I’ll tell you what it is:"
    m "(whispers) I know someone who’s gonna accept you, regardless of who you are."
    n "(surprised)"
    n "What? You know a girl?"
    m "Nahhh, hahaha! Didn’t we already establish that no sane girl wants you?"
    n "(disappointed) Oh."
    m "I’m talking about a group, a society. A holy matrimony of the greatest chaps who don’t care about money. It’s the…"
    #"Drum roll plays in the background."
    m "Japanese Cultural Society! Or JCS for short."  #(fanfares play in the background)
    n "The JCS? What? You mean that loser get-together community where unwanted virgins flock together to swoon over 2D girls that talk like a yelping penguin? "
    n "That shadowed group polluted by numbskulls people call ‘weebs’? I’m not interested in your club, bro. I’m desperate, but I’m not that desperate. Besides, do I even know who you are?"
    m "Oh c’mon, bro. We already got rejected like so many times. We need members too, so why not join the other rejects who are just like you? "
    m "We could always use a new buddy in our ranks -- a fella to add to our family, y’know? Chillax, I’ll take you there and you’re gonna have a great time."
    m "Besides, there are ladies there too. Maybe one of them will, I dunno, finally feel bad for you and endure a date with you."
    n "You know what? At this point, I just don’t care about girls anymore. But (sighs) fine, you got me at ‘family’. Alright, masked weirdo, tell me more about the JCS. What do they even do for starters?"
    m "Ahahahaha, well well well. I knew you’d take the right step! To enlighten you, I’ll say that we proud members of the JCS has got a lot of goodies and surprise events we do centering on, well, Japanese culture!"
    m "Some weeb bullsh*t, yeah, but not purely that. First off, we’ve got events we put our creative lil’ minds together to come up with: Japanese workshops and the upcoming JC Night, for example."
    m "We’ve also got trips and my favourite? The bonding camp, man. Hoooo boy, if that ain’t the best time to go fishing for hot chicks! My words impressing you, lover boy?"
    n "Hmmm, I guess there are a few trips that are grabbing my attention. Besides, I’ve already lost all hope in anything else I ever loved anyway so nothing worse can happen, I guess. (sighs)"
    n "Alright, bro, let’s try out your little club and see if it’s worth any of my time."
    m "Ayyyyy, that’s the spirit, man! Oh boy, Aida’s gonna be so proud of me for fishing in more fresh blood, hehehehe! Well chump, you just made the right choice. Like, no kidding."
    m "So, you busy right now? Like, really busy?"
    n "Nah, not really, but I’m about to head over back and get some decent sleep actually--"
    m "Bahhhh, sleep is for the weak! Be a man, lover boy! Come with me and join us in our secret JCS lair."
    n "What?! But my precious sleep…! Masked man, nooooo….!"
    "And without further ado and ignoring his pleas, the masked man dragged Nami over to the secret JCS lair."
    n "(thinking to himself) What a weird boy. He gives me the creeps already. Oh damn, I can’t even imagine how weirder his club must be with him already being like this."
    n "Gah, never mind. Nothing is better than giving it a try, right? At least, I hope I gain a chance to find some long term friendship over there."
    #scene two
    m "Kocchi, kocchi! We’re close -- just a few steps more!"

    n "What (pants) floor are we (pants) in now? We at heaven or something? Oh God, I can’t even feel my legs."

    m "Ahhhh, here we are: the best spot in MMU! Or as we like to call it… Uhhhh, wait, what do we call it again? Let me think…"

    n "I… (breathes heavily) need… (breathes heavily) water…"

    m "Oh, don’t be such a wuss. Did you even think for a second that I could be dying because I’m wearing this darn mask? Be considerate, man, sheesh."
    "Aida rushes out to check out the noise."

    a "What’s up with all the noise? Who’s there?! …Oh, Mushi, it’s just you. How very early of you to be at our club at this time. Didn’t I already tell you to not come bothering us with your jibber-jabber?!"

    m "Oh chill up, Aida. I was just sauntering around, finding myself some chicks here and there until I found this poor lad being rejected for like, the bazillionth time."

    m "(leans closer to Aida and whispers) Believe it or not, this dude had it worse than me being rejected like that."

    m "It gave me hope that one day, some girl would choose me for the sake of avoiding a doofus like him!"

    n "(hits Mushi in the stomach) I heard that, jackass!"

    m "Ouch!"

    a "Hmmmm, I like you! You’re a man of strength and refined honour for teaching the masked phantom discipline. Come in, samurai -- we have a club to burn!"
    "Aida pushes both Nami and Mushi into the club room."

    a "Sooooo, this is basically our club room… for now. I know it’s filled with dust and whatnot all over the place but hey, it’s a nice spot for us JCS folks!"

    a "(raises voice) Am I right?"

    m "Heck yeah, kaichou! Hontou ni subarashii~!"

    a"So… who is this? This is not some spot for you and your goons to lepak around, Mushi."

    m "Oh yeah, whoops, I forgot about you. Alright, fellas, meet…"

    m "Hey, wait a sec, I don’t even know what’s your name. Hahaha, some moron I am. "

    m "Alright alright, let’s trade. Ahem ahem. Watakushi no namae wa Mushi desu, or Mushi for short. Douzo yoroshiku onegaishimasu."

    m "(bows lowly to Nami) Anata no namae wa?"

    n "Uh… what?"

    a "(whispers) He’s asking for your name."

    n "Oh. Nami. My name is Nami. It’s my first semester and--"

    a "(interrupts; excited)
    Hi, my name is Aida! I’m the president of the JCS and this guy over here is Danny."

    n "Huh? Danny? I only see you and Mushi…"
    "Danny emerges from a table where he was hiding underneath."

    d "Yo, s’up? I’m Danny. Yoroshiku."

    n "What the f*ck? Hi, yoroshiblaghehwhut?"

    d "Ehh, close enough."

    n "Wait, so hold on. How many people are there in this club? Just the three of you? How is this club going to run with just the three of you? I expected more people -- maybe at least… twenty?"

    a "(offended)
    You got a problem with that?!"

    d "(meekly interrupts)
    Actually, we have four people in total. One of them isn’t here yet--"
    "Alis enters the club room."

    al "Yoo hoo, I’m here-- Oh em gee, who are you?! Are you someone new? Finally!"

    n "(awkward)
    Um… Hi there. I’m Nami. Yogoshiwho."

    al "(cheerful) Hi, I’m Alis! I’m not really good with Japanese but hey, I’ll take that intro!"

    a "(slides into the conversation) Sooo, Nami. What brings you here? You interested in being one of us?"

    a "(narrows eyes) You’re not just gonna leave, are ya?"

    m "(mutters) So he is…"

    a "(angry) Let him talk, Mushi! What do you think he is, some kind of mouthless man?!"

    m "(raises both hands in surrender) O-okay. Just rambling sh*t, jeez."

    n "Well, no, I’m not leaving yet but that doesn’t mean I’m joining either. What I want to know before I make that decision is… what exactly do you do in this club? Will it all be worth my time?"

    d "Ah shit, here we go again."

    a "(stares crossed at Mushi)
    Mushi, you just brought some random guy to this club without giving him all the details? You for real?"

    "Mushi remains silent but looks ahead with a derp face."

    a "(groans) I’ll get you for this."

    a "(looks at Nami) Alright, I’m only going to say this once, so get it stuck in your head. Our club here is about to be disbanded because as you can see, we are lacking members."
    a "In short, we need your help in getting it to grow so it won’t get disbanded. You ready for this challenge?"

    al "(cheers in the background)
    Yay, new members!"

    "Mushi continues staring off with a derp face."


    n "Mushi, need a little help here!"


    m"(sustained derp face)
    If I speak, she’ll kill me…"


    a"(intervenes)
    So are you up for the challenge or not?!"


    n"(panics; surprised)
    Ahh, okay okay! I’ll do this challenge. I mean, this will definitely work out if we put our heads together, right guys?"

    "Nami is met with silence."


    n"Um… guys?"

    "Nami looks over to Danny, Alis and Mushi, whom are all putting on the exact same derp face Mushi had earlier."

    n "(thinking to himself)
    Oh boy…"


    a "Good choice! Well team, now that we’ve added another number to our midsts,
    let’s begin our quest to find more people. We shall STRIVE! Nami,
    get over here and fill out this form."


    al "(cheerfully)
    We are soooo gonna party tonight!"


    m "Uhh, Aida?"


    d "Oh no, not again…"


    a "It’s our tradition! Masjid, here we come!"


    m "Hang on, you’re forgetting something, Aida: the best part!"


    a "Oh yeah… Considering I’m poor right now, we can’t go for an all-out karaoke party.
     Welp, if that’s the case, how about we take a rest over at the LP and gaze up at the beautiful stars over MMU?"

    a "Oh, and don’t forget about Deen’s amazing butter chicken too!"

    #KIV  &
    "Mushi and Alis" "Alaaaaaaaaa…"


    d "(relieved)
    Yes, finally. A more peaceful party."



    a "Anyway, welcome to the club, Nami! Don’t hesitate to ask us anything about the club.
     Let’s not waste our golden opportunity to form a nice, big family here!
      I’m sure you won’t be wasting a single second here."


    m "(excited)
    Welcomeeeeeee!"


    al "(equally excited)
    Yayyyyyyy~!"


    d "(muttering)
    Make sure you do your work--"

    "Both Alis and Mushi rush over to close Danny’s mouth, refraining him from continuing."


    m "Come, Nami, let’s hang out with the boys. Tell us more stuff about you!"


    al "Nak ikut!"


    a "(sighs)
    Kids these days… None of them know how to even appreciate money."


    d "(dying in the background)
    Help… me…"

    "The five of them all leave over to a mamak store to enjoy their time out and welcome the new member of their club.
     After a whole night’s part, Nami returns to his hostel exhausted and beat."




    n "(thinking to himself)
    Damn, those guys are insane. They are without a single care in the world but…
    I have to admit they’re really funny. Heh."

    n "I hope I can be like them one day too. Anyway, now that I’ve got myself into this new club,
    let’s see if I can put in the best I can for it."

    "Time jumps to three months afterwards."

    #show SCENE 3

    "In the club room of the JCS, Nami enters."


    al "Hiiii, Nami! Welcome back. How was your class today? Any new (clears throat) ahem, new girlfriends?"


    "Yo, Lis. It was a little bit tiring at class today and for the last time, I told you that that’s enough with the girlfriend thing, man."


    al "Whooooooa, who is it? You’re hiding someone, aren’t you? C’mon, tell me, tell me!"


    a "(yells)
    Silence! Have a seat! We’re about to start an important meeting so hajime yo!"


    d "(mumbles to himself)
    ‘Hajime yo’? The fu--"



    a "All right, guys! This week is an important week. It’s the week where freshmen are gonna start pouring in by massive numbers and we need people!"

    a "At the same time, I’ve got some good news: a senior from the club before us is gonna be having an event over at the MPH tonight called the ‘JC Night’."

    n "JC Night?"

    a "(angrily) Did I say you could talk, Nami?!"

    "Nami’s mouth zips shut, intimidated."

    a "JC Night is an annual event that happens every year. Do you hear me?! Every. Single. Year! Got it memorized?!"

    "Mushi, Alis and Nami nod slowly, plastered on their faces a classical derp face."


    a "(taken aback; surprised)
    What the eff, Mushi?! How long have you been there?"


    m "(pouting; saddened)
    S-since the very beginning. How did you not notice me? I’m sad now."


    al "Maybe if you weren’t putting on that ridiculous mask of yours, we’d
    notice you were there, like, right away. "

    al "Am I right or am I right, Nami? (looks expectantly at Nami, waiting for his agreement)"


    m "(sadly)
    I know that, Alis, but… my mom wouldn’t let me do that."

    a "(interrupts)
    Didn’t I tell you all to stay quiet?!"

    "Mushi, Alis and Nami immediately returned to being silent."


    a "If I may continue, JC Night is a performance night with tons of people coming over to check out the talented performers."

    a "What kind of performance, you might ask? Since, like, the dawn of time, JC Night has performances involving acting,
      dancing, singing, fighting with… Japanese culture! "

    m "(gets up and begins clapping)
    Hell yeah! Go go, Japanese culture!"

    "The others watched him in silence."


    m "(intimidated)
    Am I the only excited one here? Well, I wish I could join. (pouts sadly)"


    a "And… you guys are invited! See you at JC Night tonight, fellas! And whatever you do… don’t wear some dumbsh*t
     of an outfit in front of me, you got that?! "

    a "(sudden solemn face) Make sure to invite all your friends with you, else…"

    al "Aaaaand you don’t need to finish that line."


    d "(meekly)
    So, mind if I hang out with you guys during then--"



    al "(excited)
    Alright, who’s gonna be sitting beside me? Nami? Mushi? Aida? You three are coming right? Hehehehe!"


    d "(dejectedly; upset)
    What about me, guys…?"


    m "Well, sorry, guys. I can’t spend this clearly important event normally --
     I have to enjoy it with someone special, hehe."

    m "(speaks in a hushed tone) My mom."

    "Nami, Danny, Alis and Aida roll their eyes."


    n "(thinking to himself)
    JC Night, huh? So that means everyone is gonna be there… my crush included.
    If that’s the case, I’m definitely not missing this. Plus, I’m gonna be meeting a lot of new people
    as friends on the way."

    "But who exactly should I invite with me? Alis? Mushi? Danny? Aida?"

    #[Game provides four choices to choose from: Alis, Mushi, Danny and Aida.]
    menu:
        "Please invite one of them to the JC Night"

        "Alis":
            jump al
        "Mushi":
            jump m
        "Aida":
            jump a
        "Danny":
            jump d

    #show SCENE 4 (Alis)-
    label al:
        "At the entrance of the MPH, Nami is waiting for Alis by the door."


        al "(sneaks up behind Nami; surprises him)
        Boo!"


        n "(jolts back; surprised)
        Whoa!"

        al "(amused)
        Hahahaha, scared you, didn’t I? Anyway, hiya!"


        n "(still surprised)
        H-h-hi!"

        n "(thinking to himself; stunned) Wow, I’ve never seen Alis like this before…"


        al "(looks at Nami; confused)
        Hello? Earth to Nami? Nami? Moshi moshi?"


        n "(jolts back to reality)
        Whoops, sorry there, Alis! I was uh… in… another dimension just now, I guess. Hehe."


        al "(leans closer; interested)
        Wanna follow you there, hehe. (giggles)"


        n "(nervously)
        So… what’s up with the fancy get-up?"


        al "Oh, my outfit? Ehehe, you like it? It’s my best set of clothes! I only choose it for the most special of occasions!"


        n "(straightens up; excited)
        So does that mean I’m special?"


        al "(confused)
        Ummm… no?"

    
        "Nami frowns, disappointed by Alis’s response."


        al "(expression shifts to more amusement)
        Ahahahah, I’m just joking lah. It’s more because the night itself is special. I mean, it only happens once every year, right?"


        n "(still disappointed)
        Yeah… hahaha…"

        an "Ladies and gentlemen, gather round for in five minutes, we’re bringing this party to life!"


        al "Oh em gee, it’s about to start! I’m so excited, eeeeeeeeeeeeeeeek! Come on, let’s go!"


        n "(follows behind Alis)
        Ahahaha, alright alright."


        al "Kocchi, kocchi!"

        an "Inside the MPH building, photos of the previous JC Nights are being presented.
         Up on the stage is Farhan, who is giving a heartwarming speech as he is about to leave the university and graduate."


        f "Thank you all for attending JC Night tonight! I just wanted to let you all know how happy I am over here in MMU and how never will I ever get this experience elsewhere."

        f "Most of all, a special thank you goes out to members and the high committee of the Japanese Cultural Society for backing me up for this event and really, having my back through thick and thin during times of hardship."

        f "Once again, thank you, and just enjoy the show!"

        "Outside of MPH, Nami and Alis are together after the end of the event."


        al "Oh my God, I was asleep the whole time!"


        n "Ahahaha, you dummy! Man, the event was awesome…"


        al "(pleadingly)
        Please give me some good news and tell me you’ve recorded just a tiny little bit of it."


        n "Ahahaha, no worries, I did. I’ll hand it over to you. Well, are we gonna head back?"


        al "(deep in thought)
        Hmmm… Mind if you come with me first? Just for a little walk?"


        n "(interest piqued)
        Uh, sure."


        al "(happy)
        Hooray! Well come on, then! This way!"

        "Both Nami and Alis set out on a walk. There, they spent time indulging in petty banter and light jokes.
         After approximately fifteen minutes, Alis has led Nami into a quiet part of Cyberjaya."


        al "(in a sombre voice; serious)
        You know, it was just a coincidence that the JC Night for this year was on this particular night but…
        I figured I couldn’t miss this opportunity."
        al "I come here every year and since you brought me to JC Night, I thought that I should show you this."

        n "Show me…?"


        al "(has difficulty speaking)
        I wanted to show you my…"


        n "(waits in anticipation)
        My…?"


        al "(begins to tear up)
        ...My cat’s grave. My cat Kelabu. He used to be nothing but family to me ever since I left elementary school.
        I loved him so much, we were practically inseparable."
        al "He was there for me during my bad days at school.
        I used to get bullied a lot, but every time I came home in tears, he was always there to make things better. I… I--"

        "Alis bursts down into tears."


        n "(shocked)
        Wha--? (thinking to himself) I’ve never seen Alis cry like this before. (to Alis) Alis, are you okay?"


        al "(still crying)
        No. My cat has always been like family to me."


        n "(uncertain on what to do but was still desperate to try something anyway)
        Awww, Alis, why don’t you come here? I’ll show a bunch of memes, all right?"


        al "(sniffles)
        Where?"

        "Nami proceeds to show a bunch of memes for Alis to see.
        It takes her a while to start smiling but when she finally does,
        it was not long until she starts to laugh as well."

        "Ten minutes after the both of them had laughed over a couple of memes,
           Nami returns to ask her of her wellbeing. "


        n "You good now?"


        al "(smiling)
        Even though I might cry at times, don’t worry, I’m always good. Thanks for cheering me up though, by the way."

        al "I’m getting sleepy now though, so I’m gonna head back home. See you tomorrow, all right? It’s a promise."


        "(repeats; smiling back)
        Promise."
        jump ending
    # show SCENE 4 (Mushi)-
    label m:
        n "Mushi! I’m over here!"
        m "Ayyyy, Nami! I’m coming!"
        "Mushi walks over to where Nami is. Much to Nami’s disbelief and shock, Mushi is carrying with him a heap of anime girl models."
        n "What the--"
        m "Hahahahaha, meet all my babes! I spent every single penny I earned in my part time job to order them online. Here here, take a look at Chidori-san."
        "Mushi proceeds to show Nami one of his anime girl models. Nami leans forward, staring in interest."
        n "Damn… Hmm, mind if I have one of them?"
        m "(draws back with Chidori-san; aghast)"
        m "What, no! My mom wouldn’t allow that!"
        n "(pouts; disappointed) Meh. Mom this, mom that…"
        an "Ladies and gentlemen, gather round for in five minutes, we’re bringing this party to life!"
        m "(to his anime girl models)
        Let’s go, babes. The grand event is about to start. (looks over to Nami) You coming along or what, Nami? Here, if you really are that desperate for a girl, I’ll lend you one."
        n "(excited) Does this mean I get one?!"
        m "(snapping) No!"
        "Nami frowns, upset."
        an "The JC Night event then begins. Photos of the previous JC Nights are being presented. Up on the stage is Farhan, who is giving a heartwarming speech as he is about to leave the university and graduate."
        f "Thank you all for attending JC Night tonight!"
        f "I just wanted to let you all know how happy I am over here in MMU and how will I never ever get this experience elsewhere."
        f "Most of all, a special thank you goes out to members and the high committee of the Japanese Cultural Society for backing me up for this event and really, having my back through thick and thin in general."
        f "Once again, thank you, and just enjoy the show!"
        "Outside of MPH, Nami and Mushi are together after the end of the event. Mushi’s anime girl models are being taken away by an unrecognized man."
        n "Mushi, where are all your babes going?"
        m "(sheepishly) Well, hehehe, they weren’t mine. I rented them out so if I wanna have them for a longer amount of time, I gotta pay quite the price."
        n "But why go through the hassle of renting it up if you had to cough up all that money?"
        "Mushi stays quiet for a long time, but Nami is unable to read his expression from the mask on his face."
        "The silence persists for about ten seconds, twenty, until Mushi alas comes together and decides to speak. His head is lowered, as if he’s embarrassed to say words."
        m "Because I… wanted to impress you."
        n "(surprised) Really?"
        m "(nods) Yeah. And another thing… I lied about the mask too. I don’t wear it to hide my fame."
        m "I put it on because truthfully, I’m afraid to know what people will think of me without this funny facade of mine. It’s frightening. I just wanna have friends that love me, y’know."
        "Nami freezes in his spot, surprised to see this side of Mushi whom he did not know of."
        n "Hey… I’m sure you’re a great guy, even without your mask, Mushi."
        m "(hopeful) Really?"
        n "Yeah! I mean, though the mask gimmick is kinda hilarious and all, the jokes you speak out everyday and such all come from the real Mushi."
        n "So doesn’t that mean the real person putting up a great show would be you yourself?"
        m "(sniffles happy tears) Heh. You’re right. You’re a real great pal, Nami! How about I treat you dinner for being that awesome guy you are?"
        n "Wow, seriously? Hehehe, are we going on a dinner date?"
        m "Sure, my man. At the same time, let me show you a little something -- me without my mask on. Just for your eyes only, for just a second…"
        n "Mushi proceeds to remove his mask for Nami to see."
        jump ending

    # show SCENE 4 (Aida)-
    label a:
        a "Yo, sup, Nami? Do I… look weird tonight? (blushes)"
        n "(confused by Aida’s bashfulness) Yo, Aida! What’s the matter? You’re looking fine the way you are."
        a "What?! Just ‘fine’? Ugh…"
        n "(thinking to himself) Aida seems a little weird today. I wonder what’s going on?"
        n "So… you already taken your meal?"
        a "(blankly) Uh what? Taken my meal? I mean, yes yes, I’ve already eaten."
        n "(uneasy) Um, hey, you seriously feeling alright?"
        a "(annoyed) What?! Yes, I am --  don’t ask me such a ridiculous question!"
        n "(frightened) Oh, okay okay!"
        "An eerie silence hangs between the two of them as they both remain still in the awkwardness of the situation."
        "Nami attempts to strike a conversation but much to his disappointment, he could think of no words to say what he wishes to."
        "After finally about a minute or two later, Aida decides to speak."
        a "Can I… tell you something, Nami?"
        n "(hesitantly) Uhhh, sure. Why?"
        a "I asked a lot of people to be my partner for the night to JC Night but one after another, I’m met with rejection after rejection."
        a "Be frank and honest with me here, Nami, but… I’m not too scary-looking, am I…?"
        n "(thinking to himself) Uh, yeah. Yeah, you are. (to Aida) Nah, you’re fine. Come on, let’s--"
        an "Ladies and gentlemen, gather round for in five minutes, we’re bringing this party to life!"
        a "Oh, it’s about to start. Let’s get in there, Nami."
        an "Inside the MPH building, photos of the previous JC Nights are being presented. Up on the stage is Farhan, who is giving a heartwarming speech as he is about to leave the university and graduate."
        f "Thank you all for attending JC Night tonight!"
        f "I just wanted to let you all know how happy I am over here in MMU and how will I never ever get this experience elsewhere."
        f "Most of all, a special thank you goes out to members and the high committee of the Japanese Cultural Society for backing me up for this event and really, having my back through thick and thin in general."
        f "Once again, thank you, and just enjoy the show!"
        "Outside of MPH, Nami and Aida are together after the end of the event."
        n "Damn, that was some really good acting in there!"
        a "Yeah, it was funny too! Hahahahaha!"
        n "Yeah…"
        a "Haha, yeah…"
        "Nami looks Aida in the eyes, to which Aida returns the gaze. As quick as they had both caught one another staring, they looked away -- the awkwardness from before the event started ensuing. "
        "Unable to take its thickness in the atmosphere surrounding them, Nami burdens himself to speak. "
        n "So… wanna head out for dinner together? Maybe a late night movie over at the cinemas?"
        a "(perks up; squeals; excited) I wanna!"
        n "(thinking to himself) Wow, Aida is so very different when she's chipper. It's a lot more different than how she's always strict at the club. It's actually… pretty cute."
        n "Hahaha, alright then. On me!"
        a "But… (hesitantly) you sure you want to go out with me? I'm sure you must have a ton of other girls that you'd like better by your side."
        a "I mean, look at me. I'm just a silly, strict and bland-looking girl. There are other girls out there who overpower me by a mile away. Surely you'd want to be with them more…"
        n "Hey, listen to me. You're amazing just the way you are, all right? You look amazing too. So, of course I want to go out with you."
        n "Besides, I know how you feel when you say no one really wants to go out with you because no one wants to go out with me either."
        n "So how about we do each other a favour and make one another feel a little less lonely tonight?"
        a "(amused; overjoyed) Hahahaha, let's!"
        "And so together, Aida and Nami set off on their journey to enjoy the rest of the night with someone special in their hearts. "
        jump ending
    # Scene 4 (Danny)-
    label d:
        n "Danny? You came? I thought you were asleep over at the club room."
        d "Ah, hey there, Nami. Well, let's just say I wanted to get some fresh air, y'know. Hehe."
        d "By the way, if you don't mind, could you lend me some money? (looks at Nami pleasingly)"
        n "(confused) Uh, sure. Why though?"
        d "Well… I don't have enough money to attend the JC Night."
        n "Oof, really? If that's the case, man, I'll pay it for you. Think of it as my treat."
        d "(happily) Oh my God, you're the best friend a man could ever have, buddy!"
        n "Ahahaha, stop it, man, you're making me blush."
        an "Ladies and gentlemen, gather round for in five minutes, we’re bringing this party to life!"
        d "Eyyy, what do you know, there's our cue! C'mon, let's head on in before the best seats are taken."
        an "Inside the MPH building, photos of the previous JC Nights are being presented. Up on the stage is Farhan, who is giving a heartwarming speech as he is about to leave the university and graduate."
        f "Thank you all for attending JC Night tonight!"
        f "I just wanted to let you all know how happy I am over here in MMU and how will I never ever get this experience elsewhere."
        f "Most of all, a special thank you goes out to members and the high committee of the Japanese Cultural Society for backing me up for this event and really, having my back through thick and thin in general."
        f "Once again, thank you, and just enjoy the show!"
        "Outside of MPH, Nami and Aida are together after the end of the event."
        d "(hyped up) That… was… an epic performance! Plus having you by my side made it all the more awesome, that's for sure."
        n "Yeah, it was amazing all right but… could you really get a good view of the stage while you were hiding underneath your chair the whole time?"
        d "Oh… Well, I can. It's not that I'm doing it to get a better view or something like that but I'm just… really shy when it comes to strangers. Admittedly, I'm weak when it comes to being in large crowds. I can't handle that."
        n "Ohh, so that explains why you're always sitting underneath things, even when I first came into the club room."
        n "You should try speaking with the people around you so they can get to know you more and realize just how awesome you are. If you keep this up, things will end up bad for you, bro."
        d "Hahahaha, nice try, man. But… believe it or not, I like being this way -- remaining in the shadows, hiding where no one can see me and all because from afar, I get to watch everyone succeed with the best of their efforts."
        d "It might not look like much but I assure you, it's a better view than you think. Nevertheless, thank you for caring about me, dude."
        n "Hmmm, alright. Whatever floats your boat, bro. As long as you're happy. It's no problem at all. Anyway, if you feel like sharing more stories to someone, feel free to drop by and enlighten me with your awesome tales."
        d "Alright, I'm game, man. Welp, I'm on my way back to the club room now. I've got some new games I've been dying to try out and I can't wait any longer. See you!"
        n "See you around the campus!"
        "Happy, the two boys part ways."
    # ENDING
    label ending:
        "Nami's phone notification plays in the background."
        pm "Hey, Nami. Can we meet at MMU Stadium in a bit? There's something I need to tell you. Please come over quick."
        n "Oh my God, my crush messaged me! I have to go now and meet up with her. I mean, who knows, maybe she's gonna admit she loves me back! Finally, the time has come at last… This time, I'm gonna make things happen!"
        "Nami runs down the stairs in his excitement and dashes through the road to make his way across the street."
        "A truck, however, fails to notice Nami trying to pass and in a flash, it hits Nami with high speed."
        "When Nami opens his eyes, the world is pitch black. He sees nothing but darkness."
        n "Oh God… Am… Am I dead? Where am I?"
        "As he waited, tensed, in the darkness, time passes and slowly the void begins to clear. Though difficult to see, Nami picks up the sight of two people arguing. Grimly, he remembers."
        n "Mom… Dad…"
        "Devoured by his memories, Nami begins to sob. In that darkness, no one listens to his cries. Truly, Nami is all alone. Just as he always is."


    # This ends the game.
    return
